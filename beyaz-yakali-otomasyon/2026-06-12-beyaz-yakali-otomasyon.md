# Beyaz Yakalı Ofis Çalışanları İçin AI Otomasyonları
## Tarih: 2026-06-12 | Cuma | Odak: Haftalık Raporlama & Özet Otomasyonları

---

## 📋 ÖZET TABLO — Yeni Haftalık Raporlama Araçları (2026)

| Araç | Ne Yapıyor? | Zorluk | Haftalık Tasarruf |
|------|-------------|--------|-------------------|
| **Tickr** | Slack'te AI project manager, Jira yerine | ⭐ Kolay | 5-8 saat |
| **WinClaw** | Windows native Office otomasyonu | ⭐ Kolay | 4-6 saat |
| **Sourcetable** | Spreadsheet → API bağlantısı | ⭐⭐ Orta | 3-5 saat |
| **Gamma API** | Otomatik sunum/deck oluşturma | ⭐ Kolay | 2-4 saat |
| **RunClaudeRun** | Claude Code scheduler | ⭐ Kolay | 2-3 saat |

---

## 8. HAFTALIK RAPORLAMA & ÖZET OTOMASYONLARI (YENİ)

### Otomasyon #15: Tickr — Slack İçinde AI Project Manager

**Kimler İçin:** Proje yöneticisi, Team lead, CTO, Herhangi bir ekip lideri
**Ne Yapıyor:** Jira kurulumu yapmadan, Slack üzerinde AI ile proje takibi, görev atama, deadline takibi yapıyor.

**Nasıl Yapılır:**
```
1. Slack'te @Tickr bot'u davet ediliyor
2. Ekip üyesi: "@tickr al bu task'ı, Ahmet'e ata, cuma günü bitmeli"
3. Tickr otomatik olarak:
   - Task'ı oluşturuyor
   - Ahmet'e Slack DM atıyor
   - Cuma günü hatırlatıcı koyuyor
   - Bitmemişse pazartesi takip ediyor
4. Haftalık özet: "Bu hafta 12 task tamamlandı, 3 gecikti"
```

**Ne Kazandırırıyor:**
- Jira kurulum süresi: 0 (Slack yeterli)
- Haftalık proje takip: -%80
- Deadline kaçırma: -%90
- Ekip görünürlüğü: +%100

**Zorluk:** ⭐ Kolay (sadece Slack'e bot eklemek)
**Araçlar:** Tickr, Slack
**Fiyat:** Beta'da ücretsiz, sonra $8/kullanıcı/ay

**Kaçırılan Nokta:** Şirketler "Jira kurmalıyız" diye düşünüyor. Oysa ekip zaten Slack'te. AI project manager = Slack'e bot eklemek, 5 dakikada hazır. Jira'nın %10'i kadar özellik, %1000'i kadar kolaylık.

---

### Otomasyon #16: WinClaw — Windows AI Asistanı ile Office Otomasyonu

**Kimler İçin:** Ofis çalışanları, Yönetici asistanı, Muhasebe, İK
**Ne Yapıyor:** Windows'ta çalışan AI asistan — Word, Excel, PowerPoint dosyalarını AI ile yönetiyor, otomatik rapor oluşturuyor.

**Nasıl Yapılır:**
```
1. WinClaw kuruluyor (Windows native app)
2. "Excel'deki satış raporunu al, PowerPoint yap" diyorsunuz
3. WinClaw:
   - Excel dosyasını açıyor
   - Verileri okuyor
   - PowerPoint slide'ları oluşturuyor
   - Grafikleri ekliyor
4. "Bu hafta kaç satış yapıldı?" sorusuna AI cevap veriyor
5. Email draft'ı yazdırıyor (Word)
```

**Ne Kazandırıyor:**
- Office doküman işleme: -%70
- Rapor hazırlama: -%80
- Dosya arama: -%60
- "Şu dosyayı bul" sorusu: -%90

**Zorluk:** ⭐ Kolay (Windows'ta normal app kurmak gibi)
**Araçlar:** WinClaw, Microsoft Office
**Fiyat:** Ücretsiz (açık kaynak)
**Kaynak:** https://github.com/itc-ou-shigou/winclaw

**Kaçırılan Nokta:** İnsanlar "Office otomasyonu = VBA makro yazmak" diye düşünüyor. Oysa WinClaw ile doğal dilde komut veriyorsunuz: "Bu Excel'i PDF yap ve email ile gönder" — 5 saniye.

---

### Otomasyon #17: Sourcetable — Spreadsheet'i API'ye Bağla

**Kimler İçin:** Analist, Satış müdürü, Pazarlama, Finans
**Ne Yapıyor:** Google Sheets veya Excel'i 50+ farklı API'ye bağlayarak otomatik veri güncelleme yapıyor.

**Nasıl Yapılır:**
```
1. Sourcetable açılıyor (tarayıcıda)
2. "Shopify'a bağlan" veya "HubSpot'a bağlan" seçiliyor
3. Artık spreadsheet'de:
   - =SHOPIFY_REVENUE("last_30_days") yazıyorsunuz
   - =HUBSPOT_LEADS() yazıyorsunuz
   - Veriler otomatik geliyor
4. Haftalık raporda AI:
   - "Shopify'dan son 30 gün satış = X TL"
   - "HubSpot'tan yeni lead = Y"
5. Tek tıkla refresh
```

**Ne Kazandırıyor:**
- API entegrasyonu: -%95 (artık kod yazmaya gerek yok)
- Veri güncelleme: -%80
- Excel formülleri: -%70 (AI doğrudan veri çekiyor)
- Haftalık rapor hazırlama: -%60

**Zorluk:** ⭐⭐ Orta (formül yazma var ama çok basit)
**Araçlar:** Sourcetable, Google Sheets, Excel
**Fiyat:** Ücretsiz başlangıç, $25+/ay
**Kaynak:** https://sourcetable.com

**Kaçırılan Nokta:** İnsanlar "API'den veri çekmek = yazılımcı işi" diye düşünüyor. Sourcetable ile Excel hücresine formül yazmak kadar kolay. CRM, e-ticaret, banka verisi = tek komut.

---

### Otomasyon #18: Gamma API — Otomatik Sunum Oluşturma

**Kimler İçin:** Pazarlama, Satış, Yönetici, Herkes sunum yapan
**Ne Yapıyor:** Sadece bir metin veya topic veriyorsunuz, AI otomatik olarak profesyonel sunum oluşturuyor.

**Nasıl Yapılır:**
```
1. Gamma'ya API key alınıyor
2. Prompt gönderiliyor:
   "Q2 satış raporu sunumu yap
    - 10 slide
    - Şirket logosu var
    - Reng: mavi"
3. Gamma otomatik oluşturuyor:
   - Slide 1: Kapak
   - Slide 2: Özet
   - Slide 3-8: Veriler, grafikler
   - Slide 9: Sonuç
   - Slide 10: Teşekkür
4. PowerPoint veya PDF olarak indir
```

**Ne Kazandırıyor:**
- Sunum hazırlama: -%90 (2 saat → 10 dakika)
- Tasarım kalitesi: +%50 (profesyonel görünüm)
- Tutarlılık: +%100 (şirket standartları)

**Zorluk:** ⭐ Kolay (API key + basit API çağrısı)
**Araçlar:** Gamma API, PowerPoint, Google Slides
**Fiyat:** API başına $0.01, web arayüzü ayrı
**Kaynak:** https://developers.gamma.app

**Kaçırılan Nokta:** Sunum hazırlarken "görsel tasarım" zaman alıyor. Gamma AI hem içerik hem tasarımı bir anda yapıyor. İnsan sadece veriyi kontrol ediyor.

---

### Otomasyon #19: RunClaudeRun — Haftalık Claude Code Scheduler

**Kimler İçin:** Developer, Veri bilimci, Herkes kod yazan
**Ne Yapıyor:** Haftalık veya günlük schedule'a Claude Code komutları koyuyorsunuz, otomatik çalışıyor.

**Nasıl Yapılır:**
```
1. RunClaudeRun kuruluyor
2. Haftalık schedule tanımlanıyor:
   - Her Pazartesi 09:00: "GitHub'dan上周issue'ları özetle"
   - Her Cuma 17:00: "Haftalık commit özeti çıkar"
   - Her gün 08:00: "Bugün hangi PR'lar bekliyor?"
3. Claude Code otomatik çalışıyor
4. Sonuç Slack veya email ile geliyor
```

**Ne Kazandırıyor:**
- Haftalık kod özeti: -%100 (artık 0 dakika)
- PR takibi: +%80
- Developer productivity: +%30

**Zorluk:** ⭐⭐ Orta (CLI kullanımı gerekiyor)
**Araçlar:** RunClaudeRun, Claude Code
**Fiyat:** Ücretsiz (açık kaynak)
**Kaynak:** https://runclauderun.com

---

### Otomasyon #20: AI Destekli Haftalık KPI Dashboard

**Kimler İçin:** CEO, Yönetici, Satış müdürü, Pazarlama müdürü
**Ne Yapıyor:** 5 farklı kaynaktan (CRM, Analytics, Banka, Sheets, Email) veri çekip tek dashboard'da haftalık KPI özeti oluşturuyor.

**Nasıl Yapılır:**
```
1. Her kaynak (CRM, Analytics, vs) bir Google Sheet'e bağlı
2. n8n veya Zapier ile her gün veriler güncelleniyor
3. Cuma 16:00'da:
   - AI tüm sheet'leri okuyor
   - "Satış: bu hafta X TL, geçen hafta Y TL, değişim: +%Z"
   - "Web trafiği: X kişi, en çok hangi sayfa"
   - "Müşteri memnuniyeti: X/10"
4. Tek sayfalık özet:
   - Semaphore dashboard (yeşil/sarı/kırmızı)
   - Trend grafiği
   - "Dikkat et: şu KPI düşüyor"
5. Email ile CEO'ya gönderiliyor
```

**Ne Kazandırıyor:**
- Dashboard takibi: -%80 (artık tek email)
- Karar hızı: +%50
- "Şu anda durum ne?" sorusu: -%90

**Zorluk:** ⭐⭐ Orta
**Araçlar:** n8n, Google Sheets, Power BI, Claude API
**Kaçırılan Nokta:** CEO'lar "dashboard açıp bakmak" yerine "email ile özet almak" istiyor. Dashboard = detay, email = karar. AI email'i otomatik üretiyor.

---

## 📊 YENİ TRENDLER — 2026 Ofis Otomasyonu

### #1: "AI Native" Araçlar Pasif Oluyor
Eski yaklaşım: "Zapier ile X'i Y'ye bağla"
Yeni yaklaşım: "AI'ya ne yapmak istediğini söyle, o yapıyor"

Örnek:
- **Eski:** Zapier'de 15 adımlık workflow kur
- **Yeni:** "Email'lerimdeki faturaları oku, muhasebe programına gir" → AI yapıyor

### #2: Slack/Teams Artık İşletim Sistemi Gibi
- Tickr, Blimp gibi araçlar Slack içinde çalışıyor
- "Yeni bir app kurmak" yerine "Slack'e bot eklemek" tercih ediliyor
- Kurumsal yazılım → Slack entegrasyonu

### #3: Spreadsheet'ler API'ye Bağlanıyor
- Sourcetable: Excel/Sheets + 50+ API
- Artık "veri çekmek" için kod yazmaya gerek yok
- Formül = API çağrısı

### #4: Raporlama AI'ya Bırakılıyor
- "Rapor hazırla" = AI'ya veri kaynaklarını göster, o çıkarsın
- İnsan = karar verici, AI = veri toplayıcı

---

## 🎯 EN POPÜLER 5 OTOMASYON (2026 Güncelliği)

### #1: WinClaw — Windows AI Asistanı
- **Kim kullanıyor:** Ofis çalışanları (özellikle Windows kullananlar)
- **Neden popüler:** Kurulum 5 dakika, Office otomasyonu hemen çalışıyor
- **Sonuç:** Günde 1-2 saat tasarruf

### #2: Tickr — Slack İçinde Project Manager
- **Kim kullanıyor:** Ekip liderleri, proje yöneticileri
- **Neden popüler:** Jira kurmadan 5 dakikada AI project manager
- **Sonuç:** Haftada 5+ saat tasarruf

### #3: Sourcetable — Spreadsheet API Bağlantısı
- **Kim kullanıyor:** Analistler, satış müdürleri
- **Neden popüler:** Excel'den API'ye direkt bağlantı
- **Sonuç:** Manuel veri girişi = 0

### #4: Gamma API — Otomatik Sunum
- **Kim kullanıyor:** Pazarlama, satış, yöneticiler
- **Neden popüler:** 2 saatlik iş = 10 dakika
- **Sonuç:** Sunum kalitesi +%50

### #5: Haftalık AI KPI Dashboard
- **Kim kullanıyor:** CEO, yöneticiler
- **Neden popüler:** Tüm veriler tek email'de
- **Sonuç:** Karar hızı +%50

---

## 🔧 KAYNAKLAR VE LİNKLER

### Araçlar
- WinClaw: https://github.com/itc-ou-shigou/winclaw
- Tickr: https://tickr.ai (Slack entegrasyonu)
- Sourcetable: https://sourcetable.com
- Gamma API: https://developers.gamma.app
- RunClaudeRun: https://runclauderun.com
- Blimp: https://getblimpy.cloud

### HN Kaynakları (2026)
- "Show HN: WinClaw – Windows AI assistant, Office automation, infinite Skills" (2026-02-12)
- "Show HN: Tickr – AI project manager that lives inside Slack (replaces Jira)" (2026-02-22)
- "Show HN: Sourcetable – Operational spreadsheets that can read/write to any API" (2025-10-30)
- "Show HN: Gamma API- Auto-generate decks, docs and carousels from raw input" (2025-09-23)
- "Show HN: runCLAUDErun – Scheduler for Claude Code" (2025-10-06)
- "Show HN: Blimp – AI-Native Productivity Suite to Unify Your Tools" (2026-01-05)

---

## 📝 NOTLAR

### Cuma Raporlama Otomasyonları — Neden Önemli?
Cuma günü ofis çalışanları için en yoğun günlerden biri:
- Haftalık rapor hazırlama
- Sonuçları email ile gönderme
- Ekip özeti çıkarma
- Gelecek hafta planı yapma

AI ile bu işlerin çoğu otomatik hale geliyor:
- Veri toplama → AI
- Rapor taslağı → AI
- Email yazma → AI
- İnsan → sadece kontrol + onay

### Kaçırılan Fırsat
Ofis çalışanlarının %80'i "Excel'i açıp veri giriyorum" diyor. Oysa bugün:
- Excel = API'ye bağlanabilir
- Email = AI okuyup yanıt verebilir
- Rapor = AI hazırlayabilir
- Takvim = AI yönetebilir

"Ben ofis çalışanıyım, kod yazamam" diyenler için: Artık kod yazmaya gerek yok. No-code araçlar + AI = herkes yapabilir.

---

*Son güncelleme: 2026-06-12 | Cuma | Haftalık Raporlama & Özet Otomasyonları*