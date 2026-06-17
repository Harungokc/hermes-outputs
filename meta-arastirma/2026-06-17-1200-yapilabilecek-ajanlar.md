# Meta İçin Yapılabilecek AI Ajansları Araştırması
**Tarih:** 2026-06-17 12:00
**Slot:** Her 6 saatte bir (00:00, 06:00, 12:00, 18:00)
**Kaynak:** Bing News, HN Algolia, GitHub, Meta Developers

---

## 1. Özet Tablo

| Yapılabilecek Agent | Platform | Zorluk | Maliyet | Gerekli API |
|---------------------|----------|--------|---------|-------------|
| Sipariş Takip Bot | WhatsApp Business API | Kolay | Düşük | WhatsApp Cloud API |
| Sepeti Terk Etme Hatırlatıcı | WhatsApp Business API | Orta | Orta | WhatsApp + E-ticaret API |
| Stok Uyarı Agent'ı | WhatsApp Business API | Kolay | Düşük | WhatsApp + Stok API |
| Randevu Hatırlatma | WhatsApp Business API | Kolay | Düşük | WhatsApp + Takvim API |
| Müşteri Destek Triyaj | WhatsApp/Instagram | Orta | Orta | WhatsApp Cloud API + NLP |
| Meta Ads Performance Bot | Meta Ads API | Orta | Orta | Meta Marketing API |
| Instagram Yorum Otomasyon | Instagram Graph API | Orta | Düşük | Instagram API |
| Abandoned Cart Recovery | WhatsApp Business | Orta | Orta | WhatsApp + Shopify/WooCommerce |

---

## 2. En Kolay 3 Agent — Bugün Yapılabilir

### A. Sipariş Takip Bot (WhatsApp)

**Gerekli:** WhatsApp Business API + Basit webhook entegrasyonu

**Nasıl çalışır:**
1. Müşteri sipariş verdiğinde otomatik WhatsApp mesajı
2. "Siparişiniz alındı, takip numarası: X"
3. Kargo güncellemelerinde otomatik bildirim
4. "Teslim edildi" sonrası 72 saat içinde ürün önerisi

**Örnek Workflow (n8n):**
```
Sipariş oluştu (Webhook) → Claude'a sipariş özeti →
WhatsApp mesaj gönder (template) → 3 gün sonra ürün önerisi
```

**Maliyet:** ~$50/ay (WhatsApp Business API + n8n hosting)

### B. Sepeti Terk Etme Hatırlatıcı (WhatsApp)

**Gerekli:** WhatsApp Business API + E-ticaret platformu webhook

**Workflow:**
- 1. saat: "Sepetinizde ürünler bekliyor" (otomatik)
- 24. saat: %10 indirim kodu ile hatırlatma
- 72. saat: "Son 1 gün! Stokta son 3 adet" (gerçek zamanlı stok kontrolü)

**Metrik:** Sepeti terk eden müşterilerin %10-15'i WhatsApp hatırlatmasıyla geri dönüyor.

**Herkesin Kaçırdığı Nokta:** En yüksek ROI'li WhatsApp otomasyonu. Yatırım getirisi en yüksek olan. E-ticaret için vazgeçilmez.

### C. Instagram Yorum Otomasyonu (Instagram Graph API)

**Gerekli:** Instagram Business hesabı + Meta Developer App

**Özellikler:**
- Belirli hashtag'lere yorum yapma
- Yorumdaki sorulara otomatik yanıt
- Story mention'larına DM atma
- Yeni takipçilere hoş geldin mesajı

**Nasıl Yapılır (Adım Adım):**
1. Meta Developer'da uygulama oluştur → "Business" tipi seç
2. Instagram Graph API permissions ekle: `instagram_basic`, `pages_read_engagement`, `instagram_manage_comments`
3. Instagram Business hesabını Bağla
4. Webhook setup: `instagram_comments` → n8n workflow tetikle
5. n8n'de: Yorum metni → Claude API → Yanıt oluştur → Instagram API ile yorum yap

---

## 3. Meta Ads Agent — n8n + Claude + Meta Marketing API

### Kurulum Adımları

**1. Meta Developer App Oluştur:**
- https://developers.facebook.com adresine git
- "My Apps" → "Create App" → "Business" seç
- App ID ve App Secret al

**2. Meta Marketing API Erişimi:**
- App'a "Marketing API" ürününü ekle
- `ads_read`, `business_management` permissions iste
- User Access Token al (Facebook Login ile)

**3. n8n Workflow:**
```
Meta Ads Webhook (kampanya performans değişimi) →
Claude API (analiz + öneri) →
Meta Ads API (bid/budget güncellemesi veya alert)
```

### MCP Server ile Daha Hızlı Kurulum

`google-meta-ads-ga4-mcp` (1009⭐) veya `meta-ads-mcp` (992⭐) kullanarak:
- n8n → MCP Server → Meta Ads API
- Claude Code → MCP Server → Kampanya oluşturma
- Cursor → MCP Server → Rakip analizi

---

## 4. Yapılabilecek En Güçlü Agent: Abandoned Cart Recovery

**Bu, Meta Business Agent'ın yapabileceklerinin ötesinde — özelleştirilmiş bir ajan.**

### Workflow Detayı

```
SAAT 0: Müşteri sepete ürün ekledi (webhook)
SAAT 1: Otomatik WhatsApp: "Sepetinizde [ürün] bekliyor 👀"
        → 72 saat kuralına uygun, serbest mesaj

SAAT 24: Ödeme yapılmadı
        → %10 indirim kodu: "SEPETTE10"
        → Template message (Meta onayı gerekir)

SAAT 48: Hâlâ ödeme yok
        → "Stokta son 3 adet kaldı!"
        → Gerçek zamanlı stok API kontrolü

SAAT 72: Son fırsat
        → "Yarın son! Fırsat kaçıyor"
        → Aciliyet yarat

SAAT 73+: 72 saat doldu
        → Sadece template message ile ulaşılabilir
        → "Hoşçakal" mesajı + gelecek kampanya için izin al
```

### Teknoloji Stack

| Bileşen | Araç |
|---------|------|
| E-ticaret Platform | Shopify / WooCommerce / Magento |
| Otomasyon | n8n |
| AI Brain | Claude API |
| Mesajlaşma | WhatsApp Business API |
| CRM / Log | Google Sheets / Airtable |
| Raporlama | Google Data Studio |

### Maliyet

- WhatsApp Business API: ~$50-200/ay (mesaj başına $0.05-0.15)
- n8n cloud: ~$20/ay
- Claude API: ~$20-50/ay (mesaj hacmine bağlı)
- Toplam: ~$100-250/ay

### ROI Beklentisi

Sepeti terk eden 100 müşteriden:
- Normalde: 15-20 geri döner (%15-20)
- WhatsApp hatırlatma ile: 25-35 geri döner (%25-35)
- Ek gelir: 10-15 ek sipariş x ortalama sepet değeri

---

## 5. LinkedIn Post Fikri

**Başlık:** WhatsApp'ta 72 Saat Kuralını Bilmeyen Kaybediyor

WhatsApp Business API'de toplu mesaj göndermek isteyen herkesin ilk çarptığı duvar: "Müşteri yazmadı, mesaj atamıyorum."

72 saat kuralı — müşteriyle son temasından itibaren 3 gün boyunca serbest mesaj atabilirsin. Sonrası? Template message zorunlu, Meta onayı gerekir.

Ama asıl kaçırılan fırsat şu: 72 saat kuralı bir kısıtlama DEĞİL, bir strateji. Doğru yapılandırılmış bir otomasyon, müşteriyi 71. saatte yakalar ve dönüşüm sağlar.

İşte bugün keşfettiğim en yüksek ROI'li pattern: n8n + WhatsApp Business API + 72 saat takip akışı.

Bu döngü e-ticaret için %15-20 ek dönüşüm sağlıyor.

Siz hangi aşamada kaybettiğinizi biliyor musunuz?

#WhatsAppBusiness #EcommerceAutomation #AI

---

## 6. Kaynaklar

- https://github.com/nowork-studio/NotFair (2873⭐)
- https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp (1009⭐)
- https://github.com/pipeboard-co/meta-ads-mcp (992⭐)
- https://developers.facebook.com/docs/whatsapp/overview
- https://github.com/nikhilmuz/WhatsApp-Bulk-Sender (284⭐)
