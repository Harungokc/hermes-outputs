# Meta Araştırma — Yapılabilecek Meta Ajansları
**Tarih:** 2026-06-14 06:00
**Session:** Meta Platform Araştırması — Her 6 Saatte Bir

---

## 1. Özet

Meta platformları (Instagram, WhatsApp, Facebook) için AI ajanı geliştirmek artık hemfikir kaynak ve API'lerle oldukça erişilebilir durumda. Kullanıcının mevcut stack'i (n8n + Claude Code + Instagram Graph API + WhatsApp Business API) zaten doğru yönde — buradan hareketle 5 farklı ajan türü inşa edilebilir.

---

## 2. Bulunan Yapılmış Ajanslar ve Linkler

### Meta MCP Server — 200+ Araç İçeren AI Agent Altyapısı

| Özellik | Değer |
|---------|-------|
| **GitHub** | [oliverames/meta-mcp-server](https://github.com/oliverames/meta-mcp-server) |
| **Yıldız** | 15 ⭐ |
| **Dil** | TypeScript |
| **Kapsam** | Facebook Pages, Instagram, Threads, Ads Manager, Commerce, Conversions API, Audiences, Insights, Ad Library |
| **Maliyet** | Ücretsiz (açık kaynak) |
| **Geliştirici** | Oliver Ames |

### n8n WhatsApp Otomasyon — Sipariş İşleme Ajanı

| Özellik | Değer |
|---------|-------|
| **GitHub** | [mubashir-786/n8n-whatsapp-automation](https://github.com/mubashir-786/n8n-whatsapp-automation) |
| **Yıldız** | 105 ⭐ |
| **Dil** | JavaScript/Node.js |
| **Kapsam** | WhatsApp Business API ile sipariş işleme, stok kontrolü, müşteri bildirimi |
| **Maliyet** | Ücretsiz (n8n açık kaynak) + WhatsApp Business API ücreti |

### Social Flow — Meta Operasyonları Kontrol Plane

| Özellik | Değer |
|---------|-------|
| **GitHub** | [vishalgojha/social-flow](https://github.com/vishalgojha/social-flow) |
| **Yıldız** | 144 ⭐ |
| **Dil** | TypeScript |
| **Kapsam** | Facebook, Instagram, WhatsApp, Ads Manager workflow'ları için CLI |
| **Maliyet** | Ücretsiz (açık kaynak) |

---

## 3. Herkesin Kaçırdığı Nokta #1 — Meta MCP Server'ın 200+ Aracı ile Neredeyse Her Şey Yapılabilir

**Herkes ne konuşuyor?** "Meta için AI ajanı yapmak için çok fazla API bilgisi gerekiyor, başlamak zor."

**Ama gerçekte ne var?** Meta MCP Server, Meta'nın tüm API'lerini 200+ hazır "tool" olarak sarıyor. Bir AI agent bu tool'ları kullanarak:
- Instagram'da fotoğraf paylaşabilir (tamamen AI ile)
- Ads Manager'da kampanya oluşturabilir
- WhatsApp'tan gelen siparişleri işleyebilir
- Audience segmentasyonu yapabilir

**Somut örnek:** Kullanıcı "1 dk'da sipariş sistemi" diyor. Meta MCP Server + n8n + WhatsApp Business API ile: müşteri WhatsApp'tan "sipariş ver" diyor → ajan ürün katalogını çekiyor → sepet oluşturuyor → ödeme linki gönderiyor → sipariş onaylanıyor.

---

## 4. Herkesin Kaçırdığı Nokta #2 — Instagram Graph API + Claude Code = Otonom İçerik Ajanı

**Herkes ne konuşuyor?** "Instagram'da içerik paylaşmak için her gün manual olarak uğraşmak gerekiyor."

**Ama gerçekte ne var?** Instagram Graph API + n8n + Claude Code ile:
1. Haftalık içerik takvimi tanımla
2. Claude Code her gün için caption + hashtag üretsin
3. n8n bu içeriği Instagram Graph API ile zamanlı olarak paylaşsın
4. Yorumları çeksin, AI yanıt versin

**Kullanıcının mevcut stack'i zaten bunu destekliyor:** Instagram Messaging API + Claude AI bot (DM, yorum, story mention → otomatik DM) — bu mevcut sistem Meta MCP Server ile genişletilebilir.

---

## 5. Herkesin Kaçırdığı Nokta #3 — "Abandoned Cart Recovery" Ajanı — En Yüksek ROI

**Herkes ne konuşuyor?** "E-ticaret için WhatsApp botu yapmak istiyorum ama nereden başlayacağımı bilmiorum."

**Ama gerçekte ne var?** En yüksek ROI'li WhatsApp ajanı: **Sepeti terk eden müşterilere otomatik hatırlatma.**

Workflow:
- Müşteri web sitenizde ürünü sepete koydu ama satın almadı
- 1 saat sonra: WhatsApp'tan "Sepetinizi mi unuttunuz? 😄" + ürün görseli + ödeme linki
- 24 saat sonra: "Stokta son 2 adet kaldı!" urgency mesajı
- 72 saat sonra: %10 indirim kodu

**Metrikler:** Bu tip otomasyonlar %10-15 ek dönüşüm artışı sağlıyor (Meta Business duyurusuna göre).

---

## 6. Yapılabilecek 5 Meta Ajanı

### Ajan 1: Instagram İçerik Ajanı
```
Görev: Haftalık içerik üretimi + paylaşım + yorum yanıtlama
Stack: Instagram Graph API + n8n + Claude Code
Zaman tasarrufu: Haftada ~4 saat
Gereken: Instagram Business hesabı, Content API erişimi
```

### Ajan 2: WhatsApp Sipariş Ajanı
```
Görev: 7/24 sipariş alma, stok sorgulama, ödeme linki gönderme
Stack: WhatsApp Business API + n8n + Claude Code
Zaman tasarrufu: Günde ~2 saat müşteri sorgulaması
Gereken: WhatsApp Business hesabı, e-ticaret entegrasyonu
```

### Ajan 3: Abandoned Cart Recovery Ajanı
```
Görev: Sepeti terk eden müşterilere otomatik hatırlatma
Stack: WhatsApp Business API + webhooks + n8n
ROI: %10-15 ek dönüşüm
Gereken: WooCommerce/Shopify webhook + WhatsApp Business API
```

### Ajan 4: Meta Ads Performans Ajanı
```
Görev: Günlük reklam performansı izleme + otomatik bid ayarı
Stack: Meta Marketing API + Social Flow + Claude Code
Zaman tasarrufu: Günde ~1 saat manuel kontrol
Gereken: Ads Manager erişimi, API token
```

### Ajan 5: Müşteri Hizmetleri Triyaj Ajanı
```
Görev: WhatsApp/Instagram DM'lerini triyaj et, AI yanıtlasın, insan gerektirenleri yönlendirsin
Stack: WhatsApp Business API + Instagram Messaging API + n8n + Claude Code
Triage kriterleri: Sipariş sorgusu, şikayet, ürün bilgisi, diğer
```

---

## 7. Adım Adım Yapım Rehberi — Meta MCP Server + Claude Code

### Kurulum

```bash
# 1. Node.js projesi oluştur
mkdir meta-agent && cd meta-agent
npm init -y

# 2. Meta MCP Server'ı yükle
npm install @oliverames/meta-mcp-server

# 3. Environment değişkenleri
cat > .env << EOF
META_ACCESS_TOKEN=your_page_access_token
META_APP_SECRET=your_app_secret
META_AD_ACCOUNT_ID=act_xxxxx
INSTAGRAM_BUSINESS_ACCOUNT_ID=ig_xxxxx
EOF

# 4. Claude Code başlat
claude-code --mcp-server meta-mcp-server
```

### Örnek Claude Code Prompt

```
Meta MCP Server kullanarak Instagram hesabıma:
1. Haftalık içerik takvimime uygun bir post paylaş
2. İçerik konusu: [konu]
3. Caption: Samimi, e-ticaret odaklı, emoji kullan
4. Hashtag'ler: 8-10 tane, alakalı
5. Paylaşım saatini optimize et (10:00-11:00 arası)
```

---

## 8. Görsel Önerisi — LinkedIn Post

**Taslak görsel:** Beyaz tahta üzerine çizilmiş akış diyagramı — "Terkedilen Sepet" → "1s: Hatırlatma" → "24s: Urgency" → "72s: İndirim" → "%10-15 Ek Dönüşüm". Altında mavi ok: "WhatsApp Business API + n8n + Claude Code = Otomatik Recovery Ajanı"

---

## 9. Kaynaklar

- [Meta MCP Server](https://github.com/oliverames/meta-mcp-server)
- [Social Flow](https://github.com/vishalgojha/social-flow)
- [n8n WhatsApp Automation](https://github.com/mubashir-786/n8n-whatsapp-automation)
- [Meta Business Agent](https://business.whatsapp.com/business-agent)
- [Instagram Graph API Docs](https://developers.facebook.com/docs/instagram-api)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)