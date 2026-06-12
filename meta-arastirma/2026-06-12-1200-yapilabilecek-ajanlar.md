# Meta Platformları İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-12 12:00
**Kaynak:** Bing News, Meta Developer Docs, GitHub, Reuters

---

## Özet

Meta platformları (WhatsApp, Instagram, Facebook, Messenger) için bugün yapılabilecek AI ajanları şunlardır: (1) Müşteri hizmetleri chatbot ajanı, (2) Satış otomasyon ajanı, (3) Abandoned cart recovery ajanı, (4) Lead qualification ajanı, (5) İçerik üretim ajanı. Hepsinin ortak noktası: Meta Business API + bir AI modeli (Claude/GPT) + bir orchestration katmanı (n8n/Zapier/custom kod).

**Herkesin kaçırdığı nokta:** Meta'nın yeni Business Agent platformu sadece büyük şirketler için değil — aynı API'leri kullanarak herkes kendi ajanını inşa edebilir. WhatsApp Business API Cloud API + n8n + Claude Code = ücretsiz, güçlü AI ajanı.

---

## Yapılabilecek AI Ajansları

### 1. Müşteri Hizmetleri Chatbot Ajanı

**Ne yapar?**
- WhatsApp/Instagram DM'lerine otomatik yanıt
- Sık sorulan soruları yanıtlar (FAQ)
- Müşteriyi doğru departmana yönlendirir
- Sipariş takibi, stok sorgulama

**Kullanılan API'ler:**
- WhatsApp Business Cloud API
- Instagram Graph API (DM gelen mesajlar)
- Dialogflow / Claude API / GPT-4

**GitHub Örnekleri:**
- https://github.com/pedroslopez/whatsapp-web.js (kişisel kullanım için)
- https://github.com/n8n-io/n8n (workflow otomasyonu)

**Adım adım:**
```
1. WhatsApp Business API kurulumu (developers.facebook.com)
2. n8n'de WhatsApp trigger node (gelen mesajlar)
3. AI node (Claude/GPT) → yanıt üret
4. Koşul node → FAQ mı? Sipariş mi? Şikayet mi?
5. Uygun node → otomatik yanıt / insan devretme
```

### 2. Abandoned Cart Recovery Ajanı

**Ne yapar?**
- Sepeti terk eden müşteriye otomatik WhatsApp hatırlatması
- 1 dk, 24 saat, 72 saat sonra hatırlatma
- İndirim kodu teklifi
- "Hâlâ ilginizi çekiyor mu?" anketi

**Kullanılan API'ler:**
- WhatsApp Business Cloud API
- E-ticaret platformu API (Shopify, WooCommerce)
- CRM entegrasyonu

**Pratik sonuç:** Ortalama %10-15 ek dönüşüm artışı. E-ticaret için en yüksek ROI'li WhatsApp otomasyonu.

**Adım adım:**
```
1. E-ticaret platformunda "sepet terk edildi" event'i tetiklenir
2. n8n workflow: "sepet_terk_edildi" trigger
3. 1 dk sonra → WhatsApp API → "Sepetinizi mi unuttunuz?" mesajı (ücretsiz - 72 saat window içinde)
4. 24 saat sonra → Farklı template → "%10 indirim kodu" (ücretsiz)
5. 72 saat sonra → Son hatırlatma template (ücretli)
```

### 3. Lead Qualification Ajanı

**Ne yapar?**
- Instagram/Facebook'tan gelen lead'leri otomatik puanlar
- Hangi lead sıcak? Hangi ürüne ilgili?
- Satış ekibine öncelikli lead'leri iletir
- İlk filtreleme yapar — insan müdahalesi minimum

**Kullanılan API'ler:**
- Instagram Graph API (lead form submissions)
- WhatsApp Business API
- Claude API (lead scoring logic)

**Adım adım:**
```
1. Instagram Lead Form → webhook ile n8n'e veri gelir
2. AI node → lead'in mesajını analiz eder
   - "fiyat sordu" = sıcak lead (+10 puan)
   - "ürün özellikleri" = orta (+5 puan)
   - "merhaba" = soğuk (+1 puan)
3. CRM'e puanlı lead kaydedilir
4. 8+ puan → WhatsApp ile satış ekibine bildirim
5. 8- puan → email drip campaign
```

### 4. Satış Otomasyon Ajanı

**Ne yapar?**
- Ürün kataloğunu müşteriye WhatsApp'tan gösterir
- "Beğendiğiniz ürünün stokta var mı?" → otomatik kontrol
- Sipariş alır, ödeme linki gönderir
- Sipariş onayı ve takip numarası gönderir

**Kullanılan API'ler:**
- WhatsApp Business API (Cloud API)
- Shopify/WooCommerce API
- Ödeme API (Iyzico, Stripe)

**Adım adım:**
```
1. Müşteri WhatsApp'tan "Ürün kataloğu" ister
2. AI ajan → katalogdan ürün önerir (müşteri geçmişine göre)
3. Müşteri ürün seçer → stok kontrolü yapılır
4. Ödeme linki gönderilir → tahsilat yapılır
5. Sipariş onayı + kargo takip numarası gönderilir
```

### 5. İçerik Üretim Ajanı (Instagram/LinkedIn)

**Ne yapar?**
- Haftalık içerik planı oluşturur
- Görsel açıklaması üretir (alt text)
- Caption/hashtag önerir
- En iyi zamanları hesaplar

**Kullanılan API'ler:**
- Instagram Graph API (post scheduling)
- Claude API (içerik üretimi)
- Later / Buffer API (opsiyonel)

**Adım adım:**
```
1. Haftalık schedule trigger
2. AI node → "bu hafta [sektör] için 5 post fikri üret"
3. Her fikir için: görsel önerisi, caption, hashtag, zamanlama
4. n8n'in Instagram node'u ile post'lar schedule edilir
5. Performans verileri toplanır → bir sonraki hafta için öğrenilir
```

---

## Meta API'leri — Hangi API Neyi Yapar?

| API | Platform | Kullanım Alanı |
|-----|----------|---------------|
| WhatsApp Business Cloud API | WhatsApp | Mesaj gönder/al, chatbot, template |
| Instagram Graph API | Instagram | Post, Story, DM, Insights, Reels |
| Meta Marketing API | Facebook | Reklam kampanyası, hedefleme, raporlama |
| Messenger Platform API | Messenger | DM, webhook, otomatik yanıt |
| WhatsApp Business Management API | WhatsApp | Business account yönetimi, phone number |

---

## Adım Adım: Meta Business Agent Benzeri Kendi Ajanını Yap

### Gereksinimler
1. Meta Business Manager hesabı
2. WhatsApp Business API erişimi (Cloud API)
3. n8n (veya Zapier, veya custom kod)
4. Claude API key (veya OpenAI)

### Mimari
```
[WhatsApp/Instagram] → [Webhook] → [n8n Trigger] → [AI Modeli (Claude)] → [Koşul/İş Mantığı] → [WhatsApp/Instagram API] → [Müşteriye Yanıt]
```

### Örnek n8n Workflow

```
Trigger Node (WhatsApp gelen mesaj):
{
  "from": "905551234567",
  "message": "Sepetimdeki ürünün fiyatı ne?"
}

AI Node (Claude):
Prompt: "Bu müşteri sepet sorgulaması yapıyor. 
Kısa ve nazik bir yanıt ver. 
Eğer ürün varsa fiyatı söyle, 
yoksa 'stokta mevcut değil' de."

If Node:
- "fiyat" içeriyor → Shopify API → ürün fiyatı al → WhatsApp yanıt
- "sipariş" içeriyor → sipariş workflow'u başlat
- Diğer → Claude'a daha detaylı yanıt sor
```

---

## GitHub Repoları ve Açık Kaynak Projeler

1. **whatsapp-web.js** — https://github.com/pedroslopez/whatsapp-web.js
   - WhatsApp Web'e bağlanma (kişisel kullanım için)
   - Bot geliştirme, otomatik mesaj

2. **n8n** — https://github.com/n8n-io/n8n
   - Workflow otomasyonu — Meta API entegrasyonu
   - WhatsApp, Instagram, Facebook node'ları

3. **ChatGPT Twilio WhatsApp** — https://github.com/openai-tj/chatgpt-twilio-whatsapp
   - ChatGPT + Twilio + WhatsApp chatbot
   - AI destekli müşteri hizmetleri

4. **Meta Marketing SDK** — https://github.com/facebook/facebook-python-business-sdk
   - Resmi Python SDK — reklam kampanyası yönetimi

5. **instagram-api-node** — https://github.com/pedroslopez/instagram-api-node
   - Instagram Graph API wrapper — post, story, DM

---

## Kaynaklar

1. https://developers.facebook.com/docs/whatsapp — WhatsApp Business API
2. https://developers.facebook.com/docs/instagram — Instagram Graph API
3. https://github.com/pedroslopez/whatsapp-web.js — WhatsApp Web JS
4. https://github.com/n8n-io/n8n — n8n workflow otomasyon
5. https://www.bing.com/news/search?q=Meta+Business+Agent+2026 — Meta Business Agent haberleri
6. https://www.reuters.com/tech/meta-launches-ai-powered-business-agent-2026-06-03/ — Reuters (3 Haziran 2026)
7. https://www.theinformation.com — Meta Business Agent fiyatlandırma ($200/ay Hatch)
