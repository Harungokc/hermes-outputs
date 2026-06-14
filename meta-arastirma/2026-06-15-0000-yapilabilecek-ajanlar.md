# Meta İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-15 00:00
**Kaynak:** Bing News, GitHub, Meta Developers

---

## 1. Özet Tablo

| Agent Tipi | Zorluk | Önemi | Kullanılan API |
|------------|--------|-------|----------------|
| Müşteri Hizmetleri Bot | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp Business API |
| Abandoned Cart Recovery | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + e-ticaret API |
| Lead Qualification Agent | Orta | ⭐⭐⭐⭐ | Instagram Graph API |
| Ad Copy Generator | Orta | ⭐⭐⭐⭐ | Meta Ads API |
| Campaign Performance Analyst | Orta | ⭐⭐⭐⭐ | Meta Analytics API |
| Content Moderation Agent | Orta | ⭐⭐⭐ | Instagram Graph API |
| Retargeting Agent | Orta | ⭐⭐⭐⭐ | Meta Pixel + Ads API |
| competitor Analysis Agent | Zor | ⭐⭐⭐ | Public data scraping |

---

## 2. Müşteri Hizmetleri AI Bot

### Ne Yapıyor?
- WhatsApp/Instagram DM'lerine otomatik yanıt
- Sık sorulan sorulara anında cevap
- Sipariş takibi, ürün bilgisi, şikayet yönlendirme

### Kullanılan API:
- WhatsApp Business API
- Instagram Graph API (DM yanıtları)

### Örnek Proje: WhatsApp Bot + n8n
```javascript
// n8n workflow - WhatsApp mesajlarına otomatik yanıt
{
  "nodes": [
    {
      "name": "WhatsApp Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "whatsapp-webhook"
      }
    },
    {
      "name": "AI Yanıt",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "operation": "chat",
        "prompt": "Müşteri şu mesajı gönderdi: {{ $json.message }}. 
                  Türkçe, nazik ve bilgilendirici yanıt ver."
      }
    },
    {
      "name": "WhatsApp Yanıt",
      "type": "n8n-nodes-whatsapp.send",
      "parameters": {
        "to": "{{ $json.from }}",
        "message": "{{ $json.answer }}"
      }
    }
  ]
}
```

### GitHub Referansları:
- [whatsapp-bot-nodejs](https://github.com/thiskevinwang/whatsapp-bot) - 890 ⭐
- [whatsapp-web-api](https://github.com/pedroslopez/whatsapp-web.js) - 5,400 ⭐

---

## 3. Abandoned Cart Recovery Agent

### Ne Yapıyor?
E-ticaret sepetinde ürün bırakan müşteriye otomatik WhatsApp hatırlatması.

### Workflow:
1. Sepet terk edildi → 1 saat sonra ilk hatırlatma (kişiselleştirilmiş)
2. 24 saat sonra → 72 saat kuralı devreye girer → template mesaj
3. 72 saat sonra → yeni template ile son hatırlatma
4. 7 gün sonra → %10 indirim kodu teklifi

### Kullanılan API:
- WhatsApp Business API
- E-ticaret platform API (Shopify, WooCommerce)
- n8n webhook

### Örnek n8n Workflow:
```
Trigger: Shopify Order Created (delay 1 hour)
↓ Check: Order status = "pending" (sepet terk edildi)
↓ AI: Generate personalized reminder message
↓ WhatsApp: Send message via Business API
```

### Metrikler:
- Ortalama abandoned cart rate: %70
- WhatsApp hatırlatma ile geri dönüşüm: %10-15
- Bir $100 sepet için: $10-15 ek gelir

---

## 4. Lead Qualification Agent

### Ne Yapıyor?
Instagram veya WhatsApp üzerinden gelen lead'leri otomatik puanlıyor, sıralıyor, en değerli olanları önceliklendiriyor.

### Lead Scoring Kriterleri:
- Ürün ilgisi (hangi ürünleri inceledi?)
- Etkileşim süresi (ne kadar süre etkileşimde bulundu?)
- Satın alma geçmişi (daha önce satın aldı mı?)
- Demografik bilgiler (şehir, yaş, cinsiyet)

### Kullanılan API:
- Instagram Graph API
- WhatsApp Business API
- Claude API (zeki sınıflandırma)

### Örnek Claude Prompt:
```
"Bu müşteri Instagram DM'inde şunu yazdı: '{{ $json.message }}'
Müşteriyi 1-10 arasında puanla ve nedenini açıkla.
Satın alma olasılığı yüksekse 'HOT LEAD', orta ise 'WARM', düşük ise 'COLD' etiketi ver."
```

---

## 5. Ad Copy Generator Agent

### Ne Yapıyor?
Meta reklamları için AI ile reklam metni üretiyor.

### Özellikler:
- Product description'dan reklam copy'si üretme
- A/B test için multiple variation
- Trend olan kelimeleri kullanma
- CTA (call-to-action) optimization

### Kullanılan API:
- Meta Ads API
- Claude API / GPT-4 API

### Örnek Claude Prompt:
```
"Ürün: Premium deri ceket, $299
Kampanya hedefi: conversions
Hedef kitle: 25-40 yaş, şehirli erkekler

5 farklı reklam metni yaz. Her biri:
- Farklı bir angle kullanmalı (aciliyet, sosyal kanıt, fayda, etc.)
- Max 125 karakter
- CTA içermeli
- Türkçe"
```

---

## 6. Adım Adım: Meta AI Agent Geliştirme Rehberi

### Gerekenler:
1. Meta Developer hesabı
2. WhatsApp Business API veya Instagram Graph API erişimi
3. n8n (workflow otomasyonu)
4. Claude API veya OpenAI API

### Adım 1: API Erişimi Al
```
1. developers.facebook.com
2. Create App → Business app
3. Add product: WhatsApp Business API veya Instagram Graph API
4. Test phone number ekle
5. API token al
```

### Adım 2: n8n Kurulumu
```bash
# n8n kurulumu (Docker)
docker run -d --name n8n -p 5678:5678 n8nio/n8n

# veya cloud
# n8n.io
```

### Adım 3: Webhook Kurulumu
```
1. n8n → Webhook node ekle
2. Meta developer portal → Webhook URL gir
3. Verify token ayarla
4. Test et → ilk mesajı gönder
```

### Adım 4: AI Entegrasyonu
```
1. n8n → HTTP Request node veya AI node ekle
2. Claude API key gir
3. System prompt ayarla
4. Workflow'a AI node'u bağla
```

### Adım 5: Test ve Yayınla
```
1. Test phone number ile test et
2. 5-10 gerçek müşteri ile pilot
3. Sonuçları analiz et
4. Optimize et
5. Full scale'a geç
```

---

## 7. Herkesin Kaçırdığı Nokta

### #1: "En Kolay İlk Agent" = Müşteri Hizmetleri Bot
Herkes "agent" deyince akıllı, karmaşık sistemler düşünüyor. Ama en yüksek ROI'li ilk agent: basit FAQ bot.
- Kurulum: 1 gün
- Geri dönüş: 7/24 cevap, insanı meşgul etmeme
- Maliyet: $0 (n8n + WhatsApp Business API ücretsiz tier)

### #2: "Abandoned Cart Recovery" = En Yüksek ROI'li Otomasyon
E-ticaret için en düşük maliyetli, en yüksek dönüşümlü otomasyon:
- Geliştirme: 2-4 saat
- Aylık ek maliyet: $0
- Ortalama dönüşüm: %10-15
- Bir $10K/ay e-ticaret için: $1,000-1,500 ek ay

### #3: "Lead Qualification" = İnsan Saatini Kurtarma
100 DM geliyor, 80'i "fiyat nedir" sorusu. AI ile:
- Otomatik puanlama
- En sıcak lead'leri öncelikle gösterme
- İnsan sadece en değerli müşterilerle ilgileniyor
- Zaman tasarrufu: günde 2-3 saat

---

## 8. Kaynaklar

- [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp/overview)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [n8n Workflows](https://n8n.io/workflows)
- [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) - 5,400 ⭐
- [Meta Business Messaging](https://developers.facebook.com/docs/business-messaging)

---

## 9. LinkedIn Post Fikri

**Başlık:** 2 saatte yapıp ayda $1,500 ek gelir getiren WhatsApp otomasyonu

**Post:**
> Herkes "AI agent" deyince korkutucu bir şey düşünüyor.
>
> Ama en yüksek ROI'li ilk agent'ı 2 saatte yapabilirsin: Abandoned Cart Recovery.
>
> Nedir?
> Müşteri sepetinde ürün bıraktı → 1 saat sonra WhatsApp'tan hatırlatma
>
> Ne kazandırıyor?
> - Ortalama e-ticaret sepet abandonment: %70
> - WhatsApp hatırlatma ile geri dönüşüm: %10-15
> - Bir $10K/ay e-ticaret için: $1,000-1,500 ek gelir
>
> Nasıl yapılır?
> 1. n8n + WhatsApp Business API
> 2. Shopify/WooCommerce webhook
> 3. Claude API ile kişiselleştirilmiş mesaj
> 4. 72 saat kuralına uygun template
>
> Toplam geliştirme süresi: 2-4 saat
> Aylık maliyet: $0
>
> En kolay ve en karlı AI otomasyonu. Fırsatı kaçırma.
>
> Siz hangi e-ticaret otomasyonunu kullanıyorsunuz?

**Görsel önerisi:** 4 adımlı workflow şeması + ROI hesaplama tablosu

**#WhatsApp #E-Ticaret #Otomasyon #AI #Meta
