# Meta Araştırma — Yapılabilecek Meta Ajansları
**Tarih:** 2026-06-14 12:00
**Session:** Meta Platform Araştırması — Her 6 Saatte Bir

---

## 1. Özet

Meta platformları (Instagram, WhatsApp, Facebook) için AI ajanı geliştirmek 2026'da açık kaynak MCP server'lar sayesinde oldukça kolaylaştı. Kullanıcının mevcut stack'i (n8n + Claude Code + Instagram Graph API + WhatsApp Business API) zaten doğru yönde — buradan hareketle 5 farklı ajan türü inşa edilebilir. Bu session'da 2849 yıldızlı NotFair'den 40 yıldızlı Markifact MCP'e kadar tüm seçenekleri taradım.

**Herkesin Kaçırdığı Nokta:** Çoğu kişi "Meta ajanı" deyince sadece chatbot yapmayı düşünüyor. Ama Meta Graph API + MCP server kombinasyonu ile neredeyse tüm iş süreçlerini otomatize edebilirsin — reklam kampanyası oluşturma, müşteri segmentasyonu, hatta finansal raporlama bile. Tek gereken bir API erişimi ve 15 dakika n8n.

---

## 2. Bulunan Yapılmış Ajanslar ve Linkler

### NotFair — 2849 Yıldız (En Popüler AI Agent Toolkit)

| Özellik | Değer |
|---------|-------|
| **GitHub** | [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) |
| **Dil** | TypeScript |
| **Kapsam** | SEO, GEO, Google Ads, Meta Ads — Claude Code ile tümü yönetilebilir |
| **Maliyet** | Ücretsiz (açık kaynak) |
| **Platform** | Claude Code |

**Ne iş yapıyor:** Claude Code'a reklam analizi, kampanya oluşturma, A/B test karşılaştırması, SEO optimizasyonu yaptırabilirsin. Tek komutla tüm Meta Ads operasyonlarını AI'a devredersin.

### google-meta-ads-ga4-mcp — 1009 Yıldız (En Kapsamlı)

| Özellik | Değer |
|---------|-------|
| **GitHub** | [irinabuht12-oss/google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) |
| **Dil** | Python |
| **Kapsam** | 250+ araç — kampanya yönetimi, analitik, GA4 entegrasyonu |
| **Uyumlu** | ChatGPT, Claude, Cursor, n8n, Windsurf |
| **Maliyet** | Ücretsiz (açık kaynak) |

**Ne iş yapıyor:** Meta Ads + Google Ads + GA4'ü tek bir MCP server'dan yönet. n8n workflow'larına entegre et — kampanya oluşturma, durdurma, bütçe değiştirme, performans raporlama.

### Meta MCP Server — 15 Yıldız (Resmi En Kapsamlı)

| Özellik | Değer |
|---------|-------|
| **GitHub** | [oliverames/meta-mcp-server](https://github.com/oliverames/meta-mcp-server) |
| **Dil** | TypeScript |
| **Kapsam** | 200+ araç — Facebook Pages, Instagram, Threads, Ads Manager, Commerce, Conversions API, Audiences, Insights, Ad Library |
| **Maliyet** | Ücretsiz (açık kaynak) |

### Markifact MCP — 40 Yıldız (Çoklu Platform)

| Özellik | Değer |
|---------|-------|
| **GitHub** | [markifact/markifact-mcp](https://github.com/markifact/markifact-mcp) |
| **Dil** | Shell |
| **Kapsam** | Google Ads, Meta Ads, GA4, TikTok Ads, LinkedIn Ads — 300+ araç |
| **Özellik** | Human-in-the-loop on every write |
| **Uyumlu** | Claude, ChatGPT, Gemini, Cursor |

### Social Flow — 144 Yıldız (Ajanslar İçin)

| Özellik | Değer |
|---------|-------|
| **GitHub** | [vishalgojha/social-flow](https://github.com/vishalgojha/social-flow) |
| **Dil** | Python |
| **Kapsam** | Facebook, Instagram, WhatsApp, Ads Manager kontrol plane |
| **Maliyet** | Ücretsiz (açık kaynak) |
| **Hedef Kitle** | Ajanslar, growth ekipleri |

---

## 3. Adım Adım Yapım Rehberi — Kendi Meta AI Ajanını Yap

### Ajan Tipi: Instagram → WhatsApp Sipariş Bot (Kullanıcının Stack'i)

**Kullanılan Teknoloji:** n8n + Claude Code + Instagram Graph API + WhatsApp Business API

**Adımlar:**

**1. Instagram DM Trigger (Instagram Graph API)**
```n8n
Webhook Trigger (Instagram DM geldiğinde)
↓
n8n-MCP-Server → Claude Code
↓
"Bu mesajı analiz et: sipariş mi, şikayet mi, sorgulama mı?"
```

**2. Claude Code Karar Verir**
```
Eğer "sipariş" kelimesi varsa:
  → WhatsApp Business API'ye sipariş onay mesajı gönder
  → DB'ye sipariş kaydet
  → Stok kontrolü yap
Eğer "şikayet" kelimesi varsa:
  → Destek ekibine bildirim
  → Şikayet kaydı oluştur
Eğer "fiyat/sorgu" kelimesi varsa:
  → Ürün bilgisi çek
  → WhatsApp'dan bilgi gönder
```

**3. WhatsApp ile Takip**
```
Sipariş onaylandı → 1 saat sonra "hazırlanıyor" mesajı
Kargo çıktı → 24 saat sonra kargo takip mesajı
Teslimattan 72 saat sonra → "Memnuniyetiniz bizim için önemli" mesajı
```

### Ajan Tipi: Reklam Performans Asistanı

**Kullanılan Teknoloji:** Claude Code + google-meta-ads-ga4-mcp

**1. MCP Server Kurulumu**
```bash
# n8n'de MCP server node'u ekle
# URL: https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp
# Token: Meta developer access token
```

**2. Claude Code'a Sor**
```
"Son 7 günde hangi reklam setlerim düşük ROAS gösterdi?
 Önerilerin neler? Türkçe raporla."
```

**3. AI Yanıt Verir**
```
"Rapor:
- Düşük performans: Interest targeting, 25-34 kadın, İstanbul
- Öneri: Advantage+ AI'a geç veya creative test yap
- Fırsat: %15 daha düşük CPA ile aynı sonuç alınabilir"
```

### Ajan Tipi: Haftalık Meta Raporlama Botu

**Kullanılan Teknoloji:** Social Flow + n8n + Claude Code

```n8n
Schedule: Her Pazartesi 09:00
↓
Social Flow API → Geçen hafta Meta Ads verilerini çek
↓
Claude Code → Verileri analiz et, Türkçe rapor yaz
↓
WhatsApp Business API → Raporu pazarlama ekibine gönder
```

---

## 4. Meta Graph API Kullanımı — Referans

### WhatsApp Business API

- **Endpoint:** `graph.facebook.com/v18.0`
- **Kullanım:** Mesaj gönder/al, şablon yönetimi, müşteri bilgileri
- **Rate Limit:** ~1000 mesaj/gün (standart), yükseltilebilir
- **Dokümantasyon:** [developers.facebook.com/docs/whatsapp](https://developers.facebook.com/docs/whatsapp)

### Instagram Graph API

- **Endpoint:** `graph.facebook.com/v18.0`
- **Kullanım:** Post paylaşımı, DM yanıtlama, yorum yönetimi, story
- **Dokümantasyon:** [developers.facebook.com/docs/instagram](https://developers.facebook.com/docs/instagram)

### Meta Ads API

- **Endpoint:** `graph.facebook.com/v18.0/act_{ad_account_id}`
- **Kullanım:** Kampanya oluşturma, hedefleme, bütçe yönetimi
- **Dokümantasyon:** [developers.facebook.com/docs/marketing-apis](https://developers.facebook.com/docs/marketing-apis)

---

## 5. Herkesin Kaçırdığı Nokta #1 — Meta Ajansı = Reklam Değil, Tüm İş Süreci

**Herkes ne düşünüyor?** "Meta ajanı = reklam optimizasyonu veya chatbot."

**Ama gerçekte ne var?** Meta Graph API ile şunlar da yapılabilir:
- Instagram'da yeni yorum → otomatik olarak ürün sayfasına yönlendirme
- WhatsApp'tan gelen sipariş → ERP'ye kaydet → stok güncelle → muhasebe yazılımına fatura kes
- Facebook Page'te yeni olumsuz yorum → Slack'e bildirim → müşteri hizmetleri devreye girsin

Tüm bu süreçler n8n + Meta API + Claude Code ile 15-30 dakikada kurulur.

---

## 6. Herkesin Kaçırdığı Nokta #2 — MCP Server ile n8n'e Gelen "Superpowers"

**Herkes ne yapıyor?** n8n'de Meta entegrasyonu için hazır node'ları kullanıyor.

**Ama gerçekte ne var?** google-meta-ads-ga4-mcp (1009 ⭐) veya Meta MCP Server (200+ araç) ile n8n'e bağlanınca:
- Sadece "mesaj gönder" değil, 250+ farklı işlem yapılabilir
- "Tüm reklam kampanyalarımın optimal performans gösteren targeting'lerini bul" gibi karmaşık sorgular
- Doğal dil ile Meta operasyonları

---

## 7. Kaynaklar

- [NotFair](https://github.com/nowork-studio/NotFair) (2849 ⭐)
- [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) (1009 ⭐)
- [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) (987 ⭐)
- [Meta MCP Server](https://github.com/oliverames/meta-mcp-server) (15 ⭐)
- [Markifact MCP](https://github.com/markifact/markifact-mcp) (40 ⭐)
- [Social Flow](https://github.com/vishalgojha/social-flow) (144 ⭐)
- [Meta Developers Dokümantasyon](https://developers.facebook.com/)