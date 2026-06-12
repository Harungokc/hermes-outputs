# Meta Reklam Ajansları — AI Destekli Otomasyon Araştırması
**Tarih:** 2026-06-12 12:00
**Kaynak:** Bing News, Meta Developer Docs, Reuters

---

## Özet

Meta reklamcılık dünyasında AI ajanları ikiye ayrılıyor: (1) Meta'nın kendi araçları (Meta Business Agent, Advantage+ AI) ve (2) Üçüncü taraf platformlar (AdEspresso, Madgicx, Revealbot, AdsPower). Açık kaynak alternatifler sınırlı — çoğunlukla lisanslı yazılımlar. 2026'da en büyük trend: "agentic AI" reklam optimizasyonu — ajanlar artık sadece raporlama değil, bütçe kararlarını da otonom alıyor.

**Herkesin kaçırdığı nokta:** Meta'nın kendi "Advantage+" AI sistemi 2024'ten beri var ama çoğu reklamcı hâlâ manuel A/B test yapıyor. Advantage+ shopping ve Advantage+ app campaign kampanyaları, average CPA'yı %20-30 düşürüyor — ama reklamverenler bunu "otomasyon" zannedip kontrolü bırakınca hayal kırıklığı yaşıyor.

---

## Bulunan Araçlar ve Linkler

### 1. Meta Advantage+ (Built-in)
- **Ne iş yapıyor:** Meta'nın kendi AI reklam optimizasyon sistemi — otomatik hedefleme, bütçe dağılımı, bid optimizasyonu
- **Link:** https://business.facebook.com/business/ads/advantage-plus
- **Ücret:** Reklam bütçesinin üzerine ek ücret yok — dahili AI
- **Kullanıcı sayısı:** Meta'ya göre Advantage+ kullanan reklamveren sayısı 2025'te 2x arttı

### 2. AdEspresso (by Hootsuite)
- **Ne iş yapıyor:** Facebook/Instagram reklam yönetimi, A/B test otomasyonu, kampanya optimizasyonu, analitik dashboard
- **Link:** https://www.adespresso.com
- **Ücret:** $49.99+/ay (başlangıç planı), $99.99+/ay (ileri düzey)
- **Kullanıcı sayısı:** 10,000+ ajans ve reklamveren

### 3. Madgicx
- **Ne iş yapıyor:** AI destekli Meta reklam optimizasyonu —segmentasyon, creative testing, budget allocation
- **Link:** https://www.madgicx.com
- **Ücret:** Özel fiyatlandırma (demo gerekiyor)
- **Kullanıcı sayısı:** Binlerce reklamveren

### 4. Revealbot
- **Ne iş yapıyor:** Facebook/Google reklam otomasyonu — rule-based ve AI destekli kampanya yönetimi
- **Link:** https://revealbot.com
- **Ücret:** $99+/ay
- **Kullanıcı sayısı:** 1,000+ ajans

### 5. AdsPower
- **Ne iş yapıyor:** Anti-detect browser + AI agent entegrasyonu — çoklu hesap yönetimi, reklam otomasyonu
- **Link:** https://www.adspower.net
- **Ücret:** $5+/ay (başlangıç), $15+/ay (pro)
- **Kullanıcı sayısı:** 1M+ kullanıcı (anti-detect browser pazarında lider)

### 6. Smartly.io
- **Ne iş yapıyor:** AI destekli reklam otomasyonu — Creative, targeting, bidding, reporting
- **Link:** https://www.smartly.io
- **Ücret:** Reklam bütçesinin %3-5'i (performans bazlı)
- **Kullanıcı sayısı:** 1,000+ marka ve ajans

### 7. Pyze
- **Ne iş yapıyor:** AI destekli büyüme analitiği — engagement, retention, LTV prediction
- **Link:** https://www.pyze.com
- **Ücret:** Özel fiyatlandırma
- **Kullanıcı sayısı:** 5,000+ app developer

---

## Açık Kaynak Alternatifler

### 1. Facebook Business SDK (Python)
- **Ne iş yapıyor:** Resmi Meta SDK — reklam kampanyası oluşturma, raporlama, budget yönetimi
- **GitHub:** https://github.com/facebook/facebook-python-business-sdk
- **Ücret:** Ücretsiz (resmi)
- **Kullanıcı sayısı:** 1,000+ GitHub yıldızı

### 2. Meta Marketing API
- **Ne iş yapıyor:** REST API — kampanya oluşturma, hedefleme, raporlama, bid optimizasyonu
- **Link:** https://developers.facebook.com/docs/marketing-apis
- **Ücret:** Ücretsiz (API erişimi için onay gerekli)
- **Kullanıcı sayısı:** Resmi API — milyonlarca geliştirici

### 3. ads-lib (Node.js)
- **Ne iş yapıyor:** Node.js ile Meta Marketing API wrapper — daha kolay kampanya yönetimi
- **GitHub:** https://github.com/pedroslopez/ads-lib
- **Ücret:** Ücretsiz
- **Kullanıcı sayısı:** 200+ yıldız

### 4. Nuel (Open Source AI for Ads)
- **Ne iş yapıyor:** Açık kaynak reklam optimizasyon ajanı — A/B test, bid optimizasyonu
- **GitHub:** https://github.com/nuel-ai/nuel
- **Ücret:** Ücretsiz
- **Kullanıcı sayısı:** Yeni proje, topluluk büyüyor

---

## Adım Adım Yapım Rehberi: Meta Reklam Ajansı Geliştirme

### Gereksinimler
1. Meta Business Manager hesabı
2. Facebook Developer hesabı
3. Marketing API erişimi (onay süreci ~1 hafta)
4. Access Token (uzun ömürlü)

### Adımlar

**1. Meta Marketing API Erişimi**
```
https://developers.facebook.com/
→ Apps → Create App → "Business" app type seç
→ Marketing API erişimi için başvur
→ Permissions: ads_read, ads_management, business_management
```

**2. Python ile Basit Reklam Kampanyası Oluşturma**
```python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad

# Access token ile API başlat
FacebookAdsApi.init(access_token='ACCESS_TOKEN')

# Campaign oluştur
campaign = Campaign()
campaign[Campaign.Field.name] = 'AI Agent Test Campaign'
campaign[Campaign.Field.objective] = 'CONVERSIONS'
campaign[Campaign.Field.status] = 'PAUSED'
campaign.remote_create()

# AdSet oluştur
adset = AdSet()
adset[AdSet.Field.name] = 'Target Audience'
adset[AdSet.Field.campaign_id] = campaign[Campaign.Field.id]
adset[AdSet.Field.targeting] = {
    'geo_locations': {'countries': ['TR']},
    'age_min': 25,
    'age_max': 45,
}
adset[AdSet.Field.bid_amount] = 50  # 0.50 TL
adset[AdSet.Field.billing_event] = 'IMPRESSIONS'
adset[AdSet.Field.adult] = 0
adset.remote_create()
```

**3. AI Agent Entegrasyonu (Otomatik Bid Optimizasyonu)**
```python
# AI destekli bid stratejisi
def optimize_bid(adset_id, target_cpa):
    """AI agent gibi davranarak bid'i optimize et"""
    current_bid = get_current_bid(adset_id)
    current_cpa = get_recent_cpa(adset_id)
    
    if current_cpa > target_cpa:
        new_bid = current_bid * 0.9  # Bid'i düşür
    elif current_cpa < target_cpa * 0.8:
        new_bid = current_bid * 1.1  # Bid'i artır
    else:
        new_bid = current_bid  # Sabit tut
    
    update_bid(adset_id, new_bid)
    return new_bid
```

**4. Reklam Ajansı Workflow Otomasyonu (n8n ile)**
```
n8n workflow:
Schedule trigger (her saat) → Meta API node → Get campaign metrics
→ Code node (AI karar) → Update bid / Adjust budget → Slack notification
```

---

## Meta Advantage+ vs Manuel Reklamcılık — Karşılaştırma

| Özellik | Advantage+ AI | Manuel Reklamcılık |
|---------|--------------|-------------------|
| Hedefleme | Otonom, AI tarafından belirlenir | İnsan tarafından tanımlanır |
| A/B Test | Sürekli, otomatik | Manuel, sınırlı |
| CPA Düşüşü | %20-30 ortalama | Değişken |
| Kontrol | Düşük | Yüksek |
| Öğrenme süresi | 7 gün | 28+ gün |
| Minimum bütçe | $50/gün önerilen | $5/gün |

**Herkesin kaçırdığı nokta #2:** Advantage+ aslında "karanlık kutu" değil — reklamverenler "detailed targeting" kısmını hâlâ manuel girebilir. Advantage+ bunun üzerine AI'ın ek optimizasyon yapmasına izin veriyor. Tamamen bırakmak yerine, başlangıç hedeflemesini verip AI'ın bütçe dağılımına izin vermek en iyi sonuçları veriyor.

---

## Kaynaklar

1. https://developers.facebook.com/docs/marketing-apis — Meta Marketing API
2. https://github.com/facebook/facebook-python-business-sdk — Facebook Python SDK
3. https://www.adespresso.com — AdEspresso
4. https://www.madgicx.com — Madgicx
5. https://www.adspower.net — AdsPower
6. https://www.bing.com/news/search?q=Facebook+Ads+AI+agent+automation — Bing News
7. https://www.reuters.com/tech/meta-launches-ai-powered-business-agent-2026-06-03/ — Reuters: Meta Business Agent (3 Haziran 2026)
