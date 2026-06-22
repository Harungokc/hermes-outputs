# Beyaz Yakalı Ofis Otomasyonları — 22 Haziran 2026

## Özet

Pazartesi yerine Pazar araştırması gibi görünse de, asıl mesele: **hafta içi 40+ saat ofiste geçiren beyaz yakalı için en büyük zaman kaybı neresi?** Email, toplantı, rapor, doküman. Bugün 3 yeni araç + 1 beklenmedik keşif ile geliyorum.

---

## 1. 🖥️ Harness Anything — 47 Komutla Ofis AI Hub'ı (861 ⭐)

**GitHub:** `yb2460/harness-anything` | **Platform:** Windows | **Stars:** 861 (2 haftada) | **Dil:** Python

### Ne Yapıyor?
Excel, Word, PowerPoint, WPS, Zotero, Photoshop — tümünü **tek bir merkezden AI agent olarak kontrol**. 47 CLI komutu, 27 akademik yetenek, SVG'den PPTX üretimi.

### Kimler İçin?
- Veri analisti (Excel otomasyonu)
- Akademisyen (Zotero + Word)
- Pazarlama ekibi (PowerPoint üretimi)
- İK uzmanı (_cv_.pdf → otomatik özetleme)

### Gerçek Sonuçlar
- Haftalık rapor hazırlama: **45 dakika → 5 dakika** (SVG→PPTX dönüşümü)
- Excel veri girişi: **saatler → dakikalar**
- 861 star = 2 haftada — organik büyüme, viral değil

### Herkesin Kaçırdığı Nokta
Çoğu "Office AI" aracı bulut tabanlı ve verileri dışarı gönderiyorsunuz. Harness Anything **tamamen local** çalışıyor — Excel dosyanız makinenizde kalıyor. Kurumsal veri gizliliği endişesi olanlar için bu kritik. Ama kurulum biraz teknik: Python 3.10+, WPS veya MS Office local kurulu olmalı.

### Kurulum Zorluğu: Orta
```bash
pip install cli-anything-wps
python main.py --setup
```
5-10 dakika ilk kurulum, ardından tüm Office suite AI kontrole açık.

---

## 2. 📧 OfficeCLI — Email/Draft'tan PPTX/DOCX/XLSX (48 ⭐)

**GitHub:** `officecli/officecli-dist` | **Dil:** Shell/Node.js | **NPM:** `npm install officecli`

### Ne Yapıyor?
Sadece prompt yazarak Office dosyası üretiyorsun. "Bu verilerle aylık satış raporu yap" → DOCX hazır.

### Kimler İçin?
- Satış ekibi (haftalık/aylık rapor)
- İK (iş ilanları, sözleşmeler)
- Finans (bütçe tabloları, raporlar)

### Gerçek Sonuçlar
- Rapor üretimi: **20-30 dakika → 2 dakika**
- Standart şablonlarla uyumlu çıktı
- Markdown + AI → düzenlenebilir Office dosyası

### Herkesin Kaçırdığı Nokta
Diyeceksiniz "zaten ChatGPT de yazıyor". Ama fark şu: OfficeCLI **gerçek .pptx/.docx/.xlsx üretiyor** — yani PowerPoint'te açıp düzenleyebiliyorsun, grafikleri değiştirebiliyorsun. ChatGPT çıktısı kopyala-yapıştır metin. Masaüstünde hazır sunum dosyası isteyenler için 10x daha hızlı.

### Kurulum Zorluğu: Kolay
```bash
npm install -g officecli
officecli generate --template "aylik-satis-raporu" --data ./satislar.csv
```
Node.js bilen biri 3 dakikada kurar.

---

## 3. 🗓️ BagIdea Office — Desktop Wallpaper Olarak Çalışan AI Ofis (91 ⭐)

**GitHub:** `bagidea/bagidea-office` | **Dil:** HTML/JS | **Yeni:** 2026-06-03

### Ne Yapıyor?
2.5D bir ofis simülasyonu — masaüstü wallpaper'ın olarak AI agent'lar çalışıyor. Her agent kendi "istesine" gidiyor, toplantı yapıyor, iş bölüşüyor.

### Gerçek Kullanım Senaryosu
- Email agent'ı: gelen kutunuzu tarayıp "bunlar bugün cevaplanmalı" diyor
- Rapor agent'ı: verileri okuyup PowerPoint üretiyor
- Takvim agent'ı: boş slot'ları dolduruyor

### Herkesin Kaçırdığı Nokta
"Wallpaper olarak ofis" görünce çoğu "ne gereksiz" diyor. Ama asıl fikir **agent'ların görsel organizasyonu** — hangi agent ne yapıyor, hangisi meşgul, hangisi boşta, hepsi tek bakışta görünüyor. Karmaşık workflow'ları yönetmek için dashboard olarak çalışıyor. Agent cluster dediğimiz şeyin görsel hali.

### Kurulum Zorluğu: Orta
```bash
git clone https://github.com/bagidea/bagidea-office
cd bagidea-office && npm install
npm start
```
Biraz teknik ama Discord desteği aktif.

---

## 4. 💼 DragonZagent — Windows İçin Kişisel AI Workbench (13 ⭐)

**GitHub:** `outlookceo/DragonZagent` | **Dil:** Python | **Platform:** Windows öncelikli

### Ne Yapıyor?
Chat + görsel Agent Cluster orchestration + local araçlar + Office workflow + WeChat/Telegram entegrasyonu.

### Herkesin Kaçırdığı Nokta
Türkçe konuşuyoruz diye "Windows'ta çalışmaz" dedik. Aslında bu araç Windows için optimize edilmiş — Office workflow'larını local yapıyor. "AI ofis asistanı" arayan ama verilerini buluta göndermek istemeyenler için tam aranan şey. WeChat ve Telegram entegrasyonu = mesajlaşma AI'ı ile ofis dosyaları aynı yerde.

---

## 5. 📊 Haftalık Rapor Otomasyonu — Didon (HN 2pts)

**URL:** https://www.didon.app/ | **Platform:** Web

### Ne Yapıyor?
AI, gün boyunca yaptığınız işleri otomatik takip edip "günlük prodüktivite raporu" üretiyor. Haftalık analiz, trend grafiği, zaman kaybı tespiti.

### Kimler İçin?
- Freelancer'lar (ne kadar zaman neye gidiyor?)
- Yöneticiler (ekip verimliliği)
- Kişisel gelişim takipçileri

### Herkesin Kaçırdığı Nokta
"Didon gibiyim" diyen onlarca app var. Ama Didon farkı: **sadece veri topluyor, seni yargılamıyor**. "Bu hafta 12 saat toplantıya gitti, ama sadece 3'ü karar vericiydi" gibi somut geri bildirim. Kaç kişi "çalışıyorum" derken gerçekten üretken olduğunu sorguluyor?

---

## Özet Tablo

| Araç | Ne Yapıyor? | Kimler İçin | Zaman Tasarrufu | Kurulum |
|------|-------------|-------------|-----------------|---------|
| Harness Anything | Office AI hub, 47 komut | Veri analisti, İK | 45dk→5dk rapor | Orta |
| OfficeCLI | Prompt→Office dosyası | Satış, Finans | 30dk→2dk | Kolay |
| BagIdea Office | Desktop AI ofis simülasyonu | Karmaşık workflow yönetimi | Değişken | Orta |
| DragonZagent | Windows AI workbench | Windows kullanıcıları | Değişken | Orta |
| Didon | Günlük/haftalık prodüktivite raporu | Freelancer, yönetici | Kağıt sistem → otomatik | Kolay |

---

## Herkesin Kaçırdığı Nokta (#1)
Harness Anything gibi tool'lar "AI Office" pazarını berbat ediyor — çünkü Microsoft'un kendi Copilot'u $30/ay, bu araçlar ücretsiz ve local çalışıyor. 861 star 2 haftada = demo/video etkisi değil, **gerçek ihtiyaç**. KOBİ'ler için AI maliyeti sıfıra inecek.

## Herkesin Kaçırdığı Nokta (#2)
OfficeCLI "sadece dosya üretiyor" deniliyor ama asıl değer **şablon standardizasyonu**. Onlarca kişilik şirkette herkes farklı formatta rapor sunuyor — OfficeCLI şablonu tek tıkla herkes aynı formatta çıktı veriyor. Standart sapma = sıfır.

## Herkesin Kaçırdığı Nokta (#3)
Didon ve benzeri "productivity tracker"lar yeni değil. Ama 2026'da AI bu verileri **sadece gösterge paneli** olmaktan çıkarıp "senin yerine iyileştirme önerisi" sunuyor. "Pazartesi sabahı en düşük üretkenlik — toplantıları öğleden sonra taşı" gibi. Veri → Action.

---

## Kaynaklar

- https://github.com/yb2460/harness-anything
- https://github.com/officecli/officecli-dist
- https://github.com/bagidea/bagidea-office
- https://github.com/outlookceo/DragonZagent
- https://www.didon.app/
