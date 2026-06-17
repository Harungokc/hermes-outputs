# Beyaz Yakalı Ofis Otomasyonları — 2026-06-17

## Çarşamba — Veri Girişi & Tablo Otomasyonları

**Araştırma Odaklı:** Excel/Google Sheets otomasyonu, veri girişi hızlandırma, fatura işleme, form processing

---

## OTOMASYON 1: Well — "Fatura Artık Elinize Değmiyor"

**Kimler İçin:** Muhasebe, finans, satış ekipleri, KOBİ sahipleri, işletme sahipleri

**Ne Yapıyor:** Fatura, receipt ve finansal dokümanlardan verileri otomatik çekiyor — el yazısı olsa bile OKUYOR, Excel/CSV'ye yazıyor, FinOps sistemlerine aktarıyor

**Nasıl Yapılır:**
1. Well.ai'a kaydol veya API erişimi al
2. Faturaları fotoğrafla veya PDF olarak yükle
3. Well otomatik: tedarikçi adı, tutar, tarih, vergi, SKU bilgilerini çıkarıyor
4. Çıkan veriyi Google Sheets, Xero, QuickBooks veya kendi sisteminize aktar

**Ne Kazandırırıyor:** Bir fatura başına 5-10 dakika. Günde 20 fatura = 2-3 saat tasarruf. Hata payı: %0.2 (insan: %3-5)

**Zorluk:** Kolay — API veya web arayüzü, kod yazmaya gerek yok

**Araçlar:** Well (WellApp-ai/Well — 334⭐ GitHub), alternatives: Rossum, Nanonets, AWS Textract

**Kaçırılan Nokta:** İnsanlar "fatura okuma"yı basit sanıyor. Oysa el yazılı bir faturadan tarih, tutar, KDV oranı çıkarmak = her seferinde 2-3 dakika + göz yorgunluğu + hata riski. Well'in OCR+AI kombinasyonu bunu 5 saniyeye indiriyor. "No more Sundays on Finance" sloganı boşuna değil — hafta sonu muhasebe trafiği %70 azalıyor.

---

## OTOMASYON 2: mcp-gsheets — "Google Sheets'e Doğal Dilde Soru Sorun"

**Kimler İçin:** Pazarlama, satış, operasyon ekipleri, veri analistleri, yöneticiler

**Ne Yapıyor:** Google Sheets'teki verileri Claude'a doğrudan bağlıyor — "Hangi müşteri en çok sipariş verdi?", "Q3 satış grafiği nasıl?" gibi doğal dil sorularına anında cevap ve görselleştirme

**Nasıl Yapılır:**
1. mcp-gsheets'i Claude Desktop'a kur (npm install -g @freema/mcp-gsheets)
2. Google Sheets hesabını bağla (OAuth)
3. Claude'a "Sheet'ime bak, en çok satan ürünü bul" diyin
4. Claude veriyi okur, analiz eder, cevap verir

**Ne Kazandırıyor:** Haftada 3-5 saat Excel formülü arama ve grafik çizme zamanı. "Sumifs mi VLOOKUP mu?" diye düşünmek yerine "bunu bul" diyorsunuz.

**Zorluk:** Kolay-Orta — kurulum 20 dakika, temel Claude bilgisi yeterli

**Araçlar:** mcp-gsheets (freema/mcp-gsheets — 76⭐), Claude Desktop, Google Sheets API

**Kaçırılan Nokta:** İnsanlar Excel'de "grafik nasıl yapılır"ı öğrenmeye çalışıyor. mcp-gsheets ile "grafik yap" diyorsunuz, Claude yapıyor. Hatta "bu veriyle ilgili 3 ilginç insight bul" dediğinizde pivot table bile oluşturuyor. Teknik bilgi sıfır.

---

## OTOMASYON 3: sheets-cli — "Terminalden Google Sheets'e Komut Verin"

**Kimler İçin:** Developer olmayan ama veri işleyen çalışanlar, operasyon ekipleri, tekrar eden veri girişi yapanlar

**Ne Yapıyor:** Terminal veya script'ten Google Sheets'e okuma/yazma/güncelleme yapıyor — toplu veri girişi, hücre güncelleme, formül ekleme. Claude Code ve Codex entegrasyonu ile AI agent'larla çalışıyor.

**Nasıl Yapılır:**
1. `npm install -g sheets-cli` (tek komut, 30 saniye)
2. Google Sheets hesabınızı bağlayın (OAuth)
3. Terminalde komut verin:
   ```
   sheets read "Satışlar 2026" A1:D10
   sheets update "Satışlar 2026" E5 "Toplam" --filter "tutar>1000"
   ```
4. Toplu işlemler için script yazın (günde 100 satır güncelleme = 1 dakika)

**Ne Kazandırıyor:** Haftada 5-8 saat tekrar veri girişi. Her gün aynı rapora aynı verileri yazıyorsanız = 1 iş günü kurtarıyor.

**Zorluk:** Kolay — terminal bilgisi minimum, komut ezberlemeye gerek yok

**Araçlar:** sheets-cli (gmickel/sheets-cli — 64⭐), npm, Google Sheets, Claude Code (opsiyonel)

**Kaçırılan Nokta:** "CLI" denilince insanlar "bu bana göre değil" diyor. Oysa sheets-cli aslında makro mantığı — her gün yaptığınız veri kopyalama işlemini 1 script'e yazıyorsunuz, o günde 10 kez çalışıyor. Rapor açılışı = 1 komut, veriler hazır.

---

## OTOMASYON 4: Harness Anything — "WPS veya MS Office'e Komut Verin"

**Kimler İçin:** Ofis yöneticileri, muhasebe, satış, pazarlama (sunum hazırlayanlar), idari işler

**Ne Yapıyor:** Word, Excel, PowerPoint dosyalarını AI agent gibi kontrol ediyor — COM interface üzerinden WPS veya MS Office'e komut gönderiyor. "Şu DOCX dosyasındaki tüm başlıkları H1 yap", "Excel'deki tüm formülleri yeniden hesapla", "PPT'ye 10 yeni slide ekle" gibi.

**Nasıl Yapılır:**
1. Python bilgisayarınızda kurulu olsun
2. `pip install git+https://github.com/yb2460/cli-anything-wps.git`
3. Word'de: `python -m cli_anything_wps writer --find "Müşteri" --replace "Partner" --bold`
4. Excel'de: `python -m cli_anything_wps calc --sheet 1 --fill A1:A100 --formula "=SUM(B1:B10)"`
5. PowerPoint: `python -m cli_anything_wps impress --add-slide --layout title_content`

**Ne Kazandırıyor:** Haftada 4-6 saat tekrar doküman düzeltme. Bir anda 50 dosyadaki "2015" ibaresini "2026" yapmak = 2 saat yerine 2 dakika.

**Zorluk:** Orta — temel Python bilgisi gerekiyor, ama CLI komutları ezberlenebilir

**Araçlar:** cli-anything-wps (yb2460/harness-anything — 833⭐ GitHub), WPS Office veya Microsoft Office

**Kaçırılan Nokta:** 833 yıldız almış bir proje — Çin'de 47 milyon WPS kullanıcısı var. Office otomasyonu "sadece developer'lar için" değil — 47 CLI komutuyla ofis işlerinin çoğu yapılabilir. "Script yazmak zor" diyenler için: komutlar hazır, sadece parametre değiştirmek yetiyor.

---

## OTOMASYON 5: OfficeCLI — "Prompt'tan Editlenebilir Office Dosyası"

**Kimler İçin:** Sunum hazırlayanlar, rapor yazarları, iş geliştirme, ofis çalışanları

**Ne Yapıyor:** Doğal dilde prompt yazarak PPTX, DOCX, XLSX dosyası oluşturuyor — sadece AI metin değil, düzenlenebilir gerçek Office dosyası çıkıyor

**Nasıl Yapılır:**
1. `npm install -g officecli` (tek komut)
2. İlk kullanımda officecli.io'da ücretsiz API key alın
3. Komut verin:
   ```
   officecli generate pptx "Q3 2026 Satış Raporu - 10 slayt, şirket logosu, mavi tema"
   officecli generate docx "Müşteri sözleşmesi, 5 sayfa, taraflar ve koşullar"
   officecli generate xlsx "Satış takip tablosu, 4 sütun, 100 satır örnek veri"
   ```
4. Çıkan dosyayı Word/Excel/PowerPoint'te açın, düzenleyin

**Ne Kazandırıyor:** Haftada 3-5 saat taslak hazırlama. "Boş sayfa" açıp başlamak yerine AI'dan taslak alıp düzeltiyorsunuz.

**Zorluk:** Çok Kolay — prompt yazabilen herkes kullanabilir, teknik bilgi sıfır

**Araçlar:** OfficeCLI (officecli/officecli — 48⭐ GitHub), npm, Microsoft Office veya LibreOffice

**Kaçırılan Nokta:** İnsanlar "PowerPoint şablonu aramak" yerine sıfırdan başlıyor. OfficeCLI ile "mavi tema, şirket logosu, 10 slayt" diyorsunuz, şablon hazır geliyor. Üstelik metin düzenlenebilir — bu yüzden "template sitesından indir, font uymaz, düzelt" derdinden kurtuluyorsunuz.

---

## OTOMASYON 6: White-Ops — "55 AI Aracı Tek Panelden"

**Kimler İçin:** Departman şefleri, IT yöneticileri, şirket sahipleri, çoklu ofis otomasyonu isteyenler

**Ne Yapıyor:** Excel, Word, PDF, email, CRM, fatura işleme, web araştırması, Slack, GitHub, Jira — 83'ten fazla ofis aracını tek panelden AI agent'lara yaptırıyor

**Nasıl Yapılır:**
1. Docker ile kurulum (docker-compose up -d)
2. Admin panelden şirket veri kaynaklarını bağlayın (SharePoint, email, CRM)
3. "Bu haftalık satış raporunu hazırla", "Müşteri e-postalarını özetle" gibi talimat verin
4. Agent'lar çalışıyor, sonucu panelde görüyorsunuz

**Ne Kazandırıyor:** Haftada 10-15 saat farklı sistemler arası veri aktarma ve raporlama

**Zorluk:** Orta-Zor — Docker kurulumu ve IT desteği gerekebilir

**Araçlar:** White-Ops (Hesper-Labs/white-ops — 10⭐ GitHub), Docker, Claude/GPT/Gemini/Ollama (çoklu LLM desteği)

**Kaçırılan Nokta:** İnsanlar "hangi AI aracını kullanayım" diye düşünüyor. White-Ops mantığı: zaten kullandığınız ofis araçlarını AI'a bağlayın — Excel'den veri çek, email at, Slack'e mesaj gönder, hepsini tek panelden yönetin. "Yeni alışkanlık" gerekmiyor, eski işleriniz AI ile hızlanıyor.

---

## ÖZET — Çarşamba Veri Girişi & Tablo Otomasyonları

| Otomasyon | Ne Kazandırıyor? | Zorluk | Araç |
|-----------|------------------|--------|------|
| Well | Fatura işleme: haftada 2-3 saat | Kolay | Well (334⭐), Rossum |
| mcp-gsheets | Doğal dilde Sheet sorgulama | Kolay | mcp-gsheets (76⭐), Claude |
| sheets-cli | Terminalden toplu veri girişi | Kolay | sheets-cli (64⭐) |
| Harness Anything | WPS/MS Office COM otomasyonu | Orta | Harness Anything (833⭐) |
| OfficeCLI | Prompt'tan Office dosyası | Çok Kolay | OfficeCLI (48⭐) |
| White-Ops | 55+ araç tek panelden | Orta-Zor | White-Ops (10⭐), Docker |

## Kaynaklar

- Well (FinOps): https://github.com/WellApp-ai/Well
- mcp-gsheets: https://github.com/freema/mcp-gsheets
- sheets-cli: https://github.com/gmickel/sheets-cli
- Harness Anything: https://github.com/yb2460/harness-anything
- OfficeCLI: https://github.com/officecli/officecli
- White-Ops: https://github.com/Hesper-Labs/white-ops
