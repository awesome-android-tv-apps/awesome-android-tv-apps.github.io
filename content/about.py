"""About page: identity, sources and what the website itself does."""

PAGE = {
    "slug": "about",
    "kind": "about",
    "title": "About Reblucky Software: Who Makes These Android TV Apps",
    "description": (
        "Reblucky Software develops and publishes Streamova, Trimo and AirPlay Receiver. "
        "This site is published by the maker and is not an independent review site."
    ),
    "h1": "About Reblucky Software",
    "crumb": "About",
    "lead": (
        "<p>Reblucky Software develops and publishes Streamova, Trimo and AirPlay Receiver, three apps "
        "for Android TV and Google TV. It also makes other Android apps, web tools and an iPhone "
        "app.</p>"
    ),
    "sections": [
        {
            "id": "who",
            "h2": "Who runs this site",
            "html": """
<div class="prose">
<p>Reblucky Software publishes this site and makes the apps it describes. It is the maker's own site, not an independent review site. It lists only these three apps and does not compare them with apps from other developers.</p>
<p>The developer's other work is on the <a href="https://rebluckysoftware.gitlab.io/">Reblucky Software developer site</a>. The <a href="https://play.google.com/store/apps/developer?id=Reblucky+Software">Google Play developer page</a> shows the Android apps.</p>
</div>""",
        },
        {
            "id": "apps",
            "h2": "The apps",
            "html": """
<div class="prose">
<ul>
<li><a href="/streamova/">Streamova</a> plays movies and shows from a NAS, shared folder or USB drive on Android TV.</li>
<li><a href="/trimo/">Trimo</a> frees up storage on Android TV and disables pre-installed apps.</li>
<li><a href="/airplay-receiver/">AirPlay Receiver</a> mirrors an iPhone, iPad or Mac to an Android TV.</li>
</ul>
</div>""",
        },
        {
            "id": "sources",
            "h2": "Where the facts come from",
            "html": """
<div class="prose">
<p>Each page uses the facts from the app's Google Play listing, its official website and its privacy policy. If a page here disagrees with the Play listing or the privacy policy, the listing and the policy take precedence.</p>
<ul>
<li>Streamova: <a href="https://play.google.com/store/apps/details?id=com.reblucky.streamova">Google Play</a>, <a href="https://streamova.gitlab.io/">website</a> and <a href="https://streamova.gitlab.io/privacy.html">privacy policy</a></li>
<li>Trimo: <a href="https://play.google.com/store/apps/details?id=storage.cache.debloat.cleaner">Google Play</a>, <a href="https://trimo.gitlab.io/">website</a> and <a href="https://trimo.gitlab.io/privacy.html">privacy policy</a></li>
<li>AirPlay Receiver: <a href="https://play.google.com/store/apps/details?id=com.reblucky.airplaymirror">Google Play</a>, <a href="https://airplaymirrorreceiver.gitlab.io/android-tv/">website</a> and <a href="https://airplaymirrorreceiver.gitlab.io/android-tv/privacy.html">privacy policy</a></li>
</ul>
</div>""",
        },
        {
            "id": "contact",
            "h2": "Contact and support",
            "html": """
<div class="prose">
<p>Questions about an app go through the developer contact details on its Google Play listing.</p>
</div>""",
        },
        {
            "id": "website",
            "h2": "About this website",
            "html": """
<div class="prose">
<p>This website uses Google Analytics to count visits. The Google tag loads from Google's servers and sets cookies in your browser. Google receives usage data such as the pages you open, your approximate location and your device and browser type, and describes how it handles that data on its <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use our services</a> page. The site loads no other third-party scripts, fonts or images.</p>
<p>It is a static site hosted on GitHub Pages, so GitHub's own privacy statement applies to its server logs. The source is public in the <a href="https://github.com/awesome-android-tv-apps/awesome-android-tv-apps.github.io">awesome-android-tv-apps</a> organization on GitHub.</p>
</div>""",
        },
    ],
    "updated": "2026-10-29",
}
