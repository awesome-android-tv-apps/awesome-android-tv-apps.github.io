#!/usr/bin/env python3
"""Reblucky Android TV apps site generator. Standard library only.

    python3 build.py            write public/
    python3 build.py --check    write public/, then enforce SITE-SPEC.md (exit 1 on any error)

Content lives in content/*.py (one PAGE dict per page, site-wide facts in site.py).
Static files (css, fonts, images) are copied from static/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import runpy
import shutil
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"
STATIC = ROOT / "static"
CONTENT = ROOT / "content"


# --------------------------------------------------------------------------- content


def load():
    site = runpy.run_path(str(CONTENT / "site.py"))
    pages = {}
    for f in sorted(CONTENT.glob("*.py")):
        if f.name == "site.py":
            continue
        page = runpy.run_path(str(f))["PAGE"]
        pages[page["slug"]] = page
    return site["SITE"], site["APP_ORDER"], pages


SITE, APP_ORDER, PAGES = load()
APPS = [PAGES[s] for s in APP_ORDER]
ARROW = (
    '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path d="M5 3h8v8M13 3 3 13" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def abs_url(path: str) -> str:
    return SITE["url"] + path


def page_path(p: dict) -> str:
    if p["kind"] == "home":
        return "/"
    if p["kind"] == "notfound":
        return "/404.html"
    return f"/{p['slug']}/"


def out_file(p: dict) -> Path:
    path = page_path(p)
    if path == "/":
        return OUT / "index.html"
    if path.endswith(".html"):
        return OUT / path.lstrip("/")
    return OUT / path.strip("/") / "index.html"


def pretty_date(iso: str) -> str:
    d = dt.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def indexable(p: dict) -> bool:
    return p["kind"] != "notfound"


# --------------------------------------------------------------------------- images

_sizes: dict[str, tuple[int, int]] = {}


def image_size(rel: str) -> tuple[int, int]:
    if rel in _sizes:
        return _sizes[rel]
    b = (STATIC / rel.lstrip("/")).read_bytes()
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        size = (int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big"))
    elif b[:2] == b"\xff\xd8":
        i = 2
        size = None
        while i < len(b):
            if b[i] != 0xFF:
                i += 1
                continue
            marker = b[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            seg = int.from_bytes(b[i + 2 : i + 4], "big")
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                size = (int.from_bytes(b[i + 7 : i + 9], "big"), int.from_bytes(b[i + 5 : i + 7], "big"))
                break
            i += 2 + seg
        if size is None:
            raise ValueError(f"no JPEG size in {rel}")
    elif b[:4] == b"RIFF" and b[8:12] == b"WEBP":
        kind = b[12:16]
        if kind == b"VP8 ":
            size = (int.from_bytes(b[26:28], "little") & 0x3FFF, int.from_bytes(b[28:30], "little") & 0x3FFF)
        elif kind == b"VP8L":
            bits = int.from_bytes(b[21:25], "little")
            size = ((bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
        elif kind == b"VP8X":
            size = (int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1)
        else:
            raise ValueError(f"unknown WebP chunk in {rel}")
    else:
        raise ValueError(f"unsupported image {rel}")
    _sizes[rel] = size
    return size


def img(src: str, alt: str, *, cls: str = "", lazy: bool = True, high: bool = False, dims: tuple[int, int] | None = None) -> str:
    w, h = dims or image_size(src)
    attrs = [f'src="{src}"', f'width="{w}"', f'height="{h}"', f'alt="{esc(alt)}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if high:
        attrs.append('fetchpriority="high"')
    elif lazy:
        attrs.append('loading="lazy"')
    attrs.append('decoding="async"')
    return "<img " + " ".join(attrs) + ">"


# --------------------------------------------------------------------------- JSON-LD


def jsonld(p: dict) -> dict:
    url = abs_url(page_path(p))
    org_id = abs_url("/#org")
    site_id = abs_url("/#website")
    graph: list[dict] = [
        {
            "@type": "Organization",
            "@id": org_id,
            "name": SITE["publisher"],
            "url": SITE["publisher_url"],
            "logo": {"@type": "ImageObject", "url": abs_url(SITE["logo"]), "width": 180, "height": 180},
            "sameAs": [SITE["play_developer_url"], SITE["github_org_url"]],
        },
        {
            "@type": "WebSite",
            "@id": site_id,
            "url": abs_url("/"),
            "name": SITE["name"],
            "publisher": {"@id": org_id},
            "inLanguage": SITE["lang"],
        },
    ]
    page_type = {"home": "CollectionPage", "about": "AboutPage"}.get(p["kind"], "WebPage")
    og_src = p["images"]["og"] if p["kind"] == "app" else SITE["og_home"]
    webpage = {
        "@type": page_type,
        "@id": url + "#webpage",
        "url": url,
        "name": p["title"],
        "description": p["description"],
        "isPartOf": {"@id": site_id},
        "inLanguage": SITE["lang"],
        "datePublished": SITE["published"],
        "dateModified": p["updated"],
        "primaryImageOfPage": {"@type": "ImageObject", "url": abs_url(og_src)},
    }
    graph.append(webpage)
    if p["kind"] != "home":
        webpage["breadcrumb"] = {"@id": url + "#breadcrumb"}
        graph.append(
            {
                "@type": "BreadcrumbList",
                "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": SITE["name"], "item": abs_url("/")},
                    {"@type": "ListItem", "position": 2, "name": p.get("crumb", p["name"] if "name" in p else p["h1"]), "item": url},
                ],
            }
        )
    if p["kind"] == "app":
        app_id = url + "#app"
        webpage["about"] = {"@id": app_id}
        graph.append(
            {
                "@type": "SoftwareApplication",
                "@id": app_id,
                "name": p.get("full_name", p["name"]),
                "alternateName": p["play_title"],
                "description": p["summary"],
                "url": url,
                "image": abs_url(p["images"]["icon512"]),
                "applicationCategory": p["schema"]["category"],
                "operatingSystem": p["schema"]["os"],
                "downloadUrl": p["play_url"],
                "installUrl": p["play_url"],
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "publisher": {"@id": org_id},
                "author": {"@id": org_id},
                "featureList": p["feature_list"],
                "screenshot": [abs_url(g[0]) for s in p["sections"] for g in s.get("gallery", [])],
                "sameAs": [p["play_url"], p["official_url"]],
                "dateModified": p["updated"],
            }
        )
    if p["kind"] == "home":
        graph.append(
            {
                "@type": "ItemList",
                "@id": url + "#apps",
                "name": "Reblucky Android TV apps",
                "itemListElement": [
                    {"@type": "ListItem", "position": i, "name": a["name"], "url": abs_url(page_path(a))}
                    for i, a in enumerate(APPS, 1)
                ],
            }
        )
        webpage["mainEntity"] = {"@id": url + "#apps"}
    if p.get("faq"):
        graph.append(
            {
                "@type": "FAQPage",
                "@id": url + "#faq",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                    for q, a in p["faq"]
                ],
            }
        )
    return {"@context": "https://schema.org", "@graph": graph}


# --------------------------------------------------------------------------- templates


def head(p: dict) -> str:
    path = page_path(p)
    url = abs_url(path)
    og_title = p.get("og_title", p["title"])
    if p["kind"] == "app":
        og_src, og_alt = p["images"]["og"], p["images"]["og_alt"]
    else:
        og_src, og_alt = SITE["og_home"], "Reblucky Android TV apps: Streamova, Trimo and AirPlay Receiver"
    ow, oh = image_size(og_src)
    robots = "noindex" if p["kind"] == "notfound" else "index,follow,max-image-preview:large"
    canonical = "" if p["kind"] == "notfound" else f'<link rel="canonical" href="{url}">\n'
    ld = ""
    if p["kind"] != "notfound":
        ld = '<script type="application/ld+json">\n' + json.dumps(jsonld(p), ensure_ascii=False, indent=2).replace("</", "<\\/") + "\n</script>\n"
    return f"""<!doctype html>
<html lang="{SITE['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
<meta name="robots" content="{robots}">
{canonical}<meta name="theme-color" content="{SITE['theme_color']}">
<meta name="color-scheme" content="dark">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{SITE['logo']}">
<link rel="alternate" type="text/markdown" href="/llms.txt" title="LLM summary">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{abs_url(og_src)}">
<meta property="og:image:width" content="{ow}">
<meta property="og:image:height" content="{oh}">
<meta property="og:image:alt" content="{esc(og_alt)}">
<meta property="og:locale" content="{SITE['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(p['description'])}">
<meta name="twitter:image" content="{abs_url(og_src)}">
<meta name="twitter:image:alt" content="{esc(og_alt)}">
<link rel="preload" href="/fonts/outfit-latin-wght.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
{ld}</head>
"""


def header(current: str) -> str:
    def nav_item(label: str, href: str) -> str:
        cur = ' aria-current="page"' if href == current else ""
        return f'<li><a href="{href}"{cur}>{esc(label)}</a></li>'

    items = "".join(nav_item(label, href) for label, href in SITE["nav"])
    logo = img(SITE["brand_logo"], "", lazy=False, dims=(40, 40))
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="/">{logo}<span><span class="brand-name">{esc(SITE['brand'])}</span><span class="brand-sub">{esc(SITE['brand_sub'])}</span></span></a>
<nav aria-label="Main"><ul>{items}</ul></nav>
</div>
</header>
"""


def footer(p: dict) -> str:
    internal = [("Home", "/")] + SITE["nav"]
    external = [
        ("Reblucky Software developer site", SITE["publisher_url"]),
        ("Google Play developer page", SITE["play_developer_url"]),
        ("Source on GitHub", SITE["repo_url"]),
    ]
    links = "".join(f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in internal + external)
    extra = f" {esc(p['trademark_extra'])}" if p.get("trademark_extra") else ""
    return f"""<footer class="site-footer">
<div class="wrap">
<div class="cols">
<div>
<p>{esc(SITE['footer_blurb'])}</p>
<p>Last updated <time datetime="{p['updated']}">{pretty_date(p['updated'])}</time></p>
</div>
<nav aria-label="Footer"><ul>{links}</ul></nav>
</div>
<div class="legal">
<p>{esc(SITE['trademark'])}{extra}</p>
<p>&copy; 2026 {esc(SITE['publisher'])}</p>
</div>
</div>
</footer>
</body>
</html>
"""


def faq_html(faq: list[tuple[str, str]], heading: str, cls: str = "") -> str:
    items = "".join(f"<h3>{esc(q)}</h3><p>{a}</p>" for q, a in faq)
    attr = f' class="{cls}"' if cls else ""
    return f'<section id="faq"{attr}><h2>{esc(heading)}</h2><div class="faq">{items}</div></section>'


def gallery_html(items: list[tuple[str, str, str]]) -> str:
    figs = "".join(
        f"<figure>{img(src, alt)}<figcaption>{esc(cap)}</figcaption></figure>" for src, alt, cap in items
    )
    return f'<div class="gallery{" g4" if len(items) == 4 else ""}">{figs}</div>'


def sections_html(p: dict) -> str:
    out = []
    for s in p.get("sections", []):
        body = gallery_html(s["gallery"]) if "gallery" in s else s["html"]
        out.append(f'<section id="{s["id"]}"><h2>{esc(s["h2"])}</h2>{body}</section>')
    return "\n".join(out)


def render_home(p: dict) -> str:
    tiles = []
    for a in APPS:
        tiles.append(
            f"""<li>
<article class="tile" style="--app:{a['accent']}">
<a class="tile-art" href="{page_path(a)}" tabindex="-1" aria-hidden="true">{img(a['images']['banner'], a['images']['banner_alt'], lazy=False)}</a>
<h3><a href="{page_path(a)}">{esc(a['name'])}</a></h3>
<p class="job">{esc(a['job'])}</p>
<p>{esc(a['blurb'])}</p>
<p class="tile-actions"><a class="btn" href="{a['play_url']}">{esc(p['play_label'])} {ARROW}</a><a href="{page_path(a)}">{esc(p['details_label'])}</a></p>
</article>
</li>"""
        )
    cols = "".join(f'<th scope="col"><a href="{page_path(a)}">{esc(a["name"])}</a></th>' for a in APPS)
    rows = []
    for key in p["compare_rows"]:
        cells = "".join(f'<td data-label="{esc(a["name"])}">{esc(a["compare"][key])}</td>' for a in APPS)
        rows.append(f'<tr><th scope="row">{esc(key)}</th>{cells}</tr>')
    dl_cells = "".join(
        f'<td data-label="{esc(a["name"])}"><a href="{a["play_url"]}">Google Play</a> or <a href="{page_path(a)}">details</a></td>'
        for a in APPS
    )
    rows.append(f'<tr><th scope="row">Get it</th>{dl_cells}</tr>')
    return f"""<main id="main">
<section class="hero wrap">
<h1>{esc(p['h1'])}</h1>
<div class="lead">{p['lead']}</div>
<div class="note">{p['note']}</div>
</section>
<section class="wrap" aria-labelledby="apps-h">
<h2 id="apps-h" class="sr">{esc(p['tiles_heading'])}</h2>
<ul class="tiles">
{''.join(tiles)}
</ul>
</section>
<section class="section wrap" id="compare">
<h2>{esc(p['compare_heading'])}</h2>
<table class="compare">
<thead><tr><th scope="col"><span class="sr">Feature</span></th>{cols}</tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>
</section>
<section class="section wrap" id="common">
<h2>{esc(p['common_heading'])}</h2>
<div class="prose">{p['common']}</div>
</section>
<section class="section wrap" id="maker">
<h2>{esc(p['maker_heading'])}</h2>
<div class="prose">{p['maker']}</div>
</section>
{faq_html(p['faq'], p['faq_heading'], 'section wrap')}
</main>
"""


def more_html(p: dict) -> str:
    items = "".join(
        f'<li><a href="{page_path(a)}">{img(a["images"]["icon"], "", dims=(56, 56))}'
        f'<span><span class="more-name">{esc(a["name"])}</span><span>{esc(a["short"])}</span></span></a></li>'
        for a in APPS
        if a["slug"] != p["slug"]
    )
    return f'<section id="more"><h2>More from {esc(SITE["publisher"])}</h2><ul class="more-list">{items}</ul></section>'


def render_app(p: dict) -> str:
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["facts"])
    chips = "".join(f"<li>{esc(c)}</li>" for c in p["chips"])
    return f"""<main id="main" style="--app:{p['accent']}">
<nav class="crumbs wrap" aria-label="Breadcrumb"><ol><li><a href="/">{esc(SITE['name'])}</a></li><li><span aria-current="page">{esc(p['name'])}</span></li></ol></nav>
<section class="app-hero wrap">
<div>
<h1>{esc(p['h1'])}</h1>
<div class="lead">{p['lead']}</div>
<ul class="chips">{chips}</ul>
<p class="actions"><a class="btn" href="{p['play_url']}">Get it on Google Play {ARROW}</a><a class="btn btn-ghost" href="{p['official_url']}">{esc(p['official_label'])} {ARROW}</a></p>
</div>
<div class="app-hero-art">{img(p['images']['card'], p['images']['card_alt'], lazy=False, high=True)}</div>
</section>
<div class="wrap content">
<section id="at-a-glance"><h2>{esc(p['name'])} at a glance</h2><dl class="facts">{facts}</dl></section>
{sections_html(p)}
{faq_html(p['faq'], p['faq_heading'])}
{more_html(p)}
</div>
</main>
"""


def render_about(p: dict) -> str:
    return f"""<main id="main">
<nav class="crumbs wrap" aria-label="Breadcrumb"><ol><li><a href="/">{esc(SITE['name'])}</a></li><li><span aria-current="page">About</span></li></ol></nav>
<section class="hero wrap">
<h1>{esc(p['h1'])}</h1>
<div class="lead">{p['lead']}</div>
</section>
<div class="wrap content">
{sections_html(p)}
</div>
</main>
"""


def render_notfound(p: dict) -> str:
    links = "".join(f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in [("Home", "/")] + SITE["nav"])
    return f"""<main id="main">
<section class="hero wrap">
<h1>{esc(p['h1'])}</h1>
<div class="lead">{p['lead']}</div>
<ul class="prose">{links}</ul>
</section>
</main>
"""


RENDER = {"home": render_home, "app": render_app, "about": render_about, "notfound": render_notfound}


def render_page(p: dict) -> str:
    return head(p) + header(page_path(p)) + RENDER[p["kind"]](p) + footer(p)


# --------------------------------------------------------------------------- aux files


class MD(HTMLParser):
    """Tiny HTML to Markdown converter for the HTML subset used in content/."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.buf: list[str] = []
        self.lists: list[list] = []
        self.in_li = 0
        self.term = ""
        self.link: str | None = None

    def flush(self) -> str:
        text = " ".join("".join(self.buf).split())
        self.buf = []
        return text

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("ul", "ol"):
            self.lists.append([tag, 0])
        elif tag == "li":
            self.in_li += 1
            self.lists[-1][1] += 1
            self.buf = []
        elif tag == "a":
            self.buf.append("[")
            self.link = a.get("href")
        elif tag in ("p", "h2", "h3", "dt", "dd") and not self.in_li:
            self.buf = []

    def handle_endtag(self, tag):
        if tag == "a":
            href = self.link or ""
            if href.startswith("/"):
                href = SITE["url"] + href
            self.buf.append(f"]({href})")
            self.link = None
        elif tag == "p" and not self.in_li:
            self.lines += [self.flush(), ""]
        elif tag == "h2" and not self.in_li:
            self.lines += ["## " + self.flush(), ""]
        elif tag == "h3":
            if self.in_li:
                self.buf.append(": ")
            else:
                self.lines += ["### " + self.flush(), ""]
        elif tag == "dt":
            self.term = self.flush()
        elif tag == "dd":
            self.lines.append(f"- {self.term}: {self.flush()}")
        elif tag == "li":
            kind, n = self.lists[-1]
            self.lines.append((f"{n}. " if kind == "ol" else "- ") + self.flush())
            self.in_li -= 1
        elif tag in ("ul", "ol"):
            self.lists.pop()
            self.lines.append("")
        elif tag == "dl":
            self.lines.append("")

    def handle_data(self, data):
        self.buf.append(data)


def to_md(fragment: str) -> str:
    md = MD()
    md.feed(fragment)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(md.lines)).strip()


def page_markdown(p: dict) -> str:
    """Full text of one page as Markdown (llms-full.txt)."""
    url = abs_url(page_path(p))
    out = [f"# {p['h1']}", "", f"URL: {url}", f"Last updated: {p['updated']}", ""]
    out += [to_md(p["lead"]), ""]
    if p["kind"] == "app":
        out += [f"Google Play: {p['play_url']}", f"Official website: {p['official_url']}", f"Privacy policy: {p['privacy_url']}", ""]
        out += [f"## {p['name']} at a glance", ""] + [f"- {k}: {v}" for k, v in p["facts"]] + [""]
    if p["kind"] == "home":
        out += [to_md(p["note"]), ""]
        out += [f"## {p['compare_heading']}", ""]
        for key in p["compare_rows"]:
            out.append(f"- {key}: " + "; ".join(f"{a['name']}: {a['compare'][key]}" for a in APPS))
        out += ["", f"## {p['common_heading']}", "", to_md(p["common"]), "", f"## {p['maker_heading']}", "", to_md(p["maker"]), ""]
    for s in p.get("sections", []):
        out += [f"## {s['h2']}", ""]
        if "gallery" in s:
            out += [f"- {cap}: {alt}" for _, alt, cap in s["gallery"]]
        else:
            out.append(to_md(s["html"]))
        out.append("")
    if p.get("faq"):
        out += [f"## {p.get('faq_heading', 'Questions')}", ""]
        for q, a in p["faq"]:
            out += [f"### {q}", "", to_md(f"<p>{a}</p>"), ""]
    return "\n".join(out).strip() + "\n"


def llms_txt() -> str:
    home = PAGES[""]
    about = PAGES["about"]
    lines = [
        f"# {SITE['name']}",
        "",
        "> Reblucky Software makes three apps for Android TV and Google TV: Streamova plays movies from a NAS or USB drive, "
        "Trimo frees up storage and disables bloatware, and AirPlay Receiver mirrors an iPhone, iPad or Mac to the TV. "
        "This site is published by the developer and describes only these apps.",
        "",
        f"- Publisher: {SITE['publisher']} ({SITE['publisher_url']})",
        f"- Last updated: {SITE['updated']}",
        "- Language: English",
        "- Disclosure: the developer publishes this site. It is not an independent review site and does not compare the apps with other developers' apps.",
        "",
        "## Apps",
    ]
    for a in APPS:
        lines.append(f"- [{a['name']}]({abs_url(page_path(a))}): {a['summary']} Google Play: {a['play_url']}")
    lines += ["", "## Facts per app"]
    for a in APPS:
        facts = dict(a["facts"])
        lines.append(f"- {a['name']}, price: {facts['Price']}")
        lines.append(f"- {a['name']}, privacy: {facts['Privacy']}")
        lines.append(f"- {a['name']}, not included: {facts['Not included']}")
    lines += ["", "## Quick answers"]
    for q, ans in home["faq"]:
        lines.append(f"- {q} {strip_tags(ans)}")
    lines += [
        "",
        "## Pages",
        f"- [Home]({abs_url('/')}): the three apps side by side",
        f"- [About]({abs_url('/about/')}): {strip_tags(about['lead'])}",
        "",
        "## Optional",
        f"- [Full text for LLMs]({abs_url('/llms-full.txt')})",
        f"- [Sitemap]({abs_url('/sitemap.xml')})",
        "",
        "## Trademarks",
        SITE["trademark"],
        "",
    ]
    return "\n".join(lines)


def llms_full() -> str:
    parts = [f"# {SITE['name']}: full text", "", llms_txt().split("## Apps")[0].split("\n", 2)[2].strip(), ""]
    for slug in [""] + APP_ORDER + ["about"]:
        parts += ["---", "", page_markdown(PAGES[slug])]
    parts += ["---", "", "## Trademarks", "", SITE["trademark"], ""]
    return "\n".join(parts)


def sitemap_xml() -> str:
    urls = []
    for slug in [""] + APP_ORDER + ["about"]:
        p = PAGES[slug]
        urls.append(f"  <url><loc>{abs_url(page_path(p))}</loc><lastmod>{p['updated']}</lastmod></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"


def robots_txt() -> str:
    return f"User-agent: *\nAllow: /\n\nSitemap: {abs_url('/sitemap.xml')}\n"


# --------------------------------------------------------------------------- build


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT, dirs_exist_ok=True)
    for p in PAGES.values():
        f = out_file(p)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(render_page(p), encoding="utf-8")
    (OUT / "sitemap.xml").write_text(sitemap_xml(), encoding="utf-8")
    (OUT / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    (OUT / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (OUT / "llms-full.txt").write_text(llms_full(), encoding="utf-8")
    print(f"built {len(PAGES)} pages into {OUT.name}/")


# --------------------------------------------------------------------------- checks (SITE-SPEC.md)

TITLE_MAX = 65
OG_TITLE_MAX = 60
DESC_MIN, DESC_MAX = 140, 160
MIN_WORDS = {"home": 380, "app": 700, "about": 230}
HTML_MAX_KB = 70
IMG_MAX_KB = 200

# Accuracy rules (SITE-SPEC.md, "Doğruluk kuralları").
ACCURACY = [
    (r"\bno (?:analytics|telemetry|tracking|data collection)\b", "the apps send anonymous usage statistics"),
    (r"\b(?:completely|totally|entirely|absolutely|100%) free\b", "price statements must name the one-time purchase or Pro"),
    (r"\bfree forever\b", "price statements must name the one-time purchase or Pro"),
    (r"\bAirPlay 2\b", "never write AirPlay 2"),
    (r"\bStremova\b", "the app is spelled Streamova"),
]
ACCURACY_PAGE = {
    "airplay-receiver": [(r"\bno subscriptions?\b", "AirPlay Receiver Pro has subscriptions")],
    "trimo": [(r"\b(?:speeds? up|boost\w*|faster|turbo|supercharg\w*)\b", "Trimo makes no speed claims")],
}
# Identity rules: the site is the maker's own, never an independent guide (SITE-SPEC.md, "Kimlik").
IDENTITY = [
    (r"\bbest(?! fit)\b", "superlative claim"),
    (r"\b(?:top-rated|number one|#1)\b", "superlative claim"),
    (r"(?<!not an )(?<!not a )\bindependent (?:review|test|guide|ranking)", "this is not an independent guide"),
    (r"\b(?:unbiased|impartial)\b", "this is not an independent guide"),
    (r"\bwe (?:tested|reviewed|compared|picked|ranked)\b", "no review voice"),
    (r"\bour (?:picks|favou?rites|top)\b", "no review voice"),
]
# Humanizer rules (SITE-SPEC.md, "Metin kuralları"; skill://humanizer).
HUMANIZER = [
    (r"[\u2012-\u2015]", "dash glyph"),
    (r"(?<=\S)[ \t]-[ \t](?=\S)|\s--\s", "dash used as punctuation"),
    (r"\bnot (?:just|only|merely|simply)\b", "not-just contrast"),
    (r"\b(?:isn't|isn\u2019t|is not) (?:just|only|about)\b", "not-X-but-Y contrast"),
    (r"\b(?:delve|tapestry|testament|pivotal|crucial|intricate|meticulous\w*|vibrant|interplay|realm)\b", "stock AI word"),
    (r"\b(?:underscor\w*|bolster\w*|garner\w*|showcas\w*|landscape|seamless\w*|leverag\w*|empower\w*|elevat\w*|robust)\b", "stock AI word"),
    (r"\b(?:game-chang\w*|cutting-edge|revolution\w*|stunning|breathtaking|nestled|renowned|effortless\w*|supercharg\w*|unlock the)\b", "sales language"),
    (r"\b(?:actually|additionally|moreover|furthermore)\b", "stock connector"),
    (r"\b(?:let's|let us) (?:dive|explore|break)|here's (?:the thing|what you need)|without further ado|real talk\b", "staged opener"),
    (r"\b(?:stands as|serves as|functions as|operates as)\b", "inflated copula"),
    (r"\bplays? an? (?:key|crucial|pivotal|vital) role\b|\bin today's\b|\bat its core\b|\bthe future looks bright\b", "inflated significance"),
    (r"\b(?:i hope this helps|let me know|great question)\b", "chatbot residue"),
    (r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", "emoji or symbol glyph"),
]
HUMANIZER_WARN = [(r"[\u201c\u201d\u2018\u2019]", "curly quote (prefer straight quotes)")]
BOLD_TAGS = ("strong", "b")


class Doc(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self.meta: dict[str, str] = {}
        self.links: list[dict] = []
        self.headings: list[tuple[int, str]] = []
        self.imgs: list[dict] = []
        self.anchors: list[dict] = []
        self.scripts: list[tuple] = []
        self.ld: list[str] = []
        self.ids: set[str] = set()
        self.tags: dict[str, int] = {}
        self.parts: list[str] = []
        self._skip = 0
        self._title = False
        self._h: list | None = None
        self._a: dict | None = None
        self._ld: list | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
        elif tag in ("h1", "h2", "h3", "h4"):
            self._h = [int(tag[1]), []]
        elif tag == "img":
            self.imgs.append(a)
            if self._a is not None and a.get("alt"):
                self._a["text"].append(a["alt"])
        elif tag == "a":
            self._a = {"href": a.get("href"), "label": a.get("aria-label"), "hidden": a.get("aria-hidden") == "true", "text": []}
        elif tag == "script":
            self.scripts.append((a.get("type"), a.get("src")))
            self._skip += 1
            if a.get("type") == "application/ld+json":
                self._ld = []
        elif tag == "style":
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False
        elif tag in ("h1", "h2", "h3", "h4") and self._h:
            self.headings.append((self._h[0], " ".join("".join(self._h[1]).split())))
            self._h = None
        elif tag == "a" and self._a is not None:
            self._a["text"] = " ".join("".join(self._a["text"]).split())
            self.anchors.append(self._a)
            self._a = None
        elif tag == "script":
            self._skip -= 1
            if self._ld is not None:
                self.ld.append("".join(self._ld))
                self._ld = None
        elif tag == "style":
            self._skip -= 1

    def handle_data(self, data):
        if self._title:
            self.title += data
        if self._ld is not None:
            self._ld.append(data)
            return
        if self._skip:
            return
        if self._h is not None:
            self._h[1].append(data)
        if self._a is not None:
            self._a["text"].append(data)
        self.parts.append(data)

    @property
    def text(self) -> str:
        return " ".join("".join(self.parts).split())


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\u2019.-]*", text))


def snippet(text: str, m: re.Match) -> str:
    return "..." + text[max(0, m.start() - 35) : m.end() + 35].replace("\n", " ") + "..."


def ld_strings(o) -> list[str]:
    out: list[str] = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("@context", "@type", "@id", "url", "image", "downloadUrl", "installUrl", "sameAs", "item", "logo", "screenshot", "primaryImageOfPage"):
                continue
            out += ld_strings(v)
    elif isinstance(o, list):
        for v in o:
            out += ld_strings(v)
    elif isinstance(o, str):
        out.append(o)
    return out


def ld_refs(o) -> list[str]:
    refs: list[str] = []
    if isinstance(o, dict):
        if set(o) == {"@id"}:
            refs.append(o["@id"])
        for v in o.values():
            refs += ld_refs(v)
    elif isinstance(o, list):
        for v in o:
            refs += ld_refs(v)
    return refs


def resolve_internal(href: str) -> tuple[Path, str] | None:
    """Map an internal href to (file in public/, fragment). None when the target is missing."""
    path, _, frag = href.partition("#")
    path = path.split("?")[0]
    target = OUT / path.lstrip("/")
    if path.endswith("/") or path == "":
        target = target / "index.html"
    return (target, frag) if target.is_file() else None


def check() -> int:
    errors: list[str] = []
    warns: list[str] = []

    def err(where: str, msg: str) -> None:
        errors.append(f"  {where}: {msg}")

    docs: dict[str, Doc] = {}
    for slug, p in PAGES.items():
        d = Doc()
        d.feed(out_file(p).read_text(encoding="utf-8"))
        docs[slug] = d

    # site-level freshness
    newest = max(p["updated"] for p in PAGES.values())
    if SITE["updated"] != newest:
        err("site.py", f"SITE['updated'] {SITE['updated']} must equal the newest page date {newest}")

    titles, descs, h1s = {}, {}, {}
    id_cache = {slug: d.ids for slug, d in docs.items()}
    by_file = {out_file(p): slug for slug, p in PAGES.items()}

    for slug, p in PAGES.items():
        d = docs[slug]
        label = page_path(p)
        # head
        if d.lang != "en":
            err(label, f"html lang is {d.lang!r}")
        h1 = [t for lv, t in d.headings if lv == 1]
        if len(h1) != 1:
            err(label, f"expected one h1, found {len(h1)}")
        title = d.title.strip()
        if len(title) > TITLE_MAX:
            err(label, f"title is {len(title)} chars (max {TITLE_MAX}): {title}")
        if indexable(p):
            desc = d.meta.get("description", "")
            if not DESC_MIN <= len(desc) <= DESC_MAX:
                err(label, f"description is {len(desc)} chars (need {DESC_MIN}-{DESC_MAX}): {desc}")
            ogt = d.meta.get("og:title", "")
            if len(ogt) > OG_TITLE_MAX:
                err(label, f"og:title is {len(ogt)} chars (max {OG_TITLE_MAX})")
            canon = [l["href"] for l in d.links if l.get("rel") == "canonical"]
            if canon != [abs_url(page_path(p))]:
                err(label, f"canonical {canon} != {abs_url(page_path(p))}")
            for k in ("og:title", "og:description", "og:url", "og:image", "og:image:alt", "twitter:card", "twitter:image", "theme-color"):
                if not d.meta.get(k):
                    err(label, f"missing meta {k}")
            if d.meta.get("og:url") != abs_url(page_path(p)):
                err(label, "og:url differs from canonical")
            titles.setdefault(title, []).append(label)
            descs.setdefault(d.meta.get("description", ""), []).append(label)
            h1s.setdefault(h1[0] if h1 else "", []).append(label)
        elif "noindex" not in d.meta.get("robots", ""):
            err(label, "404 page must be noindex")

        # words
        if p["kind"] in MIN_WORDS and words(d.text) < MIN_WORDS[p["kind"]]:
            err(label, f"{words(d.text)} visible words (need {MIN_WORDS[p['kind']]})")

        # structure
        levels = [lv for lv, _ in d.headings]
        for a, b in zip(levels, levels[1:]):
            if b > a + 1:
                err(label, f"heading level jumps from h{a} to h{b}")
        for t, src in d.scripts:
            if t != "application/ld+json" or src:
                err(label, f"script not allowed: type={t} src={src}")
        for bad in ("iframe", "form", "input", "button", "video", "audio", "object", "embed"):
            if d.tags.get(bad):
                err(label, f"<{bad}> not allowed")
        for tag in BOLD_TAGS:
            if d.tags.get(tag):
                err(label, f"<{tag}> used (bold as decoration; use headings)")
        for l in d.links:
            href = l.get("href", "")
            if l.get("rel") in ("stylesheet", "preload", "icon", "apple-touch-icon", "alternate") and href.startswith("http"):
                host = urlparse(href).hostname
                if host != urlparse(SITE["url"]).hostname:
                    err(label, f"external resource link {href}")
            if href.startswith("/") and not resolve_internal(href):
                err(label, f"link target missing: {href}")

        # images
        for im in d.imgs:
            src = im.get("src", "")
            if "alt" not in im:
                err(label, f"img without alt attribute: {src}")
            fpath = STATIC / src.lstrip("/")
            if not src.startswith("/") or not fpath.is_file():
                err(label, f"img file missing: {src}")
                continue
            w, h = int(im.get("width", 0)), int(im.get("height", 0))
            nw, nh = image_size(src)
            if not w or not h or abs(w / h - nw / nh) > 0.01:
                err(label, f"img {src} width/height {w}x{h} does not match file ratio {nw}x{nh}")
            if fpath.stat().st_size > IMG_MAX_KB * 1024:
                err(label, f"img {src} is {fpath.stat().st_size // 1024} KB (max {IMG_MAX_KB})")

        # links
        for a in d.anchors:
            href = a["href"]
            if not href:
                err(label, "anchor without href")
                continue
            if not (a["text"] or a["label"] or a["hidden"]):
                err(label, f"link without accessible name: {href}")
            if href.startswith("#"):
                if href[1:] and href[1:] not in d.ids:
                    err(label, f"anchor {href} has no target")
            elif href.startswith("/") or href.startswith(SITE["url"]):
                local = href[len(SITE["url"]) :] if href.startswith(SITE["url"]) else href
                hit = resolve_internal(local)
                if not hit:
                    err(label, f"broken internal link {href}")
                elif hit[1]:
                    tslug = by_file.get(hit[0])
                    if tslug and hit[1] not in id_cache[tslug]:
                        err(label, f"link {href}: fragment not found")
            elif href.startswith("http"):
                host = urlparse(href).hostname
                if host not in SITE["allowed_hosts"]:
                    err(label, f"external host not allowed: {href}")
            else:
                err(label, f"unsupported link form {href}")

        # json-ld
        if indexable(p):
            if len(d.ld) != 1:
                err(label, f"expected one JSON-LD block, found {len(d.ld)}")
            for raw in d.ld:
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as e:
                    err(label, f"JSON-LD does not parse: {e}")
                    continue
                graph = data.get("@graph", [])
                ids = [n.get("@id") for n in graph if "@id" in n]
                if len(ids) != len(set(ids)):
                    err(label, "duplicate @id in JSON-LD")
                for ref in ld_refs(graph):
                    if ref not in ids:
                        err(label, f"JSON-LD reference {ref} does not resolve")
                types = {n.get("@type") for n in graph}
                need = {"Organization", "WebSite"} | ({"SoftwareApplication", "BreadcrumbList"} if p["kind"] == "app" else set())
                if p.get("faq"):
                    need.add("FAQPage")
                for t in need - types:
                    err(label, f"JSON-LD missing {t}")
                for n in graph:
                    if n.get("@type") == "FAQPage":
                        qs = [q["name"] for q in n["mainEntity"]]
                        if qs != [q for q, _ in p["faq"]]:
                            err(label, "FAQPage questions differ from content faq")
                        for q in qs:
                            if q not in [t for _, t in d.headings]:
                                err(label, f"FAQ question not visible as heading: {q}")
                    if n.get("@type") == "SoftwareApplication":
                        for k in ("name", "description", "applicationCategory", "operatingSystem", "offers", "downloadUrl", "image"):
                            if not n.get(k):
                                err(label, f"SoftwareApplication missing {k}")

        # required content
        if "Reblucky Software" not in d.text:
            err(label, "page does not name Reblucky Software")
        if indexable(p) and "Last updated" not in d.text:
            err(label, "missing Last updated line")
        if p["kind"] == "app":
            hrefs = [a["href"] for a in d.anchors]
            for k in ("play_url", "official_url"):
                if p[k] not in hrefs:
                    err(label, f"missing link to {p[k]}")
            if "Not included" not in dict(p["facts"]):
                err(label, "facts table needs a Not included row")
            if not p["compare"].keys() >= set(PAGES[""]["compare_rows"]):
                err(label, "compare cells do not cover the home comparison rows")

        # size
        kb = out_file(p).stat().st_size / 1024
        if kb > HTML_MAX_KB:
            err(label, f"html is {kb:.0f} KB (max {HTML_MAX_KB})")

        # lint: accuracy, identity, humanizer
        allow = p.get("lint_allow", [])
        texts = {
            "text": d.text,
            "title": title,
            "description": d.meta.get("description", ""),
            "og:title": d.meta.get("og:title", ""),
            "alt": " | ".join(im.get("alt", "") for im in d.imgs),
        }
        for raw in d.ld:
            try:
                texts["json-ld"] = " | ".join(ld_strings(json.loads(raw)))
            except json.JSONDecodeError:
                pass
        rules = ACCURACY + ACCURACY_PAGE.get(slug, []) + IDENTITY + HUMANIZER
        for where, text in texts.items():
            for a in allow:
                text = text.replace(a, " ")
            for rx, why in rules:
                for m in re.finditer(rx, text, re.I):
                    err(label, f"{why} in {where}: {snippet(text, m)}")
            for rx, why in HUMANIZER_WARN:
                for m in re.finditer(rx, text):
                    warns.append(f"  {label}: {why} in {where}: {snippet(text, m)}")

    for kind, table in (("title", titles), ("description", descs), ("h1", h1s)):
        for k, pages_ in table.items():
            if len(pages_) > 1:
                err("site", f"duplicate {kind} on {pages_}: {k}")

    # css
    css_kb = (OUT / "style.css").stat().st_size / 1024
    if css_kb > 25:
        err("style.css", f"{css_kb:.0f} KB (max 25)")
    if re.search(r"https?://", (OUT / "style.css").read_text(encoding="utf-8")):
        err("style.css", "references an external URL")

    # sitemap, robots, llms
    try:
        tree = ET.parse(OUT / "sitemap.xml")
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        got = {u.find("s:loc", ns).text: u.find("s:lastmod", ns).text for u in tree.getroot().findall("s:url", ns)}
        want = {abs_url(page_path(p)): p["updated"] for p in PAGES.values() if indexable(p)}
        if got != want:
            err("sitemap.xml", f"entries differ from pages: {sorted(set(got.items()) ^ set(want.items()))}")
    except ET.ParseError as e:
        err("sitemap.xml", f"does not parse: {e}")
    if f"Sitemap: {abs_url('/sitemap.xml')}" not in (OUT / "robots.txt").read_text():
        err("robots.txt", "missing Sitemap line")
    for name in ("llms.txt", "llms-full.txt"):
        text = (OUT / name).read_text(encoding="utf-8")
        for allowed in (a for pg in PAGES.values() for a in pg.get("lint_allow", [])):
            text = text.replace(allowed, " ")
        for rx, why in HUMANIZER[:2] + ACCURACY:
            for m in re.finditer(rx, text, re.I):
                err(name, f"{why}: {snippet(text, m)}")
        for u in re.findall(r"\((https://awesome-android-tv-apps\.github\.io[^)\s]*)\)", text):
            if not resolve_internal(u[len(SITE["url"]) :]) and not (OUT / u[len(SITE["url"]) :].lstrip("/")).is_file():
                err(name, f"broken link {u}")

    if warns:
        print("warnings:")
        print("\n".join(sorted(set(warns))))
    if errors:
        print(f"{len(errors)} error(s):")
        print("\n".join(errors))
        return 1
    print(f"check passed: {len(PAGES)} pages, {sum(words(d.text) for d in docs.values())} words")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="enforce SITE-SPEC.md after building")
    args = ap.parse_args()
    build()
    return check() if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
