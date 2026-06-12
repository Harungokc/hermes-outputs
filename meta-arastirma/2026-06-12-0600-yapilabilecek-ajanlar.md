# Meta Platformları İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-12 06:00
**Kaynak:** Meta Developers, GitHub, n8n Workflows, Bing News, TechCrunch, Reuters

---

## Özet

Meta platformları (Instagram, WhatsApp, Facebook) için bugün yapılabilecek AI ajanları, kullanıcının mevcut stack'i (n8n + Claude Code + Instagram Messaging API) ile doğrudan uyumlu. 2026'da Meta Business Agent'ın global lansmanı ile WhatsApp'ta AI müşteri desteği artık resmi olarak destekleniyor. En değerli ajanlar: Instagram DM'den WhatsApp'a yönlendirme, otomatik müşteri sorgulama, ve sipariş takip ajanları.

**🔴 Herkesin Kaçırdığı Nokta:** Meta Business Agent "yapay zeka müşteri temsilcisi" olarak lanse ediliyor ama aslında sadece WhatsApp Business Premium içinde gelen bir template. Kendi ajanınızı n8n + Claude Code ile yaparsanız çok daha fazla kontrolünüz olur — ve Instagram DM trigger'ından itibaren başlayabilirsiniz.

**🆕 06:00 Güncelleme:** Meta Business Agent artık sadece WhatsApp'ta değil — Instagram Direct ve Messenger'da da çalışıyor. Yeni "Business Agent Platform" duyuruldu. Bu önemli çünkü artık tek bir ajan ile 3 platformda müşteri hizmeti verilebiliyor.

---

## Yapılabilecek AI Ajansları

### 1. Instagram → WhatsApp Satış Ajansı (En Değerli)

**Ne yapıyor:**
- Instagram DM'e gelen soruları otomatik yanıtlama
- Ürün/hizmet bilgisi verme
- WhatsApp'a yönlendirme
- Sipariş alma

**Kullanılan API/Stack:**
- Instagram Graph API (webhook trigger)
- n8n workflow
- Claude Code (karar mantığı)
- WhatsApp Business API (mesaj gönderim)

**GitHub Örnekleri:**
- https://github.com/niccolof/instagram-whatsapp-bot
- Kullanıcının mevcut sistemi zaten bu formatta çalışıyor

### 2. Meta Business Agent (2026 Yeni — GLOBAL, 3 Platformda Çalışıyor)

**Ne yapıyor:**
- 7/24 WhatsApp, Instagram DM ve Messenger yanıtı (artık 3 platformda!)
- Sık sorulan soruları yanıtlama
- Ürün önerisi
- Randevu booking
- Lead qualification
- Gece konuşmaları özeti (daily briefing)

**Stack:**
- WhatsApp Business Premium
- Meta Business Suite
- Shopify/Zendesk/Shopee entegrasyonu (enterprise)

**Fark:** Bu ajan müşteri başlatmalı konuşmalar için tasarlanmış. Ban riski yok. Ancak özelleştirme seçenekleri sınırlı.

**Yeni (06/2026):** Business Agent Platform duyuruldu — tek ajan ile 3 platform yönetimi mümkün.

### 3. Otomatik Müşteri Hizmetleri Ajansı

**Ne yapıyor:**
- 7/24 WhatsApp yanıtı
- Sık sorulan soruları yanıtlama
- Sipariş durumu sorgulama
- Şikayetleri yönlendirme

**Stack:**
- WhatsApp Business API
- n8n + Claude Code
- SQLite (müşteri veritabanı)

### 4. Reklam Performans Monitor Ajansı

**Ne yapıyor:**
- Günlük reklam metriklerini çekme
- Anormal değişiklikleri tespit etme
- Alert gönderme
- Haftalık özet rapor

**Stack:**
- Meta Business SDK
- Python/Node.js script
- Telegram/Email bildirimi

### 5. Content Scheduling Agent

**Ne yapıyor:**
- Instagram post zamanlaması
- Caption + hashtag optimizasyonu
- Comment yanıtlama
- Story posting

**Stack:**
- Instagram Graph API (scheduled posts)
- Claude Code (caption generation)
- n8n workflow

### 6. Lead Scoring Agent

**Ne yapıyor:**
- Instagram/WhatsApp üzerinden gelen lead'leri puanlama
- Satış ekibine öncelik sıralama
- Takip zamanlaması

**Stack:**
- Instagram DM webhook
- Claude Code (lead scoring logic)
- Google Sheets / CRM entegrasyonu

### 7. Abandoned Cart Recovery Agent (YENİ — 2026)

**Ne yapıyor:**
- Sepeti terk eden müşterilere otomatik WhatsApp hatırlatması
- Koşullu mesaj: 1 saat sonra → 24 saat sonra → 72 saat sonra
- İndirim kodu sunma

**Stack:**
- WooCommerce/Shopify webhook
- WhatsApp Business API
- n8n workflow + Claude Code

**Metrik:** Sepet terk oranı %60-80 olan e-ticaret sitelerinde, hatırlatma ile %10-15 ek dönüşüm sağlanıyor.

---

## Adım Adım Yapım Rehberi

### Instagram → WhatsApp Yönlendirme Ajansı

```
Adım 1: Instagram Developer Portal
- Uygulama oluştur
- Webhook subscription ayarla
- permissions: pages_messaging, instagram_basic

Adım 2: n8n Workflow
- Instagram Webhook Trigger
- Claude Code node (mesaj analizi)
- Koşul: "WhatsApp numarası isteyen" → WhatsApp mesajı gönder

Adım 3: Claude Code Prompt
---
Sen bir satış asistanısın. Instagram DM'inde gelen mesajı analiz et.
Eğer müşteri ürün bilgisi veya fiyat soruyorsa, kısa ve net yanıt ver.
Eğer sipariş vermek istiyorsa, WhatsApp'a yönlendir.
Her yanıt 2-3 cümle olmalı.
---
```

### Meta Business Agent vs Kendi Ajansınız

| Özellik | Meta Business Agent | Kendi Ajansınız (n8n+Claude) |
|---------|---------------------|-------------------------------|
| Kurulum | 5 dakika | 2-4 saat |
| Özelleştirme | Sınırlı | Sınırsız |
| Ban riski | Yok | Düşük (resmi API) |
| Maliyet | Premium gerektirir | n8n hosting ücreti |
| Entegrasyon | Shopify/Zendesk | Her şey |
| Instagram trigger | Yok (sadece WhatsApp/Messenger) | Var |

**Herkesin kaçırdığı nokta (#2):** Meta Business Agent hızlı kurulum için iyi ama Instagram DM trigger'ı yok. Mevcut sisteminiz (Instagram → WhatsApp) Meta Business Agent ile değil, n8n + Claude Code ile çalışıyor. Meta Business Agent sadece WhatsApp/Messenger/Instagram'a gelen müşteriler için.

**Yeni (06/2026):** Meta Business Agent artık Instagram DM'den gelen mesajları da yanıtlıyor — ancak hâlâ Instagram webhook trigger'ı yok, sadece gelen mesajlara yanıt veriyor.

### Kod Örneği: Instagram Webhook Handler
```javascript
// n8n Function Node
const instagramMessage = $json.body.entry[0].changes[0].value;
const senderId = instagramMessage.from.id;
const message = instagramMessage.message.text;

// Claude Code'a gönder
const response = await callClaudeCode(message);

// WhatsApp'a yönlendir
if (response.redirectToWhatsapp) {
  await sendWhatsAppMessage(senderId, response.whatsappNumber);
}
```

### Abandoned Cart Recovery Agent Kodu
```javascript
// n8n: WooCommerce Order Created trigger (status = pending)
// Koşul: payment_status = "pending" for 1+ hours
const customerPhone = $json.billing_address.phone;
const cartUrl = $json.cart_url;

const messages = [
  { delay: 3600000, text: "Sepetinizde unuttuğunuz ürünler var! 🛒" },
  { delay: 86400000, text: "Hala buradayız! İndirim kodu: HATIRLA10" },
  { delay: 172800000, text: "Son şans! Sepetiniz yarın silinecek 😱" }
];

// Claude Code ile kişiselleştirilmiş mesaj
const personalized = await callClaudeCode(`Müşteri ${customerName} için sepet hatırlatma mesajı yaz`);
```

---

## GitHub Repoları ve Projeler

| Proje | Link | Açıklama |
|-------|------|----------|
| instagram-graph-api-sdk | https://github.com/niccolof/instagram-graph-api | Instagram API wrapper |
| whatsapp-business-node | https://github.com/jarrodsampson/whatsapp-business-node | WhatsApp Node.js SDK |
| n8n-nodes-meta | https://github.com/n8n-io/n8n-nodes-base | n8n Meta nodes (topluluk) |
| meta-conversation-bot | https://github.com/jakbin/meta-conversation-bot | Multi-platform bot |
| facebook-business-sdk | https://github.com/facebook/facebook-business-sdk | Resmi Meta SDK |
| baileys | https://github.com/WhiskeySockets/Baileys | WhatsApp Web API (unofficial) |

---

## Meta API'ları Listesi

1. **Instagram Graph API** - Instagram içerik, DM, insights
2. **WhatsApp Business API** - WhatsApp mesajlaşma
3. **Facebook Marketing API** - Reklam kampanyaları
4. **Facebook Pages API** - Sayfa yönetimi
5. **Messenger Platform API** - Messenger botları
6. **Meta Business Agent** - AI müşteri desteği (WhatsApp Business Premium) — Artık 3 platformda çalışıyor!

---

## Kaynaklar

- https://developers.facebook.com/docs/ - Meta Developer Docs
- https://github.com/niccolof/instagram-graph-api - Instagram API
- https://n8n.io/ - n8n Workflow Automation
- https://developers.facebook.com/docs/whatsapp/ - WhatsApp Business API
- TechCrunch (06/03/2026): "Meta's AI agent for WhatsApp Business is now available globally"
- Reuters (06/03/2026): "Meta enters enterprise AI race with new business agent"
- Bing News (06/2026): "Meta expands Business Agent globally across WhatsApp, Messenger and Instagram, introduces Business Agent Platform"