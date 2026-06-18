# Meta Business Suite Verimli Kullanım — 2026-06-19 00:00

## Özet Tablo

| Otomasyon | Zaman Tasarrufu | Zorluk | Hangi Platform |
|-----------|----------------|--------|----------------|
| A/B Test Otomasyonu | 2-3 saat/hafta | ⭐ Kolay | Meta Ads API |
| Analitik Raporlama | 5-7 saat/hafta | ⭐⭐ Orta | n8n + Meta API |
| Kampanya Schedule | 3-4 saat/hafta | ⭐ Kolay | Meta Business Suite |
| Otomatik Budget Yönetimi | 4-6 saat/hafta | ⭐⭐ Orta | Meta Ads API + n8n |
| Performance Alert | 1-2 saat/hafta | ⭐ Kolay | Meta API + Discord/Slack |

---

## A/B Test Otomasyonu

### Meta Business Suite'te Manuel A/B Test (Eski Yöntem)

1. Her reklam seti için 2-3 farklı creative hazırla
2. Manuel olarak kampanya oluştur
3. Her biri için ayrı budget ayır
4. 3-7 gün bekle
5. Sonuçları manuel karşılaştır
6. Kazananı seç, diğerlerini kapat

**Sorun:** Haftada 2-3 kampanya = 6-9 saat iş. Ve insan yanlılığı (hangi reklamın "daha iyi" olduğuna karar verirken).

### AI ile Otomatik A/B Test (Yeni Yöntem)

**n8n + Claude + NotFair workflow:**
```
[Her Pazartesi 09:00]
→ Yeni A/B test kampanyası oluştur (3 creative, eşit budget)
→ 48 saat bekle
→ Her 12 saatte: sonuçları analiz et
→ 48. saatte: Kazananı belirle, budget'u %80'ini kazanana kaydır
→ Kaybedenleri durdur
→ Raporu Slack/Discord'a gönder
```

**Claude Code prompt örneği:**
```
Bu haftanın A/B test sonuçları:
- Ad Set A: 3.2% CTR, $12.40 CPA
- Ad Set B: 4.1% CTR, $9.80 CPA  
- Ad Set C: 2.8% CTR, $15.20 CPA

En iyi performans göstereni belirle, budget allocation öner,
kaybedenleri durdur ve raporla.
```

### Kaçırılan Nokta — Test Süresi Kuralı

**Kural:** A/B test en az 50 conversion event'i olana kadar beklemeli.

**Otomasyon kodu (pseudocode):**
```
IF kampanya.conv_count < 50:
    PRINT "Learning phase devam ediyor, bekleniyor..."
ELSE:
    analiz_et()
    kazanani_belirle()
```

---

## Analitik Raporlama Otomasyonu

### Günlük Rapor (n8n Workflow)

**Trigger:** Her gün saat 09:00

**İçerik:**
- Dünün toplam spend'i
- En iyi 5 kampanya (ROAS sıralı)
- En kötü 3 kampanya (düzeltme önerisiyle)
- Haftalık trend karşılaştırması
- Anomali uyarıları (normalin 2x üzerinde spend/artış)

**n8n + Discord/Slack Entegrasyonu:**
```json
{
  "name": "Meta Daily Report",
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.schedule",
      "parameters": { "rule": {"interval": [{"field": "cron", "expression": "0 9 * * *"}]} }
    },
    {
      "name": "Meta API - Kampanya Verileri",
      "type": "httpRequest",
      "parameters": {
        "url": "https://graph.facebook.com/v18.0/act_{AD_ACCOUNT_ID}/insights",
        "qs": {
          "fields": "campaign_name,spend,reach,impressions,ctr,cpc,roas",
          "date_preset": "yesterday",
          "level": "campaign"
        }
      }
    },
    {
      "name": "Claude - Rapor Oluştur",
      "type": "httpRequest",
      "parameters": {
        "url": "https://api.anthropic.com/v1/messages",
        "method": "POST",
        "body": {
          "model": "claude-3-5-sonnet-20241022",
          "max_tokens": 1000,
          "system": "Sen bir Meta Ads analistsin. Verdiğim verileri Türkçe rapora dönüştür.",
          "messages": [{"role": "user", "content": "Şu kampanya verilerini analiz et: {{ $json }}"}]
        }
      }
    },
    {
      "name": "Discord Webhook - Gönder",
      "type": "httpRequest",
      "parameters": {
        "url": "https://discord.com/api/webhooks/...",
        "method": "POST",
        "body": {"content": "{{ $json.rapor }}"}
      }
    }
  ]
}
```

### Haftalık Derin Analiz

**Trigger:** Her Pazar gece 23:00

**İçerik:**
- Haftalık toplam performans
- En iyi/worst performer'lar
- Budget efficiency score (harcanan her TL'in karşılığı)
- Gelecek hafta önerileri
- A/B test sonuçları özeti

---

## Kampanya Schedule Otomasyonu

### Meta Business Suite Native Features

Meta Business Suite zaten bazı scheduling özellikleri sunuyor:
- Post scheduling (Instagram, Facebook)
- Campaign start/end date belirleme
- Ad scheduling (belirli saatlerde reklam gösterimi)

**Eksik olan:** Tam zamanlı campaign optimization. Bunu n8n + Meta Ads API ile kapatıyoruz.

### Smart Campaign Scheduling

**Kural:** Reklam performansı günün saatine göre değişir.

**Otomasyon:**
- Peak saatler: 09:00-11:00, 19:00-21:00 → Budget %30 artır
- Düşük performans saatleri: 00:00-06:00 → Budget %50 düşür veya durdur
- Hafta sonu farklı budget allocation

**Bunun için:** Meta Ads API `ad_schedule_recommendations` endpoint'i yok, bunu kendi verilerinizden öğrenmeniz gerekiyor. İlk 4-6 hafta manual takip, sonra AI öğrenmiş olur.

---

## Otomatik Budget Yönetimi

### Rule-Based Budget Optimization

**Kurallar:**
```
EĞER kampanya ROAS < 2.0 VE spend > ₺1000/gun:
    → Budget'u %25 düşür
    → Alert gönder

EĞER kampanya ROAS > 4.0 VE conv_count > 50:
    → Budget'u %30 artır
    → Alert gönder

EĞER kampanya 7 gündür learning phase'te:
    → Durdur, yeniden başlat veya audience değiştir
    → Alert gönder

EĞER kampanya spend normalin 3x üzerinde AMA conversion yok:
    → Derhal durdur
    → Alert gönder (acil!)
```

### Dynamic Budget Allocation (İleri Seviye)

**Haftalık budget pool:** ₺50,000

**AI karar:**
- Geçen hafta hangi kampanyalar en iyi performansı gösterdi?
- Bu hafta beklenen seasonality (hafta sonu farklı mı?)
- A/B test sonuçları
- Yeni kampanya fırsatları var mı?

**Claude Code prompt:**
```
Toplam haftalık budget: 50,000 TL
Kampanya performansları (geçen hafta):
1. Summer Sale: 4.2 ROAS, 12,000 TL spend
2. New Arrivals: 3.1 ROAS, 8,000 TL spend
3. Retargeting: 5.8 ROAS, 5,000 TL spend
4. Brand Awareness: 1.2 ROAS, 15,000 TL spend
5. Prospecting: 2.4 ROAS, 10,000 TL spend

Bu hafta için optimal budget allocation öner. 
Kurallar:
- ROAS < 2 olanlar minimum budget alsın
- ROAS > 4 olanlara daha fazla kaynak
- Toplam spend 50,000 TL'yi geçmesin
```

---

## Kaçırılan Nokta #1 — Meta Business Suite'in Raporlama Gecikmesi

**Problem:** Meta Business Suite'te veriler 24-48 saat gecikmeli görünüyor. "Dün ne oldu?" sorusunu tam olarak cevaplayamıyorsunuz.

**Çözüm:** Meta Marketing API ile gerçek zamanlı veri çekme. n8n'in 15 dakikalık schedule'ı ile her 15 dakikada bir güncellenen dashboard.

**Ama dikkat:** API ile çekilen veri Business Suite ile %100 uyumlu olmayabilir. Margin of error: ~5%. Bunu not edin.

---

## Kaçırılan Nokta #2 — Automated Rules = AI Değil

**Meta Business Suite'in "Automated Rules" özelliği** sadece IF-THEN kurallarıdır. Gerçek AI değil.

**Automated Rules örneği:**
- "Spend > 1000 TL AND ROAS < 2.0 → Pause campaign"

**AI Agent farkı:**
- Sadece durdurmaz, NEDEN analiz eder
- "ROAS düşük çünkü audience çok geniş → daralt öner"
- "CPM yüksek çünkü rakip sezon başlamış → bidding strategy değiştir"

**Automated Rules = iyi başlangıç. AI Agent = sürekli iyileşen sistem.**

---

## Kaçırılan Nokta #3 — Haftalık Optimizasyon Yeterli Değil

**Eski yaklaşım:** "Haftada bir bakarız, günlük takip çok sıkıcı"

**AI çağı yaklaşımı:** Günlük 2 dakikalık müdahale + AI sürekli izleme

**Günlük AI monitoring:**
- 09:00 → Günlük özet (otomatik)
- 12:00 → Anomali kontrol (beklenmedik spike/drop)
- 18:00 → Akşam performans kontrolü
- 22:00 → Gün sonu raporu + yarın önerileri

**Toplam insan müdahalesi:** Günde 10 dakika (sadece onay vermek)

---

## Meta Business Agent — Hatch ($200/ay)

**Duymayanlar için:** Meta yeni "Hatch" AI agent'ını $200/ay fiyatlandırmasıyla piyasaya sürüyor (2026).

**Hatch ne yapıyor:**
- Müşteri hizmetleri otomasyonu
- Randevu/rezervasyon yönetimi
- Sipariş takibi
- SSS yanıtlama
- Email/sms/WhatsApp entegre

**Kimler için:** Büyük işletmeler (günde 1000+ müşteri etkileşimi olan)

**Küçük işletmeler için alternatif:** n8n + Claude + WhatsApp Business API = Aynı işlevsellik, %90 daha düşük maliyet

**Maliyet karşılaştırması:**
- Hatch: $200/ay = ~₺7,000/ay
- n8n (self-hosted): Ücretsiz + Claude API: ~₺2,000-5,000/ay

---

## Kaynaklar

- [Meta Automated Rules](https://business.facebook.com/business/help/389849297878635)
- [Meta Marketing API - Insights](https://developers.facebook.com/docs/graph-api/reference/ads-insights/)
- [NotFair GitHub](https://github.com/nowork-studio/NotFair)
- [n8n Workflow Examples](https://n8n.io/workflows/)
- [Meta Business Agent - Hatch](https://about.fb.com/news/2026/05/meta-hatch-ai-agent/)

---

## LinkedIn Post Fikri

**Başlık:** Meta Reklamcılığında Günlük 10 Dakikada Haftalık İş Bitiriyorum

**Post:**
Meta reklamcılığı yapanların çoğu ya "bırak çalışsın" ya da "her şeyi manuel yap" arasında seçim yapıyor.

Benim yöntemüm: AI ile günlük 10 dakika.

Nasıl çalışıyor:

✓ 09:00 → AI günlük raporu hazırlıyor (n8n + Claude)
✓ 12:00 → AI anomali kontrolü (beklenmedik sonuçlar)
✓ 18:00 → AI akşam performans kontrolü
✓ 22:00 → AI gün sonu + yarın önerileri

Ben sadece onay veriyorum.

Örnek: Geçen hafta bir kampanya beklenmedik şekilde 3x spend yaptı. AI hemen yakaladı, durdurdu, beni uyardı. 2 saat içinde müdahale ettim. Toplam tasarruf: 8,000 TL.

Siz Meta reklamlarınızı nasıl yönetiyorsunuz?

#MetaAds #ReklamOtomasyon #AI #DijitalPazarlama #n8n

---

**Son Güncelleme:** 2026-06-19 00:00