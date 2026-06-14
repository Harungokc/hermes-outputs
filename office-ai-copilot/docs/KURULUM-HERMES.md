# 🤖 Hermes Agent — Sıfırdan Kurulum Rehberi

> Eski bir bilgisayarı (ya da ucuz bir sunucuyu) açık kaynaklı **Hermes Agent** ile
> 7/24 senin yerine çalışan bir yapay zekâ ajanına dönüştür. Telegram'dan komut ver,
> sonuçları GitHub'da sakla, her sabah senin için araştırma yapsın.
>
> Bu rehber sıfır bilgiyle, adım adım kuruluma göre yazıldı. Hiç terminal kullanmamış
> biri bile takip edebilir.

**Hazırlayan:** Harun Gökçe — AI Otomasyon & Agent Geliştirici
[LinkedIn](https://linkedin.com/in/harun-gokce-08843a298) · harungokce70@gmail.com

---

## İçindekiler

1. [Neden Hermes Agent?](#1-neden-hermes-agent)
2. [Neden Hermes + MiniMax?](#2-neden-hermes--minimax)
3. [Sistem Gereksinimleri](#3-sistem-gereksinimleri)
4. [Adım Adım Kurulum — Windows](#4-adım-adım-kurulum--windows)
5. [Adım Adım Kurulum — Linux / Sunucu](#5-adım-adım-kurulum--linux--sunucu)
6. [Telegram & GitHub Entegrasyonu](#6-telegram--github-entegrasyonu)
7. [Sık Karşılaşılan Hatalar](#7-sık-karşılaşılan-hatalar)
8. [Örnek Çalışma Akışı](#8-örnek-çalışma-akışı)
9. [Maliyet Analizi](#9-maliyet-analizi)

---

## 1. Neden Hermes Agent?

Yazılım dünyası inanılmaz bir hızla değişiyor. Her gün yeni bir SaaS ürünü, yeni bir
mobil uygulama, yeni bir araç çıkıyor. Hangisinin tutacağını tek başına takip etmek
artık mümkün değil. Peki ya bir ajan bunu senin için yapsa?

**Hermes Agent**, Nous Research tarafından geliştirilmiş açık kaynaklı, özgürleştirilebilen
bir AI ajanıdır. Eski bir bilgisayara kurulabilir, 7/24 senin adına çalışır, Telegram'dan
komut alır, GitHub'a sonuçları kaydeder ve her geçen gün seni daha iyi tanımaya başlar.

| Özellik    | Hermes Agent              | Diğer Araçlar      |
|------------|---------------------------|--------------------|
| Maliyet    | Ayda ~$10                 | Ayda $50–200+      |
| Kurulum    | Tek komut                 | Saatler / günler   |
| Hafıza     | Kalıcı, öğrenir           | Her sohbet sıfırlanır |
| Platform   | Telegram, Discord, WhatsApp… | Sadece web      |
| Kaynak Kod | Açık kaynak               | Kapalı             |

---

## 2. Neden Hermes + MiniMax?

### Hermes Agent
- **Kalıcı Hafıza** — Her konuşmayı hatırlar, projelerini öğrenir, her geçen gün daha akıllı hâle gelir.
- **Özerk Çalışma** — Her sabah kendi kendine kalkıp görevleri yapar. Sen uyurken o çalışır.
- **Açık Kaynak** — Hiçbir platforma bağımlı değilsin. İstediğin modele tek komutla geçiş yapabilirsin.
- **Her Yerde** — Telegram, Discord, WhatsApp — telefonundan anlık erişim.
- **Ücretsiz** — Hermes'in kendisi ücretsiz. Sadece AI modeli için ödeme yaparsın.

### MiniMax (AI Modeli)
- **Fiyat–Performans** — Ayda $10 ile başla. Aynı iş için diğer platformlara $50–200 ödersin.
- **Token Planı** — Kullandıkça öde yerine sabit aylık ücret. Fatura sürprizi yapmaz.
- **Güçlü Model** — MiniMax-M2.7, geniş bağlam penceresiyle karmaşık görevleri rahatça tamamlar.
- **OAuth Girişi** — API key ile uğraşma. Tarayıcıdan bir kez giriş yap, Hermes otomatik bağlanır.
- **Yerel Destek** — Hermes'in resmî sağlayıcı listesinde yer alıyor. Özel kurulum gerektirmez.

> **Kısaca:** Hermes Agent + MiniMax = en az maliyetle en güçlü kişisel AI ajan.
> Eski donanım, yeni teknoloji.

---

## 3. Sistem Gereksinimleri

Hermes Agent çok büyük bir donanım gerektirmiyor. AI işlemleri bulut üzerinde
(MiniMax, OpenRouter vb.) gerçekleşiyor; bilgisayarın görevi sadece ajanı ayakta tutmak.

### Eski Bilgisayar ile Kurulum

|                | Minimum                  | Önerilen                |
|----------------|--------------------------|-------------------------|
| İşletim Sistemi| Windows 10 / Ubuntu 20.04| Windows 11 / Ubuntu 22.04 |
| RAM            | 4 GB                     | 8 GB+                   |
| Depolama       | 20 GB boş alan           | 50 GB+                  |
| İşlemci        | Herhangi bir x64         | Intel i3+ / Ryzen 3+    |
| Grafik Kartı   | Gerekmiyor               | Gerekmiyor              |
| İnternet       | Sabit bağlantı           | En az 10 Mbps           |

### Sunucu ile Kurulum (Bulut)

Bilgisayarın yoksa veya 7/24 açık tutmak istemiyorsan ucuz bir VPS kiralayabilirsin.
Ayda $5–10 ile Hermes'i bulutta çalıştırabilirsin.

| Sağlayıcı    | Plan          | Fiyat / Ay | Notlar                  |
|--------------|---------------|------------|-------------------------|
| DigitalOcean | Droplet Basic | ~$6        | En kolay kurulum        |
| Hetzner      | CX11          | ~€4        | Avrupa merkezli, hızlı  |
| Vultr        | Cloud Compute | ~$6        | Türkiye'ye yakın lokasyon |
| Contabo      | VPS S         | ~€5        | Çok uygun fiyat         |

> **Sunucu notu:** Sunucu kurulumu için gerekli komutlar Windows bilgisayardan
> farklıdır. Sunucuya SSH ile bağlanıp Linux komutlarını kullanman gerekir.
> Bölüm 5'te adım adım anlatılmıştır.

---

## 4. Adım Adım Kurulum — Windows

### 1. PowerShell 7 Kur
Windows'un varsayılan PowerShell'i (5.1) yeterince modern değil. Önce eski PowerShell'i
**yönetici olarak** aç ve şu komutu çalıştır:
```powershell
winget install Microsoft.PowerShell
```

### 2. PowerShell 7'yi Yönetici Olarak Aç
Başlat menüsü → 'PowerShell 7' ara → sağ tıkla → 'Yönetici olarak çalıştır'

### 3. Hermes'i Kur (tek komut)
Bu komut yükleyiciyi indirir ve çalıştırır. Python 3.11, Node.js, Git, ripgrep ve
ffmpeg dahil her şeyi otomatik kurar:
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### 4. Model Seçimi (MiniMax)
Kurulum bittikten sonra sağlayıcı kur sihirbazını başlat. Listeden **MiniMax (OAuth)**
seç → tarayıcı açılır → MiniMax hesabınla giriş yap:
```powershell
hermes model
```
> Not: MiniMax hesabın yoksa önce [minimax.io](https://minimax.io) üzerinden ücretsiz
> bir hesap aç. Kimlik bilgileri `~/.hermes/auth.json` dosyasına kaydedilir.

### 5. Gateway'i Otomatik Başlat
Bilgisayar her açıldığında Hermes'in otomatik başlaması için:
```powershell
hermes gateway install
hermes gateway start
```

### 6. Durumu Kontrol Et
Her şeyin yolunda olduğunu görmek için:
```powershell
hermes gateway status
```

---

## 5. Adım Adım Kurulum — Linux / Sunucu

Bilgisayarın yoksa ya da ajan 7/24 kesintisiz çalışsın istiyorsan ucuz bir VPS en iyi
seçenektir. Aşağıdaki adımlar **Ubuntu 22.04 / 24.04** içindir ve sıfırdan eksiksiz
kurulumu kapsar.

> **Ön gereksinim:** Linux'ta tek ön gereksinim **Git**'tir. Python 3.11, Node.js,
> ripgrep, ffmpeg gibi her şeyi kurulum betiği otomatik halleder. Sağlayıcıdan sunucu
> açarken işletim sistemi olarak Ubuntu 22.04 veya 24.04 seç.

### 1. Sunucuya SSH ile Bağlan
Sağlayıcının verdiği IP ve şifre/anahtar ile bağlan (Windows'ta PowerShell veya PuTTY):
```bash
ssh root@SUNUCU_IP_ADRESI
```

### 2. Sistemi Güncelle ve Git'i Kur
```bash
apt update && apt upgrade -y
apt install -y git curl
```

### 3. (Önerilen) Ayrı Kullanıcı Oluştur
root ile çalıştırmak güvenli değildir. Ajan için ayrı bir kullanıcı aç ve ona geç:
```bash
adduser hermes
usermod -aG sudo hermes
su - hermes
```

### 4. Hermes'i Kur
Tek komutla kurulum; bittiğinde kabuğu yenile:
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
```

### 5. Model Seç (MiniMax)
`hermes model` çalıştır → listeden MiniMax (OAuth) seç.
> **Önemli:** Sunucuda tarayıcı yoktur; ekrana bir giriş bağlantısı (URL) yazılır — bu
> linki **kendi bilgisayarındaki** tarayıcıya yapıştırıp MiniMax hesabınla giriş yap.
> Kimlik bilgisi sunucudaki `~/.hermes/auth.json` dosyasına kaydedilir.
```bash
hermes model
```

### 6. Telegram'ı Bağla & Kalıcı Servis Yap
Telegram'ı bağla, ardından gateway'i systemd servisi olarak kur ve başlat:
```bash
hermes gateway setup
hermes gateway install
hermes gateway start
```
SSH oturumunu kapatınca da çalışmaya devam etmesi için **linger** aç:
```bash
loginctl enable-linger $USER
```

### 7. Durum, Loglar & Alternatif
```bash
hermes gateway status
hermes logs gateway -f
hermes doctor
```
> systemd servisi SSH kopsa bile çalışır. Alternatif: `tmux` içinde
> `hermes gateway run` çalıştırıp **Ctrl+B → D** ile ayrıl.

---

## 6. Telegram & GitHub Entegrasyonu

### Telegram Bot Oluşturma
Hermes'e telefonundan komut verebilmek için bir Telegram botu oluşturman gerekiyor.
Bu işlem 2 dakika sürer ve ücretsizdir.

1. Telegram'ı aç ve **@BotFather** hesabını ara
2. **/newbot** komutunu gönder
3. Bot için bir isim gir (örnek: HermesAjanım)
4. Bot için bir kullanıcı adı gir — sonu 'bot' bitmeli (örnek: hermesajanim_bot)
5. BotFather sana bir token verir: `123456:ABC-DEF…` şeklinde — bunu kopyala
6. İnteraktif kurulumu başlat: `hermes gateway setup` → Telegram'ı seç → token'ı ve izinli kullanıcı ID'ni gir
7. Telegram'da botuna **/start** yaz, hazır!

Alternatif (manuel) yöntem — `~/.hermes/.env` dosyasına ekle:
```
TELEGRAM_BOT_TOKEN=token_buraya
TELEGRAM_ALLOWED_USERS=senin_telegram_id
```

### GitHub Entegrasyonu
Hermes'in araştırma sonuçlarını ve hazırladığı dosyaları GitHub'a kaydetmesi için bir
Personal Access Token oluşturman gerekiyor.

1. [github.com/settings/tokens](https://github.com/settings/tokens) adresine git
2. **Generate new token (classic)** butonuna tıkla
3. **repo** kapsamını seç (tam erişim)
4. **Generate token** → token'ı kopyala
5. `~/.hermes/.env` dosyasını aç (`notepad $env:USERPROFILE\.hermes\.env`) ve şu satırı ekle:
   ```
   GITHUB_TOKEN=token_buraya
   ```
6. Telegram'dan Hermes'e: *"hermes-outputs adında bir GitHub reposu oluştur"* de

> **Güvenlik notu:** Bu botu ve GitHub token'ını yalnızca senin kullanabilmen için
> `TELEGRAM_ALLOWED_USERS` alanına kendi Telegram ID'ni yaz. Token'larını kimseyle
> paylaşma; sızarsa GitHub'dan iptal edip yenisini oluştur.

---

## 7. Sık Karşılaşılan Hatalar

### ❗ HTTP 401 — API Anahtarı Hatası
*MiniMax veya başka bir servisin kimliği yanlış ya da eksik.*
- `.env` dosyasını kontrol et: `notepad $env:USERPROFILE\.hermes\.env`
- İlgili anahtar satırının başında `#` olmamalı
- Anahtarın başında veya sonunda boşluk olmamalı
- MiniMax OAuth kullanıyorsan `hermes model` ile tekrar giriş yap

### ❗ PowerShell 'Invalid Choice' Hatası
*hermes komutu yanlış yazılmış veya tanımlanmıyor.*
- Komutu dikkatli yaz: `hermes gateway` (geteway değil)
- PowerShell 7 kullandığından emin ol (5.1 değil)
- Terminali kapatıp yeniden aç

### ❗ Gateway Telegram'a Bağlanmıyor
*Bot token'ı eksik veya yanlış kaydedilmiş.*
- `hermes gateway` ile önplanda çalıştır, hata mesajını gözlemle
- `~/.hermes/.env` içinde `TELEGRAM_BOT_TOKEN=` satırının doğru olduğunu kontrol et
- BotFather'dan aldığın token'ı boşluk bırakmadan tekrar kopyala

### ❗ UnicodeDecodeError (cp1254)
*Windows Türkçe karakter seti sorunu — işlevselliği etkilemez ama hata görünür.*
- Bu hata sadece görsel; ajan çalışmaya devam eder
- Geçici çözüm: `$env:PYTHONUTF8 = '1'` komutunu önce çalıştır
- Kalıcı çözüm: Windows Bölge ayarlarından 'Beta: UTF-8' seçeneğini aktif et

### ❗ MiniMax Stream Drop (RemoteProtocolError)
*MiniMax sunucusuyla bağlantı geçici olarak kesildi.*
- Hermes otomatik olarak yeniden bağlanır (retry 2/3 gibi mesaj görünür)
- Tekrar ederse: `hermes gateway stop && hermes gateway start`
- İnternet bağlantını kontrol et

### ❗ 'hermes' Komutu Tanımıyor
*Hermes'in kurulduğu dizin PATH'e eklenmemiş.*
- Terminali kapat ve yeniden aç
- Hâlâ çalışmıyorsa kurulum çıktısında belirtilen Scripts dizinini PATH'e ekle
- Kalıcı çözüm için sistem ortam değişkenlerine ekle

### Gateway Durumunu Kontrol Etme
```bash
hermes gateway status     # durum
hermes gateway restart    # yeniden başlat
hermes gateway stop       # durdur
```

> **Güncelleme:** Hermes'i güncellemek için kurulum komutunu (install.ps1 / install.sh)
> tekrar çalıştırman yeterlidir; mevcut ayarların ve hafızan korunur.

---

## 8. Örnek Çalışma Akışı

### Agent Kurulduktan Sonra Ne Olur?
Agent kurulup Telegram'a bağlandıktan sonra tek yapman gereken promptları vermek.

**Hızlı Kurulum Özeti:**
1. PowerShell 7'yi yönetici olarak aç
2. Kurulum: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
3. Model: `hermes model` → MiniMax (OAuth) → tarayıcıdan giriş yap
4. Telegram botu oluştur (@BotFather → /newbot) ve `hermes gateway setup` ile bağla
5. `hermes gateway install && hermes gateway start` ile otomatik başlatmayı ayarla
6. Telegram'da botuna /start yaz, hazır!

### Agent Hangi Siteleri Tarar?
Hermes'e istediğin siteyi taratabilirsin. En yaygın kullanılan kaynaklar:

| Kaynak                | Ne İçin?                               |
|-----------------------|----------------------------------------|
| producthunt.com       | Yeni çıkan SaaS ve mobil uygulamalar, beğeni sayıları |
| github.com/trending   | En çok yıldız alan repolar, popüler teknolojiler |
| reddit.com/r/SideProject | Geliştirici topluluğunda öne çıkan projeler |
| news.ycombinator.com  | Hacker News — startup ve tech haberleri |
| linkedin.com          | Sektörel paylaşımlar, agent geliştiriciler |
| arxiv.org             | Yeni AI araştırma makaleleri ve bulgular |

### Örnek Promptlar
Telegram'dan Hermes'e şu şekilde komut verebilirsin:

> **Pazar Araştırması:** "Her gün sabah 09:00'da Product Hunt'taki yeni ürünleri tara.
> Kaç beğeni aldıklarını, hangi kategoride olduklarını ve öne çıkan özellikleri GitHub'a
> kaydet, bana Telegram'dan gönder."

> **Rakip Analizi:** "GitHub'da 'AI agent' konusunda bu hafta en çok yıldız alan 10 repoyu
> bul. Her birinin ne yaptığını, hangi dilde yazıldığını ve kaç yıldızı olduğunu listele."

> **LinkedIn İçeriği:** "Bugün AI ve otomasyon alanında öne çıkan 3 haber bul. Her biri
> için kısa, sade, insan gibi yazılmış bir LinkedIn gönderisi hazırla. Kaynak ve görsel
> önerisi ekle."

> **Haftalık Rapor:** "Her Pazar akşam 20:00'da bu haftanın özet raporunu hazırla: öne
> çıkan ürünler, popüler teknolojiler, dikkat çeken haberler. GitHub'a kaydet ve bana gönder."

### Örnek Günlük Akış

| Saat       | Agent Ne Yapar?                              | Sen Ne Yaparsın?           |
|------------|----------------------------------------------|----------------------------|
| 09:00      | Product Hunt, GitHub, LinkedIn tarar. Haberleri toplar. | Uyuyorsun / başka işle meşgulsün |
| 09:15      | 3–5 LinkedIn gönderisi hazırlar, görsel önerisi ekler. | Hâlâ başka işlesin       |
| 09:20      | Sonuçları GitHub'a kaydeder.                 | —                          |
| 09:21      | Sana Telegram'dan özet mesaj gönderir.       | Telefona bakıyorsun        |
| 09:25      | En beğendiğin gönderiyi seçip LinkedIn'e yapıştırırsın. | 2 dakikalık iş          |
| Pzt 10:00  | Haftalık proje araştırması yapar, 5 fikir sunar. | İstersen birini seçtirirsin |
| Seçtiğin an| Seçtiğin proje için adım adım rehber hazırlar.| PDF yapıp paylaşabilirsin  |

> Örnek günlük akış — sen uyurken ajan çalışır.

---

## 9. Maliyet Analizi

Hermes Agent açık kaynaklı ve ücretsizdir. Sadece kullandığın AI modeli için ödeme yaparsın.

| Senaryo         | Aylık Maliyet | Ne Dahil?                              |
|-----------------|---------------|----------------------------------------|
| Basit Kullanım  | ~$10          | MiniMax Starter, günlük araştırma      |
| Orta Kullanım   | ~$20–30       | MiniMax Plus, haftalık projeler + otomasyon |
| Yoğun Kullanım  | ~$50+         | MiniMax Max, tüm özellikler aktif      |
| Sunucu Eklenirse| +$5–10        | VPS kiralama (Hetzner, DigitalOcean)   |

> **Maliyet karşılaştırması:** Bir freelancer asistana ayda 1000–5000 TL ödersin.
> Hermes ile aynı işi ayda 300–500 TL'ye yapabilirsin. Üstelik 7/24 çalışır, izin
> istemez, yorulmaz.

---

> Bu rehber Harun Gökçe tarafından hazırlanmıştır. Soru ve destek için:
> [LinkedIn](https://linkedin.com/in/harun-gokce-08843a298) · harungokce70@gmail.com
