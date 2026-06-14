# Meta İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-14 18:00  
**Slot:** Her 6 saatte bir (12:00, 18:00)

---

## 1. Özet Tablo

| Agent | Platform | Zorluk | Kullanım Alanı |
|-------|----------|--------|----------------|
| Müşteri Hizmetleri Agent | WhatsApp/IG/FB | Kolay | 7/24 yanıt, triyaj |
| Abandoned Cart Agent | WhatsApp | Orta | Sepet terk, hatırlatma |
| Sipariş Takip Agent | WhatsApp | Kolay | Kargo, teslimat bildirimi |
| Lead Scoring Agent | Instagram | Orta | Potansiyel müşteri sıralama |
| Content Agent | IG/FB | Orta | Görsel + caption üretimi |
| A/B Test Agent | Meta Ads | İleri | Reklam test otomasyonu |
| RFM Analiz Agent | E-ticaret | Orta | Müşteri segmentasyonu |
| Churn Prediction Agent | WhatsApp/IG | İleri | Terk edecek müşteri tespiti |

---

## 2. Müşteri Hizmetleri AI Agent

### Ne Yapıyor?
7/24 WhatsApp, Instagram DM ve Facebook Messenger'da müşteri sorularını yanıtlıyor. Karmaşık soruları insan temsilciye yönlendiriyor.

### Nasıl Kurulur?
```
1. WhatsApp Business API + Meta Agent (hazır çözüm)
2. Veya: n8n + Claude Code + Instagram/WhatsApp MCP
3. Bilgi bankası: Ürün FAQ, sıkça sorulan sorular
4. Yönlendirme kuralları: Para iadesi → insan, sipariş sorgusu → AI
```

### Gerçek Örnek: E-ticaret Sipariş Sorgusu
```
Müşteri: "Siparişim ne zaman gelir?"
AI: "Sipariş no #12345, KargoTR ile kargoya verildi. 
     Tahmini teslimat: yarın 14:00-18:00 arası.
     Kargo takip: [link]"
```

---

## 3. Abandoned Cart Recovery Agent

### Ne Yapıyor?
Sepeti terk eden müşteriye WhatsApp veya Instagram'dan hatırlatma mesajı atıyor. En yüksek ROI'li e-ticaret otomasyonu — %10-15 ek dönüşüm.

### Zamanlama Stratejisi
- **1 saat sonra:** "Sepetinizi unuttunuz mu?" + küçük indirim
- **24 saat sonra:** "Bu ürünleri sevenler bunları da aldı" (cross-sell)
- **72 saat sonra:** "%10 indirim kodu" (final hatırlatma)

### Nasıl Kurulur?
```
1. E-ticaret platformundan (Shopify, WooCommerce) sepet verisini çek
2. n8n ile webhook: Sepet terk → 1 saat bekle → WhatsApp mesaj
3. Template onayı WhatsApp'tan al
4. Kişiselleştirme: {{musteri_adi}}, {{urun_adi}}, {{fiyat}}
```

### Herkesin Kaçırdığı Nokta
Çoğu şirket sadece e-posta hatırlatması yapıyor. WhatsApp'ta **açılma oranı %98**, e-postada %20. Aynı mesaj WhatsApp'ta 5 kat daha etkili.

---

## 4. Content Generation Agent

### Ne Yapıyor?
Instagram ve Facebook için görsel + caption üretiyor. Hashtag öneriyor. Post zamanlaması yapıyor.

### Kullanılan Araçlar
- **Görsel:** DALL-E, Midjourney, Stable Diffusion
- **Caption:** Claude Code, GPT-4
- **Zamanlama:** n8n + Meta API

### Örnek Workflow
```
1. Ürün fotoğrafı çek → upload
2. Claude: "Bu ürün için Instagram caption yaz, 3 varyasyon"
3. AI hashtag'leri öner
4. n8n ile zamanla → Instagram API ile paylaş
```

---

## 5. A/B Test Agent

### Ne Yapıyor?
Reklam kreatiflerini, başlıkları ve hedef kitleleri otomatik test ediyor. En iyi performans göstereni ölçeklendiriyor.

### Adım Adım Kurulum
```
1. google-meta-ads-ga4-mcp veya meta-ads-mcp kur
2. 3 farklı ad creative hazırla
3. n8n workflow: Her 24 saat → performans kontrolü → en iyiyi ölçeklendir
4. Claude Code ile rapor analizi
```

### Test Edilecek Değişkenler
- Görsel (3 farklı format)
- Başlık (duygusal vs mantıksal)
- CTA ("Hemen Al" vs "Detaylar")
- Hedef kitle (interest vs lookalike)

---

## 6. Lead Scoring Agent

### Ne Yapıyor?
Instagram veya WhatsApp üzerinden gelen potansiyel müşterileri puanlıyor. Kim dahalikely alışveriş yapacak, kim sadece meraklı?

### Skor Kriterleri
| Davranış | Puan |
|----------|------|
| Ürün sayfasını 3+ kez ziyaret | +20 |
| Fiyat sorusu sordu | +30 |
| "Satın almak istiyorum" dedi | +50 |
| 24 saat içinde cevap vermedi | -10 |
| Rakip markadan bahsetti | -20 |

### Nasıl Kurulur?
```
1. Instagram DM veya WhatsApp mesajlarını logla
2. Claude Code ile mesaj analizi (duygu, niyet)
3. Rapor: En yüksek skorlu 10 potansiyel müşteri
4. Satış ekibine bildirim
```

---

## 7. Herkesin Kaçırdığı Nokta

### #1: En Basit Agent En Çok Kazandırıyor
Şirketler "churn prediction AI" peşinde koşuyor. Ama en basit agent — sipariş takip bildirimi — müşteri memnuniyetini %40 artırıyor. Küçük başla, hızla sonuç al.

### #2: Agent'ı Değil, Workflow'u Tasarla
"AI agent yap" dersen yapay zeka ile boğuşursun. "Sepet terk eden müşteriye 72 saat sonra hatırlat" diyince net bir workflow'un olur. Workflow önce, agent sonra.

### #3: Çoklu Kanal Tek Agent
WhatsApp + Instagram + Facebook hepsi aynı agent'ı kullanabilir. Her kanalın API'si farklı ama prompt aynı. Tek bir "customer service agent" prompt'u tüm platformlarda çalışır.

---

## 8. Adım Adım: Kendi Meta AI Agent'ını Yap

### Minimum Viable Agent (1 gün)
```
1. WhatsApp Business API hesabı aç
2. n8n kur ve MCP server ekle
3. Basit FAQ yanıtı workflow'u kur (5-10 soru-cevap)
4. Test et, yayına al
```

### Gelişmiş Agent (1 hafta)
```
1. Knowledge base oluştur (ürünler, fiyatlar, SSS)
2. Claude Code + RAG entegrasyonu
3. Çoklu kanal desteği (WA, IG, FB)
4. Human handoff (AI → insan geçişi)
5. Analytics dashboard
```

---

## 9. Görsel Önerisi

**LinkedIn için tasarım önerisi:**
- Akış şeması: "Müşteri mesajı → AI analiz → Yanıt/ Yönlendirme"
- Her adım farklı renk kutusu ile
- Altın kural: "72 saat içinde yanıt yoksa müşteri kaybı"

---

## 10. Kaynaklar

- [Meta Business Agent Duyurusu](https://www.bing.com/news/search?q=Meta+Business+Agent+global+2026)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [n8n Meta nodes](https://n8n.io/integrations/meta/)
- [Abandoned Cart Recovery Vakaları](references/eticaret-geo-ai-agent-2026-06-12.md)

---

## 11. LinkedIn Post Fikri

**Başlık:** "Meta için 5 AI ajanı — hangisini yaparsanız kazanırsınız."

**Post:**
Meta platformlarında kullanılabilecek 5 AI ajanı, zorluk sırasına göre:

1. **Sipariş Takip Agent** (Kolay, 1 gün)
En basit ama en çok müşteri memnuniyeti kazandıran. "Siparişiniz yarın geliyor" mesajı = %40 daha az şikayet.

2. **Abandoned Cart Agent** (Orta, 3 gün)
Sepeti terk edene 72 saat sonra WhatsApp'tan hatırlatma. E-ticaret için en yüksek ROI. %10-15 ek satış.

3. **Müşteri Hizmetleri Agent** (Orta, 1 hafta)
7/24 WhatsApp'ta FAQ yanıtı. Karmaşık soruları insan'a yönlendir.

4. **Content Agent** (Orta, 1 hafta)
Instagram için görsel + caption üretimi. Haftada 20 post yerine 5 dakikada üret.

5. **Lead Scoring Agent** (İleri, 2 hafta)
Instagram DM'lerini analiz edip en sıcak lead'leri işaretle.

Hangisi sizin için öncelikli?

#MetaAI #AIAgent #WhatsApp #Instagram