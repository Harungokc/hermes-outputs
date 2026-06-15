# Meta İçin Yapılabilecek AI Ajansları
**Tarih:** 2026-06-15 12:00
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

---

## 2. Yeni Keşif: B2B SDR Agent (b2b-sdr-hermes-skill)

### Ne Yapıyor?
WhatsApp, Email ve Telegram üzerinden B2B satış ajanı. Lead discovery, qualification, quotation ve takip süreçlerini tam otomatik yapıyor.

**Workflow:**
```
Lead Discovery (web araması)
    ↓
BANT Qualification (sohbet üzerinden puanlama)
    ↓
Company Research (karar verici kimliklendirme)
    ↓
Quotation (teklif oluşturma)
    ↓
4-touch Outreach Sequence (e-posta serisi)
    ↓
Pipeline Report (günlük/haftalık)
```

**Kullanılan Teknolojiler:**
- Hermes Agent (ana beyin)
- WhatsApp Business API
- Claude API (GPT alternatifi)
- n8n (workflow otomasyonu)
- Web search (lead discovery)

**Kurulum:**
```bash
hermes skills install github:iPythoning/b2b-sdr-hermes-skill
```

**GitHub:** https://github.com/iPythoning/b2b-sdr-hermes-skill

---

## 3. claude-ops — Business Operating System (18⭐)

**Link:** https://github.com/Lifecycle-Innovations-Limited/claude-ops

Claude Code için 57 skills, 21 agent içeren business operating system.

**WhatsApp Unified Inbox Özelliği:**
- WhatsApp, Email, Slack, Telegram tek panelde
- Gelen mesajları otomatik sınıflandırma
- AI ile yanıt önerileri
- Cron ile pipeline inspection

**Diğer Entegrasyonlar:**
| Kategori | Araçlar |
|----------|---------|
| Marketing | Klaviyo, Meta Ads, GA4 |
| E-commerce | Shopify, Stripe, RevenueCat |
| Voice | Bland AI, ElevenLabs |
| AWS | Datadog, NewRelic, OTEL |
| PR | Autonomous PR merge |

---

## 4. Adım Adım: WhatsApp Business Agent Yapımı

### Gerekenler:
1. WhatsApp Business API hesabı
2. Meta Business Manager hesabı
3. n8n (workflow otomasyonu)
4. Claude API key veya OpenAI API key
5. WhatsApp Business uygulaması

### Adımlar:

**1. WhatsApp Business API Kurulumu:**
```
Meta Business Manager → WhatsApp Business → API Setup
Phone Number ekle
Test phone number ile API token al
```

**2. n8n Workflow:**
```
Trigger: Webhook (WhatsApp'tan gelen mesaj)
    ↓
LLM Node: Mesajı analiz et, intent'i belirle
    ↓
Switch: Intent'e göre yönlendir
    - Sipariş sorgusu → Ürün veritabanı
    - Şikayet → Destek ekibi
    - Fiyat → Otomatik teklif
    ↓
WhatsApp Node: Yanıt gönder
```

**3. Template Message Ayarlama:**
- Meta Business Manager → Message Templates
- Her senaryo için template oluştur
- Template onay süreci: ~24 saat

**4. Claude Entegrasyonu:**
```
n8n HTTP Request → Claude API
Prompt: "Bu müşteri mesajına doğal bir yanıt ver"
Yanıtı al → WhatsApp'a gönder
```

---

## 5. Herkesin Kaçırdığı Nokta

### #1 — B2B İçin WhatsApp = En Etkili Kanal
Herkes B2C'de WhatsApp'ı konuşuyor. B2B'de ise kimse kullanmıyor. 

Gerçek şu: WhatsApp B2B'de email'den 3x daha yüksek açılma oranına sahip. Karar vericilere doğrudan mesaj atabilmek = avantaj.

b2b-sdr-hermes-skill tam bu boşluğu dolduruyor.

### #2 — n8n + Claude + WhatsApp = Gold Standard
En düşük maliyetli, en esnek AI agent mimarisi:

- n8n: Workflow otomasyonu (hosted veya self-hosted)
- Claude: Doğal dil işleme
- WhatsApp: Müşteri iletişimi

Aylık maliyet: ~$20-50 (API key'ler dahil)

### #3 — FIFA World Cup Agent = Hemen Yapılabilir
2026 FIFA Dünya Kupası = En büyük fırsat.

**Workflow:**
```
Maç Takvimi API
    ↓
n8n (maç 1 saat kala tetikle)
    ↓
Claude (kişiselleştirilmiş mesaj oluştur)
    ↓
WhatsApp (müşteriye gönder)
    ↓
Maç sonrası → Ürün önerisi
```

---

## 6. Görsel Önerisi — LinkedIn Post

**Konsept:** "B2B WhatsApp Agent" mimari diyagramı

**Tasarım:**
- Sol: Lead kaynakları (web, LinkedIn, fuar)
- Orta: n8n + Claude beyin
- Sağ: WhatsApp + Email + Telegram çıktıları
- Alt: Metrikler (açılma oranı, dönüşüm)

**Renk:** WhatsApp yeşili + Claude mavisi

---

## 7. LinkedIn Post Fikri

**Başlık:** B2B'de WhatsApp kullanmak = rakiplerinizi 3x geride bırakmak

**İçerik:**

Email açılma oranı: %20-30
WhatsApp açılma oranı: %70-80

B2B satışta WhatsApp kullanmak, email'e göre 3x daha etkili.

Ama kimse yapmıyor.

Yeni keşfettiğim b2b-sdr-hermes-skill bunu tamamen otomatik yapıyor:

- Lead discovery → Web aramasıyla potansiyel alıcıları buluyor
- BANT qualification → Sohbet üzerinden puanlama
- Personalized outreach → 4-touch email serisi
- Daily pipeline reports → Her sabah durum özeti

Toplam maliyet: $0 (açık kaynak)

B2B satışta WhatsApp'ı kimse kullanmıyor. Siz ilk olun.

#B2B #WhatsApp #SATIŞ #AI #Otomasyon

---

## 8. Kaynaklar

- GitHub b2b-sdr-hermes-skill: https://github.com/iPythoning/b2b-sdr-hermes-skill
- GitHub claude-ops: https://github.com/Lifecycle-Innovations-Limited/claude-ops
- Meta Business Agent: https://business.whatsapp.com/business-agent
- Meta Developers WhatsApp: https://developers.facebook.com/docs/whatsapp
