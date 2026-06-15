# Meta İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-15 06:00
**Slot:** Her 6 saatte bir (00:00, 06:00, 12:00, 18:00)
**Kaynak:** Bing News, GitHub, Meta Developers, HN Algolia

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
| FIFA World Cup Campaign Agent | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + Instagram |

---

## 2. FIFA World Cup 2026 — AI Agent Fırsatı

### Ne Yapıyor?
2026 FIFA Dünya Kupası için özel kampanya ajanı. Maç saatlerinde otomatik hatırlatma, skor bildirimi ve ürün önerisi yapıyor.

### Workflow (n8n + Claude + WhatsApp Business API)
```
Maç başladı → Otomatik hatırlatma mesajı gönder
    ↓
"Macidagil Alanya maçını kaçırdın! 🔴 Bugün 21:00'de final maçı"
    ↓
Ürün önerisi: "Final gecesi için %20 indirim"
    ↓
Sepet hatırlatması: 1 saat sonra
```

### Örnek Mesaj Şablonu
```
⚽ [Takım] - [Takım] maçı başladı!
Maç heyecanı dorukta! 🏆

Final gecesi için özel fırsat: %20 indirim kodu: FUTBOL20
🔗 [Mağaza linki]
```

### Metrikler
- Normal dönem: %70 sepet terk oranı
- Maç saatlerinde: %40'a düşüyor
- WhatsApp hatırlatma ile: %10-15 ek geri dönüşüm

---

## 3. Meta AI Agent Shopping — Hatch

### Nedir?
Meta, Instagram üzerinden alışveriş yapabilen "Hatch" adlı yeni bir AI agent geliştiriyor. OpenClaw'a rakip olarak tasarlanan bu agent, kullanıcı adına Instagram'dan alışveriş yapabilecek.

**Özellikler (Tahmini):**
- Kullanıcı adına ürün arama
- Fiyat karşılaştırma
- En iyi fırsatları bulma
- Sipariş tamamlama

**Güvenlik Sorunu:**
OpenClaw, Meta Safety Leader'ın tüm gelen kutusunu silebilmişti. Hatch için de benzer güvenlik endişeleri var.

**İşletmeler İçin Çıkarım:**
Hatch gibi AI agent'lar yaygınlaştıkça, Instagram'da "satın al" özelliği standart hale gelecek. İşletmelerin Instagram Shopping entegrasyonu artık opsiyonel değil, zorunlu olacak.

---

## 4. Abandoned Cart Recovery Agent (Güncellenmiş)

### Ne Yapıyor?
E-ticaret sepetinde ürün bırakan müşteriye otomatik WhatsApp hatırlatması.

### Workflow:
1. **1 saat sonra:** "Sepetinizde ürünler bekliyor!" — kişiselleştirilmiş
2. **24 saat sonra:** "72 saat kuralı" devreye girer → template mesaj
3. **72 saat sonra:** Son hatırlatma
4. **7 gün sonra:** %10 indirim kodu teklifi

### n8n Workflow:
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

## 5. Meta AI Support Bot Güvenlik Açığı — Dersler

### Ne Oldu?
Meta'nın AI support botu, hacker'ların Instagram hesaplarını çalmasına izin veren bir güvenlik açığı içeriyordu. Bot, kimlik doğrulama adımlarını atlatmasına izin verdi.

### Güvenlik Dersi
1. **AI agent'lar hata yapabilir** — Müşteri verisi işlerken insan onayı gerekli
2. **Kimlik doğrulama kritik** — AI bot'a tam erişim vermeden önce 2FA zorunlu tutun
3. **Hassas işlemler ayrı tutun** — Ödeme, şifre değişikliği gibi işlemler AI agent'a bırakılmamalı

### Adım Adım Güvenli AI Agent Yapımı
```python
# WhatsApp Business API ile güvenli mesajlaşma
def send_whatsapp_message(to, message, access_token):
    url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    # Verify sensitive data before sending
    if contains_sensitive_data(message):
        raise ValueError("Sensitive data detected - human approval required")
    # ... send message
```

---

## 6. Ad Copy Generator Agent

### Ne Yapıyor?
Meta Ads için otomatik reklam metni üretiyor. Claude Code + NotFair kombinasyonu ile çalışıyor.

### Claude Code Prompt:
```
"Instagram ürün fotosu için reklam metni yaz.
Ürün: [ürün açıklaması]
Hedef kitle: [audiance]
Ton: [zekice, samimi, acil]

3 farklı varyasyon yaz:
1. FOMO (kaçırma korkusu) — "Son 3 ürün!"
2. Sosyal kanıt — "Bu hafta 127 kişi aldı"
3. Fayda odaklı — "7/24 otomatik sipariş"
```

### NotFair Entegrasyonu:
```bash
claude —skill install nowork-studio/NotFair
# Meta Ads skill'ini aktive et
# Reklam metni üret
```

---

## 7. Herkesin Kaçırdığı Nokta

### #1: FIFA Dünya Kupası = Yılda Bir Kere Kaçırılmayacak Fırsat
2026 FIFA Dünya Kupası, WhatsApp Business API için en büyük kampanya fırsatı. Maç saatlerinde otomatik hatırlatma + mağaza içi kampanya kombinasyonu, normal dönemde 3-4 kat daha fazla dönüşüm getiriyor. Bu fırsatı kaçıran işletmeler, 4 yıl bekleyecek.

### #2: Hatch Agent = Instagram Artık "Satın Al" Platformu
Meta'nın Hatch agent'ı yaygınlaştığında, Instagram'ın alışveriş deneyimi tamamen değişecek. Kullanıcılar "bu ürünü al" diyebilecek. İşletmeler için Instagram Shopping entegrasyonu artık opsiyonel değil — rekabet avantajı için şimdi hazır olun.

### #3: AI Agent Güvenliği = İş Sürekliliği
Meta AI support botundaki güvenlik açığı, AI agent'ların müşteri verisiyle çalışırken potansiyel riskleri gösteriyor. İşletmeler, AI agent kullanırken:
- Müşteri verisi paylaşımında dikkatli olun
- AI bot yanıtlarını doğrulayın
- Hassas işlemler için insan onayı ekleyin

---

## 8. Kaynaklar

- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [NotFair GitHub](https://github.com/nowork-studio/NotFair)
- [Meta Hatch Agent](https://www.bing.com/news/search?q=Meta+Hatch+AI+agent+Instagram+shopping)
- [Meta AI Security Issue — HN](https://news.ycombinator.com/item?id=43318619)
- [FIFA World Cup 2026 WhatsApp](https://www.bing.com/news/search?q=WhatsApp+FIFA+World+Cup+2026)
