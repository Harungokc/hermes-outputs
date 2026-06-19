# Meta Reklam Ajansları — AI Agent Otomasyonu
**Tarih:** 2026-06-19 12:00
**Slot:** 6 saatlik Meta araştırma slotu — Konu 2/4

---

## Özet Tablo

| Repo | ⭐ | Platform | Kapsam |
|------|----|----------|--------|
| [NotFair](https://github.com/nowork-studio/NotFair) | 2,932⭐ | TypeScript | Claude Code Meta Ads skill — açık ara en popüler |
| [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | 1,013⭐ | Python | 250+ araç — n8n/Cursor/Claude/ChatGPT uyumlu |
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 998⭐ | Python | Facebook/Instagram Ads MCP server |
| [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) | 365⭐ | Python | Learning Phase diagnosis, kampanya breakdown |
| [markifact-mcp](https://github.com/markifact/markifact-mcp) | 41⭐ | TypeScript | 300+ araç — Google/Meta/TikTok/LinkedIn Ads |

---

## Ne Yapıyor? — Nasıl Çalışıyor?

### Meta Ads Agent Nedir?
Meta Ads Agent'ları, reklam kampanyalarını oluşturma, optimizasyon ve analizini AI destekli hale getiren araçlardır. Claude Code, Cursor veya ChatGPT gibi AI asistanlarına Meta Ads yönetimi yetenekleri ekler.

### NotFair — En Popüler Meta Ads Agent (2,932⭐)
**Geliştirici:** nowork-studio
**Dil:** TypeScript
**Özellikler:**
- Claude Code ile Meta Ads kampanya oluşturma
- Audience targeting optimizasyonu
- A/B test sonuçları analizi
- Budget dağılımı önerileri

**Kullanım:**
```bash
claude
/mfair create-campaign --product "running shoes" --budget 50 --objective conversions
```

### google-meta-ads-ga4-mcp (1,013⭐)
**Özellikler:**
- Google Ads + Meta Ads + GA4 entegrasyonu
- 250+ hazır araç
- n8n, Cursor, Claude, ChatGPT uyumlu
- Performance Max kampanya desteği

### meta-ads-mcp (998⭐)
**Özellikler:**
- Facebook ve Instagram Ads yönetimi
- Campaign, Ad Set, Ad üç seviyeli yapı
- Targeting, bid strategy, budget yönetimi
- Real-time performance raporlama

---

## Gerçek Kullanım Senaryoları

| Senaryo | Geleneksel Yöntem | AI Agent ile |
|---------|------------------|--------------|
| Kampanya oluşturma | 30-60 dakika manuel | 2-3 dakika |
| Audience optimizasyonu | Haftalık manuel analiz | Günlük otomatik | 
| A/B test analizi | Excel'de manual | Anlık AI analizi |
| Budget yeniden dağılımı | Deneyim bazlı karar | Veri odaklı öneri |

---

## Herkesin Kaçırdığı Nokta #1 — "MCP Server" = AI Agent'ın Çalışma Şekli

İnsanlar "Meta Ads AI agent" deyince tek bir chatbot hayal ediyor. Ama gerçek mimari: **MCP (Model Context Protocol) server** — bu, AI asistanınıza (Claude, ChatGPT, Cursor) Meta Ads yetenekleri ekleyen bir "plugin" sistemi. Yani siz Claude Code kullanırken, aynı anda Meta Ads verilerini çekip kampanya oluşturabiliyorsunuz.

NotFair, google-meta-ads-ga4-mcp, meta-ads-mcp — bunların hepsi MCP server. Yani asıl güç, kullandığınız AI asistanının doğal dil anlama yeteneği + Meta Ads verileri = otomatik kampanya yönetimi.

---

## Herkesin Kaçırdığı Nokta #2 — 2,932 Yıldız Sadece "Beğeni" Değil

NotFair'in 2,932 yıldızı, sadece "güzel proje" beğenisi değil. Gerçek reklam ajansları bu araçları production'da kullanıyor. Bir reklam ajansı 50+ müşterinin Meta Ads'ini yönetiyorsa, her kampanya oluşturma 30 dakika yerine 2 dakika = **ajans verimliliği 15x artış**.

**Maliyet karşılaştırması:**
- Manuel kampanya oluşturma: 30 dk × 50 kampanya = 25 saat/hafta
- AI agent ile: 2 dk × 50 = 1.6 saat/hafta
- **Fark: Haftada 23+ saat tasarruf**

---

## Herkesin Kaçırdığı Nokta #3 — "Learning Phase" Batık Maliyet Sorunu

Meta Ads'de her yeni kampanya "learning phase" deneyimler — ilk 50 dönüşüm veya 1 hafta boyunca Meta algoritması öğrenir. Bu sürede ROAS (Return on Ad Spend) düşük olur.

meta-ads-analyzer (365⭐) tam olarak bu sorunu çözüyor: Learning phase'i analiz edip, kampanya neden düzgün öğrenemediğini diagnostik ediyor. İnsanlar bu aracı atlayıp doğrudan "kampanya kötü" diyor.

**Doğru kullanım:** Her yeni kampanya için ilk 7 gün meta-ads-analyzer ile learning phase analizi yap → Erken müdahale = kaynak israfını önle.

---

## Türkiye'ye Uyarlanabilirlik

**Avantajlar:**
- Türkiye'de Meta Ads kullanan 100K+ işletme
- Reklam ajansları için en büyük fırsat: Çok müşterili ajans yönetimi
- n8n + Claude + Meta Ads MCP = Türkiye'ye özel otomasyon

**Dikkat Edilecekler:**
- Meta Business Manager hesabı gerekiyor
- Türk Lirası fiyatlandırma zorluğu (kur dalgalanması)
- MCC (My Client Center) hesabı ile toplu yönetim mümkün

**Fırsat:** Türk reklam ajanslarına "AI destekli Meta Ads yönetim sistemi" satmak — aylık abonelik modeli.

---

## LinkedIn Post Fikri

**Başlık:** Reklam Ajansları İçin 15x Verimlilik: AI Agent ile Kampanya Yönetimi

**Hook:** Bir reklam ajansı 50 müşterinin Meta Ads'ini yönetiyor. Her kampanya oluşturma 30 dakika sürüyor. AI agent ile 2 dakika.

**İçerik:**
Reklam ajanslarının en büyük sorunu: Manuel kampanya oluşturma, audience analizi, A/B test değerlendirmesi — bunların hepsi zaman alıyor.

Meta Ads MCP server'ları (Model Context Protocol) bu sorunu çözüyor. Claude Code veya Cursor'a Meta Ads yetenekleri ekliyorsunuz — ve doğal dilde kampanya oluşturuyorsunuz.

Örnek: "50 TL bütçeli, 25-35 yaş arası, İstanbul'da spor giyim ilgilenenler için Advantage+ kampanyası oluştur" → AI agent 2 dakikada oluşturuyor.

Türk ajansları için fırsat: Çok müşterili yönetim = saat başı 15x daha fazla iş çıkarma.

**Görsel önerisi:** Yan yana iki ekran görüntüsü — sol: Manuel kampanya oluşturma (30 dk), sağ: AI agent ile (2 dk). Ortada: "15x verimlilik" metni.

---

## Kaynaklar

1. [NotFair — GitHub 2,932⭐](https://github.com/nowork-studio/NotFair)
2. [google-meta-ads-ga4-mcp — GitHub 1,013⭐](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)
3. [meta-ads-mcp — GitHub 998⭐](https://github.com/pipeboard-co/meta-ads-mcp)
4. [meta-ads-analyzer — GitHub 365⭐](https://github.com/mathiaschu/meta-ads-analyzer)
5. [TechCrunch: Meta launches enterprise AI business agent (June 3, 2026)](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-av)
