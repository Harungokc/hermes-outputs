# Meta İçin Yapılabilecek AI Ajansları Araştırması — 2026-06-13 06:00

## Özet

Meta platformları için özel AI ajanları geliştirmek artık her zamankinden kolay. Meta'nın kendi siteleri (developers.facebook.com, business.whatsapp.com) bot koruması olmadan çalışıyor ve açık kaynak MCP server'lar ile Claude AI entegrasyonu çok basit. 200+ API endpoint'i ile Facebook Pages, Instagram, WhatsApp Business, Ads Manager'ın hepsi programatik olarak yönetilebiliyor.

**Herkesin Kaçırdığı Nokta:** Meta'nın 200+ araçlık MCP server'ı var (oliverames/meta-mcp-server) ve bu server ile sadece "veri çekme" değil, "otomatik karar alma" da yapabilirsiniz. Örneğin: "Reklam performansı %20 düşerse otomatik olarak budget'ı düşür ve yeni creative öner" gibi bir ajan bile mümkün.

---

## Bulunan Araçlar ve Linkler

### 1. oliverames/meta-mcp-server (En Kapsamlı)
| Özellik | Değer |
|---------|-------|
| **Stars** | 15 |
| **Language** | TypeScript |
| **Link** | https://github.com/oliverames/meta-mcp-server |
| **Son Güncelleme** | 2026-04-21 |
| **Açıklama** | Meta business platform için 200+ araç. Facebook Pages, Instagram, Threads, Ads Manager, Commerce, Conversions API, Audiences, Insights, Ad Library |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **API Coverage** | 200+ tools |
| **Kullanım** | Claude AI ile doğal dil ile Meta yönetimi |

### 2. mubashir-786/n8n-whatsapp-automation
| Özellik | Değer |
|---------|-------|
| **Stars** | 105 |
| **Language** | JavaScript |
| **Link** | https://github.com/mubashir-786/n8n-whatsapp-automation |
| **Son Güncelleme** | 2026-06-12 |
| **Açıklama** | n8n workflow ile WhatsApp Business API sipariş otomasyonu |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **Özellik** | Order management, customer management, real-time processing |
| **Kullanım** | E-ticaret WhatsApp botu |

### 3. itallstartedwithaidea/advertising-hub
| Özellik | Değer |
|---------|-------|
| **Stars** | 19 |
| **Language** | Markdown |
| **Link** | https://github.com/itallstartedwithaidea/advertising-hub |
| **Açıklama** | 14 platform için açık kaynak reklam otomasyon hub'ı |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **AI Agents** | 25+ |

---

## API'ler ve Kullanım Alanları

### Meta Platform API'leri

| API | Endpoint | Kullanım Alanı |
|-----|----------|----------------|
| **Facebook Graph API** | graph.facebook.com | Pages, Posts, Comments, Analytics |
| **Instagram Graph API** | graph.facebook.com/v18.0/instagram | Media, Comments, DMs, Insights |
| **WhatsApp Business API** | business.whatsapp.com | Mesajlaşma, Sipariş, Destek |
| **Marketing API** | graph.facebook.com/v18.0/act_{ad_account_id} | Reklam kampanyaları, Targeting |
| **Conversions API** | graph.facebook.com/v18.0/events | Event tracking, Pixel verileri |
| **Business Manager API** | graph.facebook.com/v18.0/businesses | Account management, Users |

### Kullanılabilecek API'ler (Meta Developer Console'dan)

```bash
# Facebook Graph API
https://graph.facebook.com/v18.0/me/accounts
https://graph.facebook.com/v18.0/{page-id}/posts
https://graph.facebook.com/v18.0/{page-id}/comments

# Instagram Graph API
https://graph.facebook.com/v18.0/{instagram-user-id}/media
https://graph.facebook.com/v18.0/{instagram-user-id}/comments
https://graph.facebook.com/v18.0/{instagram-user-id}/insights

# WhatsApp Business API
https://graph.facebook.com/v18.0/{phone-number-id}/messages
https://graph.facebook.com/v18.0/{waba-id}/message_templates

# Marketing API
https://graph.facebook.com/v18.0/act_{ad_account_id}/ads
https://graph.facebook.com/v18.0/act_{ad_account_id}/insights
```

---

## Adım Adım Yapım Rehberi

### Proje 1: WhatsApp Sipariş Botu (n8n + Claude Code)

**1. Gerekli Araçlar**
- Node.js 16+
- n8n (global kurulum)
- WhatsApp Business API hesabı
- Claude Code (isteğe bağlı)

**2. Kurulum**
```bash
# n8n-whatsapp-automation reposunu indir
git clone https://github.com/mubashir-786/n8n-whatsapp-automation.git
cd n8n-whatsapp-automation

# Bağımlılıkları kur
npm install

# Ortam değişkenlerini ayarla
cp .env.example .env
# .env dosyasını doldur:
# WHATSAPP_ACCESS_TOKEN=...
# WHATSAPP_PHONE_NUMBER_ID=...
# WHATSAPP_WEBHOOK_VERIFY_TOKEN=...
```

**3. n8n Workflow Import**
```
1. n8n'i başlat: n8n start
2. http://localhost:5678 adresine git
3. Settings → Import from JSON
4. n8n-workflows/whatsapp-order-automation.json dosyasını seç
5. Import et
```

**4. Bot Komutları**
Müşteriler şu komutları kullanabilir:
- `menu` — Ürün menüsünü görüntüle
- `order [ürün]` — Sipariş ver
- `track [sipariş-no]` — Sipariş takibi
- `help` — Yardım

### Proje 2: Instagram AI Community Manager (Claude + MCP)

**1. MCP Server Kurulumu**
```bash
# Claude Desktop kullanıyorsanız
# settings.json dosyasına ekleyin:
{
  "mcpServers": {
    "meta": {
      "command": "npx",
      "args": ["-y", "@oliverames/meta-mcp-server"]
    }
  }
}
```

**2. Claude AI ile Instagram Yönetimi**
```
# Yorumlara otomatik yanıt
Claude: "Instagram'daki son 10 yorumu oku ve her birine uygun yanıt öner"

# Post scheduling
Claude: "Bu hafta için 3 post planla, pazartesi 09:00, çarşamba 14:00, cuma 18:00"

# Analytics
Claude: "Son 30 günün Instagram insights'ını özetle, en iyi performans gösteren post'u bul"
```

### Proje 3: Meta Ads Performance Monitor

**1. Kurulum**
```bash
git clone https://github.com/ana-romero-lopez/meta-ads-ai-monitor.git
cd meta-ads-ai-monitor
pip install -r requirements.txt
```

**2. Konfigürasyon**
```python
# config.py
AD_ACCOUNT_ID = "act_123456789"
ACCESS_TOKEN = "your_facebook_access_token"
DAYS_TO_MONITOR = 7
ALERT_THRESHOLD = 0.2  # %20 düşüşte alert
SLACK_WEBHOOK = "your_slack_webhook_url"
```

**3. Çalıştır**
```bash
python meta-ads-monitor.py --days 7 --send-alerts
```

---

## Örnek Projeler ve GitHub Repoları

| Proje | Stars | Dil | Ne Yapıyor |
|-------|-------|-----|------------|
| oliverames/meta-mcp-server | 15 | TypeScript | 200+ Meta tool, Claude entegrasyonu |
| mubashir-786/n8n-whatsapp-automation | 105 | JavaScript | WhatsApp sipariş botu |
| advertising-hub | 19 | Markdown | 14 platform, 25+ AI agent |
| facebook-ads-library-mcp | 238 | Python | Rakip reklam analizi |
| peeomid/trak-social-cli | 2 | Python | Terminalden Meta yönetimi |

---

## Herkesin Kaçırdığı Nokta #1: Conversions API + CDP Entegrasyonu

Çoğu geliştirici sadece Pixel kullanıyor. Oysa **Conversions API** çok daha güvenilir veri sağlıyor çünkü sunucu tarafında çalışıyor, tarayıcı engellerinden etkilenmiyor. Bir ajan yazarken hem Pixel hem CAPI'yi birlikte kullanmak veri doğruluğunu artırır.

## Herkesin Kaçırdığı Nokta #2: WhatsApp Business API ile Otomatik Satış

WhatsApp'ta "1 dakikada sipariş" sistemi kurmak sadece hayal değil. n8n workflow + WhatsApp Business API + Claude Code birleşimi ile:
1. Müşteri DM'den "sipariş vermek istiyorum" yazıyor
2. Bot otomatik menüyü gönderiyor
3. Müşteri ürün seçiyor
4. Bot siparişi alıp SQLite'a kaydediyor
5. Stok kontrolü yapıyor
6. Ödeme linki gönderiyor
7. Onay sonrası kargo takip numarası veriyor

**Tüm bu süreç kod yazmadan n8n ile yapılabilir.**

## Herkesin Kaçırdığı Nokta #3: Multi-Agent Sistemleri

Meta'yı yönetmek için tek bir ajan yetmiyor. En iyi sonuç için specialization var:
- **Content Agent** — Post scheduling, hashtag önerileri
- **Engagement Agent** — Yorum yanıtlama, DM yönetimi
- **Ads Agent** — Kampanya optimizasyonu, budget yönetimi
- **Analytics Agent** — Raporlama, trend analizi
- **Support Agent** — Müşteri şikayetleri, sipariş takibi

Bu ajanlar MCP server üzerinden koordineli çalışabilir.

---

## Kaynaklar

1. oliverames/meta-mcp-server — https://github.com/oliverames/meta-mcp-server
2. mubashir-786/n8n-whatsapp-automation — https://github.com/mubashir-786/n8n-whatsapp-automation
3. itallstartedwithaidea/advertising-hub — https://github.com/itallstartedwithaidea/advertising-hub
4. proxy-intell/facebook-ads-library-mcp — https://github.com/proxy-intell/facebook-ads-library-mcp
5. Meta for Developers — https://developers.facebook.com/docs/marketing-apis
6. WhatsApp Business API — https://business.whatsapp.com/developers/developer-hub
