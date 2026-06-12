# Meta Business Verimli Kullanım Araştırması — 2026-06-13 06:00

## Özet

Meta Business Suite'i en verimli kullanan şirketler aslında sadece dashboard'a bakmıyor. Onlar otomasyon katmanları kuruyor: otomatik A/B test, akıllı budget allocation, real-time alerting ve cross-platform analytics. Elde edilen verileri CDP ve CRM sistemleriyle entegre ederek müşteri yolculuğunu tam olarak görünür hale getiriyorlar.

**Herkesin Kaçırdığı Nokta:** Meta Business Suite'in kendisi zaten güçlü ama çoğu kullanıcı sadece yüzeysel metriklere bakıyor. Asıl değer "Attribution Window" ayarlarında gizli — aynı kampanya farklı attribution window'larda tamamen farklı sonuçlar gösterebilir. 7 gün vs 1 gün click attribution arasında %40+ fark olabiliyor.

---

## Bulunan Araçlar ve Linkler

### 1. oliverames/meta-mcp-server
| Özellik | Değer |
|---------|-------|
| **Stars** | 15 |
| **Link** | https://github.com/oliverames/meta-mcp-server |
| **Kullanım** | Claude AI ile Meta Business verilerine doğal dil sorgulama |
| **Özellik** | 200+ tools, Insights, Audiences, Ad Library |

### 2. ana-romero-lopez/meta-ads-ai-monitor
| Özellik | Değer |
|---------|-------|
| **Stars** | 1 |
| **Link** | https://github.com/ana-romero-lopez/meta-ads-ai-monitor |
| **Kullanım** | 7 günlük performans delta hesaplama, otomatik alert |
| **Özellik** | Performance monitoring, Slack/email alerts |

### 3. peeomid/trak-social-cli
| Özellik | Değer |
|---------|-------|
| **Stars** | 2 |
| **Link** | https://github.com/peeomid/trak-social-cli |
| **Kullanım** | Terminalden Meta Business yönetimi |
| **Özellik** | JSON output, script-friendly |

### 4. luisrx7/PostPoster
| Özellik | Değer |
|---------|-------|
| **Stars** | 3 |
| **Link** | https://github.com/luisrx7/PostPoster |
| **Açıklama** | Meta Business Suite yerine post paylaşımı — daha hızlı ve kolay |
| **Ücret** | Ücretsiz (Açık Kaynak) |

---

## En Çok Zaman Kazandıran Otomasyonlar

### 1. Otomatik A/B Test Analizi
```
Geleneksel: Reklam yöneticisi her gün manual olarak A/B test sonuçlarını kontrol eder
Otomasyon: AI ajanı her 4 saatte bir sonuçları çeker, %95 güven aralığında istatistiksel 
           olarak anlamlı fark varsa otomatik "kazanan" seçer ve kaybedeni durdurur
Zaman tasarrufu: Haftada ~3-5 saat
```

### 2. Akıllı Budget Allocation
```
Geleneksel: Haftada bir kez manual budget dağılımı
Otomasyon: Günlük olarak ROAS'a göre otomatik budget yeniden dağılımı
           (En yüksek ROAS → En yüksek budget, düşük ROAS → Düşük budget veya durdurma)
Zaman tasarrufu: Haftada ~2-3 saat
```

### 3. Real-Time Alerting
```
Geleneksel: Günün sonunda raporları kontrol et, sorunları tespit et
Otomasyon: Spend artışı >%20, CTR düşüşü >%30, Frequency artışı >%2 gibi 
           tetikleyicilerde anında Slack/Email alert
Zaman tasarrufu: Anlık müdahale ile günlük ~1 saat kayıp önlenir
```

### 4. Cross-Platform Reporting
```
Geleneksel: Her platform için ayrı rapor, Excel'de birleştir
Otomasyon: Google Ads + Meta Ads + LinkedIn Ads tek dashboard'da otomatik konsolidasyon
Zaman tasarrufu: Haftada ~2-4 saat
```

---

## A/B Test Otomasyonu Nasıl Yapılır

### Adım 1: Test Yapısını Belirle
```python
# Test değişkenleri
test_config = {
    "ad_set_id": "act_123456789",
    "test_variable": "creative",  # creative, audience, placement
    "variants": [
        {"name": "Control", "creative_id": "123"},
        {"name": "Variant A", "creative_id": "456"},
        {"name": "Variant B", "creative_id": "789"}
    ],
    "budget_percentage": 20,  # Her varianta %20 budget
    "duration_days": 7,
    "min_sample_size": 1000,
    "confidence_level": 0.95
}
```

### Adım 2: Test'i Başlat
```python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adset import AdSet

# Facebook Marketing API init
FacebookAdsApi.init(access_token=ACCESS_TOKEN)

# Yeni ad set oluştur (test için)
test_adset = AdSet()
test_adset[AdSet.Field.name] = "A/B Test - Creative"
test_adset[AdSet.Field.campaign_id] = CAMPAIGN_ID
test_adset[AdSet.Field.daily_budget] = DAILY_BUDGET
test_adset[AdSet.Fieldbilling_event] = "IMPRESSIONS"
test_adset[AdSet.Field.optimization_goal] = "LINK_CLICKS"
test_adset.create()
```

### Adım 3: Sonuçları Analiz Et
```python
def analyze_ab_test(adset_ids, metric="ROAS"):
    results = {}
    for adset_id in adset_ids:
        insights = get_adset_insights(adset_id, days=7)
        results[adset_id] = calculate_roas(insights)
    
    # İstatistiksel significance kontrolü
    winner = max(results, key=results.get)
    p_value = calculate_p_value(results)
    
    if p_value < 0.05:
        return {"winner": winner, "confidence": "95%", "action": "scale_winner"}
    else:
        return {"winner": None, "confidence": "insufficient", "action": "continue_test"}
```

---

## Analitik Takibi Nasıl Otomatize Edilir

### Önerilen Metrics to Track
| Metric | Takip Sıklığı | Alert Threshold |
|--------|---------------|-----------------|
| CTR (Click-Through Rate) | 4 saat | <%1 veya >%5 |
| CPC (Cost Per Click) | 4 saat | >$2 veya <$0.50 |
| ROAS (Return on Ad Spend) | Günlük | <2x veya >5x |
| Frequency | Günlük | >3 |
| Spend | Saatlik | >%20 günlük budget |
| Conversions | Günlük | <10 (düşük volume) |

### Otomasyon Pipeline
```
1. Meta Marketing API → Günlük/4 saatlik veri çekme
2. Python Script → Hesaplama ve alert trigger kontrolü
3. Slack/Email → Anlık bildirim
4. Notion/Google Sheets → Log ve raporlama
```

### Örnek Python Script
```python
import facebook_business
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.insightsresult import InsightsResult
import time, json

# Config
ACCOUNT_ID = "act_123456789"
ACCESS_TOKEN = "your_token"
ALERT_THRESHOLDS = {
    "ctr_low": 0.01,
    "ctr_high": 0.05,
    "cpc_high": 2.00,
    "frequency_high": 3.0
}

def check_adset_health(adset_id):
    params = {
        'date_preset': 'last_7d',
        'fields': 'impressions,clicks,spend,ctr,cpc,frequency,actions'
    }
    insights = AdSet(adset_id).get_insights(params=params)
    return insights

def send_alert(message, channel="slack"):
    # Slack webhook veya email gönder
    pass

def main():
    FacebookAdsApi.init(access_token=ACCESS_TOKEN)
    accounts = AdAccount(ACCOUNT_ID).get_ad_sets()
    
    for account in accounts:
        health = check_adset_health(account.id)
        
        if health['ctr'] < ALERT_THRESHOLDS['ctr_low']:
            send_alert(f"⚠️ Düşük CTR: {account.name} - {health['ctr']}")
        elif health['frequency'] > ALERT_THRESHOLDS['frequency_high']:
            send_alert(f"⚠️ Yüksek Frequency: {account.name} - {health['frequency']}")
        
        time.sleep(0.5)  # Rate limit
```

---

## Şirketlerin Kullandığı En İyi Uygulamalar

### Büyük E-ticaret Şirketleri
```
1. Dynamic Product Ads (DPA) — Sepete eklenen ürünleri otomatik reklamla
2. Advantage+ Shopping Campaigns — AI-powered bidding
3. Multi-country pixel tracking — Her ülke için ayrı conversion tracking
4. Real-time inventory integration — Stok olmayan ürünleri otomatik durdurma
```

### SaaS Şirketleri
```
1. Lead Gen Forms → CRM entegrasyonu (HubSpot, Salesforce)
2. Video ads + retargeting — 50%+ izlenme sonrası retarget
3. Lifetime value tracking — Müşteri başlangıç değerini hesaplama
4. Competitor ad monitoring — Rakip kampanyalarını takip
```

### Yerel İşletmeler
```
1. Local awareness ads — 5-10 km radius hedefleme
2. Store visits tracking — Fiziksel ziyaretleri ölçme
3. Call tracking — Telefon tıklamalarını izleme
4. WhatsApp/Message button — Direkt mesajlaşma
```

---

## Herkesin Kaçırdığı Nokta #1: Attribution Window Farkları

Aynı kampanya farklı attribution window'larda tamamen farklı sonuçlar verir:
- **1-day click:** Kimin bugün tıkladığı
- **7-day click:** 7 gün içinde tıklayıp dönüşüm yapanlar
- **1-day view:** 1 gün içinde görüp dönüşüm yapanlar

**Kaçırılan Gerçek:** Bir "awareness" kampanyası 7-day attribution'da %30 daha iyi görünebilir ama 1-day'de düşük performans gösterebilir. Kampanya optimizasyonu yaparken attribution window'u sabit tutmak şart.

## Herkesin Kaçırdığı Nokta #2: Advantage+ AI'ın Gücü

Meta'nın Advantage+ AI sistemi artık çok güçlü. " Advantage+ Shopping Campaigns" ile manual bidding'den 20-30% daha iyi ROAS alanlar var. Ama çoğu reklamveren hâlâ manual bidding kullanıyor çünkü "kontrolü kaybetmek" istemiyor.

## Herkesin Kaçırdığı Nokta #3: Custom Audience Recency

Custom audience oluştururken en önemli parametre "recency" — son 30 gün, 60 gün, 90 gün? Çoğu kişi 90 gün kullanıyor ama 30 gün daha yüksek performans verebiliyor çünkü daha "sıcak" leads.

---

## Kaynaklar

1. oliverames/meta-mcp-server — https://github.com/oliverames/meta-mcp-server
2. ana-romero-lopez/meta-ads-ai-monitor — https://github.com/ana-romero-lopez/meta-ads-ai-monitor
3. peeomid/trak-social-cli — https://github.com/peeomid/trak-social-cli
4. Meta Marketing API — https://developers.facebook.com/docs/marketing-apis
5. Meta Business — https://www.facebook.com/business/news
