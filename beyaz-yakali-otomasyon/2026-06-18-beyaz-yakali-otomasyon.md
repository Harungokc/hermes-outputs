# Beyaz Yakalı Ofis Otomasyonları — 2026-06-18

## Perşembe — İletişim & Takip Otomasyonları

**Araştırma Odaklı:** Slack/Teams otomasyonları, müşteri ve tedarikçi takip sistemleri, otomatik bildirimler, CRM entegrasyonları, dahili iletişim AI araçları

---

## OTOMASYON 1: Slack/Teams + Jira Otomasyon Botu — "Ekip İçi Görev Takibini AI Yapıyor"

**Kimler İçin:** Proje yöneticileri, takım liderleri, yazılım ekipleri, departman şefleri

**Ne Yapıyor:** Slack veya Teams'te "/task" yazdığınızda otomatik olarak Jira ticket'ı oluşturuyor, iş arkadaşlarınızı atıyor, deadline belirliyor. Hiç Jira'ya girmeden sadece Slack üzerinden tüm proje takibi yapılıyor.

**Nasıl Yapılır:**
```
1. Slack'te BennyDanielT/Slack-Jira-Automation bot'unu kur
2. Jira hesabınızı bot'a bağla (OAuth)
3. Slack'te yazın: "/task [açıklama] @ahmet @zeynep due:cuma"
4. Bot otomatik olarak:
   - Jira'da ticket oluşturuyor
   - Ahmet ve Zeynep'e Slack'ten bildirim gidiyor
   - Deadline'i takvime ekliyor
5. Biten işler için: "/done TASK-123" yazın, otomatik kapanır
```

**Ne Kazandırıyor:** Haftada 3-5 saat Jira açma, ticket güncelleme, takip email'leri yazma zamanı

**Zorluk:** Kolay — Slack'te /slash command yazmak kadar basit, IT kurulumu 15 dakika

**Araçlar:** Slack, Jira, BennyDanielT/Slack-Jira-Automation (GitHub), alternatif: n8n Slack+Jira entegrasyonu

**Kaçırılan Nokta:** İnsanlar hâlâ "Jira açıp ticket bakmak" zorunda olduklarını sanıyor. Oysa Slack'e `/task müşteri raporunu güncelle @ayşe due:salı` yazmak = 3 dakikalık iş, 30 saniyede yapılmış oldu. Jira'nın kendisine girmek tamamen opsiyonel haline geldi.

---

## OTOMASYON 2: Microsoft Scout — "Gece 3'te Email Atan AI Çalışma Arkadaşınız"

**Kimler İçin:** Yoğun yöneticiler, satış temsilcileri, müşteri ilişkileri yöneticileri, 7/24 erişilebilir olması gereken profesyoneller

**Ne Yapıyor:** Şirketinizin AI "çalışanı" — email atıyor, toplantı ayarlıyor, dosya buluyor, sizin adınıza müşteri takibi yapıyor. Gece uyurken bile çalışıyor. OpenClaw tabanlı, şirket verilerinizle çalışıyor (gizli bilgi sızmıyor).

**Nasıl Yapılır:**
```
1. Microsoft 365 Copilot 2026 redesign'ında Scout'u aktif et
2. IT yöneticisi: SharePoint, Teams, Outlook, dosyaları Scout'a bağlar
3. Siz doğal dilde talimat verin:
   - "Her sabah 8'de bugünün toplantılarını özetle"
   - "Bu müşteriyle bir haftadır yazışmadık, hatırlatma at"
   - "Onay belgelerini bul, yöneticiye email at"
4. Scout arka planda çalışır, 7/24
```

**Ne Kazandırıyor:** Günde 1-2 saat email yazma, takvim kontrolü, dosya arama zamanı

**Zorluk:** Kolay — doğal dilde talimat vermek yetiyor, teknik bilgi gerektirmiyor

**Araçlar:** Microsoft 365 Copilot Scout (OpenClaw-based), Teams, Outlook, SharePoint

**Kaçırılan Nokta:** Scout sıradan bir chatbot değil — "şirket context'ini" anlıyor. Normal ChatGPT'den farkı: şirketinizin kendi verileriyle çalışıyor. Geçen haftaki müşteri email'lerinizi, toplantı notlarınızı, şirket dosyalarınızı biliyor. Bugün (Haziran 2026) ABD'de canlıya girdi, henüz çok az şirket kullanıyor = erken adapte olanlar avantaj sağlayacak.

---

## OTOMASYON 3: AI Lead Takip & Otomatik Hatırlatma — "Müşteriyle İletişimi AI Kesmiyor"

**Kimler İçin:** Satış temsilcileri, iş geliştirme uzmanları, müşteri ilişkileri yöneticileri, KOBİ sahipleri

**Ne Yapıyor:** Potansiyel müşterilerinizle iletişimi hiç kesilmiyor. Müşteriye ilk email'i attınız, cevap gelmedi — 3 gün sonra otomatik hatırlatma geliyor. Müşteri soru sordu, cevap verdiniz — 7 gün sonra "nasıl yardımcı olabiliriz?" follow-up geliyor. Tüm bu takip süreçleri AI tarafından yönetiliyor.

**Nasıl Yapılır:**
```
Seçenek A — No-code (Kolay):
1. Google Sheets'e müşteri verilerinizi koyun (isim, email, son iletişim tarihi, aşama)
2. n8n veya Make.com'da workflow kurun:
   - "Son iletişim > 3 gün > Cevap yok" → Otomatik hatırlatma email
   - "Son iletişim > 7 gün > Cevap yok" → Farklı email taslağı
   - "Müşteri soru sordu > Cevap verdim > 7 gün sonra" → Follow-up
3. Gmail veya email hesabınızdan otomatik gönderim

Seçenek B — PressedCoffee/client-reminder (Google Sheets + Gmail):
1. GitHub'dan PressedCoffee/client-reminder reposunu kur
2. Google Sheets'e client verilerini gir
3. Gmail hesabınızı bağla
4. Otomatik hatırlatma mailleri gider
```

**Ne Kazandırıyor:** Haftada 4-6 saat müşteri takip email'i yazma. Satış döngüsünde "%20-30 daha az müşteri kaybı" (sekmeleri takip etmeyi bırakan şirketlerin kaybı)

**Zorluk:** Kolay (no-code platform ile) — Google Sheets bilmek yeterli

**Araçlar:** n8n, Make.com, PressedCoffee/client-reminder (GitHub, apps-script + Gmail), NDDimension/clientsense-ai-lead-engine (n8n + Gemini + Sheets)

**Kaçırılan Nokta:** Araştırmalar gösteriyor ki satışta "ikinci email'i atan" kazanıyor. İlk email atıldıktan sonra 46% müşteri hiç cevap vermiyor, ama 2-3 follow-up ile bu oran %60'a düşüyor. İnsanlar "spam gibi hissettirir" kaygısıyla follow-up yapmaktan kaçınıyor — oysa AI kişiselleştirilmiş follow-up taslakları çıkarıyor, spam hissi yok.

---

## OTOMASYON 4: Dahili Bildirim & Onay Sistemi — "İmzayı Bekleyen İşler Size Ulaşıyor"

**Kimler İçin:** Yöneticiler, muhasebe departmanı, hukuk departmanı, satın alma, insan kaynakları

**Ne Yapıyor:** Şirket içinde bekleyen onayları, imzaları, kararları AI takip ediyor. "Fatura bekliyor", "Sözleşme imzaya gitti", "Yönetici onayı bekliyor" gibi durumları otomatik izliyor ve ilgili kişiye Slack/Teams/Email ile bildirim gönderiyor.

**Nasıl Yapılır:**
```
1. n8n veya Zapier'da workflow kurun:
   - Uygunluk matrix (dosya/yazılım):
     * Fatura geldiğinde → Muhasebeciye Slack mesajı + Onay linki
     * Sözleşme imzaya gittiğinde → Yöneticiye email hatırlatma
     * İzin başvurusu → Varantı'ya bildirim
2. Öncelik seviyesi belirleyin:
   - Normal: 24 saat içinde hatırlatma
   - Acil: 2 saat sonra hatırlatma + Slack'te mention
3. Onay linkine tıklayınca → Durum güncellenir, takip kapanır
```

**Ne Kazandırıyor:** Haftada 2-4 saat "neyi kime soracağım, kim ne bekliyor" email'i yazma zamanı

**Zorluk:** Kolay — no-code platform ile kurulabilir, temel mantık: "X oldu → Y'ye bildirim git"

**Araçlar:** n8n, Zapier, Make.com, Microsoft Power Automate

**Kaçırılan Nokta:** Şirketlerde en büyük zaman kaybı "bir şeyin nerede olduğunu sormak." Fatura müdürde mi? Sözleşme imzalandı mı? AI bu takip işlemini tamamen ortadan kaldırıyor. Herkes sadece kendisine gelen bildirimlerle ilgileniyor.

---

## OTOMASYON 5: Otomatik Müşteri Durumu Güncellemesi — "Herkes Aynı Sayfayı Görüyor"

**Kimler İçin:** Satış ekipleri, proje yöneticileri, müşteri hizmetleri, account manager'lar

**Ne Yapıyor:** Müşteriyle yapılan görüşme sonrasında AI otomatik olarak CRM'e not düşüyor, sonraki adımları belirliyor, ve ekip arkadaşlarınıza Slack'ten durum güncellemesi atıyor. "Müşteri X şirketiyle görüştüm, teklif hazır, perşembe günü sunum var" dediğinizde AI bunu herkese iletiyor.

**Nasıl Yapılır:**
```
1. Vincent29191160/crm-booking-automation (GitHub) kurulumu
2. CRM'inizi (HubSpot, Zoho, Pipedrive) bağlayın
3. Slack'te bot kurulumu
4. Her görüşmeden sonra:
   - Bot'a mesaj atın: "@crmbot Müşteri Y ile görüştüm, teklif hazırlandı, perşembe sunum"
   - AI otomatik olarak:
     * CRM'e not düşüyor
     * Sonraki adımları belirliyor (takvim daveti)
     * Ekip arkadaşlarınıza Slack'ten bildirim atıyor
```

**Ne Kazandırıyor:** Haftada 3-5 saat "durum güncellemesi email'i" yazma + CRM'e manuel not girme zamanı

**Zorluk:** Orta — CRM entegrasyonu gerekiyor, ama n8n veya Zapier ile bağlanabilir

**Araçlar:** Vincent29191160/crm-booking-automation (GitHub), n8n, HubSpot, Pipedrive, Zoho CRM

**Kaçırılan Nokta:** Ekip içi iletişim kopukluğu şirketlere yılda milyonlarca dolara mal oluyor. Aynı müşteriyle iki farklı kişi ayrı şeyler söylüyor, veya önceki görüşmenin detayları kayboluyor. AI sayesinde her görüşme anında kaydediliyor ve tüm ekip erişebiliyor.

---

## OTOMASYON 6: Refly AI — "Ekip İçi Bilgi Paylaşımını AI Yönetiyor"

**Kimler İçin:** Bilgi paylaşımı yoğun ekipler, IT departmanları, onboarding yapan şirketler, dokümantasyon eksikliği yaşayan ekipler

**Ne Yapıyor:** Ekip üyelerinin sorularına otomatik cevap veriyor — "nasıl yaparız", "kim yapıyor", "döküman nerede" gibi. 7,370+ yıldız almış, açık kaynak. Slack veya web üzerinden erişilebiliyor.

**Nasıl Yapılır:**
```
1. refly-ai/refly (GitHub, 7,370⭐) reposunu kur
2. Şirket dokümanlarınızı veya bilgi tabanınızı yükleyin
3. Slack veya web arayüzünden erişin
4. Sorun: "müşteri sözleşmesi şablonu nerede?"
5. AI otomatik olarak cevaplıyor ve ilgili dokümanı paylaşıyor
```

**Ne Kazandırıyor:** Haftada 5-10 saat "şu dokümanı kim biliyor" sorusuyla geçen zaman

**Zorluk:** Kolay (web tabanlı) — kurumsal bilgi tabanı oluşturmak 1 gün, kullanmak 1 dakika

**Araçlar:** Refly AI (refly-ai/refly — 7,370⭐ GitHub), alternatif: Notion AI, Confluence AI

**Kaçırılan Nokta:** Refly "sadece soru cevaplayan" bir bot değil — "öğrenen" bir sistem. Ekip üyeleri ne soruyor, hangi konular tekrar geliyor, hangi dokümanlar eksik? AI bunları analiz edip yöneticilye raporluyor. Yani şirketin "bilgi boşluklarını" da tespit ediyor.

---

## OTOMASYON 7: Slack/Teams Daily Stand-up Bot — "Her Sabah 5 Dakika Kazanın"

**Kimler İçin:** Uzaktan çalışan ekipler, hibrit ofisler, yazılım ekipleri, proje bazlı çalışan grupları

**Ne Yapıyor:** Her sabah otomatik olarak Slack veya Teams'te stand-up mesajı istiyor: "Dün ne yaptın? Bugün ne yapacaksın? Engel var mı?" Cevapları alıyor, özetliyor, yöneticiye tek bir mesajda gönderiyor.

**Nasıl Yapılır:**
```
1. prioliveira50/daily-bot (GitHub) veya benzer bir stand-up bot kur
2. Slack/Teams kanalına bot'u ekle
3. Her sabah saat 9'da bot otomatik olarak stand-up sorularını atıyor
4. Ekip üyeleri reply veriyor
5. Bot tüm yanıtları özetliyor, yöneticiye tek mesajda gönderiyor
6. Özet: n8n veya Make.com ile Notion veya Google Sheets'e kaydediliyor
```

**Ne Kazandırıyor:** Haftalık 2-3 saat toplantı organize etme ve not tutma zamanı

**Zorluk:** Kolay — mevcut stand-up bot'ları doğrudan kullanılabilir

**Araçlar:** prioliveira50/daily-bot (GitHub), Standuply (Slack app), GeekBot (Slack)

**Kaçırılan Nokta:** İnsanlar "daily stand-up" toplantısını "zaman kaybı" zannediyor. Oysa asıl zaman kaybı stand-up yapmamak — ekiptekiler birbirinin ne yaptığını bilmediği için gereksiz yere bekliyor, tekrar eden hatalar yapılıyor. Bot ile toplantıya gerek kalmıyor, bilgi akışı asenkron olarak sağlanıyor.

---

## OTOMASYON 8: Hi Marley — "Sigorta Sektöründe İletişim AI'sı"

**Kimler İçin:** Müşteri hizmetleri ekipleri, sigorta şirketleri, çağrı merkezleri, büyük işletmeler

**Ne Yapıyor:** Sigorta sektöründe müşteriyle tüm iletişimi AI yönetiyor — tahkim dosyaları, evrak takibi, müşteri sorguları. ama her sektöre uyarlanabilir yapıda.

**Nasıl Yapılır:**
```
1. Hi Marley platformunda şirketinizi kurun
2. Müşteri mesajlaşmaları AI tarafından analiz ediliyor
3. AI:
   - Sık sorulan soruları otomatik cevaplıyor
   - Karmaşık konuları doğru kişiye yönlendiriyor
   - Tüm konuşmaları kaydediyor ve analiz ediyor
4. İnsan devreye sadece AI'nın çözemediği konularda giriyor
```

**Ne Kazandırıyor:** Müşteri hizmetleri maliyetini %40'a kadar düşürüyor, yanıt süresini 90% kısaltıyor

**Zorluk:** Orta — platform entegrasyonu gerekiyor

**Araçlar:** Hi Marley (insurance-focused intelligent communication platform)

**Kaçırılan Nokta:** Hi Marley'in "iletişim platformu" olarak konumlanması sigorta dışı sektörler için de fırsat — her sektörde müşteriyle iletişim AI'a devredilebilir. Özellikle "standart sorgular" (fatura durumu, sipariş takibi, randevu değişikliği) tamamen AI'a bırakılabilir.

---

## OTOMASYON 9: AI ile Tedarikçi Takibi — "Ödemeler ve Teslimatlar Kaçmıyor"

**Kimler İçin:** Satın alma departmanları, muhasebe, tedarik zinciri yöneticileri, KOBİ sahipleri

**Ne Yapıyor:** Tedarikçilerinizden gelen faturaları, teslimatları, ödeme vadelerini AI takip ediyor. "X tedarikçisine 2 hafta önce ödeme yaptık ama mal gelmedi" gibi sorunları otomatik tespit ediyor ve ilgili kişiye bildiriyor.

**Nasıl Yapılır:**
```
1. Google Sheets veya Excel'e tedarikçi veritabanı oluşturun:
   - Tedarikçi adı, iletişim, son sipariş, son ödeme, vade
2. n8n veya Make.com'da workflow kurun:
   - Fatura geldiğinde → Sheets'e otomatik kayıt
   - Vade tarihi yaklaştığında → Muhasebeciye bildirim
   - Mal gelmedi (sipariş tarihi > X gün) → Satın alma'ya alarm
3. AI ek olarak:
   - Tedarikçi geçmişini analiz eder (kim sürekli gecikiyor?)
   - En iyi tedarikçileri işaretler
   - Riskli tedarikçileri raporlar
```

**Ne Kazandırıyor:** Haftada 2-4 saat tedarikçi takip, ödeme kontrolü zamanı

**Zorluk:** Kolay — Google Sheets + no-code platform ile kurulabilir

**Araçlar:** n8n, Make.com, Google Sheets, Excel, SarmadSiyal/ai-powered-lead_qualification-crm-automation-system (CRM otomasyonu referans)

**Kaçırılan Nokta:** Türkiye'de tedarikçi takibi hâlâ Excel ile yapılıyor. "Firma X'e 45 gün önce sipariş verdik, ne oldu?" sorusu her hafta toplantıda soruluyor. AI ile bu soru tarihe karışıyor — sistem zaten takip ediyor, sorun olunca bildirim geliyor.

---

## Herkesin Kaçırdığı Nokta #1

**Slack ve Teams otomasyonları hâlâ "gadget" olarak görülüyor, ama gerçek fayda "haberleşme verimliliği" değil — "kurumsal hafıza."** Bir şirketin en büyük sorunu: "Geçen ay müşteriyle ne konuşmuştuk?" Soran var, cevap veren yok. AI bot'lar bu kurumsal hafızayı oluşturuyor — her email, her toplantı, her karar kaydediliyor ve bot üzerinden erişilebiliyor.

## Herkesin Kaçırdığı Nokta #2

**Microsoft Scout'un "7/24 çalışan AI asistan" özelliği, aslında ofis çalışanlarının en büyük avantajını gösteriyor: insan uyumuyor, AI uyuyor.** Gece 2'de email atılabiliyor, sabah 6'da takvim güncellenebiliyor, hafta sonu müşteri takibi yapılabiliyor. Rekabet avantajı artık "ne kadar erken kalkıyorsunuz" değil — "AI'ınız uyuyor mu?"

## Herkesin Kaçırdığı Nokta #3

**Follow-up otomasyonu "spam" değil — sistematik müşteri ilişkisi yönetimi.** İnsanların %80'i "bir daha hatırlatma yapmaktan utangaç" hissediyor. Oysa araştırmalar gösteriyor ki müşterilerin %60'ı 2-3 follow-up'tan sonra cevap veriyor. AI ile kişiselleştirilmiş follow-up taslakları oluşturuluyor — spam hissi vermeden, satış döngüsü kısaltılıyor.

---

## Özet Tablo

| Otomasyon | Kimler İçin | Ne Kazandırıyor | Zorluk |
|-----------|-------------|-----------------|--------|
| Slack/Jira Bot | Proje yöneticileri, ekipler | 3-5 saat/hafta | ⭐ Kolay |
| Microsoft Scout | Yoğun yöneticiler, satış | 5-8 saat/hafta | ⭐ Kolay |
| Lead Takip AI | Satış, iş geliştirme | 4-6 saat/hafta | ⭐ Kolay |
| Onay Bildirimi | Yönetici, muhasebe, hukuk | 2-4 saat/hafta | ⭐ Kolay |
| CRM Durum Güncelleme | Satış, proje yöneticileri | 3-5 saat/hafta | ⭐⭐ Orta |
| Refly AI | IT, onboarding, bilgi yönetimi | 5-10 saat/hafta | ⭐ Kolay |
| Daily Stand-up Bot | Uzaktan/hibrit ekipler | 2-3 saat/hafta | ⭐ Kolay |
| Tedarikçi Takibi | Satın alma, muhasebe | 2-4 saat/hafta | ⭐ Kolay |

---

## Kaynaklar

- Microsoft Scout & OpenClaw: https://www.bing.com/news/search?q=Microsoft+Scout+AI+personal+assistant+2026
- Slack-Jira Automation: https://github.com/BennyDanielT/Slack-Jira-Automation
- Client Reminder (Google Sheets): https://github.com/PressedCoffee/client-reminder
- Lead Engine (n8n + Gemini): https://github.com/NDDimension/clientsense-ai-lead-engine
- CRM Booking Automation: https://github.com/Vincent29191160/crm-booking-automation
- Refly AI (7,370⭐): https://github.com/refly-ai/refly
- Daily Slack Bot: https://github.com/prioliveira50/daily-bot
- Hi Marley: https://www.bing.com/news/search?q=Hi+Marley+intelligent+communication+platform+2026
- Microsoft Work Trend Index 2026: https://www.microsoft.com/work-trend-index

---

*Son güncelleme: 2026-06-18 — Perşembe (İletişim & Takip Otomasyonları)*
