# Meta Reklam Ajansları ve AI Agent Araştırması
**Tarih:** 2026-06-14 18:00  
**Slot:** Her 6 saatte bir (12:00, 18:00)

---

## 1. Özet Tablo

| Araç | Tip | Yıldız | Ücret | Kapsam |
|------|-----|--------|-------|--------|
| NotFair | Claude Code Skill | 2848⭐ | Ücretsiz | Meta + Google Ads, SEO/GEO |
| google-meta-ads-ga4-mcp | MCP Server | 1010⭐ | Ücretsiz | 250+ araç, tüm platformlar |
| meta-ads-mcp | MCP Server | 987⭐ | Ücretsiz | Meta Ads (FB + IG) |
| meta-ads-analyzer | Claude Code Skill | 365⭐ | Ücretsiz | Campaign diagnosis |
| markifact-mcp | MCP Server | 40⭐ | Ücretsiz | 300+ araç, 5 platform |
| AdEspresso | SaaS | - | $49/ay~ | Reklam yönetim platformu |
| Revealbot | SaaS | - | $49/ay~ | Otomasyon + reporting |
| Madgicx | SaaS | - | $99/ay~ | AI-powered reklam optimizasyonu |

---

## 2. Meta Ads İçin En İyi Açık Kaynak AI Agent Araçları

### NotFair (2848⭐) — En Popüler
**Link:** https://github.com/nowork-studio/NotFair

Claude Code ile çalışan açık kaynak skill set. SEO, GEO, Google Ads ve **Meta Ads** için uzmanlaşmış.

**Özellikler:**
- Campaign oluşturma ve optimizasyon
- A/B test otomasyonu
- Budget allocation
- Performance tracking

**Kullanım:**
```bash
claude —skill install nowork-studio/NotFair
```

### google-meta-ads-ga4-mcp (1010⭐)
**Link:** https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp

250+ araç içeren MCP server. n8n, Cursor, Claude, ChatGPT ile entegre çalışır.

**Özellikler:**
- Campaign management
- Analytics & reporting  
- Budget optimization
- Audience targeting
- Meta Ads + Google Ads + GA4 desteği

### meta-ads-mcp (987⭐)
**Link:** https://github.com/pipeboard-co/meta-ads-mcp

Facebook ve Instagram Ads yönetimi için özelleşmiş MCP server.

**Özellikler:**
- Campaign creation
- Ad set management
- Creative optimization
- Performance monitoring

### meta-ads-analyzer (365⭐)
**Link:** https://github.com/mathiaschu/meta-ads-analyzer

Learning Phase diagnosis ve campaign breakdown için uzmanlaşmış.

**Özellikler:**
- Effect breakdown analysis
- Learning Phase tespiti
- Campaign performance diagnosis

---

## 3. Ücretli Reklam Ajansı Platformları

### AdEspresso ($49/ay~)
Facebook, Instagram ve Google Ads için reklam yönetim platformu.
- görsel A/B test
- Otomatik budget optimizasyonu
- Reporting dashboard

### Revealbot ($49/ay~)
- Otomatik kampanya yönetimi
- Rule-based automation
- Cross-platform reporting (FB, Google, TikTok)

### Madgicx ($99/ay~)
- AI-powered audience discovery
- Automated creative testing
- Full funnel optimization

---

## 4. Herkesin Kaçırdığı Nokta

### #1: MCP Server'lar Sadece "Bağlantı" Değil
Herkes bunları sadece "API bağlantısı" olarak görüyor. Ama asıl güç: **Claude Code + MCP = Tam otonom reklam ajansı.** Campaign oluştur, optimize et, raporla — tek prompt ile.

### #2: Açık Kaynak Ücretliye Göre Daha Hızlı Güncelleniyor
Ücretli platformlar (AdEspresso, Madgicx) 2-3 ayda bir özellik ekler. Ama NotFair ve google-meta-ads-ga4-mcp **haftalık** güncelleniyor. Topluluk destekli oldukları için Meta'ın her yeni özelliğine hemen uyum sağlıyorlar.

### #3: "Learning Phase" Otomasyonu Kaçırılıyor
Meta reklamcılığının en kritik dönemi "Learning Phase" (ilk 7 gün). Bu dönemde yanlış optimizasyon = gereksiz harcam. meta-ads-analyzer tam bu dönem için tasarlanmış — ama kimse bunu kullanmıyor.

---

## 5. Adım Adım Meta Ads AI Agent Kurulumu

### Seçenek A: Claude Code + NotFair (Ücretsiz)
```
1. Claude Code kurulumu yap
2. NotFair skill'ini yükle: claude —skill install nowork-studio/NotFair
3. Meta Business hesabını bağla (access token)
4. Prompt ile campaign oluştur veya optimize et
```

### Seçenek B: n8n + MCP Server (Ücretsiz)
```
1. n8n kur (Docker veya cloud)
2. n8n-MCP server kurulumu yap
3. meta-ads-mcp veya google-meta-ads-ga4-mcp ekle
4. Workflow oluştur: Trigger → Meta Ads Action → Report
5. Zamanlamalı çalıştır veya webhook ile tetikle
```

---

## 6. Görsel Önerisi

**LinkedIn için tasarım önerisi:**
- Screenshot: n8n + MCP entegrasyonu dashboard
- Tablo: Açık kaynak vs ücretli karşılaştırması
- Renk: Mor (#8B5CF6) ve WhatsApp yeşili (#25D366) gradient

---

## 7. Kaynaklar

- [NotFair GitHub](https://github.com/nowork-studio/NotFair) (2848⭐)
- [google-meta-ads-ga4-mcp GitHub](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) (1010⭐)
- [meta-ads-mcp GitHub](https://github.com/pipeboard-co/meta-ads-mcp) (987⭐)
- [meta-ads-analyzer GitHub](https://github.com/mathiaschu/meta-ads-analyzer) (365⭐)
- [markifact-mcp GitHub](https://github.com/markifact/markifact-mcp) (40⭐)
- [AdEspresso](https://adespresso.com)
- [Madgicx](https://madgicx.com)

---

## 8. LinkedIn Post Fikri

**Başlık:** "Meta reklam ajansı tutmak yerine kendi AI ajanını kur — aylık $500 tasarruf."

**Post:**
Reklam ajansı maaşı: minimum $2,000/ay.
Açık kaynak AI ajan kurulumu: $0.

Ama asıl mesele para değil. Mesele kontrol.

NotFair + Claude Code ile:
- Campaign oluşturma → 5 dakika
- A/B test → otomatik
- Budget optimizasyonu → gerçek zamanlı
- Raporlama → her sabah e-postanda

Ücretli platformlar bunu 2-3 ayda bir güncelliyor. Açık kaynak MCP server'lar haftalık güncelleniyor.

Siz reklam yönetimini nasıl yapıyorsunuz?

#MetaAds #AIAgent #Reklam #Otomasyon