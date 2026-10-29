"""Streamova page. Facts come from the Play listing (smb-nas-browser/release/store/listings/en-US.txt)."""

PAGE = {
    "slug": "streamova",
    "kind": "app",
    "name": "Streamova",
    "play_title": "Streamova NAS/SMB Video Player",
    "short": "Play movies from a NAS or USB drive",
    "job": "Play movies from your NAS",
    "blurb": (
        "Plays video from SMB2 and SMB3 shares, USB drives and the TV's own storage, "
        "with subtitles and resume, and works without a media server."
    ),
    "accent": "#37d3e7",
    "title": "Streamova: Play Movies From a NAS or USB Drive on Android TV",
    "description": (
        "Streamova plays movies and shows from a NAS, shared folder or USB drive on Android TV "
        "and Google TV. SMB2 and SMB3, subtitles, resume, no ads and no accounts."
    ),
    "h1": "Streamova: play movies from your NAS on Android TV",
    "lead": (
        "<p>Streamova is a video player for Android TV and Google TV that plays movies and shows "
        "straight from a NAS, a shared folder on a computer or a USB drive. It opens SMB2 and SMB3 "
        "shares over your home network and reads the files in place, so nothing is copied to the TV "
        "first and no media server is needed.</p>"
    ),
    "summary": (
        "Streamova is a video player for Android TV and Google TV that plays movies and shows from "
        "SMB2 and SMB3 network shares, USB drives and the TV's own storage, with subtitles, resume and "
        "no media server."
    ),
    "chips": ["Android 7.0 or newer", "SMB2 and SMB3", "No ads", "No accounts"],
    "compare": {
        "Job": "Play movies and shows from a NAS, shared folder or USB drive",
        "Runs on": "Android TV and Google TV, Android 7.0 or newer",
        "You also need": "A NAS or computer with SMB2 or SMB3 on the same network, or a USB drive",
        "Price": "5 free minutes per session, then a one-time purchase. No subscription",
        "Ads and accounts": "None",
        "Usage data": "Anonymous usage statistics only",
        "Languages": "13",
    },
    "package": "com.reblucky.streamova",
    "play_url": "https://play.google.com/store/apps/details?id=com.reblucky.streamova",
    "official_url": "https://streamova.gitlab.io/",
    "official_label": "Streamova website",
    "privacy_url": "https://streamova.gitlab.io/privacy.html",
    "schema": {
        "category": "MultimediaApplication",
        "os": "Android TV, Google TV (Android 7.0 or newer)",
    },
    "images": {
        "card": "/img/streamova-card.webp",
        "card_alt": "Streamova on Android TV: your own film library, straight from the NAS",
        "banner": "/img/streamova-banner.webp",
        "banner_alt": "Streamova app banner as shown on the Android TV home screen",
        "icon": "/img/streamova-icon-256.webp",
        "icon512": "/img/streamova-icon-512.png",
        "og": "/img/og-streamova.jpg",
        "og_alt": "Streamova: your own film library, straight from the NAS",
    },
    "facts": [
        ("What it is", "Video player and file browser for SMB2 and SMB3 network shares, USB drives and the TV's own storage."),
        ("Made by", "Reblucky Software, the developer who also publishes this site."),
        ("Platform", "Android TV and Google TV on Android 7.0 or newer, operated with the TV remote."),
        ("Sources", "SMB2 and SMB3 shares on a NAS, a Windows, Mac or Linux computer or any Samba server; folders on a USB drive or the TV's internal storage."),
        ("Price", "Every session includes 5 minutes of free playback. A one-time purchase unlocks unlimited playback. There is no subscription."),
        ("Privacy", "No accounts and no ads. Only anonymous usage statistics leave the device. The server password is encrypted with a key kept in the Android Keystore."),
        ("Languages", "13 interface languages: English, Turkish, German, Spanish, French, Portuguese, Japanese, Hindi, Indonesian, Arabic, Russian, Simplified Chinese and Traditional Chinese."),
        ("Not included", "SMB1-only servers, FTP, SFTP, WebDAV, DLNA, UPnP, casting, transcoding, downloads and image-based subtitles (PGS, VobSub)."),
    ],
    "feature_list": [
        "Plays video from SMB2 and SMB3 shares without copying files to the TV",
        "Plays video from USB drives and the TV's internal storage",
        "Embedded subtitles and subtitle files with encoding detection",
        "Switches subtitle and audio tracks during playback",
        "Resumes where you stopped and recognizes episodes",
        "Read-only: never renames, moves or deletes files",
    ],
    "sections": [
        {
            "id": "how-to-play",
            "h2": "How to play a movie from your NAS",
            "html": """
<ol class="steps">
<li><h3>Add a source</h3><p>Streamova can scan the network for SMB servers, or you can type the address of your NAS or computer. For a USB drive or the TV's own storage, pick a folder with the built-in folder picker.</p></li>
<li><h3>Browse with the remote</h3><p>Open a share, move through its folders and pick a movie or an episode. A folder lists its files with their names and sizes.</p></li>
<li><h3>Press play</h3><p>The video starts straight from the source. Streamova remembers where you stopped, and unfinished videos wait on the Continue page.</p></li>
</ol>""",
        },
        {
            "id": "what-it-does",
            "h2": "What Streamova does",
            "html": """
<div class="prose">
<ul>
<li>Streams over SMB2 and SMB3 from a NAS, a Windows, Mac or Linux computer or any Samba server on your local network. The video is read from the share and never downloaded to the TV.</li>
<li>Plays video from a USB drive or the TV's internal storage.</li>
<li>Shows embedded subtitles and subtitle files next to the video (.srt, .ass, .ssa, .vtt, .smi and .sub). It detects UTF-8, UTF-16, Turkish Windows-1254 and most Western European encodings.</li>
<li>Switches subtitle and audio tracks during playback.</li>
<li>Recognizes episodes from names like S01E02 and starts the next file in the folder with one press.</li>
<li>Shows posters stored in the folder (poster.jpg, folder.jpg or an image named like the video). Nothing is looked up online.</li>
<li>Hides NAS system folders such as @eaDir and #recycle.</li>
<li>Finds a file in a folder after you type two characters on the on-screen keypad.</li>
<li>Works with the D-pad on every screen, and the focused item is always highlighted.</li>
<li>Only reads your files. It never renames, moves or deletes anything on the server.</li>
</ul>
</div>""",
        },
        {
            "id": "screenshots",
            "h2": "Streamova on a TV screen",
            "gallery": [
                ("/img/streamova-sources.webp", "Streamova source list on Android TV with a saved SMB2/3 network share and a folder on the TV", "Sources: a saved SMB2/3 share and a folder on the TV"),
                ("/img/streamova-films.webp", "Film folders inside an SMB share listed in Streamova on Android TV", "Film folders on the NAS"),
                ("/img/streamova-player.webp", "Streamova player on Android TV showing a film with the on-screen transport controls", "The player with its on-screen controls"),
                ("/img/streamova-tracks.webp", "Subtitle and audio track menu open over the video in Streamova", "Subtitle and audio track menu during playback"),
            ],
        },
        {
            "id": "limits",
            "h2": "What Streamova does not do",
            "html": """
<div class="prose">
<ul>
<li>Servers that only support SMB1 will not connect.</li>
<li>Image-based subtitles (PGS and VobSub) are not supported. Subtitles in other alphabets need to be saved as UTF-8.</li>
<li>Which video and audio codecs play depends on the hardware decoders in the TV.</li>
<li>FTP, SFTP, WebDAV, DLNA, UPnP and casting are not supported. Streamova does not transcode, download or cache videos, and it does not fetch movie information from the internet.</li>
</ul>
</div>""",
        },
        {
            "id": "price-privacy",
            "h2": "Price and privacy",
            "html": """
<div class="prose">
<p>Every session includes 5 minutes of free playback. A one-time purchase in Google Play unlocks unlimited playback, and there is no subscription. Google Play shows the price in your local currency.</p>
<p>Streamova has no accounts and no ads. The password for your server is encrypted on the TV with a key kept in the Android Keystore. Only anonymous usage statistics leave the device, such as which screen opened or whether a connection or playback failed. File, folder and server names, search terms, viewing history and the advertising ID are never sent. The details are in the <a href="https://streamova.gitlab.io/privacy.html">Streamova privacy policy</a>.</p>
</div>""",
        },
    ],
    "faq_heading": "Questions about Streamova",
    "faq": [
        (
            "Do I need a media server to play movies from my NAS on Android TV?",
            "Not with Streamova. It reads video files directly from an SMB2 or SMB3 share, so the NAS only needs file sharing turned on. Nothing is copied to the TV first.",
        ),
        (
            "Which NAS brands does Streamova work with?",
            "Any server that offers SMB2 or SMB3 file sharing, including Windows, Mac and Linux computers and other Samba servers. Streamova is not affiliated with any NAS manufacturer.",
        ),
        (
            "Can Streamova play videos from a USB drive?",
            "Yes. Pick a folder on the USB drive, or on the TV's internal storage, with the built-in folder picker and play the files like any other source.",
        ),
        (
            "Does Streamova support subtitles?",
            "Yes. It shows embedded subtitle tracks and subtitle files in .srt, .ass, .ssa, .vtt, .smi and .sub formats, and you can switch subtitle and audio tracks during playback. Image-based subtitles such as PGS and VobSub are not supported.",
        ),
        (
            "Is Streamova free?",
            "Every session includes 5 minutes of free playback. A one-time purchase in Google Play unlocks unlimited playback. There is no subscription.",
        ),
        (
            "Why does my server not connect?",
            "Servers that only support SMB1 will not connect. Check that SMB2 or SMB3 is turned on in the file-sharing settings of the NAS or computer, and that it is on the same local network as the TV.",
        ),
        (
            "What data does Streamova collect?",
            "Only anonymous usage statistics, such as which screen opened or whether a connection or playback failed. File, folder and server names, search terms, viewing history and the advertising ID are never sent. There are no accounts and no ads.",
        ),
        (
            "Which Android TV versions does Streamova support?",
            "Android TV and Google TV devices running Android 7.0 or newer, including smart TVs, TV boxes, streaming sticks and projectors.",
        ),
    ],
    "trademark_extra": "Streamova is not affiliated with any NAS manufacturer.",
    "updated": "2026-10-29",
}
