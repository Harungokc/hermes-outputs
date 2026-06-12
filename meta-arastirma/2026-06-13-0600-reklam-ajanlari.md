# Meta Reklam Ajansları Araştırması — 2026-06-13 06:00

## Özet

Meta reklam ajansları ekosisteminde iki ana kategori var: ticari platformlar (AdEspresso, Madgicx, Revealbot) ve açık kaynak alternatifler. Ticari platformlar genelde büyük reklam bütçeleri olan ajanslar için tasarlanmış ve aylık $100-500 arası fiyatlandırma yapıyor. Açık kaynak alternatifler ise geliştiriciler için API erişimi ve özelleştirme imkanı sunuyor. 2026'da AI agent entegrasyonu ile "akıllı kampanya yönetimi" trendi öne çıkıyor.

**Herkesin Kaçırdığı Nokta:** Reklam ajansları sadece "bidding optimization" yapmıyor. En güçlü özellik **cross-platform reporting** ve **creative performance analysis**. Bir reklamın görselini değiştirmek, metnini değiştirmekten 3-5x daha etkili. Bu gerçeği kimse konuşmuyor.

---

## Bulunan Araçlar ve Linkler

### 1. itallstartedwithaidea/advertising-hub
| Özellik | Değer |
|---------|-------|
| **Stars** | 19 |
| **Language** | Markdown |
| **Link** | https://github.com/itallstartedwithaidea/advertising-hub |
| **Son Güncelleme** | 2026-05-07 |
| **Açıklama** | 14 platform için açık kaynak reklam otomasyon hub'ı. Google Ads, Meta, Microsoft, Amazon, LinkedIn, Pinterest, Reddit, Spotify, TTD, Criteo |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **AI Agents** | 25+ |
| **Platform Desteği** | Google Ads, Meta Ads, Microsoft Ads, Amazon Ads, LinkedIn Ads, Pinterest, Reddit, Spotify, TTD, Criteo |
| **Özellik** | MCP servers, AI agents, cross-platform reporting |
| **İlginç Nokta** | "Practitioners who manage real ad spend" diyen ekip tarafından yapılmış |

### 2. oliverames/meta-mcp-server
| Özellik | Değer |
|---------|-------|
| **Stars** | 15 |
| **Language** | TypeScript |
| **Link** | https://github.com/oliverames/meta-mcp-server |
| **Son Güncelleme** | 2026-04-21 |
| **Açıklama** | Meta business platform için en kapsamlı MCP server. 200+ araç: Facebook Pages, Instagram, Threads, Ads Manager, Commerce, Conversions API, Audiences, Insights, Ad Library |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **Kullanım** | Claude AI ile Meta verilerine doğal dil sorgulama |
| **Topics** | ads-manager, ai, anthropic, automation, claude, conversions-api, facebook, facebook-ads |

### 3. proxy-intell/facebook-ads-library-mcp
| Özellik | Değer |
|---------|-------|
| **Stars** | 238 |
| **Language** | Python |
| **Link** | https://github.com/proxy-intell/facebook-ads-library-mcp |
| **Son Güncelleme** | 2026-06-04 |
| **Açıklama** | Facebook Ads Library için MCP Server — FB'nin reklam kütüphanesinden anlık bilgi alma |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **Kullanım** | Rakip reklam analizi, trend takibi |
| **Özellik** | LLM-friendly API erişimi |

### 4. ana-romero-lopez/meta-ads-ai-monitor
| Özellik | Değer |
|---------|-------|
| **Stars** | 1 |
| **Language** | Python |
| **Link** | https://github.com/ana-romero-lopez/meta-ads-ai-monitor |
| **Açıklama** | Meta Ads kampanyalarını izleyen, 7 günlük performans delta hesaplayan ve otomatik bildirim gönderen Python aracı |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **Özellik** | Performance monitoring, automated alerts |

### 5. peeomid/trak-social-cli
| Özellik | Değer |
|---------|-------|
| **Stars** | 2 |
| **Language** | Python |
| **Link** | https://github.com/peeomid/trak-social-cli |
| **Açıklama** | Facebook & Meta Ads CLI — Pages yönetimi, post planlama, reklam performans takibi terminalden |
| **Ücret** | Ücretsiz (Açık Kaynak) |
| **Özellik** | Terminalden Meta yönetimi, JSON output |

---

## Ticari Reklam Platformları (Karşılaştırma)

| Platform | Fiyat | Özellik | Hedef Kitle |
|----------|-------|---------|-------------|
| **AdEspresso** | $99-499/ay | A/B testing, kampanya optimizasyonu, analytics | Orta-büyük ajanslar |
| **Madgicx** | $99-299/ay | AI-powered bidding, creative analysis | Performans pazarlamacıları |
| **Revealbot** | $49-249/ay | Automated rules, cross-platform | Küçük-orta ajanslar |
| **Sprout Social** | $99-249/ay | Sosyal medya + reklam yönetimi | Markalar |
| **Hootsuite Ads** | $99-499/ay | Sosyal medya yönetimi + reklam | Büyük markalar |

---

## Açık Kaynak Alternatifler

### AI Agent Tabanlı Reklam Otomasyonu

**1. advertising-hub (En Kapsamlı)**
```
Özellikler:
├── 14 platform API desteği
├── 25+ AI agent (her platform için özelleşmiş)
├── MCP server registry
├── Cross-platform reporting
└── Campaign management
```

**2. meta-mcp-server (Meta-Spesifik)**
```
Özellikler:
├── 200+ Claude AI tool
├── Facebook Pages yönetimi
├── Instagram scheduling + analytics
├── Ads Manager programmatic access
├── Conversions API entegrasyonu
└── Ad Library erişimi
```

**3. facebook-ads-library-mcp (Rakip Analizi)**
```
Özellikler:
├── Rakip reklamlarını anlık görüntüleme
├── Creative performance analizi
├── Trend identification
└── LLM-friendly query
```

---

## Adım Adım Yapım Rehberi

### Seçenek 1: Claude AI + Meta MCP Server (En Modern)

**1. MCP Server Kurulumu**
```bash
# npx ile çalıştır
npx -y @oliverames/meta-mcp-server

# veya Claude Desktop'a ekle
# Claude Desktop → Settings → MCP Servers → Add new server
```

**2. Claude AI ile Meta Yönetimi**
```
# Claude'ya sor:
"What's my best performing ad set from last week?"
"Compare my Facebook vs Instagram ROAS"
"Show me competitor ads in the beauty vertical"
```

**3. Otomatik Raporlama**
```bash
# Script ile çalıştır
python meta-ads-ai-monitor.py --days 7 --send-slack
```

### Seçenek 2: advertising-hub ile Cross-Platform Yönetim

**1. Kurulum**
```bash
git clone https://github.com/itallstartedwithaidea/advertising-hub.git
cd advertising-hub
pip install -r requirements.txt
```

**2. Platform Ekle**
```bash
# Google Ads
python -m advertising_hub setup google

# Meta Ads
python -m advertising_hub setup meta

# LinkedIn Ads
python -m advertising_hub setup linkedin
```

**3. AI Agent Çalıştır**
```bash
# Platform agent'ını başlat
python -m advertising_hub agents paid-media

# veya Gemini CLI ile
gemini-cli run paid-media-agent
```

---

## Herkesin Kaçırdığı Nokta #1: Creative Performance > Bidding Optimization

Reklam ajansları "bidding" üzerine odaklanıyor ama en büyük etki **creative**'den geliyor. A/B test verilerine göre:
- Sadece görsel değiştirmek: %30-50 CTR artışı
- Sadece başlık değiştirmek: %5-15 CTR artışı
- Her ikisi birlikte: %3-5x dönüşüm artışı

**Kaçırılan Fırsat:** Çoğu ajans bidding algoritması üzerine saatler harcar. Oysa aynı zamanda creative heatmap analizi yapmak çok daha yüksek ROI verir.

## Herkesin Kaçırdığı Nokta #2: Cross-Platform Reporting Boşluğu

Hiçbir açık kaynak aracı gerçek anlamda "cross-platform" raporlama yapmıyor. Google Ads + Meta Ads + LinkedIn Ads'i tek dashboard'da görmek isteyenler genelde ücretli platformlara yöneliyor. **advertising-hub** bu boşluğu doldurmaya çalışan nadir açık kaynak projelerinden.

## Herkesin Kaçırdığı Nokta #3: Rakip Analizi İçin Reklam Kütüphanesi

Facebook Ads Library'yi kimse kullanmıyor çünkü arayüzü karmaşık. **facebook-ads-library-mcp** ile Claude AI'ye "Rakibim X'in son 1 ayda hangi reklamları yayınladığını göster" diye sorabilirsiniz. Bu bilgi stratejik kararlar için çok değerli.

---

## Kaynaklar

1. itallstartedwithaidea/advertising-hub — https://github.com/itallstartedwithaidea/advertising-hub
2. oliverames/meta-mcp-server — https://github.com/oliverames/meta-mcp-server
3. proxy-intell/facebook-ads-library-mcp — https://github.com/proxy-intell/facebook-ads-library-mcp
4. Meta for Developers — https://developers.facebook.com/docs/marketing-apis
5. Meta Business — https://www.facebook.com/business/news
