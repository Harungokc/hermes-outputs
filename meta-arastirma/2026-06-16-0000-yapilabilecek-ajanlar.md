# Meta İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-16 00:00
**Slot:** Her 6 saatte bir (00:00, 06:00, 12:00, 18:00)
**Kaynak:** Bing News, GitHub, Meta Developers, HN Algolia

---

## 1. Özet Tablo

| Agent Tipi | Zorluk | Önemi | Kullanılan API |
|------------|--------|-------|----------------|
| Müşteri Hizmetleri Bot | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp Business API |
| Abandoned Cart Recovery | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + e-ticaret API |
| Lead Qualification Agent | Orta | ⭐⭐⭐⭐ | Instagram Graph API |
| Ad Copy Generator | Orta | ⭐⭐⭐⭐ | Meta Ads API |
| Campaign Performance Analyst | Orta | ⭐⭐⭐⭐ | Meta Analytics API |
| Content Moderation Agent | Orta | ⭐⭐⭐ | Instagram Graph API |
| Retargeting Agent | Orta | ⭐⭐⭐⭐ | Meta Pixel + Ads API |
| FIFA World Cup Campaign Agent | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + Instagram |
| B2B SDR Agent | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + Email + Telegram |
| WhatsApp RAG Knowledge Agent | Kolay | ⭐⭐⭐⭐⭐ | WhatsApp + Vector DB |

---

## 2. Yeni Keşif: WhatsApp RAG Knowledge Agent

### CaseAI — 2 Dakikada WhatsApp AI Agent
**Link:** https://www.caseai.ai

No-code platform. Knowledge base yükleyip WhatsApp AI agent oluşturma.

**Kullanım Adımları:**
1. Knowledge base dosyalarını yükle (PDF, CSV, web sitesi)
2. Agent'ı eğit
3. WhatsApp Business API'ye bağla
4. Canlıya al

**Fiyatlandırma:** ~$99/ay

### Manuel Geliştirme: WhatsApp + RAG + Claude

```python
# RAG tabanlı WhatsApp agent (pseudo-code)
1. Knowledge base → Embeddings (Claude API)
2. Kullanıcı mesajı → Embed query
3. Cosine similarity → En yakın 3 cevap
4. Claude'a context + soru → Yanıt
5. WhatsApp üzerinden cevap
```

---

## 3. Yeni Keşif: AaaS — Agent as a Service
**Link:** https://github.com/Tem-Degu/streetai-aaas (HN: 2026-05-11, 2 pts)

Messaging apps için AI agent build etme ve deploy etme platformu. Natural language ile çalışıyor.

**Özellikler:**
- Multi-platform destek (WhatsApp, Telegram, web)
- No-code builder
- Natural language workflow
- Analytics dashboard

---

## 4. FIFA World Cup 2026 Campaign Agent

### Otomatik Maç Takibi + Ürün Önerisi

**Workflow (n8n + Claude + WhatsApp Business API):**
```
1. Maç Takvimi API → Yaklaşan maçları çek
2. Maçtan 1 saat önce → Claude ile kişiselleştirilmiş hatırlatma mesajı oluştur
3. WhatsApp üzerinden gönder
4. Maç bitti → Skor analizi + ürün önerisi
5. Tekrar WhatsApp ile gönder
```

**Metrikler:**
- Maç saatlerinde sepet terk oranı: %40 (normalde %70)
- WhatsApp hatırlatma ile %10-15 ek geri dönüşüm
- Dünya Kupası boyunca 5 milyar+ izleyici

---

## 5. Meta Business Agent Global Kullanım

### Artık Global Erişilebilir
**Kaynak:** TechCrunch, 3 Haziran 2026

Meta Business Agent artık WhatsApp, Facebook ve Instagram'da global olarak kullanılabilir durumda.

**Neler Yapabiliyor:**
- Müşteri sorularını otomatik yanıtlama
- Sipariş takibi
- Randevu rezervasyonu
- Ürün önerisi
- 70+ dil desteği

**Fiyatlandırma:** $200/ay (Hatch plan)

### Nasıl Erişilir:
1. Meta Business Suite → AI agents bölümü
2. "Create Agent" → İşletme kategorisi seç
3. Bilgi bankası yükle (FAQ, ürün bilgileri)
4. WhatsApp/Instagram/Facebook'a bağla

---

## 6. Adım Adım: Meta Business Agent Kurulumu

```
1. Meta Business Suite'e git (business.facebook.com)
2. "AI Agents" sekmesine tıkla
3. "Create your first agent" seç
4. Agent tipini seç:
   - Customer support agent
   - Sales agent
   - Booking agent
5. Knowledge base oluştur (FAQ, ürünler, politikalar)
6. Entegrasyonları ayarla:
   - WhatsApp Business API
   - Instagram Direct
   - Facebook Messenger
7. Test et ve canlıya al
```

---

## 7. Herkesin Kaçırdığı Nokta

**#1 — Meta Rakiplerine WhatsApp Erişimi Veriyor**
Meta, OpenAI ve Anthropic gibi şirketlere WhatsApp üzerinden sınırlı AI erişimi sunuyor. Bu, WhatsApp'ı bir "AI agent marketplace"e dönüştürecek hamle. Bugün Meta Business Agent kullananlar, yarın kendi agent'larını marketplace'de satabilecek.

**#2 — FIFA Dünya Kupası = En Büyük E-ticaret Fırsatı**
2026 Dünya Kupası 5+ milyar izleyici. Maç saatlerinde alışveriş terk oranı %40'a düşüyor. WhatsApp hatırlatma ile %10-15 ek dönüşüm. Bu fırsatı kaçıran e-ticaret şirketleri büyük kayıp yaşayacak.

---

## 8. Kaynaklar

- https://www.caseai.ai
- https://github.com/Tem-Degu/streetai-aaas
- https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/
- https://developers.facebook.com/docs/whatsapp/overview
- https://cardynal.io
