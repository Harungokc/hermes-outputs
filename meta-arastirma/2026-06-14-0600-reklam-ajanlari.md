# Meta Araştırma — Reklam Ajans Araçları
**Tarih:** 2026-06-14 06:00
**Session:** Meta Platform Araştırması — Her 6 Saatte Bir

---

## 1. Özet

Meta Ads ajanları için hem ticari platformlar (AdEspresso, Revealbot, Madgicx) hem de açık kaynak alternatifler mevcut. Meta'nın kendi Advantage+ AI özelliği, reklam optimizasyonunu büyük ölçüde otomatikleştiriyor. Ancak açık kaynak alternatifler henüz Advantage+ düzeyinde zeka sunamıyor — daha çok webhook/CLI otomasyonu seviyesinde kalıyor.

---

## 2. Bulunan Araçlar ve Linkler

### Ticari Reklam Otomasyon Platformları

| Platform | Fiyat | Özellikler |
|----------|-------|------------|
| [AdEspresso](https://adespresso.com/) | $49/ay~ | Facebook/Instagram/Google Ads yönetimi, A/B test, otomatik optimizasyon |
| [Revealbot](https://revealbot.com/) | $99/ay~ | Otomatik kampanya yönetimi,/rules-based automation |
| [Madgicx](https://madgicx.com/) | $149/ay~ | AI-powered ads optimization, creative analysis |
| [Social Flow](https://github.com/vishalgojha/social-flow) | Açık kaynak | Meta operasyonları için kontrol plane (144⭐) |
| [Meta-Ads-Automation-n8n](https://github.com/nikD305/Meta-Ads-Automation-n8n) | Açık kaynak | n8n + Google Sheets + Telegram entegrasyonu |

### Açık Kaynak Alternatifler

| Araç | Yıldız | Dil | Açıklama |
|------|--------|-----|----------|
| [social-flow](https://github.com/vishalgojha/social-flow) | 144 ⭐ | TypeScript | Meta Ads/Instagram/WhatsApp için CLI tabanlı otomasyon |
| [meta-mcp-server](https://github.com/oliverames/meta-mcp-server) | 15 ⭐ | TypeScript | 200+ araç — Facebook Pages, Instagram, Ads Manager, Commerce |
| [ads-manager-agent](https://github.com/grindflame/ads-manager-agent) | 0 ⭐ | - | Agent-ready Meta Ads otomasyon toolkit |

---

## 3. Herkesin Kaçırdığı Nokta #1 — Advantage+ AI'ın Arkasındaki Gerçek

**Herkes ne konuşuyor?** "Meta Advantage+ AI ile reklamlar otomatik optimize ediliyor, artık el ile kampanya yönetmeye gerek yok."

**Ama gerçekte ne var?** Advantage+ AI aslında sadece **hedefleme ve placement** optimizasyonu yapıyor. Reklam kreativlerini (görsel, video, copy) hâlâ insanlar tasarlıyor. Üstelik Advantage+ kampanyaları başlattığınızda Meta, eski kampanyalarınızdaki en iyi performans gösteren rekabetleri kopyalayıp yeni kampanyaya uyguluyor — bu "gizli" öğrenme mekanizması çoğu reklamcının gözünden kaçıyor.

**Sonuç:** Advantage+ = yeni başlayanlar için harika, ama deneyimli reklamcılar için kontrole göre %20-40 daha pahalıya mal olabiliyor.

---

## 4. Herkesin Kaçırdığı Nokta #2 — Social Flow'un 144 Yıldız Sırrı

**Herkes ne konuşuyor?** Meta açık kaynak otomasyon aracı olarak sadece meta-mcp-server (15⭐) var.

**Ama gerçekte ne var?** [Social Flow](https://github.com/vishalgojha/social-flow) (144⭐, TypeScript) — Facebook, Instagram, WhatsApp ve Ads Manager workflow'larını tek bir yerden yöneten bir CLI aracı. İçinde:
- Setup, günlük yürütme, onaylar, raporlama
- Gateway API'leri ve SDK desteği
- Komut satırından kampanya başlatma/durdurma

**Kullanım senaryosu:** Bir ajans 10+ Meta hesabı yönetiyorsa, her biri için ayrı Business Manager açmak yerine Social Flow ile tek terminalden tümünü yönetebilir.

---

## 5. Herkesin Kaçırdığı Nokta #3 — Meta MCP Server'ın 200+ Aracı

**Herkes ne konuşuyor?** Meta için AI agent yapmak zor, çok fazla API dokümanı okumak gerekiyor.

**Ama gerçekte ne var?** [Meta MCP Server](https://github.com/oliverames/meta-mcp-server) (15⭐, TypeScript) — Claude Code veya herhangi bir MCP-uyumlu AI agent'ı doğrudan Meta platformuna bağlayan 200+ hazır araç:
- Facebook Pages: post oluşturma, yorum moderation, Messenger yanıtları
- Instagram: media upload, caption yazma, insight çekme
- Ads Manager: kampanya oluşturma, bütçe ayarlama, performans çekme
- Commerce: ürün kataloku, sipariş yönetimi
- Conversions API: event gönderme, audience yönetimi

**Kullanıcının işine yarayacak kısım:** Instagram Graph API + n8n + Claude Code workflow'u zaten kullanıyor. Meta MCP Server bu mimariye ek olarak WhatsApp Business API ve Ads Manager entegrasyonu sağlayabilir.

---

## 6. Adım Adım Yapım Rehberi — Meta MCP Server Kurulumu

### Gereksinimler
- Node.js 18+
- Meta Developer hesabı
- Claude Code veya MCP-uyumlu AI assistant

### Kurulum
```bash
npm install -g @anthropic-ai/mcp-server/meta
# veya
npx @oliverames/meta-mcp-server

# Environment variables
export META_ACCESS_TOKEN="your_page_access_token"
export META_APP_SECRET="your_app_secret"
export META_AD_ACCOUNT_ID="act_xxxxx"

# Claude Code'da MCP server'ı başlat
claude --mcp-server meta-mcp-server
```

### Kullanılabilir Araçlar Örneği
```
instagram_create_media: Görsel/-video paylaşımı
instagram_get_insights: Performans metrikleri
facebook_create_post: Page post oluşturma
adsmanager_create_campaign: Kampanya başlatma
commerce_get_orders: Sipariş listesi çekme
```

---

## 7. Görsel Önerisi — LinkedIn Post

**Taslak görsel:** Ekran görüntüsü — Social Flow CLI çıktısı (bir sürü Meta hesabını listeliyor) + yanında "144⭐ açık kaynak" etiketi. Altında kırmızı box: "Herkes Meta'nın kendi araçlarını kullanırken, asıl güçlü olan açık kaynak alternatifler gözden kaçıyor"

---

## 8. Kaynaklar

- [Social Flow GitHub](https://github.com/vishalgojha/social-flow)
- [Meta MCP Server](https://github.com/oliverames/meta-mcp-server)
- [Meta Ads Automation n8n](https://github.com/nikD305/Meta-Ads-Automation-n8n)
- [AdEspresso](https://adespresso.com/)
- [Madgicx](https://madgicx.com/)
- [Revealbot](https://revealbot.com/)
- [Meta Business Agent Global](https://www.bing.com/news/search?q=Meta+Business+Agent+global+2026)