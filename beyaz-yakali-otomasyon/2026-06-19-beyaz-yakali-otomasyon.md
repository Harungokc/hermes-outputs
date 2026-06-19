# Beyaz Yakalı Ofis Otomasyonları — 2026-06-19

## Cuma — Haftalık Raporlama & Özet Otomasyonları

**Araştırma Odaklı:** Haftalık özet otomasyonu, KPI takip ve raporlama, dashboard güncelleme, çok kaynaklı veri birleştirme, Cuma özeti AI ile yazma

---

## OTOMASYON 1: Haftalık Rapor Oluşturucu — "5 Kaynaktan Gelen Veriyi AI 3 Dakikada Özetliyor"

**Kimler İçin:** Pazarlama müdürü, satış temsilcisi, operasyon şefi, yönetici asistanı, departman yöneticileri

**Ne Yapıyor:** Haftalık tüm verilerinizi (Google Analytics, CRM satışları, email metrikleri, sosyal medya) tek bir dosyada birleştirip AI'a özetlettiriyorsunuz. Cuma 17:00'da otomatik olarak yöneticiye email gidiyor — "Bu hafta neler oldu" özetiyle birlikte.

**Nasıl Yapılır:**
```
Seçenek A — No-code (n8n):
1. n8n'de yeni workflow oluştur
2. Workflow trigger: Her Cuma 16:00
3. Google Sheets node: Haftalık verileri çek
4. HTTP Request node: Google Analytics API'den hafta verisi
5. Slack/Email node: CRM'den hafta satışları
6. Claude node: Tüm verileri prompt'la özetlet:
   "Bu haftanın verilerini 5 paragraf özetle: 
   - En çok satan ürün
   - Müşteri kazanımı 
   - Web sitesi trafiği
   - Email açılma oranları
   - Haftaya dikkat edilmesi gerekenler"
7. Email node: Sonucu yöneticiye gönder

Seçenek B — Google Sheets + Claude:
1. Tüm verileri tek bir Google Sheet'e koyun
2. Sheet'te yeni bir sekme açın: "AI Özet"
3. =_claude formulası ile verileri çekin
4. "Bu haftayı özetle" prompt'u verin
5. n8n ile Cuma otomatik çalıştırma
```

**Ne Kazandırıyor:** Haftalık rapor hazırlama: 2-4 saat → 10 dakika. Rapor Cuma 17:00'da hazır, siz haftayı kapatırken email zaten gitmiş.

**Zorluk:** Kolay — no-code platform ile 1 saat kurulum, sonra tam otomatik

**Araçlar:** n8n, Make.com, Google Sheets, Claude API, Zapier, Google Analytics API, HubSpot/Zoho CRM API

**Kaçırılan Nokta:** İnsanlar "rapor yazmak" ile "raporu okumak" için harcanan zamanı karıştırıyor. Yönetici raporu okumak için 5 dakika harcar — siz onu yazmak için 3 saat harcıyorsunuz. AI raporu yazıyor, insan yorumluyor ve karar veriyor. Haftada 3 saat × 52 hafta = 156 saat = 20 iş günü.

---

## OTOMASYON 2: KPI Dashboard Otomatik Güncelleyici — "Excel'deki Sayılar Artık Kendini Güncelliyor"

**Kimler İçin:** Satış müdürü, CFO, operasyon müdürü, veri analisti, KOBİ sahipleri

**Ne Yapıyor:** Haftalık veya günlük KPI'larınızı (satış hedefi, gider, kar, müşteri memnuniyeti) bir dashboard'da görüyorsunuz. Veriler elle girilmiyor — CRM, muhasebe yazılımı, email araçlarından otomatik çekiliyor. Yapay zeka grafik yorumunu da yazıyor: "Satışlar geçen haftaya göre %12 düştü, muhtemelen tatil döneminden."

**Nasıl Yapılır:**
```
1. Google Sheets veya Excel'de KPI dashboard oluşturun
2. Veri kaynaklarını bağlayın:
   - HubSpot/Zoho/Pipedrive → Satış verileri (API veya Zapier/n8n)
   - WooCommerce/Shopify → E-ticaret verileri  
   - Gmail/Email tool → Email açılma oranları
   - Google Analytics → Web sitesi trafiği
3. n8n veya Zapier'da "her gün sabah 8:00" trigger'ı kurun
4. Veriler çekilir → Google Sheets'e yazılır
5. Optional: Claude API ile "dashboard'ta ne görüyorsun?" sorusu
   → Görsel zaten hazır, üstüne AI yorumu ekleniyor

Daha basit versiyon — sadece Google Sheets:
1. Her kaynak için ayrı Sheet sekmesi
2. IMPORTRANGE ile ana dashboard'a çek
3. Ana sayfada =AVERAGE, =SUM formülleri ile hesaplamalar
4. Grafikler otomatik güncellenir
```

**Ne Kazandırıyor:** Günlük dashboard güncelleme: 30 dakika → 0 (tamamen otomatik). Haftalık CEO raporu: 4 saat → 5 dakika.

**Zorluk:** Orta — temel Excel/Sheets bilgisi yeterli, API bağlantıları kurulum gerektirir

**Araçlar:** Google Sheets, Microsoft Power BI (ücretsiz versiyon var), n8n, Zapier, Supermetrics (veri bağlayıcı), Google Data Studio

**Kaçırılan Nokta:** İnsanlar dashboard'ı "görselleştirme aracı" olarak görüyor. Oysa dashboard'ın değeri sadece grafikte değil, **trend'te.** AI grafikteki trend'i görüyor: "Kar marjı 3 haftadır düşüyor, tedarikçi değişikliği etkili olabilir" gibi yorum ekliyor. Standart dashboard'ta bu yorumu siz yapıyorsunuz — AI'lı dashboard'ta AI yapıyor.

---

## OTOMASYON 3: Cuma Otomatik Email Özeti — "Ekip Her Cuma 17:00'de Ne Olduğunu Biliyor"

**Kimler İçin:** Takım liderleri, proje yöneticileri, yöneticiler, startup kurucuları, departman şefleri

**Ne Yapıyor:** Her Cuma (veya Pazartesi) ekip üyelerine otomatik email gidiyor: "Bu hafta kim ne yaptı, hangi projeler bitti, önümüzdeki hafta öncelikler neler?" Slack, Jira, email, Google Calendar'dan veri çekiyor. Yapay zeka haftalık özet taslağını oluşturuyor.

**Nasıl Yapılır:**
```
Seçenek A — Komple Otomatik (n8n + Claude):
1. n8n workflow:
   - Trigger: Her Cuma 16:30
   - Slack node: Haftalık channel mesajlarını çek
   - Jira node: Tamamlanan ticket'ları al
   - Google Calendar: Haftalık toplantıları özetle
   - Email node: Gönderilen/alınan önemli emailleri çek
2. Tüm verileri Claude'a gönder prompt'la:
   "Bir ekip haftalık email özeti hazırla:
   - Kim ne yaptı (Slack mesajlarından çıkar)
   - Hangi projeler bitti (Jira'dan)
   - Önümüzdeki hafta öncelikleri
   - Dikkat edilmesi gereken sorunlar"
3. Claude özet çıkarır → Email olarak gönder
4. Ekip her Cuma 17:00'de özeti alır

Seçenek B — Asistan Destekli (Ghostbug ve benzeri):
1. Ghostbug.com veya alternatifine kaydol
2. Slack/Google Calendar/Notion bağla
3. AI her Cuma otomatik özet üretir
4. İnsan sadece düzeltme yapar, gönderir
```

**Ne Kazandırıyor:** Haftalık ekip email'i yazma: 45 dakika → 2 dakika (düzenleme). Toplantıda harcanan "geçen hafta ne oldu?" bölümü: 30 dakika → 0 (herkes önceden okudu).

**Zorluk:** Orta — n8n bilgisi veya Ghostbug gibi hazır araç

**Araçlar:** n8n, Ghostbug, Spinamp (email özeti), Google Workspace + Claude, Slack, Jira, Notion

**Kaçırılan Nokta:** "Haftalık özet" çoğu şirkette email ile gönderiliyor ve 5 kişiden 3'ü okumuyor — çünkü 10 paragraflık duyuru emailsi sıkıcı. AI hazırladığında özet 3 paragraf + bullet points oluyor, okunabilir hale geliyor. "Bu hafta 3 iş aldık, 2 proje bitti, önümüzdeki hafta X öncelik" — direkt olarak.

---

## OTOMASYON 4: jopilot-ai — "İş Başvurularınız Google Sheets'ten Takip Ediliyor"

**Kimler İçin:** İK uzmanları, işe alım yöneticileri, KOBİ sahipleri (kendi işlerine başvuru alan), araştırma ekipleri

**Ne Yapıyor:** Google Sheets'teki iş başvuru takip tablonuza AI bağlıyor — başvuru sahibinin CV'sini otomatik okuyor, pozisyona uygunluğunu skorluyor, follow-up email taslakları çıkarıyor, mülakat tarihi hatırlatması atıyor. Ayrıca Gemini API ile her başvuru için detaylı değerlendirme rapu oluşturuyor.

**Nasıl Yapılır:**
```
1. GitHub: harikrishna8121999/jobpilot-ai
2. Kurulum:
   - Python 3.9+ gerekiyor
   - pip install jobpilot-ai
   - Google Sheets API credential al
   - Gemini API key al (ücretsiz var)
3. Google Sheets'te tablo oluştur:
   - Başvuru Sahibi | Pozisyon | Tarih | Durum | CV Link | Skor | Not
4. Her yeni başvuru geldiğinde:
   - CV link'ini Sheets'e koy
   - AI otomatik: CV oku → Skor ver → Gemini ile değerlendir
   - Skor 7/10 üstündeyse → Email hatırlatma
5. Haftalık özet: "Bu hafta 23 başvuru geldi, 5'i mülakata uygun"
```

**Ne Kazandırıyor:** CV tarama: başvuru başına 5 dakika → 30 saniye. Haftalık İK raporu: 2 saat → 5 dakika.

**Zorluk:** Orta — temel Python bilgisi ve API key kurulumu

**Araçlar:** jobpilot-ai (harikrishna8121999/jobpilot-ai — GitHub), Gemini API, Google Sheets, Gmail

**Kaçırılan Nokta:** İK profesyonelleri "CV okuma"yı işin doğası olarak kabul ediyor. Oysa AI aynı CV'yi 10 saniyede okuyup scoring yapabiliyor. İnsan farkı: "bu kişi şirkete kültürel açıdan uygun mu?" — bu AI'ın henüz tam yapamadığı kısım. Yani AI hızlı eleme yapıyor, insan son seçimi yapıyor. İşe alım süresi: 2 hafta → 4 gün.

---

## OTOMASYON 5: xlflow — "Excel VBA Projelerinizi AI Yönetiyor"

**Kimler İçin:** Finans analistleri, muhasebeciler, veri işleyen ofis çalışanları, Excel ağırlıklı iş yapanlar

**Ne Yapıyor:** Excel VBA (macro) projelerinizi AI agent'a bağlıyor — VBA kodlarını okuyor, test ediyor, hata buluyor, yeni fonksiyonlar ekliyor. Raporlama Excel dosyalarınız varsa, xlflow ile AI'a "bu raporu haftalık olarak çalıştır" diyebiliyorsunuz.

**Nasıl Yapılır:**
```
1. GitHub: harumiWeb/xlflow (8⭐ — yeni proje)
2. Kurulum: pip install xlflow
3. Excel dosyanızda VBA macro varsa:
   - xlflow'a Excel dosyasını verin
   - "Bu macro ne yapıyor?" diye sorun
   - "Haftalık rapor için her Cuma çalışacak şekilde ayarla" deyin
4. CLI üzerinden komut verin:
   ```
   xlflow run "HaftalikRapor.xlsx" --macro "RaporOlustur" --schedule "weekly"
   ```
5. Her Cuma otomatik çalışır, rapor hazır
```

**Ne Kazandırıyor:** Excel macro hata ayıklama: saatler → dakikalar. Haftalık rapor hazırlama: 1 saat → 5 dakika (otomatik çalışma).

**Zorluk:** Orta — temel Excel VBA bilgisi + CLI kullanımı

**Araçlar:** xlflow (harumiWeb/xlflow — 8⭐ GitHub), Excel VBA, Python, n8n (opsiyonel schedule)

**Kaçırılan Nokta:** Excel VBA "eski teknoloji" olarak görülüyor ama hâlâ milyonlarca şirkette kullanılıyor. xlflow ile AI mevcut VBA kodlarınızı okuyup "neden hata veriyor?" diye sormuyor — doğrudan düzeltiyor. Miras alınan Excel dosyaları artık kabus değil — AI anlıyor, düzeltiyor, geliştiriyor.

---

## OTOMASYON 6: Eatmydata.ai — "Veritabanından Dashboard'a Soru-Cevap ile Ulaşın"

**Kimler İçin:** Veri analistleri, BI uzmanları, CFO ofisi, pazarlama analistleri, KOBİ sahipleri

**Ne Yapıyor:** SQL bilmeden veritabanınıza doğal dilde soru soruyorsunuz — "Bu ay en çok satan ürünümüz hangisi?", "Müşteri kaybımız neden arttı?" gibi. AI SQL oluşturuyor, sorguyu çalıştırıyor, sonucu dashboard olarak gösteriyor. Local-first, veriler şirket dışına çıkmıyor.

**Nasıl Yapılır:**
```
1. eatmydata.ai adresine gidin
2. Veritabanı bağlantınızı yapın (PostgreSQL, MySQL, SQLite)
3. Doğal dilde sorun:
   - "Q2 satışlarımız Q1'e göre nasıl?"
   - "En çok şikayet aldığımız ürün hangisi?"
   - "Hangi kanaldan gelen müşteriler en çok alışveriş yapıyor?"
4. AI otomatik SQL yazar, çalıştırır, sonucu grafik olarak gösterir
5. Haftalık rapor için: "her Cuma sabahı bütün metrikleri özetle" schedule edin
```

**Ne Kazandırıyor:** SQL yazma öğrenme: haftalar → 0. Dashboard oluşturma: saatler → dakikalar. Haftalık analiz raporu: 3 saat → 5 dakika.

**Zorluk:** Kolay — SQL bilmeye gerek yok, sadece "ne görmek istiyorum?" diyorsunuz

**Araçlar:** Eatmydata.ai (Question-to-SQL-to-Dashboard, HN 8 puan), PostgreSQL, MySQL, SQLite, MongoDB

**Kaçırılan Nokta:** İnsanlar veri istemek için "BI uzmanına email atıp 3 gün beklemek" zorunda hissediyorlar. Eatmydata ile "hangi ürün bu ay en çok sattı?" diye soruyorsunuz, 30 saniyede cevap geliyor. Şirketler hâlâ "herkes Excel açsın, veri çeksin" mantığında — oysa AI çağında veri erişimi dakikalar, haftalar değil.

---

## LinkedIn Post Fikri

**Başlık:** "Haftalık Raporu 4 Saatte Yazıyordum, Şimdi 5 Dakikada Hazır"

**Herkesin gördüğü:** Her Cuma öğleden sonra "haftalık rapor" paniği — veri çek, Excel'e koy, yorumla, email at.

**Herkesin kaçırdığı nokta:** Raporu yazan ile okuyan arasındaki zaman farkı. Siz 4 saat harcıyorsunuz, yönetici onu 5 dakikada okuyor. Raporun değeri sadece içinde — verilerin nerede olduğu, nereye gittiği AI için önemli değil. Haftada 4 saat × 52 = 208 saat = 1 ay. Bunu "daha hızlı rapor yazma" değil, "haftada 1 iş günü kazanma" olarak düşünün.

---

## Kaynaklar

- n8n ($5.2B değerleme): https://n8n.io
- jopilot-ai: https://github.com/harikrishna8121999/jobpilot-ai
- xlflow: https://github.com/harumiWeb/xlflow
- Eatmydata.ai: https://eatmydata.ai (HN Show HN, Haziran 2026)
- Harness Anything (847⭐): https://github.com/yb2460/harness-anything
- Social Flow (145⭐, Meta reporting): https://github.com/vishalgojha/social-flow
