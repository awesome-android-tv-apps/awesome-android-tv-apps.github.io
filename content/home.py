"""Home page. Comparison cells come from each app module's `compare` dict, so a fact has one home."""

PAGE = {
    "slug": "",
    "kind": "home",
    "title": "Android TV Apps by Reblucky: Streamova, Trimo, AirPlay Receiver",
    "og_title": "Android TV apps by Reblucky Software",
    "description": (
        "Reblucky Software makes Streamova, Trimo and AirPlay Receiver for Android TV and Google TV: "
        "play NAS movies, free up storage and mirror an iPhone."
    ),
    "h1": "Android TV apps by Reblucky Software",
    "lead": (
        "<p>Reblucky Software makes three apps for Android TV and Google TV. Streamova plays movies "
        "from a NAS or USB drive, Trimo frees up storage and disables bloatware, and AirPlay Receiver "
        "mirrors an iPhone, iPad or Mac to the TV.</p>"
    ),
    "hero_facts": [
        ("Made by", "Reblucky Software"),
        ("This site", "Published by the developer. It describes only these three apps."),
    ],
    "tiles_heading": "The three apps",
    "play_label": "Get it on Google Play",
    "details_label": "Details",
    "compare_heading": "The three apps side by side",
    "compare_rows": [
        "Job",
        "Runs on",
        "You also need",
        "Price",
        "Ads and accounts",
        "Usage data",
        "Languages",
    ],
    "common_heading": "What the apps have in common",
    "common": (
        "<p>All three apps work with the TV remote. None of "
        "them shows ads or asks for an account, and each one reports only anonymous usage statistics "
        "with the advertising ID turned off.</p>"
        "<p>They differ in price. Streamova and AirPlay Receiver are free to try for 5 minutes per "
        "session. Trimo is free to use, apart from the disable and remove actions in Debloat.</p>"
    ),
    "maker_heading": "Who makes these apps",
    "maker": (
        "<p>Reblucky Software develops and publishes all three apps. It also makes other Android apps, "
        "web tools and an iPhone app. The <a href=\"https://rebluckysoftware.gitlab.io/\">Reblucky Software "
        "developer site</a> lists them, and the <a href=\"https://play.google.com/store/apps/developer?id=Reblucky+Software\">"
        "Google Play developer page</a> shows the Android apps. More about the developer is on the "
        "<a href=\"/about/\">About page</a>.</p>"
    ),
    "faq_heading": "Common questions",
    "faq": [
        (
            "How do I play movies from a NAS on Android TV?",
            "Install <a href=\"/streamova/\">Streamova</a> on the TV, add your NAS or computer as a source and browse to a movie. Streamova opens SMB2 and SMB3 shares directly, so no media server is needed. USB drives and the TV's own storage work too.",
        ),
        (
            "How do I free up storage on an Android TV?",
            "<a href=\"/trimo/\">Trimo</a> shows what uses the space, clears junk files and app caches, uninstalls apps you no longer use and disables pre-installed apps. It needs no root and no computer, and you do everything with the TV remote.",
        ),
        (
            "How do I mirror an iPhone to an Android TV?",
            "Open <a href=\"/airplay-receiver/\">AirPlay Receiver</a> on the TV, then tap Screen Mirroring in Control Center on the iPhone or iPad and pick the TV. You do not need an Apple TV, and nothing is installed on the phone.",
        ),
        (
            "Are the apps free?",
            "Each app is free to install. Streamova and AirPlay Receiver include 5 minutes of free use per session. Streamova unlocks with a one-time purchase and has no subscription. AirPlay Receiver Pro is a monthly or yearly subscription or a one-time lifetime purchase. Trimo is free to use, and only the disable and remove actions in Debloat need a one-time purchase.",
        ),
        (
            "Do the apps show ads or need an account?",
            "No. None of the three shows ads or asks for an account. Each one reports only anonymous usage statistics, with the advertising ID turned off.",
        ),
        (
            "Which Android TV versions do they support?",
            "Streamova and AirPlay Receiver need Android 7.0 or newer. Trimo runs on Android 5.0 or newer, and its Debloat actions need Android 8 or newer. All three are built for Android TV and Google TV devices.",
        ),
        (
            "Is this an independent review site?",
            "No. Reblucky Software publishes this site and also makes the three apps on it. The site lists only its own apps and does not compare them with apps from other developers.",
        ),
    ],
    "updated": "2026-10-29",
    "lint_allow": ["Is this an independent review site?"],
}
