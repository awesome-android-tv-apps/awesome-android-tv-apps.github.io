"""AirPlay Receiver page. Facts come from the Play listing (airplay/android-airplay-server/fastlane/metadata/android/en-US)
and airplay/site-seo-spec.md. Never write "AirPlay 2", never write "no subscription", never write "no analytics"."""

PAGE = {
    "slug": "airplay-receiver",
    "kind": "app",
    "name": "AirPlay Receiver",
    "full_name": "AirPlay Mirror Receiver",
    "play_title": "AirPlay Receiver: iPhone to TV",
    "short": "Mirror an iPhone, iPad or Mac to the TV",
    "job": "Mirror an iPhone to the TV",
    "blurb": (
        "Mirrors an iPhone, iPad or Mac to an Android TV over Wi-Fi, with no Apple TV "
        "or cable and nothing to install on the phone."
    ),
    "accent": "#3da9ff",
    "title": "AirPlay Receiver for Android TV: Mirror an iPhone, No Apple TV",
    "og_title": "AirPlay Receiver for Android TV: mirror an iPhone",
    "description": (
        "AirPlay Mirror Receiver turns an Android TV or Google TV into an AirPlay receiver. "
        "Mirror an iPhone, iPad or Mac over Wi-Fi with no Apple TV, up to 4K."
    ),
    "h1": "AirPlay Receiver for Android TV: mirror an iPhone with no Apple TV",
    "lead": (
        "<p>AirPlay Mirror Receiver turns an Android TV or Google TV into an AirPlay receiver for your "
        "iPhone, iPad or Mac. Start Screen Mirroring on the Apple device and its screen and sound appear "
        "on the TV over your home Wi-Fi. You do not need an Apple TV, a cable or an extra app on the "
        "phone.</p>"
    ),
    "summary": (
        "AirPlay Mirror Receiver is an AirPlay-compatible screen mirroring receiver for Android TV and "
        "Google TV. An iPhone, iPad or Mac mirrors its screen and audio to the TV over the local Wi-Fi "
        "network with no Apple TV."
    ),
    "chips": ["Android 7.0 or newer", "1080p to 4K", "No ads", "No accounts"],
    "compare": {
        "Job": "Mirror an iPhone, iPad or Mac screen to the TV, and play AirPlay video and music",
        "Runs on": "Android TV and Google TV, Android 7.0 or newer, with Google Play",
        "You also need": "An iPhone, iPad or Mac on the same Wi-Fi network",
        "Price": "Free 5-minute sessions. Pro (monthly or yearly subscription, or one-time lifetime purchase) removes the limit",
        "Ads and accounts": "None",
        "Usage data": "Anonymous usage statistics only",
        "Languages": "13",
    },
    "package": "com.reblucky.airplaymirror",
    "play_url": "https://play.google.com/store/apps/details?id=com.reblucky.airplaymirror",
    "official_url": "https://airplaymirrorreceiver.gitlab.io/android-tv/",
    "official_label": "AirPlay Receiver website",
    "privacy_url": "https://airplaymirrorreceiver.gitlab.io/android-tv/privacy.html",
    "schema": {
        "category": "UtilitiesApplication",
        "os": "Android TV, Google TV (Android 7.0 or newer)",
    },
    "images": {
        "card": "/img/airplay-card.webp",
        "card_alt": "AirPlay Mirror Receiver: mirror your iPhone or iPad screen and audio to an Android TV over Wi-Fi",
        "banner": "/img/airplay-banner.webp",
        "banner_alt": "AirPlay Mirror Receiver app banner as shown on the Android TV home screen",
        "icon": "/img/airplay-icon-256.webp",
        "icon512": "/img/airplay-icon-512.png",
        "og": "/img/og-airplay.jpg",
        "og_alt": "AirPlay Mirror Receiver: mirror your iPhone screen to Android TV",
    },
    "facts": [
        ("What it is", "AirPlay-compatible screen mirroring receiver for Android TV and Google TV."),
        ("Made by", "Reblucky Software, the developer who also publishes this site."),
        ("Platform", "Android TV or Google TV on Android 7.0 or newer with Google Play. Phones and tablets cannot act as the receiver."),
        ("Sender", "An iPhone, iPad or Mac with Screen Mirroring in Control Center, on the same Wi-Fi network as the TV. Nothing to install on the Apple device."),
        ("Quality", "1080p, 1440p or 4K at 30 or 60 FPS, chosen in Quick Settings."),
        ("Price", "Free mirroring sessions run for 5 minutes with every quality option available. Pro removes the limit as a monthly or yearly subscription or a one-time lifetime purchase."),
        ("Privacy", "No accounts and no ads. Screen and audio stay on your local network. Anonymous usage statistics only (Firebase Analytics, advertising ID disabled)."),
        ("Languages", "13 app languages, following the TV's system language: English, Turkish, Simplified and Traditional Chinese, Spanish, Hindi, Arabic, Portuguese, Russian, French, German, Japanese and Indonesian."),
        ("Not included", "Mirroring of DRM-protected apps such as Netflix, Prime Video, Disney+ and Apple TV+."),
    ],
    "feature_list": [
        "Screen mirroring with sound from iPhone, iPad and Mac",
        "1080p, 1440p and 4K at 30 or 60 FPS",
        "AirPlay video playback in the receiver's own player",
        "Music over AirPlay with cover art",
        "Optional PIN for new connections",
    ],
    "sections": [
        {
            "id": "how-to-mirror",
            "h2": "How to mirror an iPhone to an Android TV",
            "html": """
<ol class="steps">
<li><h3>Open the receiver on the TV</h3><p>Open AirPlay Mirror Receiver on your Android TV or Google TV. Keep the TV and the Apple device on the same Wi-Fi network.</p></li>
<li><h3>Start Screen Mirroring</h3><p>On an iPhone or iPad, open Control Center and tap Screen Mirroring. On a Mac, use Screen Mirroring in Control Center.</p></li>
<li><h3>Pick your TV</h3><p>Choose the receiver from the list. The screen and the sound appear on the TV.</p></li>
</ol>""",
        },
        {
            "id": "what-it-does",
            "h2": "What AirPlay Mirror Receiver does",
            "html": """
<div class="prose">
<ul>
<li>Mirrors the screen with sound, decoded in hardware (H.264 and H.265).</li>
<li>Lets you choose the picture quality in Quick Settings: 1080p, 1440p or 4K at 30 or 60 FPS. Higher settings can stutter depending on your network and TV.</li>
<li>Plays a video sent with the AirPlay button in a supported app. It plays in the receiver's own player, where you can rotate it, change the scaling (Best fit, Stretch, Crop) or download it.</li>
<li>Plays music over AirPlay with cover art and track info.</li>
<li>Lets you give the receiver its own name and require a PIN for new connections when you share the network.</li>
<li>Works with the TV remote on every screen.</li>
</ul>
<p>Use it on an Android TV box, smart TV or projector to show photos, home videos, slides or games from your iPhone on the big screen.</p>
</div>""",
        },
        {
            "id": "screenshots",
            "h2": "AirPlay Mirror Receiver on a TV screen",
            "gallery": [
                ("/img/airplay-dashboard.webp", "Receiver dashboard on Android TV showing how to start screen mirroring from an iPhone", "Receiver dashboard"),
                ("/img/airplay-settings.webp", "Quick Settings with resolution, frame rate and PIN options", "Quick Settings"),
                ("/img/airplay-video.webp", "iPhone screen mirrored to Android TV while playing a movie", "Playing a movie"),
            ],
        },
        {
            "id": "limits",
            "h2": "What it cannot mirror",
            "html": """
<div class="prose">
<p>Apps that protect their content with DRM, such as Netflix, Prime Video, Disney+ and Apple TV+, block mirroring to other screens. Other apps and the rest of your screen mirror normally.</p>
<p>The receiver has to be an Android TV or Google TV device. A phone or tablet cannot take that role, and nothing is installed on the iPhone or iPad.</p>
</div>""",
        },
        {
            "id": "price-privacy",
            "h2": "Free and Pro",
            "html": """
<div class="prose">
<p>Free mirroring sessions stop after 5 minutes, and every quality option is available in the free version. Pro removes the limit. You can get Pro as a monthly or yearly subscription, or as a one-time lifetime purchase that you can restore on the same Google account. Subscriptions renew automatically until you cancel them in Google Play.</p>
<p>There are no accounts and no ads. Your screen and audio stay on your local network. The app sends anonymous usage statistics (Firebase Analytics) with the advertising ID disabled. The <a href="https://airplaymirrorreceiver.gitlab.io/android-tv/privacy.html">AirPlay Receiver privacy policy</a> has the details.</p>
</div>""",
        },
    ],
    "faq_heading": "Questions about AirPlay Mirror Receiver",
    "faq": [
        (
            "How do I AirPlay from my iPhone to an Android TV?",
            "Install AirPlay Mirror Receiver on the TV and open it. Then open Control Center on the iPhone, tap Screen Mirroring and pick the receiver from the list.",
        ),
        (
            "Do I need an Apple TV or extra hardware?",
            "No. The app is the AirPlay receiver, so the Android TV does the work itself. No Apple TV, Chromecast, HDMI adapter or dongle is needed.",
        ),
        (
            "Which Android TV devices does it support?",
            "Any Android TV or Google TV device on Android 7.0 or newer with Google Play, including TV boxes, smart TVs, streaming sticks and projectors. Phones and tablets cannot act as the receiver.",
        ),
        (
            "Does it work without internet?",
            "Mirroring runs over your local Wi-Fi network, so the TV and the Apple device only need to be on the same network. You need internet to install the app from Google Play.",
        ),
        (
            "Is AirPlay Mirror Receiver free?",
            "Mirroring is free in sessions of 5 minutes, with every quality option available. A monthly or yearly subscription, or a one-time lifetime purchase that you can restore on the same Google account, removes the time limit.",
        ),
        (
            "Can I mirror Netflix, Prime Video, Disney+ or Apple TV+?",
            "No. Apps that use DRM block mirroring to other screens. Photos, videos, slides, games and the rest of your screen mirror normally.",
        ),
        (
            "Can I send a video or music instead of mirroring the screen?",
            "Yes. A video sent with the AirPlay button in a supported app plays in the receiver's own player. Music over AirPlay plays with cover art and track info.",
        ),
        (
            "Does it work with a Mac?",
            "Yes. On a Mac, use Screen Mirroring in Control Center and pick the receiver, the same way as on an iPhone or iPad.",
        ),
        (
            "What data does AirPlay Mirror Receiver collect?",
            "Anonymous usage statistics through Firebase Analytics, with the advertising ID disabled. There are no accounts and no ads, and your screen and audio never leave your local network.",
        ),
    ],
    "trademark_extra": (
        "AirPlay is a trademark of Apple Inc. AirPlay Mirror Receiver is not affiliated with, endorsed or sponsored by Apple."
    ),
    "updated": "2026-10-29",
}
