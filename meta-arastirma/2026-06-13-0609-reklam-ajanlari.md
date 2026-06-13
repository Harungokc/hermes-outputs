# Meta Reklam Ajansları Araştırması — 2026-06-13-0609

## Özet

Meta reklam ajansları ekosisteminde iki ana kategori var: ticari platformlar (AdEspresso, Madgicx, Revealbot) ve açık kaynak alternatifler. Ticari platformlar genelde büyük reklam bütçeleri olan ajanslar için tasarlanmış ve aylık $100-500 arası fiyatlandırma yapıyor. Açık kaynak alternatifler ise geliştiriciler için API erişimi ve özelleştirme imkanı sunuyor. 2026'da AI agent entegrasyonu ile "akıllı kampanya yönetimi" trendi öne çıkıyor.

**Herkesin Kaçırdığı Nokta:** Meta'nın kendi Advantage+ AI sistemi zaten oldukça güçlü ama çoğu reklamveren bunu sadece yüzeysel kullanıyor. Advantage+ audience segmentation, budget optimization ve creative rotation'ın hepsi API üzerinden programatik olarak kontrol edilebiliyor. Bugün açıklanan Meta 8.000 kişilik işten çıkarma haberleri, şirketin AI otomasyonuna daha fazla yatırım yapacağını gösteriyor — reklam ajansları için bu hem fırsat hem tehdit.

---

## Bulunan Araçlar ve Linkler

### 1. AdEspresso (Ticari)
| Özellik | Değer |
|---------|-------|
| **Link** | https://adespresso.com |
| **Açıklama** | Facebook/Instagram/Google ads yönetim platformu |
| **Fiyat** | $59/ay'den başlayan |
| **Özellik** | A/B test, otomatik kampanya optimizasyonu, analytics |

### 2. Madgicx (Ticari)
| Özellik | Değer |
|---------|-------|
| **Link** | https://madgicx.com |
| **Açıklama** | AI-powered Meta ads optimization |
| **Fiyat** | Custom pricing |
| **Özellik** | Creative analysis, audience insights, automated bidding |

### 3. Revealbot (Ticari)
| Özellik | Değer |
|---------|-------|
| **Link** | https://revealbot.com |
| **Açıklama** | Automated ad management for Facebook, Instagram, Google |
| **Fiyat** | $99/ay'den |
| **Özellik** | Rule-based automation, reporting, creative previews |

### 4. proxy-intell/facebook-ads-library-mcp ⭐238
| Özellik | Değer |
|---------|-------|
| **Stars** | 238 |
| **Fork** | 33 |
| **Link** | https://github.com/proxy-intell/facebook-ads-library-mcp |
| **Açıklama** | Facebook Ads Library için MCP Server — Claude AI ile doğal dil sorgulama |
| **Kullanım** | Rakip reklam analizi, trend takibi |
| **Ücret** | Ücretsiz (Açık Kaynak) |

### 5. dousheng34/chat-to-ads-engine ⭐0
| Özellik | Değer |
|---------|-------|
| **Link** | https://github.com/dousheng34/chat-to-ads-engine |
| **Açıklama** | Meta WhatsApp Business Agent sohbetlerini Meta Advantage+ reklamlarına köprüleyen FastAPI + SQLite MVP |
| **Özellik** | Chat'ten reklama geçiş, otomatik lead ads oluşturma |
| **Dil** | Python |
| **Ücret** | Ücretsiz (Açık Kaynak) |

---

## Açık Kaynak Alternatifler

| Araç | Dil | Özellik | GitHub |
|------|-----|---------|--------|
| facebook-ads-library-mcp | Python | Claude AI ile ads library sorgulama | proxy-intell/facebook-ads-library-mcp |
| chat-to-ads-engine | Python | WhatsApp chat → Advantage+ ads | dousheng34/chat-to-ads-engine |
| meta-ads-cli | Python | Meta Marketing Graph API v21 CLI | jon-egbdigital/meta-ads-cli |
| facebook-ads-reports | Python | Facebook Insights API ETL | machado000/facebook-ads-reports |

---

## Adım Adım Yapım Rehberi

### Meta Ads API ile Otomatik Kampanya Yönetimi

**1. Adım: Meta Business API Erişimi**
```
- Meta for Developers'da uygulama oluştur
- Marketing API iznini al
- Access Token al (Graph API Explorer)
```

**2. Adım: Claude AI ile Entegrasyon (MCP Server)**
```bash
# facebook-ads-library-mcp kurulumu:
pip install facebook-ads-library-mcp
# MCP config'e ekle:
{
  "mcpServers": {
    "facebook-ads": {
      "command": "facebook-ads-library-mcp"
    }
  }
}
```

**3. Adım: Otomatik Kampanya Oluşturma**
```python
# Claude Code ile:
# "Meta'da son 7 günde en çok reklam veren şirketler hangileri?"
# Claude ads library'yi sorgulayıp sonuçları döndürür
```

---

## Kaynaklar

- https://github.com/proxy-intell/facebook-ads-library-mcp
- https://github.com/dousheng34/chat-to-ads-engine
- https://adespresso.com
- https://madgicx.com
- https://revealbot.com
- https://www.bing.com/news/search?q=Meta+Ads+AI+agent+automation
