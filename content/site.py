"""Site-wide facts. Every other content file reads from here, never the reverse."""

SITE = {
    "url": "https://awesome-android-tv-apps.github.io",
    "name": "Awesome Android TV Apps",
    "brand": "Awesome",
    "brand_sub": "Android TV Apps",
    "publisher": "Reblucky Software",
    "publisher_url": "https://rebluckysoftware.gitlab.io/",
    "play_developer_url": "https://play.google.com/store/apps/developer?id=Reblucky+Software",
    "github_org_url": "https://github.com/awesome-android-tv-apps",
    "touch_icon": "/img/apple-touch-icon.png",
    "og_home": "/img/og-home.jpg",
    "theme_color": "#14171c",
    # Google Analytics 4 measurement ID. build.py renders the gtag.js snippet from it on every page.
    "ga_id": "G-Z58G7P06BB",
    "repo_url": "https://github.com/awesome-android-tv-apps/awesome-android-tv-apps.github.io",
    "locale": "en_US",
    "lang": "en",
    # ISO date of the last content change. Sitemap lastmod and the visible
    # "Last updated" line come from here (SITE-SPEC.md, Freshness rules).
    "published": "2026-10-29",
    "updated": "2026-10-29",
    "nav": [
        ("Streamova", "/streamova/"),
        ("Trimo", "/trimo/"),
        ("AirPlay Receiver", "/airplay-receiver/"),
        ("About", "/about/"),
    ],
    "footer_blurb": (
        "Reblucky Software makes and publishes the apps on this site. "
        "The pages describe only these apps, with the facts from their Google Play listings."
    ),
    "trademark": (
        "Android TV, Google TV and Google Play are trademarks of Google LLC. "
        "AirPlay, iPhone, iPad and Mac are trademarks of Apple Inc. "
        "The apps on this site are made by Reblucky Software and are not affiliated with, "
        "endorsed or sponsored by Google, Apple or any NAS or TV manufacturer."
    ),
    # External hosts the pages may link to (build.py --check rejects anything else).
    "allowed_hosts": [
        "play.google.com",
        "rebluckysoftware.gitlab.io",
        "streamova.gitlab.io",
        "trimo.gitlab.io",
        "airplaymirrorreceiver.gitlab.io",
        "github.com",
        "policies.google.com",
    ],
}

# Order used for navigation, home tiles, comparison columns, "more from" lists and llms.txt.
APP_ORDER = ["streamova", "trimo", "airplay-receiver"]
