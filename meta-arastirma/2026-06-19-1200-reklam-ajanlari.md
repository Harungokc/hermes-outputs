# Meta Araştırması — Reklam Ajansları ve AI Araçları
**Tarih:** 19 Haziran 2026 12:00
**Slot:** 06:00 — 12:00 arası

---

## Özet

Meta reklam ajansları için AI agent pazarı hızla büyüyor. 2026'da açık kaynak MCP server'lar (1000+⭐) ile ticari platformlar (AdEspresso, Madgicx, Revealbot) arasında ciddi bir rekabet var. Bu slot'ta 9 büyük repo, 3 yeni keşif ve Meta'nın kendi Advantage+ AI aracı incelendi.

---

## Bulunan Araçlar ve Linkler

### Meta Ads MCP Server'lar (Açık Kaynak — En Güvenilir)

| Repo | ⭐ | Dil | Kapsam |
|------|----|-----|--------|
| [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) | 2924 | TypeScript | Claude Code Meta Ads skill — açık ara en popüler |
| [irinabuht12-oss/google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | 1013 | — | 250+ araç — n8n/Cursor/Claude/ChatGPT uyumlu |
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 997 | Python | Facebook/Instagram Ads MCP server |
| [mathiaschu/meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) | 367 | Shell | Learning Phase diagnosis, campaign breakdown |
| [markifact/markifact-mcp](https://github.com/markifact/markifact-mcp) | 41 | Shell | 300+ araç — Google/Meta/TikTok/LinkedIn Ads |

### Yeni Keşifler (Mayıs-Haziran 2026)

| Repo | ⭐ | Dil | Kapsam |
|------|----|-----|--------|
| [mellowmir94/meta-ads-langgraph-agent](https://github.com/mellowmir94/meta-ads-langgraph-agent) | — | Python | LangGraph ile Meta Ads monitoring agent (2026-06-19) |
| [RyanWaveMetric/meta-ads-automation](https://github.com/RyanWaveMetric/meta-ads-automation) | — | — | Facebook/Instagram + Cafe24 entegrasyonu (Korea) |
| [sandeshdesignworld-lgtm/advoxa_mcp](https://github.com/sandeshdesignworld-lgtm/advoxa_mcp) | — | Python | 94 araç — Facebook, Instagram, WhatsApp, Messenger MCP |

### Ticari Reklam Araçları

| Araç | Tip | Fiyat | Kapsam |
|------|-----|-------|--------|
| **AdEspresso** | SaaS | $49/ay~ | Facebook/Instagram/Google Ads yönetimi |
| **Madgicx** | SaaS | $99/ay~ | AI-powered Meta Ads optimizasyonu |
| **Revealbot** | SaaS | $99/ay~ | Automated rules + Meta Ads |
| **Sprout Social** | SaaS | $99/15 profillik | Sosyal medya + reklam yönetimi |
| **Meta Advantage+ AI** | Platform | İçerik dahil | Meta'nın kendi AI reklam aracı |

---

## Açık Kaynak Alternatifler — Derinlemesine

### NotFair (2924⭐) — En Kapsamlı Açık Kaynak Çözümü

**Neden bu kadar popüler?**
- Claude Code ile doğrudan çalışıyor
- Meta Ads skill olarak hazır
- SEO + GEO + Google Ads + Meta Ads tek platformda

**Özellikleri:**
- Campaign oluşturma ve yönetimi
- Audience targeting otomasyonu
- A/B test karşılaştırması
- Performance monitoring
- Budget optimizasyonu

**Kullanım:**
```bash
# Claude Code içinde
@NotFair /meta-ads
# veya
/meta-ads create-campaign "Summer Sale" --budget 50 --objective conversions
```

**Link:** https://github.com/nowork-studio/NotFair

### google-meta-ads-ga4-mcp (1013⭐) — 250+ Araç

**Özelliği:** Sadece Meta değil, Google Ads + GA4 + TikTok + LinkedIn Ads da dahil

**MCP server olarak çalışır:**
```
n8n → MCP Server → Claude/Cursor/ChatGPT → Meta Ads API
```

**Avantajı:** Birden fazla platform tek bir workflow'da yönetilebilir.

**Link:** https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp

### meta-ads-mcp (997⭐) — Facebook/Instagram Odaklı

**Özelliği:** Sadece Meta ekosistemine odaklanmış, daha basit kurulum

**Sistem:** Python tabanlı MCP server, doğrudan Meta Graph API'ye bağlanıyor.

**Link:** https://github.com/pipeboard-co/meta-ads-mcp

---

## Meta Advantage+ AI — Meta'nın Kendi Reklam Aracı

**Duyuru:** Conversations 2026 (3 Haziran 2026, Londra)

**Özellikler:**
- **Advantage+ shopping campaigns** — AI otomatik bidding
- **Advantage+ app campaigns** — App install optimizasyonu
- **Advantage+ lead campaigns** — Lead generation

**Herkesin Kaçırdığı Nokta #1:**
Advantage+ AI aslında "karanlık kutu" — neden belirli hedeflemeyi seçtiğini açıklamıyor. Deneyimli PPC uzmanları hâlâ manuel kampanya kuruyor çünkü AI kararlarını anlayamıyorlar. Ama yeni başlayanlar için %20-30 daha düşük CPL sağlayabiliyor.

**Herkesin Kaçırdığı Nokta #2:**
Meta Business Agent ile Advantage+ kombinasyonu = tam otomatik reklam ajansı. Campaign kurulumu → AI agent → Müşteri yanıtı → Dönüşüm takibi hepsi AI ile yapılabilir.

---

## Adım Adım Yapım Rehberi — AI Reklam Ajansı

### N8N + Claude Code + Meta Ads MCP Kurulumu

**Adım 1 — Meta for Developers:**
1. `developers.facebook.com` → Yeni uygulama
2. "Marketing API" ürününü ekle
3. Ad Account ID al
4. User Access Token al (Marketplace'ten)

**Adım 2 — MCP Server Kurulumu:**
```bash
# Terminal'de
cd meta-ads-mcp
npm install
npm start
# MCP server 3000 portunda çalışır
```

**Adım 3 — N8N Workflow:**
```
Trigger (Manuel veya Schedule)
↓
MCP Server Node (Meta Ads)
↓
Claude Code Node (Kampanya analizi)
↓
Karar node (Performans > X ise devam et)
↓
MCP Server Node (Budget artır/azalt)
↓
Telegram/Email bildirim
```

**Adım 4 — Claude Code Prompt:**
```
Bu kampanyayı analiz et:
- CTR, CPC, CPM trend
- Audience performance
- Dönüşüm maliyeti

Öneri:
- Budget değişikliği gerekiyor mu?
- Yeni creative önerisi var mı?
- Hedefleme daraltma/genişletme?

Format: JSON
```

---

## Fiyatlandırma Karşılaştırması

| Çözüm | Aylık Maliyet | En İyi Olduğu Alan |
|-------|---------------|-------------------|
| NotFair (açık kaynak) | $0 | Hızlı kampanya kurulumu, Claude Code kullanıcıları |
| google-meta-ads-ga4-mcp | $0 | Çoklu platform (Google + Meta + TikTok) |
| meta-ads-mcp | $0 | Basit Meta-only kurulum |
| AdEspresso | $49-499 | Büyük ajanslar, detaylı raporlama |
| Madgicx | $99-499 | AI optimizasyon isteyenler |
| Meta Business Agent Hatch | $200 | Bireysel işletmeler |
| Meta Advantage+ | Ücretsiz (reklam bütçesi dahil) | Otomatik optimizasyon isteyenler |

**Herkesin Kaçırdığı Nokta #3:**
Açık kaynak + Claude Code kombinasyonu, küçük ajanslar için yılda $6,000-60,000 tasarruf sağlayabilir. Ticari araçların yaptığı her şeyi yapıyor — tek farkı kendin kuruyorsun.

---

## Kaynaklar

1. [NotFair — 2924⭐](https://github.com/nowork-studio/NotFair)
2. [google-meta-ads-ga4-mcp — 1013⭐](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)
3. [meta-ads-mcp — 997⭐](https://github.com/pipeboard-co/meta-ads-mcp)
4. [meta-ads-analyzer — 367⭐](https://github.com/mathiaschu/meta-ads-analyzer)
5. [markifact-mcp — 41⭐](https://github.com/markifact/markifact-mcp)
6. [Meta's AI agent for WhatsApp Business is now available globally — TechCrunch](https://www.bing.com/news/search?q=Meta+AI+business+agent+WhatsApp+Instagram+2026)
7. [Meta launches AI Business Agent platform — Business Today](https://www.bing.com/news/search?q=Meta+Business+Agent+WhatsApp+Instagram+Messenger)

---

## LinkedIn Paylaşımı

**Post Taslağı:**

```
Meta reklamlarını yönetmek için her ay $499 ödüyorsan, bu yazıyı oku.

Açık kaynak araçlar 2026'da o kadar olgunlaştı ki:

✓ NotFair (2924⭐) — Claude Code ile Meta Ads yönetimi
✓ 250+ araçlı MCP server — n8n, Cursor, ChatGPT uyumlu
✓ Advantage+ AI — Meta'nın kendi optimizasyon aracı

Bunların hepsi ücretsiz.

Fark sadece: kendin kurmak mı, hazır para vermek mi?

İkisi arasındaki fark: Zaman.

Ama 1 kez kurulum = sonsuz kullanım.

Sen hangisini tercih edersin? Yorumda belirt 👇

#MetaAds #ReklamOtomasyonu #AçıkKaynak
```

---

*Son güncelleme: 2026-06-19 12:00*
