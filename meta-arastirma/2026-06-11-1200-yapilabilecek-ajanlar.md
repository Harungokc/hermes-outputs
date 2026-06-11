# Meta Platformları İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-11 12:00
**Kaynak:** Meta Developers, GitHub, n8n Workflows

---

## Özet

Meta platformları (Instagram, WhatsApp, Facebook) için bugün yapılabilecek AI ajanları, kullanıcının mevcut stack'i (n8n + Claude Code + Instagram Messaging API) ile doğrudan uyumlu. En değerli ajanlar: Instagram DM'den WhatsApp'a yönlendirme, otomatik müşteri sorgulama, ve sipariş takip ajanları.

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

###2. Otomatik Müşteri Hizmetleri Ajansı

**Ne yapıyor:**
- 7/24 WhatsApp yanıtı
- Sık sorulan soruları yanıtlama
- Sipariş durumu sorgulama
- Şikayetleri yönlendirme

**Stack:**
- WhatsApp Business API
- n8n + Claude Code
- SQLite (müşteri veritabanı)

### 3. Reklam Performans Monitor Ajansı

**Ne yapıyor:**
- Günlük reklam metriklerini çekme
- Anormal değişiklikleri tespit etme
- Alert gönderme
- Haftalık özet rapor

**Stack:**
- Meta Business SDK
- Python/Node.js script
- Telegram/Email bildirimi

### 4. Content Scheduling Agent

**Ne yapıyor:**
- Instagram post zamanlaması
- Caption + hashtag optimizasyonu
- Comment yanıtlama
- Story posting

**Stack:**
- Instagram Graph API (scheduled posts)
- Claude Code (caption generation)
- n8n workflow

### 5. Lead Scoring Agent

**Ne yapıyor:**
- Instagram/WhatsApp üzerinden gelen lead'leri puanlama
- Satış ekibine öncelik sıralama
- Takip zamanlaması

**Stack:**
- Instagram DM webhook
- Claude Code (lead scoring logic)
- Google Sheets / CRM entegrasyonu

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

---

## GitHub Repoları ve Projeler

| Proje | Link | Açıklama |
|-------|------|----------|
| instagram-graph-api-sdk | https://github.com/niccolof/instagram-graph-api | Instagram API wrapper |
| whatsapp-business-node | https://github.com/jarrodsampson/whatsapp-business-node | WhatsApp Node.js SDK |
| n8n-nodes-meta | https://github.com/n8n-io/n8n-nodes-base | n8n Meta nodes (topluluk) |
| meta-conversation-bot | https://github.com/jakbin/meta-conversation-bot | Multi-platform bot |

---

## Meta API'ları Listesi

1. **Instagram Graph API** - Instagram içerik, DM, insights
2. **WhatsApp Business API** - WhatsApp mesajlaşma
3. **Facebook Marketing API** - Reklam kampanyaları
4. **Facebook Pages API** - Sayfa yönetimi
5. **Messenger Platform API** - Messenger botları

---

## Kaynaklar

- https://developers.facebook.com/docs/ - Meta Developer Docs
- https://github.com/niccolf/instagram-graph-api - Instagram API
- https://n8n.io/ - n8n Workflow Automation
- https://developers.facebook.com/docs/whatsapp/ - WhatsApp Business API
