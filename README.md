# Awesome Android TV Apps

Source of https://awesome-android-tv-apps.github.io/, the website for three Android TV apps made by Reblucky Software: [Streamova](https://play.google.com/store/apps/details?id=com.reblucky.streamova), [Trimo](https://play.google.com/store/apps/details?id=storage.cache.debloat.cleaner) and [AirPlay Receiver](https://play.google.com/store/apps/details?id=com.reblucky.airplaymirror).

Reblucky Software publishes this site. It is the maker's own site, not an independent review site, and it says so on every page.

## Build

```sh
python3 build.py            # writes public/
python3 build.py --check    # builds, then enforces SITE-SPEC.md (exit 1 on any error)
python3 -m http.server 8095 -d public
```

`build.py` uses only the Python standard library (3.9 or newer; CI runs 3.12). GitHub Actions runs `--check` and deploys `public/` to GitHub Pages on every push to `main`.

The pages carry one third-party script, the Google Analytics 4 tag (`ga_id` in `content/site.py`). When previewing locally, block `googletagmanager.com` and `google-analytics.com` so test visits are not counted.

## Layout

| Path | Purpose |
|---|---|
| `content/site.py` | Site-wide facts: publisher, navigation, trademark line, allowed external hosts |
| `content/<page>.py` | One `PAGE` dict per page: copy, facts table, FAQ, screenshots, schema fields |
| `static/` | CSS, Barlow fonts (SIL OFL), favicon and images copied to `public/` as they are; `*.webp.json` files are image provenance notes and are not published |
| `build.py` | Generator, JSON-LD, sitemap, `llms.txt`, `llms-full.txt` and the checks |
| `SITE-SPEC.md` | Accuracy, identity, SEO and writing rules the checks enforce (Turkish) |
| `PRODUCT.md` | Product context for design work (Turkish) |
| `DESIGN.md` | The visual system, "The Rating Plate", with `.impeccable/design.json` for tooling |

## Changing content

Edit the page in `content/`, set its `updated` date and the newest date in `content/site.py`, then run `python3 build.py --check`. The check fails on a missing meta field, a broken link, an out-of-range title or description, JSON-LD that does not resolve, banned claims and stock AI phrasing.
