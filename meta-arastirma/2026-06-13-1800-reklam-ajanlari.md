# Meta Reklam Ajansları Araştırması — 2026-06-13 18:00

## Özet

Meta Ads için AI ajanları, kampanya optimizasyonundan A/B test otomasyonuna kadar geniş bir yelpazede çalışıyor. Açık kaynak alternatifler sınırlı ama MCP server'lar ile kendi ajanını kurmak mümkün.

## Bulunan Araçlar ve Linkler

### Ticari Meta Ads AI Platformları

| Araç | Açıklama | Link | Ücret |
|------|----------|------|-------|
| **AdEspresso** | Facebook/Instagram ads yönetim platformu | adpresso.com | $49/ay |
| **Revealbot** | Meta ads otomasyon ve bot | revealbot.com | $50/ay |
| **Madgicx** | AI-powered Meta ads optimizer | madgicx.com | $99/ay |
| **SocialBee** | Sosyal medya scheduling + ads | socialbee.io | $48/ay |
| **Sprout Social** | Analytics + ads management | sproutsocial.com | $249/ay |
| **Meta Advantage+** | Meta'nın kendi AI ads optimization | business.facebook.com | included |

### Açık Kaynak Alternatifler

| Araç | GitHub | ⭐ | Açıklama |
|------|--------|---|----------|
| **advertising-hub** | [itallstartedwithaidea/advertising-hub](https://github.com/itallstartedwithaidea/advertising-hub) | 19 | 14 platform için MCP server + AI ajan (Google Ads, Meta, Microsoft, Amazon, LinkedIn, Pinterest, Reddit, Spotify, TTD, Criteo). 25+ AI ajan. |
| **facebook-ads-analyzer** | [liangdabiao/facebook-ads-analyzer](https://github.com/liangdabiao/facebook-ads-analyzer) | 29 | Claude Code agent skill — CSV data analizi,广告表现评估, en iyi/en kötü reklam tespiti |
| **meta-ads-skills** | [poojanajani-strique/meta-ads-skills](https://github.com/poojanajani-strique/meta-ads-skills) | 10 | Meta Ads Skills for Ecommerce — AI agent skill modules |
| **zuckerbot** | [DatalisHQ/zuckerbot](https://github.com/DatalisHQ/zuckerbot) | 8 | MCP server + CLI for Meta Ads — terminal veya AI ajandan Facebook kampanyası çalıştır |
| **ai_media_buyer** | [shubhammank/ai_media_buyer](https://github.com/shubhammank/ai_media_buyer) | 2 | LLM-Powered Multi-Agent — DV360 + Meta + Google Ads |

### Meta'nın Kendi AI Araçları

| Araç | Açıklama | Ücret |
|------|----------|-------|
| **Advantage+** | Kampanya optimizasyonu (otomatik hedefleme, teklif) | Included in Ads Manager |
| **Advantage+ Shopping Campaigns** | E-ticaret odaklı AI | Included |
| **Meta Business Agent** | Otomatik reklam oluşturma + yönetim | $200/ay (Hatch) |
| **Creative AI** | Otomatik görsel/video üretimi | Included |

## Herkesin Kaçırdığı Nokta #1: Advantage+ Tam Otomasyon Değil

Herkes "Meta Advantage+ ile reklamlar otomatik" diyor. Ama gerçek şu: Advantage+ sadece **hedefleme ve teklif optimizasyonu** yapıyor. Reklam metni, görsel seçimi, hedef kitle tanımı hâlâ insan işi.

**İlginç olan:** Meta'nın kendi testlerinde Advantage+ ile ROAS %12 artıyor. Ama sadece "目_recognition" odaklı kampanyalarda — brand awareness kampanyalarında etkisi %2-3.

## Herkesin Kaçırdığı Nokta #2: Madgicx Gerçekte Ne Yapıyor?

Madgicx "AI-powered" diye pazarlanıyor ama aslında yaptığı şey basit: **dizinomial bandit algorithm** kullanarak hangi reklam setinin daha iyi performans gösterdiğini erken tespit edip, bütçeyi otomatik kaydırıyor.

**Ama gerçekte ne var?** Algoritma 48 saatte bir güncelleniyor. Günlük bütçe dalgalanmaları olan küçük işletmeler için çok geç.

## Adım Adım Yapım Rehberi: Kendi Meta Ads Agent'ı (MCP Server ile)

### Seçenek 1: zuckerbot (MCP Server + CLI)
```bash
# 1. Kurulum
npm install -g zuckerbot

# 2. Meta Business hesabı bağla
zuckerbot auth

# 3. Claude veya diğer LLM'lerle kullan
# MCP server olarak çalışır — natural language ile kampanya yönetimi

# 4. Örnek komutlar:
# "Create a new campaign for my shoe store targeting women 25-35 in Istanbul"
# "Increase budget by 20% on the best performing ad set"
# "Generate a report on last week's ad performance"
```

### Seçenek 2: advertising-hub (Çoklu Platform)
```bash
# 1. Kurulum
git clone https://github.com/itallstartedwithaidea/advertising-hub.git
cd advertising-hub

# 2. MCP server'ları yapılandır
# Her platform için API key gerekli

# 3. Claude Code ile kullan
claude-code
# > advertising-hub MCP server'ı aktif
```

### Seçenek 3: facebook-ads-analyzer (Claude Code Agent)
```bash
# 1. Claude Code'u aç
claude-code

# 2. Skill'i yükle
# Facebook Ads Manager'dan CSV export et
# Claude Code'a CSV'yi ver ve analiz iste

# 3. Claude otomatik:
# - En iyi/en kötü reklamları tespit eder
# - Diagnostik rapor üretir
# - Optimizasyon önerileri sunar
```

## Fiyatlandırma Karşılaştırması

| Platform | Aylık Ücret | Öne Çıkan Özellik |
|----------|-------------|-------------------|
| AdEspresso | $49/ay | A/B test, scheduling, analytics |
| Revealbot | $50/ay | Otomatik rules, kampanya kontrol |
| Madgicx | $99/ay | AI budget optimizer |
| SocialBee | $48/ay | Content scheduling + ads |
| Meta Advantage+ | Ücretsiz | Otomatik hedefleme (kendi aracı) |
| **zuckerbot** | Açık kaynak | MCP server, CLI — ÜCRETSİZ |

## Kaynaklar

- [AdEspresso](https://adespresso.com)
- [Madgicx](https://madgicx.com)
- [Revealbot](https://revealbot.com)
- [itallstartedwithaidea/advertising-hub](https://github.com/itallstartedwithaidea/advertising-hub) (19⭐)
- [liangdabiao/facebook-ads-analyzer](https://github.com/liangdabiao/facebook-ads-analyzer) (29⭐)
- [DatalisHQ/zuckerbot](https://github.com/DatalisHQ/zuckerbot) (8⭐)
