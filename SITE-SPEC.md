# Reblucky Android TV Apps sitesi: içerik kuralları

Kaynak: `content/*.py` (kesin metin). `build.py` üretir; `python3 build.py --check` bu dosyadaki kuralları denetler ve ihlalde üretimi durdurur (CI aynı komutu çalıştırır).

## Kimlik (her sayfa)

1. Siteyi Reblucky Software yayınlar ve bunu açıkça söyler: üst bilgi ve altbilgi, ana sayfadaki not, About sayfası, ana sayfa SSS'sindeki "Is this an independent review site?" ve `llms.txt` içindeki `Disclosure` satırı.
2. Bağımsız rehber ya da inceleme dili yoktur. Yazılmaz: `best`, `top-rated`, `number one`, `we tested/reviewed/compared/picked/ranked`, `our picks`, `unbiased`, olumsuz kullanım dışında `independent review/guide`. Diğer geliştiricilerin uygulamaları anılmaz, karşılaştırılmaz.
3. Üç uygulama dışında içerik yok: Streamova, Trimo, AirPlay Receiver.

## Kaynaklar ve öncelik

Çelişkide yukarıdaki kazanır: (1) Play mağaza metni ve gizlilik politikası, (2) resmi site, (3) `llms.txt` dosyaları (bayat olabilir).

| Uygulama | Mağaza metni | Resmi site | Gizlilik |
|---|---|---|---|
| Streamova | `smb-nas-browser/release/store/listings/en-US.txt` | streamova.gitlab.io | streamova.gitlab.io/privacy.html |
| Trimo | `android-tv-cleaner/store/listings/en-US/` ve `trimo.gitlab.io/locales/en.json` | trimo.gitlab.io | trimo.gitlab.io/privacy.html |
| AirPlay Receiver | `airplay/android-airplay-server/fastlane/metadata/android/en-US/` ve `airplay/site-seo-spec.md` | airplaymirrorreceiver.gitlab.io/android-tv/ | .../android-tv/privacy.html |

Uygulama sürüm numarası yazılmaz (bayatlar). Sürüm ve tarih resmi sitelerde tutulur.

## Doğruluk kuralları

### Streamova

1. Ad **Streamova**. "Stremova" yazılmaz (Play'deki ürün başlığındaki yazım hatası).
2. Fiyat: oturum başına 5 dakika ücretsiz oynatma; tek seferlik satın alma sınırsız oynatmayı açar; abonelik yok. Fiyat rakamı yazılmaz (Play yerel para biriminde gösterir).
3. Platform: Android TV ve Google TV, Android 7.0+, kumanda.
4. Kaynaklar: SMB2 ve SMB3, USB sürücü, TV'nin kendi depolaması. Desteklenmeyenler: yalnız SMB1 konuşan sunucular, FTP, SFTP, WebDAV, DLNA, UPnP, cast, transcode, indirme, önbellek, çevrimiçi film bilgisi, görüntü tabanlı altyazı (PGS, VobSub).
5. Gizlilik: hesap ve reklam yok. Yalnız anonim kullanım istatistiği cihazdan çıkar (Firebase Analytics). Sunucu parolası Android Keystore anahtarıyla şifrelenir. Dosya, klasör, sunucu adı, arama metni, izleme geçmişi ve reklam kimliği gönderilmez. **"no analytics" yazılmaz.**
6. NAS markası anılmaz; "not affiliated with any NAS manufacturer" cümlesi kalır.
7. 13 arayüz dili.

### Trimo

1. Fiyat: tarama, ölçme, dosya silme, uygulama kaldırma, önbellek temizleme, Restore ve Undo ücretsiz; Debloat'ta sistem uygulamalarını devre dışı bırakma/kaldırma tek seferlik Google Play satın alması; abonelik yok. "Tamamen ücretsiz" yazılmaz.
2. Platform: Android TV ve Google TV, Android 5.0+; Debloat eylemleri Android 8+. Telefon ve tablet hedeflenmez.
3. Debloat: root yok, bilgisayar yok; TV'nin kendi USB hata ayıklama servisine 127.0.0.1 üzerinden bağlanır; kullanıcı bir kez USB hata ayıklamayı açar. Her değişiklik günlüğe yazılır, onay ister (odak İptal'de başlar), 15 saniye içinde Keep changes basılmazsa TV geri alır; Restore ve Undo all changes vardır. Korunan paketler seçilemez.
4. Yapmadıkları: uygulama durdurma, RAM boşaltma, süreç öldürme, hız vaadi, root. `build.py` Trimo sayfasında `boost`, `speed up`, `faster`, `turbo`, `supercharge` kelimelerini reddeder (tek istisna: "Will Trimo make my TV faster?" sorusu, `lint_allow`).
5. Gizlilik: hesap ve reklam yok; anonim kullanım istatistiği Google Analytics for Firebase ile gider; reklam kimliği yok. INTERNET izni 127.0.0.1'deki hata ayıklama servisi ve bu istatistikler içindir. **"no analytics" yazılmaz.**
6. Medya çöp taramasında önerilmez; kullanıcı elle işaretlerse silinir, onaydan sonra ve geri dönüşsüzdür.
7. Test edilen cihaz: Xiaomi Mi Box (Android 9) ve Android 14 TV emülatörü. Daha geniş uyumluluk iddiası yazılmaz.
8. 10 arayüz dili (TV diline uyar, başka dilde İngilizce).

### AirPlay Receiver

1. Ad: AirPlay Mirror Receiver (Play başlığı "AirPlay Receiver: iPhone to TV"). Sayfa kısa adı AirPlay Receiver.
2. Fiyat: ücretsiz oturumlar 5 dakikada durur, tüm kalite seçenekleri ücretsizde açıktır. Pro: aylık ya da yıllık abonelik veya aynı Google hesabında geri yüklenebilen tek seferlik ömür boyu satın alma. Abonelikler Play'de iptal edilene kadar yenilenir. **"no subscription" yazılmaz**, "free" tek başına yazılmaz.
3. Kalite: 1080p, 1440p, 4K; 30 veya 60 FPS; yüksek ayarlar ağa ve TV'ye göre takılabilir.
4. Platform: Android TV ve Google TV, Android 7.0+, Google Play. Gönderici iPhone, iPad veya Mac (Control Center'da Screen Mirroring), aynı Wi-Fi; telefona uygulama kurulmaz. Telefon ve tablet alıcı olamaz.
5. DRM'li uygulamalar (Netflix, Prime Video, Disney+, Apple TV+) yansıtılamaz.
6. Gizlilik: hesap, reklam ve bulut aktarımı yok; ekran ve ses yerel ağda kalır; anonim kullanım istatistiği (Firebase Analytics, reklam kimliği kapalı). **"no analytics" yazılmaz.**
7. **"AirPlay 2" yazılmaz.** AirPlay, iPhone, iPad ve Mac Apple Inc. markalarıdır; "not affiliated with, endorsed or sponsored by Apple" satırı kalır.
8. Doğrulanmış ek yetenekler: AirPlay düğmesiyle gönderilen video uygulamanın kendi oynatıcısında oynar (döndür, ölçekle, indir); Mac ekran yansıtma; müzik kapak resmiyle; PIN ve alıcı adı.
9. 13 uygulama dili.

### Ortak

Android TV, Google TV ve Google Play Google LLC markalarıdır; altbilgideki satır her sayfada kalır. Uygulamalar Google, Apple veya herhangi bir NAS ya da TV üreticisiyle bağlantılı değildir.

## SEO sınırları (`build.py --check` denetler)

- `title` ≤ 65, `og:title` ≤ 60, `description` 140 ile 160 karakter. Her sayfada tek `h1`, başlık sırası atlamaz.
- Her sayfada `canonical`, Open Graph, Twitter kartı, `theme-color`; tek JSON-LD `@graph`: Organization, WebSite, sayfa türü (CollectionPage, AboutPage, WebPage), uygulama sayfalarında SoftwareApplication ve BreadcrumbList, SSS olan sayfalarda FAQPage (sorular görünür başlıklarla birebir).
- `sitemap.xml` yalnız indekslenebilir sayfaları ve her sayfanın `updated` tarihini `lastmod` olarak verir; `robots.txt` sitemap'i gösterir; 404 `noindex`.
- JS, çerez, analitik, iframe, form ve üçüncü taraf kaynak yok. Harici bağlantılar yalnız `content/site.py` içindeki `allowed_hosts` listesine gider.
- Görsellerde `alt`, `width`, `height` (dosya oranıyla uyumlu), en çok 200 KB. HTML sayfası en çok 70 KB, CSS en çok 25 KB.
- Görünür kelime: ana sayfa ≥ 380, uygulama sayfası ≥ 700, About ≥ 230. Doldurma yok.

## GEO kuralları

- Her sayfanın ilk iki cümlesi tek başına alıntılanabilir (özne açık, zamire bağlı değil).
- Her uygulama sayfasında aynı anahtarlı "at a glance" tablosu: What it is, Platform, Price, Privacy, Languages, Not included (+ uygulamaya özel satırlar). Ana sayfadaki karşılaştırma hücreleri her uygulama modülündeki `compare` sözlüğünden gelir.
- Soru başlıklı SSS, gerçek sorgulara yakın ifadelerle; cevaplar listeleme metniyle tutarlı.
- `llms.txt` ve `llms-full.txt` sayfa verisinden üretilir; elle düzenlenmez. Ayrıntılı olgular "Facts per app" bölümünde.
- Varlık adları Play metniyle aynıdır (Streamova, Trimo, AirPlay Mirror Receiver). Organization `sameAs`: Play geliştirici sayfası ve GitHub org.

## Metin kuralları (skill://humanizer)

Metin elle yazılır ve `build.py --check` şu kalıpları reddeder: uzun tire ve tire gibi kullanılan ` - `, "not just/only/merely", "is not just/only/about", AI sözcükleri (pivotal, crucial, robust, seamless, leverage, showcase...), satış dili (stunning, game-changing, effortless...), "actually/additionally/moreover", hazırlık cümleleri ("Let's dive"), şişirilmiş anlam ("plays a key role", "in today's"), chatbot artığı, emoji, kalın etiket (`<strong>`, `<b>`). Düz tırnak tercih edilir (eğri tırnak uyarı verir). Zorlama üçlü ve "çelişki kalıbı" regex ile yakalanamaz; yazarken elle kontrol edilir.

## Tazelik kuralları

- Bir sayfanın içeriği değişince `content/<sayfa>.py` içindeki `updated` ve `content/site.py` içindeki `updated` (en yeni sayfa tarihi) aynı commit'te güncellenir; `--check` eşitliği denetler. Sitemap `lastmod` ve görünen "Last updated" satırı buradan gelir.
- Bir uygulamanın fiyatı, gizliliği, desteklediği sürüm ya da dil sayısı değişirse ilgili uygulama sayfası, ana sayfadaki `compare` hücreleri ve bu dosya aynı commit'te güncellenir.

## Bilinen kaynak tutarsızlıkları (2026-10-29)

- `smb-nas-browser/public/llms.txt` (streamova.gitlab.io) "no analytics" diyor; uygulama `firebase-analytics` içeriyor ve Play metni "only anonymous usage statistics leave the device" diyor. Bu site Play metnini izler.
- `trimo.gitlab.io/SITE-SPEC.md` madde 5 "analitik yok, cihazdan dışarı veri çıkmaz" diyor; `locales/en.json`, Play metni ve `android-tv-cleaner/app/build.gradle.kts` (Firebase Analytics) anonim kullanım istatistiğini gösteriyor. Bu site en.json'u izler.

## Yayın

GitHub org `awesome-android-tv-apps`, repo `awesome-android-tv-apps.github.io` (public), Pages kaynağı GitHub Actions (`.github/workflows/pages.yml`). Yerel önizleme: `python3 build.py && python3 -m http.server 8095 --bind 192.168.1.66 -d public`.

Search Console: mülk `https://awesome-android-tv-apps.github.io/` dosya yöntemiyle doğrulanır (`static/google3d1276421bb1c9bf.html`). Bu dosya silinirse doğrulama düşer. Sitemap: `https://awesome-android-tv-apps.github.io/sitemap.xml`.
