"""Trimo page. Facts come from the Play listing (android-tv-cleaner/store/listings/en-US) and trimo.gitlab.io locales/en.json."""

PAGE = {
    "slug": "trimo",
    "kind": "app",
    "name": "Trimo",
    "play_title": "Trimo: TV Cleaner & Debloat",
    "short": "Free up storage and disable bloatware",
    "job": "Free up TV storage",
    "blurb": (
        "Shows what fills the TV, clears junk and caches, uninstalls apps and disables "
        "pre-installed ones, all without root or a computer."
    ),
    "accent": "#f4b63f",
    "title": "Trimo: Free Up Storage and Disable Bloatware on Android TV",
    "description": (
        "Trimo is a storage cleaner and debloater for Android TV and Google TV. Clear junk and "
        "caches, uninstall apps and disable bloatware with no root and no computer."
    ),
    "h1": "Trimo: free up storage on your Android TV",
    "lead": (
        "<p>Trimo is a storage cleaner and debloater for Android TV and Google TV. It shows where the "
        "space went, clears junk files and app caches, helps you uninstall apps you no longer use and "
        "disables pre-installed apps. It needs no root and no computer, and you control it with the "
        "TV remote.</p>"
    ),
    "summary": (
        "Trimo is a storage cleaner and system-app manager for Android TV and Google TV. It measures "
        "where the space went, clears junk files and app caches, uninstalls unused apps and reversibly "
        "disables pre-installed apps, with no root and no computer."
    ),
    "chips": ["Android 5.0 or newer", "No root", "No ads", "No accounts"],
    "compare": {
        "Job": "Free up storage: clear junk and caches, uninstall apps, disable pre-installed apps",
        "Runs on": "Android TV and Google TV, Android 5.0 or newer (Debloat needs Android 8)",
        "You also need": "Nothing else. Debloat and Cache need USB debugging turned on once",
        "Price": "Free. Disabling or removing system apps in Debloat is a one-time purchase. No subscription",
        "Ads and accounts": "None",
        "Usage data": "Anonymous usage statistics only",
        "Languages": "10",
    },
    "package": "storage.cache.debloat.cleaner",
    "play_url": "https://play.google.com/store/apps/details?id=storage.cache.debloat.cleaner",
    "official_url": "https://trimo.gitlab.io/",
    "official_label": "Trimo website",
    "privacy_url": "https://trimo.gitlab.io/privacy.html",
    "schema": {
        "category": "UtilitiesApplication",
        "os": "Android TV, Google TV (Android 5.0 or newer; Debloat needs Android 8 or newer)",
    },
    "images": {
        "card": "/img/trimo-card.webp",
        "card_alt": "Trimo, the Android TV cleaner and debloater, with a storage breakdown on a TV screen",
        "banner": "/img/trimo-banner.webp",
        "banner_alt": "Trimo app banner as shown on the Android TV home screen",
        "icon": "/img/trimo-icon-256.webp",
        "icon512": "/img/trimo-icon-512.png",
        "og": "/img/og-trimo.jpg",
        "og_alt": "Trimo: Android TV cleaner and debloater",
    },
    "facts": [
        ("What it is", "Storage cleaner and system-app manager for Android TV and Google TV."),
        ("Platform", "Android TV or Google TV on Android 5.0 or newer. Debloat actions need Android 8 or newer."),
        ("Controls", "TV remote only. No phone app, keyboard or computer is needed."),
        ("Price", "Measuring, scanning, deleting files, uninstalling apps, clearing caches, Restore and Undo are free. Disabling or removing system apps in Debloat is a one-time purchase in Google Play. There is no subscription."),
        ("Privacy", "No accounts and no ads. Anonymous usage statistics only, sent through Google Analytics for Firebase, with no advertising ID."),
        ("Languages", "10, following the language of the TV: English, Spanish, Portuguese, Hindi, Arabic, Russian, German, French, Indonesian and Turkish. Other languages show English."),
        ("Not included", "Stopping apps, freeing RAM, speed promises and root access."),
    ],
    "feature_list": [
        "Storage breakdown by category, measured on the TV",
        "Junk, large-file and app-cache cleaning with confirmation",
        "App uninstaller sorted by size with last-used date",
        "Reversible debloat with safety ratings, a journal and Undo all changes",
        "Works with the TV remote, no root and no computer",
    ],
    "sections": [
        {
            "id": "how-it-works",
            "h2": "Clean up your TV in three steps",
            "html": """
<ol class="steps">
<li><h3>Look at the Breakdown</h3><p>Trimo opens on a ring chart of used space by category: apps, system apps, files and media, and system and other. Everything is measured on your TV. If a value cannot be measured, Trimo says "Not measured" instead of guessing.</p></li>
<li><h3>Clean files and apps</h3><p>Scan for junk, browse the largest files by type and pick apps to uninstall. Nothing is deleted before you confirm.</p></li>
<li><h3>Debloat, reversibly</h3><p>Select the recommended pre-installed apps and disable them. If you do not press Keep changes within 15 seconds, the TV reverts the change. Undo all changes brings everything back.</p></li>
</ol>""",
        },
        {
            "id": "screens",
            "h2": "What each screen does",
            "html": """
<div class="prose">
<h3>Breakdown</h3>
<p>Measures used storage by category and shows free space next to the Storage and RAM gauges in the header. It only measures and never changes anything.</p>
<h3>Storage</h3>
<p>Scans shared storage and groups junk that is safe to remove: logs, empty folders and old installer files in Downloads. You can drill down from a file type to single files, largest first. Photos, videos and music are never suggested, although you can mark them by hand. Marked files are deleted only after a confirmation that warns deleted files cannot be recovered.</p>
<h3>Apps</h3>
<p>Lists the apps you installed with their data, cache and APK size and the last-used date when the TV reports it. Select the ones you want gone and Android's own uninstall dialog opens for each one, so Trimo never removes an app on its own.</p>
<h3>Debloat</h3>
<p>Reads every installed package, explains what it is and rates it Safe, Your call, Keep or Protected. You choose which pre-installed apps to disable or remove for the current user, such as screensavers, diagnostics and bug-report services.</p>
<h3>Cache</h3>
<p>Clears the cached files of every app in one step. Accounts, settings and app data stay, and apps rebuild their caches as you use them. Trimo measures the freed space afterwards and never promises a number. It needs the same one-time USB debugging approval as Debloat.</p>
</div>""",
        },
        {
            "id": "screenshots",
            "h2": "Trimo on a TV screen",
            "gallery": [
                ("/img/trimo-breakdown.webp", "Trimo Breakdown screen on Android TV with a ring chart of used storage by category", "Breakdown"),
                ("/img/trimo-storage.webp", "Trimo Storage screen showing junk items, marked files and the file types found on the TV", "Storage"),
                ("/img/trimo-apps.webp", "Trimo Apps screen listing installed apps with their size and last-used date", "Apps"),
                ("/img/trimo-debloat.webp", "Trimo Debloat screen with the one-time ADB setup steps and a list of recommended packages", "Debloat"),
            ],
        },
        {
            "id": "safety",
            "h2": "How Debloat stays safe",
            "html": """
<div class="prose">
<p>Trimo never uses root, never flashes anything and never deletes system files. It only changes the state of a package for the current user, with Android's own package commands.</p>
</div>
<dl class="defs">
<dt>Protected list</dt>
<dd>The home screen, keyboard, Settings, Trimo itself and the core services of known TV brands cannot be selected.</dd>
<dt>Confirm first</dt>
<dd>Every disable or remove asks for confirmation, and the focus starts on Cancel.</dd>
<dt>Journal and 15 seconds</dt>
<dd>Each change is written to a journal before it runs. Afterwards you have 15 seconds to press Keep changes, otherwise the TV reverts it.</dd>
<dt>Undo</dt>
<dd>Restore re-enables one app. Undo all changes re-enables everything Trimo changed.</dd>
</dl>""",
        },
        {
            "id": "usb-debugging",
            "h2": "Set up USB debugging once",
            "html": """
<div class="prose">
<p>Debloat and Cache talk to the TV's own USB debugging service on 127.0.0.1, so that connection never leaves the TV. You turn it on one time:</p>
<ol>
<li>Open Settings, then Device Preferences, then About, and press Build 7 times.</li>
<li>Go back to Settings, open Developer options and turn on USB debugging.</li>
<li>In Trimo, open Debloat or Cache and press Connect. Choose Always allow on the TV.</li>
</ol>
<p>Everything else in Trimo works without it. Debloat actions need Android 8 or newer.</p>
</div>""",
        },
        {
            "id": "limits",
            "h2": "What Trimo does not do",
            "html": """
<div class="prose">
<p>Trimo does not stop apps, kill processes or clear RAM, and it makes no speed promises. It frees storage, which helps when a TV is nearly full, and it removes clutter by disabling apps you never open. Photos, videos and music are never suggested for deletion.</p>
</div>""",
        },
        {
            "id": "price-privacy",
            "h2": "Price and privacy",
            "html": """
<div class="prose">
<p>Trimo is free to use. Measuring, scanning, deleting files, uninstalling apps, clearing caches, Restore and Undo cost nothing. Disabling or removing system apps in Debloat is a one-time purchase in Google Play, and there is no subscription.</p>
<p>Trimo has no ads and no accounts. It sends anonymous usage statistics through Google Analytics for Firebase: which screens and features are used, counts, size ranges and whether an action succeeded. File names, app names, personal data and the advertising ID are never collected. The <a href="https://trimo.gitlab.io/privacy.html">Trimo privacy policy</a> has the details.</p>
<p>Trimo asks for four kinds of access, each for one reason. All files access lets it scan and delete only the files you mark. Usage access shows app sizes and last-used dates. The list of installed apps is the purpose of Apps and Debloat. Internet reaches the TV's own debug service on 127.0.0.1 and sends the anonymous usage statistics. The billing permission comes from the Google Play Billing library.</p>
</div>""",
        },
        {
            "id": "tested-devices",
            "h2": "Tested devices",
            "html": """
<div class="prose">
<p>Trimo has been tested on a Xiaomi Mi Box (Android 9) and on an Android 14 TV emulator. It knows the protected system services of TV brands such as Xiaomi, TCL, Sony, Philips, Hisense and NVIDIA. Other devices should work, but they have not all been tested. Phones and tablets are not targeted, because Trimo is built for the TV interface and the remote.</p>
</div>""",
        },
    ],
    "faq_heading": "Questions about Trimo",
    "faq": [
        (
            "How do I free up space on my Android TV?",
            "Open Trimo's Breakdown to see what uses the space. Then use Storage to delete junk and large files you no longer need, Apps to uninstall unused apps, Cache to clear app caches and Debloat to disable pre-installed apps. Every step asks for confirmation.",
        ),
        (
            "Is Trimo free?",
            "Yes, apart from one thing. Measuring, scanning, deleting files, uninstalling apps, clearing caches, Restore and Undo are free. Disabling or removing system apps in Debloat is a one-time purchase in Google Play, with no subscription.",
        ),
        (
            "Do I need root or a computer?",
            "No. Trimo runs on the TV. For Debloat and Cache you turn on USB debugging once in Developer options and approve the prompt on the TV. Trimo then talks to the TV's own debug service on 127.0.0.1, so no computer or cable is involved.",
        ),
        (
            "Is it safe to disable system apps?",
            "Trimo only offers reversible changes. Protected apps cannot be selected, every action needs confirmation, each change is journaled and you have 15 seconds to revert it. Still, disable only what you understand. The Safe, Your call, Keep and Protected ratings show how risky each app is.",
        ),
        (
            "Will Trimo make my TV faster?",
            "No. Trimo makes no speed promises. It does not stop apps, kill processes or clear RAM. It frees storage, which helps when a TV is nearly full, and it removes clutter by disabling pre-installed apps you never open.",
        ),
        (
            "Does Trimo delete my photos or videos?",
            "Never automatically. The junk scan does not suggest media files. In the file browser you can mark any file by hand, and deletion runs only after a confirmation that warns deleted files cannot be recovered.",
        ),
        (
            "What data does Trimo collect?",
            "Only anonymous usage statistics, sent through Google Analytics for Firebase: which screens and features are used, counts, size ranges and whether an action succeeded. Never file names, app names or personal data, and no advertising ID. There are no accounts or ads, and Google Play handles the one-time purchase.",
        ),
        (
            "Which devices does Trimo support?",
            "Android TV and Google TV devices on Android 5.0 or newer. Debloat actions need Android 8 or newer. Trimo has been tested on a Xiaomi Mi Box (Android 9) and an Android 14 TV emulator.",
        ),
    ],
    "lint_allow": ["Will Trimo make my TV faster?"],
    "trademark_extra": "Trimo is not affiliated with or endorsed by Google.",
    "updated": "2026-10-29",
}
