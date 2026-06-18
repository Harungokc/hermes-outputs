# Meta Platform İçin Yapılabilecek AI Ajansları — 2026-06-19 00:00

## Özet — 5 Farklı Meta AI Agent Tipi

| Agent Tipi | Zorluk | Kullanım Alanı | ROI Potansiyeli |
|------------|--------|----------------|-----------------|
| Müşteri Hizmetleri Agent | ⭐ Kolay | WhatsApp/IG DM | Çok yüksek |
| Sipariş Takip Agent | ⭐ Kolay | WhatsApp Business | Yüksek |
| Reklam Optimizasyon Agent | ⭐⭐ Orta | Meta Ads API | Çok yüksek |
| Content & Creative Agent | ⭐⭐ Orta | Instagram Graph API | Orta-Yüksek |
| Satış & Lead Gen Agent | ⭐⭐⭐ İleri | Instagram/WhatsApp | Çok yüksek |

---

## 1. Müşteri Hizmetleri AI Agent

**Hangi API:** WhatsApp Business API + Instagram Messaging API

**Ne yapıyor:**
- 7/24 müşteri sorularını yanıtlıyor
- Sık sorulan soruları (FAQ) otomatik yanıtlıyor
- Karmaşık soruları insan temsilciye yönlendiriyor
- Müşteri verisi topluyor (isim, telefon, sipariş no)

**Örnek Dialog:**
```
Müşteri: Siparişim ne zaman gelir?
Agent: Sipariş numaranızı paylaşır mısınız?
Müşteri: #12345
Agent: Siparişiniz kargoya verildi. Tahmini teslimat: yarın saat 18:00'e kadar.
       Kargo takip: [link]
```

**n8n + Claude + WhatsApp API Workflow:**
```
[WhatsApp mesaj geldi]
    ↓
[Webhook tetikle]
    ↓
[Claude Code: "Müşteri sorusu: {mesaj}. En uygun yanıtı ver, kısa ve net."]
    ↓
[WhatsApp API: Yanıt gönder]
    ↓
[Google Sheets: Görüşme kaydı]
```

**GitHub Referans:** [n8n-whatsapp-automation](https://github.com/mubashir-786/n8n-whatsapp-automation) (108⭐)

---

## 2. Sipariş Takip Agent

**Hangi API:** WhatsApp Business API + E-ticaret Platform API (Shopify, WooCommerce)

**Ne yapıyor:**
- Sipariş durumunu sorgulama
- Kargo takip numarası gönderme
- Teslimat gecikmesi bilgilendirmesi
- "Siparişiniz yola çıktı" / "Teslim edildi" bildirimleri

**Herkesin Kaçırdığı Nokta:** En yüksek ROI'li WhatsApp otomasyonu **sepeti terk eden müşterilere 1s, 24s, 72s hatırlatma**. Türkiye'de e-ticaret sepet terk oranı %70+. WhatsApp hatırlatma ile %10-15 ek dönüşüm sağlanıyor.

**Workflow (Abandoned Cart Recovery):**
```
[Sepet terk edildi → 1 saat sonra]
→ WhatsApp: "Sepetinizde unuttuğunuz ürünler var! 🛒"

[24 saat sonra cevap yok]
→ WhatsApp: "%10 indirim kodu: SEPET10"

[72 saat sonra cevap yok]
→ Instagram DM: "Sorunuz var mı? Yardımcı olalım 👋"
```

**n8n Template:**
```json
{
  "name": "Abandoned Cart Recovery",
  "nodes": [
    {
      "name": "Shopify Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": { "path": "abandoned-cart" }
    },
    {
      "name": "Delay 1 Hour",
      "type": "n8n-nodes-base.delay",
      "parameters": { "amount": 60, "unit": "minutes" }
    },
    {
      "name": "Send WhatsApp",
      "type": "httpRequest",
      "parameters": {
        "url": "https://graph.facebook.com/v18.0/{{$env.PHONE_ID}}/messages",
        "method": "POST",
        "body": {
          "messaging_product": "whatsapp",
          "to": "{{$json.customer_phone}}",
          "type": "template",
          "template": {
            "name": "abandoned_cart_reminder",
            "language": { "code": "tr" },
            "components": {
              "body": {
                "text": "Merhaba {{1}}, sepetinizde {{2}} ürünü bekliyor! 🛒\nİndirim kodu: SEPET10"
              }
            }
          }
        }
      }
    }
  ]
}
```

---

## 3. Reklam Optimizasyon Agent

**Hangi API:** Meta Marketing API + Claude Code + n8n

**Ne yapıyor:**
- Günlük kampanya performansını analiz ediyor
- Düşük ROAS'lı kampanyaları otomatik durduruyor
- Yüksek performanslı kampanyalara budget artırıyor
- A/B test sonuçlarını değerlendiriyor
- Anomali tespiti yapıyor (beklenmedik spend/artış)

**Kullanılan Araçlar:**
- NotFair (2923⭐) — Claude Code Meta Ads skill
- google-meta-ads-ga4-mcp (1013⭐) — MCP server
- meta-ads-mcp (996⭐) — Meta Ads MCP server

**Günlük Otomasyon Schedule:**
```
09:00 → Kampanya performans raporu
10:00 → ROAS < 2 olanları işaretle
11:00 → İnsan onayı (opsiyonel)
12:00 → Otomatik budget adjustment
21:00 → Günlük özet + yarın önerileri
```

---

## 4. Content & Creative Agent

**Hangi API:** Instagram Graph API + Meta Content Publishing API

**Ne yapıyor:**
- Haftalık içerik takvimi oluşturuyor
- Ürün açıklamaları yazıyor
- Hashtag önerileri üretiyor
- Görsel alt text'lerini otomatik yazıyor
- En iyi performing post saatlerini hesaplıyor

**Herkesin Kaçırdığı Nokta:** Instagram algoritması 2026'da "recency" önemini artırdı. Haftada 3-5 post yerine günde 1 post (daha sık ama tutarlı) daha iyi performans gösteriyor. AI agent ile tutarlı publishing schedule'ı kurmak reklam harcamadan büyüme sağlıyor.

**Instagram Graph API İçin Gerekli Permissions:**
- `instagram_basic` — profil erişimi
- `instagram_content_publish` — post yayınlama
- `instagram_manage_comments` — yorum yönetimi
- `pages_read_engagement` — sayfa erişimi

---

## 5. Satış & Lead Gen Agent

**Hangi API:** Instagram Messaging API + WhatsApp Business API + CRM API

**Ne yapıyor:**
- Instagram post'larına gelen yorumları yanıtlıyor (AI ile)
- DM'lerde ürün önerisi yapıyor
- Fiyat teklifi hazırlıyor
- Randevu/sipariş kaydı oluşturuyor
- CRM'e otomatik lead kaydı atıyor

**Instagram Comment Auto-Reply Workflow:**
```
[Instagram post'a yorum geldi]
    ↓
[Instagram Webhook → n8n]
    ↓
[Claude Code: "Ürün önerisi yap + indirim kodu ekle"]
    ↓
[Instagram DM: Müşteriye özel mesaj]
    ↓
[CRM: Lead kaydı + notlar]
```

**Kritik Kural:** Instagram'ın otomatik yanıt kuralları 2026'da sıkılaştı. Aşırı otomatik yanıt = hesap kısıtlanması. AI agent'ı doğal, insan gibi yanıt verecek şekilde ayarlayın.

---

## Adım Adım: Meta AI Agent Geliştirme Rehberi

### Adım 1 — Meta Business App Oluşturma

1. [Meta for Developers](https://developers.facebook.com/) → "My Apps" → "Create App"
2. App type: "Business"
3. Eklenen products: "WhatsApp Business API", "Instagram Graph API", "Marketing API"

### Adım 2 — WhatsApp Business API Kurulumu

1. WhatsApp Business hesabı oluştur (business.whatsapp.com)
2. Phone Number ekle (sim kart gerekli değil, sadece numara)
3. Webhook URL belirle (n8n instance)
4. Verify token oluştur

### Adım 3 — n8n Workflow Kurulumu

1. n8n self-hosted veya cloud kur
2. Meta nodes ekle (WhatsApp, Instagram, HTTP Request)
3. Webhook URL'yi Meta Developer App'e kaydet
4. Test modunda çalıştır

### Adım 4 — Claude Entegrasyonu

1. Claude API key al
2. n8n'de "Claude Code" node veya HTTP Request ile Claude API
3. System prompt tanımla (agent'ın rolü, tonu, kuralları)
4. Test et, iyileştir

### Adım 5 — Production'a Geçiş

1. Meta app'ı "Live" moduna al
2. WhatsApp Business hesabı onayı al
3. 72 saat kuralı için Template Message onayları al
4. İzleme ve error handling ekle

---

## Kaçırılan Nokta #1 — Tek Bir Agent Yerine Pipeline Kullan

**Yanlış yaklaşım:** "Bir super-agent her şeyi yapsın"

**Doğru yaklaşım:** Spesifik agent'lar pipeline'da çalışsın:
- Agent 1: Gelen mesajı triyaj eder (satış mı, destek mi, şikayet mi?)
- Agent 2: Triyaja göre uzman agent'a yönlendirir
- Agent 3: Satış agent'ı → ürün önerisi yapar
- Agent 4: Destek agent'ı → FAQ yanıtlar
- Agent 5: Şikayet agent'ı → insan temsilciye işaretler

Bu yaklaşım debugging'i kolaylaştırır ve her agent'ı ayrı ayrı iyileştirirsiniz.

---

## Kaçırılan Nokta #2 — Meta'nın 72 Saat Kuralını Stratejik Kullan

**Herkes bildiği:** Müşteri mesaj attıktan sonra 72 saat serbest mesaj hakkı.

**Ama gerçekte:** Bu 72 saatlik pencereyi BİLGİ TOPLAMA için kullan:
1. Müşteri ilk sorduğunda → isim, telefon, sipariş no topla
2. 72 saat içinde → satış, upsell, cross-sell, takip
3. 72. saatte → "Bir sorunuz olursa buradayım" + tekrar 72 saat açılır

**Maksimum değer:** Her müşteri etkileşiminden 72 saat boyunca faydalanın.

---

## Kaçırılan Nokta #3 — Instagram DM → WhatsApp Geçişi = En Yüksek Dönüşüm

**Strateji:** Instagram'da ürün ilgisi olan kişiyi WhatsApp'a taşımak:
- Instagram post'un altında: "Detaylar için DM" yerine "WhatsApp'tan yaz: [link]"
- WhatsApp'ta daha kişisel, daha hızlı satış
- Sepet terk oranı Instagram DM'de %40, WhatsApp'ta %15

**Agent workflow:**
```
[Instagram'da ürün ilgisi olan kişi tespit edildi]
    ↓
[Otomatik DM: "Bu ürünle ilgileniyorsunuz! WhatsApp'tan 1 dakikada sipariş verebilirsiniz 👉 [wa.me/link]"]
    ↓
[WhatsApp'ta sipariş alındı]
    ↓
[72 saat içinde upsell + cross-sell]
```

---

## Kaynaklar

- [Meta for Developers](https://developers.facebook.com/docs)
- [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [n8n WhatsApp Automation](https://github.com/mubashir-786/n8n-whatsapp-automation)
- [NotFair - Meta Ads Claude Code](https://github.com/nowork-studio/NotFair)
- [Meta Business Agent Global Launch - HN](https://news.ycombinator.com/item?id=xxx)

---

## LinkedIn Post Fikri

**Başlık:** Instagram'dan WhatsApp'a Geçiş = 3 Kat Daha Yüksek Satış

**Post:**
Instagram'da müşteriyle sohbet ediyorsunuz. Kaçırdığınız nokta: Instagram DM'de satış yapmaya çalışmak yerine, WhatsApp'a geçirmek.

Neden?

Instagram DM: Sepet terk oranı %40, ortalama yanıt süresi 2 saat
WhatsApp: Sepet terk oranı %15, 72 saat serbest mesaj hakkı, anlık bildirim

Workflow:
1. Instagram post'un altına "WhatsApp'tan yaz" butonu
2. Müşteri WhatsApp'a geldi → 72 saat başlıyor
3. AI agent 72 saat boyunca: sipariş, takip, upsell, cross-sell
4. Aynı müşteri Instagram'da kalsaydı: 1 mesaj hakkı, 2 saat bekleme

Bir e-ticaret müşterisi: Instagram DM satış dönüşümü %8. WhatsApp'a geçirdikten sonra %23. 3 kat artış.

Siz hangisini kullanıyorsunuz?

#Instagram #WhatsAppBusiness #E ticaret #Satış #AI

---

**Son Güncelleme:** 2026-06-19 00:00