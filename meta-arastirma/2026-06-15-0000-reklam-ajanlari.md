# Meta Reklam Ajansları Araştırması
**Tarih:** 2026-06-15 00:00
**Kaynak:** Bing News, GitHub, Meta Developers

---

## 1. Özet Tablo

| Araç | Platform | Yıldız | Ücret | Kapsam |
|------|----------|--------|-------|--------|
| NotFair | Claude Code | 2850 ⭐ | Ücretsiz | Meta Ads + SEO + GEO |
| google-meta-ads-ga4-mcp | MCP Server | 1010 ⭐ | Ücretsiz | 250+ araç |
| meta-ads-mcp | MCP Server | 987 ⭐ | Ücretsiz | FB/IG Ads |
| Markifact MCP | MCP Server | 40 ⭐ | Ücretsiz | 300+ araç |
| meta-ads-analyzer | Claude Code | 365 ⭐ | Ücretsiz | Campaign diagnosis |
| AdEspresso | SaaS | - | $99+/ay | FB/IG Ads yönetimi |
| Revealbot | SaaS | - | $99+/ay | FB/IG Ads otomasyon |
| Madgicx | SaaS | - | $149+/ay | AI-powered ads |

---

## 2. Meta Ads İçin Mevcut AI Ajanslar

### Açık Kaynak Araçlar

#### NotFair (2850 ⭐) ⭐ EN POPÜLER
**GitHub:** https://github.com/nowork-studio/NotFair
**Platform:** Claude Code skill
**Kapsam:** SEO, GEO, Google Ads, Meta Ads

**Özellikler:**
- Claude Code ile doğal dilde reklam yönetimi
- Campaign oluşturma, analiz, optimizasyon
- A/B test önerileri
- Performans comparative analizi

**Kullanım:**
```bash
# Claude Code içinde
/copilot "Meta reklam kampanyamı analiz et ve optimizasyon öner"
```

#### google-meta-ads-ga4-mcp (1010 ⭐)
**GitHub:** https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp
**Platform:** MCP Server
**Kapsam:** Google Ads + Meta Ads + GA4

**Özellikler:**
- 250+ araç
- n8n, ChatGPT, Claude, Cursor, Windsurf ile çalışır
- Campaign management, analytics, optimization
- Audience targeting
- Budget allocation

#### meta-ads-mcp (987 ⭐)
**GitHub:** https://github.com/pipeboard-co/meta-ads-mcp
**Platform:** MCP Server
**Kapsam:** Facebook + Instagram Ads

**Özellikler:**
- Meta Ads API entegrasyonu
- Campaign oluşturma ve yönetimi
- Ad set ve creative management
- Performance monitoring

#### Markifact MCP (40 ⭐)
**GitHub:** https://github.com/markifact/markifact-mcp
**Platform:** MCP Server
**Kapsam:** Google + Meta + TikTok + LinkedIn Ads

**Özellikler:**
- 300+ operasyon
- Human-in-the-loop on every write
- Claude, ChatGPT, Gemini, Cursor desteği

#### meta-ads-analyzer (365 ⭐)
**GitHub:** https://github.com/mathiaschu/meta-ads-analyzer
**Platform:** Claude Code skill + MCP Server
**Kapsam:** Campaign diagnosis

**Özellikler:**
- Effect breakdown analizi
- Learning Phase diagnosis
- Campaign performance diagnosis
- Expert-level insights

### Ücretli Platformlar

#### AdEspresso
**URL:** adespresso.com
**Fiyat:** $99+/ay
**Kapsam:** Facebook + Instagram + Google Ads

**Özellikler:**
- A/B test otomasyonu
- Campaign optimization
- Automated rules
- Reporting dashboard

#### Revealbot
**URL:** revealbot.com
**Fiyat:** $99+/ay
**Kapsam:** Facebook + Instagram + Google Ads

**Özellikler:**
- Automated rules engine
- Campaign pausing/resuming
- Budget optimization
- Slack/Discord notifications

#### Madgicx
**URL:** madgicx.com
**Fiyat:** $149+/ay
**Kapsam:** Facebook + Instagram Ads

**Özellikler:**
- AI-powered audience discovery
- Automated creative testing
- Conversion optimization
- Real-time bidding

---

## 3. Herkesin Kaçırdığı Nokta

### #1: "Ücretsiz" + "Açık Kaynak" = Kurumsal Sonuç
Ücretli platformlar $99-149/ay. Aynı işlevselliği ücretsiz alabilirsin:
- NotFair + Claude Code = kampanya analizi + optimizasyon önerileri
- meta-ads-mcp + n8n = tam otomasyonlu reklam yönetimi
- Toplam maliyet: $0 (Claude Code zaten kullanıyorsan)

### #2: MCP Server = AI Ajansının Beyni
MCP (Model Context Protocol) server'lar AI ajansının "beyni" olarak çalışıyor:
- AI → MCP Server → Meta Ads API → Kampanya güncelleme
- İnsan sadece onay veriyor (human-in-the-loop)
- 7/24 kampanya izleme + otomatik optimizasyon

### #3: "Learning Phase" Herkesin Gözden Kaçırdığı Kritik Dönem
Meta reklam kampanyaları ilk 7 gün "learning phase" geçirir. Bu dönemde:
- Herkes kampanyayı durduruyor (erken sonuç beklediği için)
- Doğru strateji: İlk 7 gün dokunma, sadece izle
- meta-ads-analyzer ile learning phase diagnosis = kritik

---

## 4. Adım Adım: Meta Ads AI Agent Kurulumu

### Gerekenler:
1. Meta Business Manager hesabı
2. Claude Code veya ChatGPT
3. MCP Server (opsiyonel)
4. n8n (opsiyonel)

### Kurulum Adımları:

**1. Meta Business Manager API Erişimi:**
```
1. business.facebook.com → Business Settings
2. Users → Add → AI agent için yeni kullanıcı
3. Permissions → Ads Management + Analytics
4. API Token oluştur
```

**2. NotFair Kurulumu (Claude Code):**
```bash
# Claude Code içinde
/claude-code skills install NotFair
```

**3. MCP Server Kurulumu (meta-ads-mcp):**
```bash
# n8n MCP Server node
npm install -g @pipeboard/meta-ads-mcp
```

**4. AI Agent Prompt Örneği:**
```
"Bana Meta reklam kampanyamın son 30 günlük performansını analiz et.
Hangi ad set'ler iyi performans gösteriyor? 
Hangi kreativler düşük CTR'a sahip?
Önerdiğin A/B testleri listele."
```

---

## 5. Kaynaklar

- [NotFair GitHub](https://github.com/nowork-studio/NotFair)
- [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)
- [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)
- [Markifact MCP](https://github.com/markifact/markifact-mcp)
- [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)
- [AdEspresso](https://adespresso.com)
- [Madgicx](https://madgicx.com)

---

## 6. LinkedIn Post Fikri

**Başlık:** $149/ay reklam aracı yerine $0'a aynı işi yapan açık kaynak araçları keşfettim

**Post:**
> Reklam ajansları için AI araçları pahalı.
>
> AdEspresso: $99/ay
> Madgicx: $149/ay
> Revealbot: $99/ay
>
> Ama aynı işlevselliği ücretsiz alabilirsin:
>
> ⭐ NotFair (2,850 yıldız) — Claude Code ile Meta Ads analizi
> ⭐ google-meta-ads-ga4-mcp (1,010 yıldız) — 250+ araç
> ⭐ meta-ads-mcp (987 yıldız) — FB/IG Ads MCP server
>
> Toplam: $0
>
> Kurulum: 15 dakika
> Sonuç: Kurumsal düzeyde kampanya optimizasyonu
>
> Bir kampanyayı "durdur" mu yoksa "sürdür" mü diye saatlerce düşünüyorsan, AI ajanına sor. 7/24 çalışıyor, ücret istemiyor.
>
> Siz hangi reklam aracını kullanıyorsunuz?

**Görsel önerisi:** Fiyat karşılaştırma tablosu — ücretli platformlar vs açık kaynak alternatifler

**#MetaAds #Reklam #Otomasyon #AI #AçıkKaynak
