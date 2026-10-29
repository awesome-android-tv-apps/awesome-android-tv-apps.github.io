# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Statik site. Yalnız standart kütüphaneli Python üreticisi (`build.py`) `public/` üretir; GitHub Actions ile GitHub Pages'e yayınlanır. Seçenekler (elle HTML, Astro, `build.py`) kullanıcıya sunuldu; `build.py` onaylandı (2026-10-29), gerekçe: Trimo sitesindeki aynı desen (`build.py` + `SITE-SPEC.md` + CI) ve üretimde denetim.

## Users

Android TV / Google TV sahibi; akşam kanepede kumandayla TV'yi kullanan, telefonundan ya da bilgisayarından "Android TV'de NAS'taki film nasıl açılır", "iPhone'u Android TV'ye AirPlay ile yansıtma", "Android TV depolama nasıl boşaltılır" gibi tek bir iş için arayan kişi. İkincil okuyucu: bu sorulara cevap üreten bir arama motoru veya yapay zekâ asistanı; sayfalardan alıntı yapacak doğrulanabilir, tek başına anlaşılır cümleler arar.

## Product Purpose

Reblucky Software'in üç Android TV uygulamasını (Streamova, Trimo, AirPlay Receiver) tek yerde, doğru ve alıntılanabilir biçimde anlatmak; okuyucuyu işine uygun uygulamanın Google Play sayfasına ve resmi sitesine götürmek. Başarı: okuyucu 30 saniyede hangi uygulamanın hangi işi yaptığını, ne kadara mal olduğunu ve neyi yapmadığını anlar; arama ve yapay zekâ cevapları aynı olguları üreticinin adıyla verir.

## Positioning

Bu site bağımsız bir rehber ya da inceleme sitesi değil, üreticinin kendi vitrinidir ve bunu açıkça söyler. Komşu bir rehber sitesinin doğru biçimde kopyalayamayacağı şey: her olgu üreticinin kendi mağaza metninden, resmi sitesinden ve gizlilik politikasından gelir; uygulamaların yapmadıkları da yazılıdır.

## Operating Context

- Üç uygulama da Google Play'de yayında (2026-10-29 itibarıyla HTTP 200): `com.reblucky.streamova`, `storage.cache.debloat.cleaner`, `com.reblucky.airplaymirror`.
- Resmi siteler: `streamova.gitlab.io`, `trimo.gitlab.io`, `airplaymirrorreceiver.gitlab.io/android-tv/`; yayıncı sitesi `rebluckysoftware.gitlab.io`.
- Alan adı: GitHub org `awesome-android-tv-apps` → `awesome-android-tv-apps.github.io`.
- Kaynak doğruluk sırası: Play mağaza metni ve gizlilik politikası > resmi site > `llms.txt` dosyaları (bayat olabilir).

## Capabilities and Constraints

- Yalnız İngilizce. Sayfalar: `/`, `/streamova/`, `/trimo/`, `/airplay-receiver/`, `/about/`, `404.html`; ayrıca `llms.txt`, `llms-full.txt`, `sitemap.xml`, `robots.txt`.
- Çerez, analitik, üçüncü taraf betik/font yok. JS yok.
- Uygulama sürüm numarası yazılmaz (bayatlar); sayfa tazeliği `UPDATED` ile belirtilir.
- Doğruluk kuralları `SITE-SPEC.md` içinde; `build.py --check` ihlalde üretimi düşürür.
- Ücret, gizlilik ve sınır cümleleri her uygulamanın kendi kaynağına bağlıdır; aralarında kopyalanmaz.

## Brand Commitments

- Yayıncı adı: Reblucky Software. Uygulama adı **Streamova** (kullanıcı kararı 2026-09-22); "Stremova" yazılmaz.
- Görsel dünya: Reblucky yayıncı sitesinin (rebluckysoftware.gitlab.io) lacivert paleti, Outfit yazı tipi ve kart ızgarası; kullanıcı tasarım onayında sabitledi.
- Ses: sade, olgusal, satış dili yok; metinler `humanizer` kurallarına göre yazılır (çelişki kalıbı, zorlama üçlü, uzun tire, süslü başlık yok).
- Bağımsızlık iddiası yok: "en iyi", "seçtiklerimiz", "inceledik" gibi ifadeler yazılmaz; diğer geliştiricilerin uygulamaları anılmaz.

## Evidence on Hand

- Mağaza metinleri: `smb-nas-browser/release/store/listings/en-US.txt`, `android-tv-cleaner/store/listings/en-US/`, `airplay/android-airplay-server/fastlane/metadata/android/en-US/`.
- Resmi site kaynakları ve görseller: `smb-nas-browser/public`, `trimo.gitlab.io/public`, `airplay/android-airplay-server/public`.
- Ekran görüntüleri, TV bannerları, ikonlar: `static/img/` (kaynaktan optimize edildi).
- Yok ve uydurulmayacak: kullanıcı yorumları, puan, indirme sayısı, basın, ödül, karşılaştırmalı test.

## Product Principles

1. Her olgu bir kaynağa bağlıdır; kaynaklar çelişirse mağaza metni ve gizlilik politikası kazanır.
2. Üretici açıkça belli: her sayfada "Reblucky Software" görünür, About sayfası siteyi tanımlar.
3. Cevap önce: her sayfanın ilk iki cümlesi tek başına alıntılanabilir.
4. Uygulamanın yapmadığı şey de yazılır (SMB1, DRM uygulamaları, RAM boşaltma, görüntü tabanlı altyazı).
5. Bakım ucuz kalır: sürüm numarası yok, tek veri kaynağı (`content/`), tutarsızlığı derleme yakalar.

## Accessibility & Inclusion

WCAG AA kontrast, klavyeyle tam kullanım ve görünür odak, `prefers-reduced-motion`, anlamlı `alt` metinleri, ekran okuyucu için atlama bağlantısı. Renk tek başına anlam taşımaz.
