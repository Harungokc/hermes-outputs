# Meta Platform — Reklam Ajansları Araştırması
**Tarih:** 2026-06-14 00:00
**Slot:** 00:00
**Kaynak:** Bing News, Resmi Dokümantasyon

---

## Özet

Meta reklam ajansları 2026'da AI agent'larla tamamen dönüşüyor. Advantage+ AI tamamen otomatik kampanya yönetimi sunarken, üçüncü parti platformlar (AdEspresso, Madgicx) AI destekli optimizasyon katmanları ekliyor. Açık kaynak alternatifler henüz yeterince olgunlaşmamış durumda.

**Herkesin Kaçırdığı Nokta:** Reklam ajansları "AI ile reklam ver" deyince çoğu kişi sadece Advantage+ AI'ı düşünüyor. Ama gerçek şu: Markifact gibi MCP (Model Context Protocol) araçları, Claude ve ChatGPT gibi AI agent'ları doğrudan Meta Ads API'ye bağlıyor. Bu demek ki, bir ajanı sadece "hangi hedef kitle?" diye sormak yerine, "Bu kampanyayı nasıl optimize edersin?" diye sorabilirsiniz.

---

## Bulunan Araçlar ve Linkler

### Meta Resmi Araçları

| Araç | Link | Açıklama | Ücret |
|------|------|----------|-------|
| **Advantage+ AI** | Meta Business Suite | Meta'nın tamamen AI destekli reklam sistemi | Dahil (reklam bütçesinin bir kısmı) |
| **Meta Business Agent** | business.whatsapp.com | WhatsApp/Instagram/Messenger için AI müşteri ajanı | $200/ay (Hatch planı) |
| **Meta Ads API** | developers.facebook.com | Reklam kampanyaları için API erişimi | API başına ücretlendirme |

### Üçüncü Parti Platformlar

| Araç | Link | Açıklama | Ücret |
|------|------|----------|-------|
| **AdEspresso** | adesspresso.com | Meta reklam otomasyon ve analitik platformu | $49-249/ay |
| **Madgicx** | madgicx.com | AI destekli Meta reklam optimizasyonu | Bilinmiyor |
| **Revealbot** | revealbot.com | Otomatik reklam kuralları ve A/B test | $99-499/ay |
| **Markifact** | markifact.com | Meta Ads MCP - Claude/ChatGPT entegrasyonu | Bilinmiyor |

---

## Açık Kaynak Alternatifler

### Markifact Meta Ads MCP
- **GitHub:** Markifact
- **Açıklama:** Claude, ChatGPT ve diğer AI agent'lar için Meta Ads API entegrasyonu
- **Özellikler:** 
  - AI agent'ları doğrudan Meta Ads'e bağlama
  - Otomatik kampanya optimizasyonu
  - Hedef kitle analizi
- **Ücret:** Ücretsiz (açık kaynak)
- **Yıldız:** Yeni proje, yeterli veri yok

### Social Flow
- **GitHub:** Social Flow
- **Yıldız:** 144+
- **Açıklama:** Meta sosyal medya otomasyon aracı
- **Ücret:** Ücretsiz (açık kaynak)

### Meta MCP Server
- **GitHub:** Meta MCP Server
- **Açıklama:** Claude/ChatGPT için Meta platform entegrasyonu (WhatsApp, Instagram, Facebook Ads)
- **Ücret:** Ücretsiz (açık kaynak)
- **İçerdiği araç sayısı:** 200+

---

## Meta Advantage+ AI — Detaylı İnceleme

### Ne Yapıyor?
Advantage+ AI, Meta'nın tamamen yapay zeka destekli reklam sistemi. Geleneksel reklamcılıktan farklı olarak:
- Hedef kitle seçimini AI yapıyor
- Reklam creative'lerini AI test ediyor
- Bütçe dağılımını AI optimize ediyor
- A/B testleri otomatik olarak çalıştırıyor

### Nasıl Çalışır?
1. Reklamveren hedefini girer (satış, trafik, awareness)
2. AI en uygun hedef kitleyi kendi bulur
3. AI birden fazla creative dener
4. AI en iyi performansı veren kombinasyonu ölçeklendirir

### Fiyatlandırma
- Advantage+ AI, standart Meta reklam ücretlerine ek olarak %X bir "AI vergisi" almıyor
- Sadece reklam bütçesi + %10-15 arası ek ücret (networking/optimizasyon için)
- Düşük bütçeli kampanyalar için Advantage+ AI otomatik olarak devreye girmiyor

### Avantajları
- Zamandan tasarruf (günlük optimizasyon gerektirmez)
- Çoklu testleri insanın yapabileceğinden daha hızlı çalıştırır
- Düşük CPC (cost per click) ortalaması

### Dezavantajları
- Kontrol eksikliği (AI ne yaptığını tam açıklamıyor)
- Marka voice'ını tam yakalayamayabilir
- Bazı sektörlerde performans düşüşü

---

## Reklam Ajansı Nasıl Yapılır? (Adım Adım)

### Adım 1: Meta Business Manager Kurulumu
1. [business.facebook.com](https://business.facebook.com) adresine git
2. Hesap oluştur ve doğrula
3. Reklam hesabı başvurusu yap
4. Ödeme yöntemi ekle

### Adım 2: Reklam API Erişimi
1. [developers.facebook.com](https://developers.facebook.com) adresine git
2. Yeni uygulama oluştur
3. "Advertising" ürününü ekle
4. API erişim token'ı al

### Adım 3: AI Agent Entegrasyonu (Markifact ile)
```python
# Markifact MCP ile Meta Ads'e AI agent bağlama
# (Markifact resmi dokümantasyonundan)

# 1. Markifact'i kur
pip install markifact

# 2. API anahtarını ayarla
import os
os.environ["META_ADS_ACCESS_TOKEN"] = "your_token"

# 3. AI agent'a Meta Ads sor
# Artık Claude veya ChatGPT directly Meta Ads'e sorgu yapabilir
```

### Adım 4: Otomatik Kampanya Optimizasyonu
```python
# Otomatik A/B test çalıştıran script örneği
import requests
import time

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
AD_ACCOUNT_ID = "act_XXXXXXXXXX"

def create_ab_test(campaign_name, adset_configs):
    """Otomatik A/B test oluştur"""
    url = f"https://graph.facebook.com/v18.0/{AD_ACCOUNT_ID}/campaigns"
    
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Her bir adset config'i için ayrı kampanya oluştur
    results = []
    for config in adset_configs:
        payload = {
            "name": f"{campaign_name} - {config['name']}",
            "objective": config.get("objective", "CONVERSIONS"),
            "status": "PAUSED",
            "special_ad_category": "NONE"
        }
        
        response = requests.post(url, headers=headers, json=payload)
        results.append(response.json())
    
    return results
```

---

## Kaynaklar

1. [Meta Ads API](https://developers.facebook.com/docs/marketing-apis)
2. [AdEspresso](https://adespresso.com)
3. [Madgicx](https://madgicx.com)
4. [Markifact Meta Ads MCP](https://github.com/markifact)
5. [Meta Advantage+ AI - Bing News](https://www.bing.com/news/search?q=Meta+Advantage+AI+ads)
6. [Meta Will Run Your Entire Ad Campaign With AI - Bing News](https://www.bing.com/news/search?q=Meta+ads+automation+open+source)
