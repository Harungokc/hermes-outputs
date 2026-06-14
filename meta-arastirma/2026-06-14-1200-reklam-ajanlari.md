# Meta Araştırma — Reklam Ajans Araçları
**Tarih:** 2026-06-14 12:00
**Session:** Meta Platform Araştırması — Her 6 Saatte Bir

---

## 1. Özet

Meta reklam ajansları 2026'da tamamen AI-first yaklaşıma geçti. Meta'nın kendi Advantage+ AI'ı kampanya optimizasyonunu neredeyse tamamen otomatikleştirirken, üçüncü parti platformlar (AdEspresso, Madgicx, Revealbot) AI katmanları ekleyerek farklılaşıyor. Açık kaynak tarafta ise MCP server'lar (Model Context Protocol) ile Claude, Cursor, ChatGPT gibi AI asistanları doğrudan Meta Ads'e bağlanabiliyor — bu 2026'ın en önemli gelişmesi.

**Herkesin Kaçırdığı Nokta:** Çoğu reklamcı hâlâ "AI reklam optimizasyonu" deyince sadece Advantage+'ı düşünüyor. Ama asıl devrim, açık kaynak MCP server'larla kendi AI ajanını inşa etmek. 2849 yıldızlı NotFair repo'su, Claude Code ile Meta Ads yönetimini tamamen devrimine uğratıyor.

---

## 2. Bulunan Araçlar ve Linkler

### Ticari Reklam Otomasyon Platformları

| Platform | Fiyat | Özellikler |
|----------|-------|------------|
| [AdEspresso](https://adespresso.com/) | $49/ay~ | Facebook/Instagram/Google Ads yönetimi, A/B test, otomatik optimizasyon |
| [Madgicx](https://madgicx.com/) | $99/ay~ | AI destekli reklam optimizasyonu, creative analysis,Audience test |
| [Revealbot](https://revealbot.com/) | $50/ay~ | Otomatik kural tabanlı reklam yönetimi |
| [Sprout Social](https://sproutsocial.com/) | $249/ay~ | Sosyal medya + reklam yönetimi, analitik |

### Açık Kaynak MCP Server'lar — 2026'ın Yükselen Yıldızları

| Araç | Yıldız | Dil | Açıklama |
|------|--------|-----|----------|
| [NotFair](https://github.com/nowork-studio/NotFair) | 2849 ⭐ | TypeScript | Claude Code için SEO, GEO, Google Ads, Meta Ads skill'leri |
| [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | 1009 ⭐ | Python | 250+ araç — kampanya yönetimi, analitik, optimizasyon |
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 987 ⭐ | Python | Facebook/Instagram Ads MCP server |
| [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) | 364 ⭐ | Shell | Claude Code için Meta Ads Analyzer skill |
| [Markifact MCP](https://github.com/markifact/markifact-mcp) | 40 ⭐ | Shell | Google Ads, Meta Ads, GA4, TikTok, LinkedIn Ads — 300+ araç |
| [Social Flow](https://github.com/vishalgojha/social-flow) | 144 ⭐ | Python | Meta operasyonları için kontrol plane |

### CLI & Automation Araçları

| Araç | Yıldız | Dil | Açıklama |
|------|--------|-----|----------|
| [meta-ads-cli](https://github.com/attainmentlabs/meta-ads-cli) | 25 ⭐ | Python | Terminalden Meta Ads kampanya yönetimi |
| [FaceBook-Ad-Manager-System](https://github.com/Awaisali36/FaceBook-Ad-Manager-System) | 19 ⭐ | Python | Uçtan uca AI otomasyon — üretim ready reklam üretimi |

---

## 3. Açık Kaynak Alternatifler — Detaylı İnceleme

### NotFair — 2849 Yıldız (En Popüler)

Claude Code ile çalışan açık kaynak reklam otomasyon skill'leri. Meta Ads, Google Ads, SEO, GEO'yu tek bir araçta birleştiriyor.

**Özellikler:**
- Claude Code'a reklam analizi yaptırma
- Kampanya oluşturma, durdurma, bütçe değiştirme
- A/B test sonuçlarını karşılaştırma
- SEO + GEO entegrasyonu

**Kullanım:**
```bash
# Claude Code'a install et
claude code install skill https://github.com/nowork-studio/NotFair
# Reklam analizi yap
claude "Meta Ads kampanyamın son 7 günlük performansını analiz et"
```

### google-meta-ads-ga4-mcp — 1009 Yıldız

n8n, Windsurf, Cursor, ChatGPT, Claude ile çalışan 250+ araçlık MCP server.

**Özellikler:**
- Kampanya oluşturma/düzenleme/silme
- Hedef kitle analizi ve segmentasyon
- Bütçe optimizasyonu
- GA4 entegrasyonu ile tam funnel analizi
- Performans raporlama

**Kullanım:**
```python
# n8n'de MCP server bağlantısı
# Meta Ads kampanyası oluştur
mcp__meta_ads__create_campaign({
  name: "Yaz Indirimi 2026",
  objective: "CONVERSIONS",
  daily_budget: 500,
  targeting: { age_min: 25, age_max: 45, locations: ["Turkey"] }
})
```

### meta-ads-mcp — 987 Yıldız

Sadece Meta (Facebook + Instagram) odaklı, Python tabanlı MCP server.

**Özellikler:**
- Hafif ve hızlı
- Facebook Pages + Instagram hesap yönetimi
- Ad set ve campaign management
- Performans metrikleri çekme

---

## 4. Meta'nın Kendi Araçları — Advantage+ AI

### Advantage+ AI Nedir?

Meta'nın tamamen AI destekli reklam optimizasyon sistemi. Reklam verenin sadece hedefini (dönüşüm, satış, trafik) ve bütçesini belirtmesi yeterli — AI hedefleme, placement, creative ve zamanlamayı kendi seçiyor.

**Avantajları:**
- Minimal setup — sadece hedef + bütçe
- Learning Phase'i AI yönetiyor
- Cross-device takip otomatik
- Dynamic creative optimizasyonu

**Dezavantajları:**
- Kontrol minimal — hedefleme üzerinde sınırlı yetki
- Black box — neden belirli sonuçlar aldığını anlamak zor
- Büyük bütçelerde riskli (yanlış öğrenme = büyük kayıp)

### Advantage+ AI Gerçek Sonuçlar (2026)

- Ortalama ROAS artışı: %15-30
- Cost per acquisition düşüşü: %10-20
- Creative fatigue süresi uzadı: 2x
- En başarılı: E-ticaret, lead generation

---

## 5. Herkesin Kaçırdığı Nokta #1 — MCP Server'lar ile "AI Reklam Uzmanı"

**Herkes ne yapıyor?** Reklam optimizasyonu için ya manuel çalışıyor ya da pahalı SaaS platformlarına bağlanıyor.

**Ama gerçekte ne var?** google-meta-ads-ga4-mcp (1009 ⭐) gibi açık kaynak MCP server'lar ile kendi AI reklam uzmanını oluşturabilirsin:
- "Dün hangi reklamlar düşük performans gösterdi?"
- "Aynı hedeflemeyle yeni bir A/B test başlat"
- "Haftalık raporu Türkçe olarak özetle"

Bu soruları normalde bir reklam danışmanına sormak aylık $500-2000'e mal oluyor. MCP server ile ücretsiz.

---

## 6. Herkesin Kaçırdığı Nokta #2 — meta-ads-analyzer ile Learning Phase'i Anlama

**Herkes ne zannediyor?** Meta reklamlarında "Learning Phase" geçici bir süreç, performans düşüklüğü normal.

**Ama gerçekte ne var?** Learning Phase'deki davranış, kampanyanın tüm hayat döngüsünü belirliyor. mathiaschu/meta-ads-analyzer (364 ⭐) ile Learning Phase'i profesyonelce analiz edip:
- Optimal event sayısı (50+ conversion/event)
- Learning Phase süresi tahmini
- Hangi kombinasyonların başarılı olduğu

---

## 7. Kaynaklar

- [NotFair - nowork-studio](https://github.com/nowork-studio/NotFair) (2849 ⭐)
- [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) (1009 ⭐)
- [meta-ads-mcp - pipeboard-co](https://github.com/pipeboard-co/meta-ads-mcp) (987 ⭐)
- [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) (364 ⭐)
- [Markifact MCP](https://github.com/markifact/markifact-mcp) (40 ⭐)
- [Social Flow](https://github.com/vishalgojha/social-flow) (144 ⭐)
- [Madgicx](https://madgicx.com/) — Ticari platform
- [AdEspresso](https://adespresso.com/) — Ticari platform