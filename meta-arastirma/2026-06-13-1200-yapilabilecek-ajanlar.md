# Meta Platform — Yapılabilecek Ajanslar Araştırması
**Tarih:** 2026-06-13 12:00
**Slot:** 1200

---

## 1. Özet Tablo

| Agent | Platform | Karmaşıklık | Açıklama |
|-------|----------|-------------|----------|
| WhatsApp AI Agent | WhatsApp Business API | Orta | 7/24 müşteri desteği, sipariş alma |
| Instagram DM Agent | Instagram Graph API | Orta-Yüksek | Yorum/DM otomatik yanıt, lead yakalama |
| Facebook Page Agent | Meta Graph API | Düşük-Orta | Mesaj yanıtlama, otomatik yanıtlar |
| Ads Manager Agent | Marketing API | Yüksek | Kampanya oluşturma, optimizasyon |
| Abandoned Cart Agent | WhatsApp + E-ticaret | Orta | Sepet terk edenlere otomatik hatırlatma |
| Customer Support Agent | WhatsApp/Instagram | Orta | Triyaj, yönlendirme, çözüm |

---

## 2. Meta Graph API — Temel Yapı Taşları

Meta'nın tüm ajanları Meta Graph API üzerine inşa edilir. Temel API'ler:

### Instagram Graph API
- Media consumption (gönderi, hikaye, reels)
- Comment management (yorum yanıtlama)
- Direct messaging (DM)
- Insights (performans verileri)
- Business discovery (rakip analizi)

### WhatsApp Business API
- Message templates (onaylı mesaj şablonları)
- Cloud API (mesaj gönderme/alma)
- Business Management API (hesap yönetimi)

### Facebook Marketing API
- Campaign creation/management
- Ad set and ad creation
- Audience management
- Reporting and insights
- Automated rules

---

## 3. En Kolay Yapılabilecek 3 Agent

### Agent #1: WhatsApp Sipariş Agent

**Zorluk:** ⭐⭐ (2/5)
**Gerekenler:** WhatsApp Business API, n8n, Claude Code

**Ne yapar?**
- Müşteri "sipariş vermek istiyorum" deyince ürün catalog paylaşır
- Müşteri ürün seçer, adres verir
- Sipariş bilgisi e-ticaret sistemine kaydedilir
- Onay mesajı gönderilir

**Örnek GitHub Projesi:**
- `fabrogarrido/clinicbot-whatsapp-n8n` — Klinik botu, hasta kabul, lead qualification (n8n + GPT-4o-mini + PostgreSQL)

**İlginç açı:** Klinik botu aslında tam bir "sipariş agent" mantığıyla çalışıyor — hastayı yönlendirme, bilgi toplama, randevu oluşturma. Aynı mantık e-ticaret için de geçerli.

---

### Agent #2: Instagram Comment-to-DM Agent

**Zorluk:** ⭐⭐⭐ (3/5)
**Gerekenler:** Instagram Graph API, n8n veya Meta MCP Server

**Ne yapar?**
- Gönderiye yorum gelince otomatik DM atar
- Yorumda "bilgi için DM at" veya "link için DM at" yazar
- AI yoruma göre kişiselleştirilmiş mesaj gönderir
- Müşteriyi WhatsApp'a yönlendirir

**Örnek GitHub Projesi:**
- `praj2408/Smart-Marketing-Assistant-Crew-AI` — Instagram pazarlama workflow otomasyonu (CrewAI tabanlı)

**İlginç açı:** Comment-to-DM, e-ticaret için en yüksek dönüşüm getiren otomasyonlardan biri. Instagram'da gönderiye yorum atan kişi %80 ihtimalle alışverişe yakın. Bu fırsatı kaçırmak = para kaybetmek.

---

### Agent #3: Abandoned Cart Recovery Agent

**Zorluk:** ⭐⭐⭐ (3/5)
**Gerekenler:** WhatsApp Business API, e-ticaret veritabanı, n8n

**Ne yapar?**
1. Müşteri sepeti bırakıp ayrılır
2. 1 saat sonra: "Sepetinizde ürünler bekliyor" mesajı
3. 24 saat sonra: "%10 indirim kodu" teklifi
4. 72 saat sonra: Son hatırlatma

**ROI:** Ortalama %10-15 ek dönüşüm artışı

**Örnek:**
- Booking.com: Rezervasyon tamamlamayanlara 3 kademeli hatırlatma
- E-ticaret: Sepet kurtarma, 72 saatlik pencere

---

## 4. Herkesin Kaçırdığı Nokta #1

**Meta'nın kendi "AI agent" duyurusu aslında sadece bir CHATBOT.**

Meta Business Agent'ı duyurulduğunda herkes "devrim" dedi. Ama gerçek şu: Meta'nın resmi ajanı şu anda sadece:
- Karşılıklı sohbet (Q&A)
- Basit yönlendirme
- Hazır template'lere dayalı yanıtlar

**Yapılabilecek ajanlar Meta'nın sunduklarından ÇOK DAHA karmaşık ve değerli olabilir.** Meta'nın API'leri açık — kendi ajanınızı inşa edebilirsiniz. Meta'nın ajanı sadece başlangıç noktası.

---

## 5. Herkesin Kaçırdığı Nokta #2

**GitHub'da bolca örnek var ama kimse kullanmıyor.**

`docbiker/whatsapp-agent-setup` (OpenClaw entegrasyonu), `atifali-pm/cue` (WhatsApp AI agent + RAG), `fabrogarrido/clinicbot-whatsapp-n8n` — bunların hepsi açık kaynak, hepsi çalışıyor, hepsi n8n ile entegre edilebilir. Ama kimse bakmıyor çünkü "Made for business" değil diye düşünüyorlar.

**Asıl mesele:** Bu projelerdeki kodu ALIP kendi use case'inize uyarlamak. Örneğin clinicbot'un lead qualification mantığını e-ticarete uyarlamak = 10 dakikalık iş.

---

## 6. Adım Adım Yapım Rehberi

### En Basit: WhatsApp Sipariş Agent (n8n + Claude Code)

** Gerekenler:**
- WhatsApp Business API hesabı
- n8n kurulumu
- Claude Code erişimi
- E-ticaret veritabanı (veya Google Sheets)

**Adımlar:**

1. **n8n'de trigger oluştur:**
   - WhatsApp webhook gelen mesaj tetikleyicisi

2. **Claude Code'a mesaj gönder:**
   ```
   System: Müşteri [mesaj] geldi. 
   Ürün catalog: [link]
   Müşteri niyeti: sipariş/bilgi/şikayet
   Uygun yanıtı üret ve WhatsApp formatında döndür
   ```

3. **Yanıtı WhatsApp'tan gönder:**
   - Template message kullan (önceden onaylı)

4. **Sipariş oluşursa:**
   - Veritabanına kaydet
   - E-posta bildirimi gönder
   - Stok güncelle

**Kod örneği (n8n Function node):**
```javascript
const message = $json.body.entry[0].changes[0].value.messages[0];
const from = message.from;
const text = message.text.body;

const response = await callClaude(`Müşteri diyor ki: "${text}". 
Ürünlerimiz: ${catalog}. En uygun ürün önerisini yap.`);

// WhatsApp API ile yanıt gönder
return { response, from };
```

---

## 7. Kaynaklar

1. https://github.com/docbiker/whatsapp-agent-setup (OpenClaw + Meta API)
2. https://github.com/atifali-pm/cue (WhatsApp AI agent + RAG)
3. https://github.com/fabrogarrido/clinicbot-whatsapp-n8n (n8n + GPT-4o-mini + PostgreSQL)
4. https://github.com/praj2408/Smart-Marketing-Assistant-Crew-AI (Instagram CrewAI)
5. https://github.com/oliverames/meta-mcp-server (Meta MCP Server - 200+ araç)
6. https://developers.facebook.com/docs/graph-api