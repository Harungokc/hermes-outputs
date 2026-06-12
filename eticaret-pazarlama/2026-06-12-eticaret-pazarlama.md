# E-Ticaret & Dijital Pazarlama Araştırması
**Tarih:** 12 Haziran 2026, Cuma
**Bot:** Her gün 10:00 (E-ticaret & Pazarlama)

---

## 12 Haziran 2026 — Yeni Bulgular

### 1. AI Agent'ların E-Ticaret'e Etkisi — "Herkesin Kaçırdığı Nokta"

**Kaynak:** Hacker News - Mersel AI launch (Feb 2026)

Herkes "AI agent'lar alışveriş yapacak" diyor. Ama asıl hikaye daha başka:

AI agent'lar (ChatGPT, Perplexity) e-ticaret sitelerini ZİYARET EDİYOR ama CİTATION YAPMIYOR.

**Neden?** Yapısal bir sorun:
- LLMs raw HTML parse ediyor
- JavaScript-rendered content'i skip ediyor
- Yotpo/Judge.me gibi review widget'ları görünmüyor
- React'te gömülü ürün dataları yanlış okunuyor

**Sonuç:** Google'da 1. sırada olsan bile, AI answer'larda YOKSUN.

**Kritik Rakamlar:**
- ChatGPT'ye yönlendirilen trafiğin dönüşüm oranı: **%15.9** (Google organic: %1.76)
- ABD perakende AI referans trafiği: **%4,700 yıllık büyüme** (Adobe, mid-2025)
- ChatGPT'nin cita ettiği URL'lerin **%80'i** Google top 100'de değil (Ahrefs)

**İlginç Açı:** Bu aslında yeni bir SEO türü — "GEO" (Generative Engine Optimization). Siteler artık sadece Google için değil, AI agent'lar için de optimize edilmeli. Yapısal data, server-side HTML, schema.org Product zorunlu.

**Türkiye Fırsatı:** Türk e-ticaret siteleri (Trendyol, Hepsiburada, n11) AI agent dostu değil. Erken adapte olanlar avantaj kazanır.

---

### 2. AI E-Ticaret Agent'ları — Gerçek Kullanım Örnekleri

**Kaynak:** HN araştırması, 2026

#### a) PixelRipple.ai — AI Ads Agent for E-commerce
- **Ne yapıyor:** Viral sosyal reklamları keşfediyor, yapısını kopyalıyor, üretim-hazır kreativler oluşturuyor
- **Buld:** AI + deneyimli mühendis = **10x verimlilik**. AI + deneyimsiz = **3x + teknik borç**
- **İlginç kısım:** Context window duvarı — 3-4 hafta sonra kod tabanında 8 component'te duplicate fetch(), 3 farklı kredi validasyonu, Stripe webhook race conditions
- **Öğrenme:** 3 terminal window + 2 Claude instance paralel çalışıyor, ama paralelizasyon duplication problemi artırıyor

#### b) Octogen — E-commerce Capabilities for AI Agents
- **Ne yapıyor:** Herhangi bir e-ticaret sitesinden unified product catalog çıkarıyor (schema.org/Product superset)
- **Agentic checkout:** Herhangi bir sitede sanal kartla ödeme yapabiliyor
- **Kullanım:** AI agent'lar RAG-based product search yapabiliyor, tam checkout akışı gerçekleştirebiliyor
- **Önemli:** ~95% store otomatik işleniyor

#### c) Neuwark — AI Agent for E-commerce Marketing Emails
- **Ne yapıyor:** Ürün, offer, promosyon detaylarını yazıyorsunuz → agent tam email yazıyor (subject, structure, tone, CTA)
- **Sonuç:** Email writing'i saatlerden saniyelere indiriyor, doğal insan tonunu koruyor

#### d) Ecommerce CFO Skill — Diagnostic Frameworks for AI Agents
- **Ne yapıyor:** AI agent'ları için e-ticaret finansal teşhis framework'leri
- **Kullanım:** Agent'lar karar destek, maliyet analizi, ROI hesaplama yapabiliyor

---

### 3. AI Agent E-ticaret Workflow'ları — Popüler Kategoriler

**Kaynak:** GitHub Awesome E-Commerce Skills listesi (finsilabs)

11 kategori AI agent e-ticaret workflow'ı:
1. **Müşteri Hizmetleri** — Triyaj, yönlendirme, çok dilli destek, duygu analizi
2. **Satış & CRM** — Lead scoring, otomatik takip, rakip karşılaştırma
3. **İçerik Üretimi** — Blog, sosyal medya, çeviri, görsel + alt text
4. **Finans & Muhasebe** — Fatura işleme, anomali tespiti, raporlama
5. **E-ticaret & Lojistik** — Stok tahmini, terk edilmiş sepet, kargo optimizasyonu
6. **Abandoned Cart Recovery** — WhatsApp hatırlatması (1s, 24s, 72s), %10-15 ek dönüşüm

---

### 4. E-ticaret Dönüşüm Optimizasyonu — Meta-Analiz

**Kaynak:** Qubit meta-analysis (2017 ama hâlâ referans)

E-ticaret deneylerinden çıkan sonuçlar:
- **Kişiselleştirme** en yüksek etki (%10-30 dönüşüm artışı)
- **Sosyal kanıt** (review, testimonials) kritik
- **Shipping maliyeti** en büyük terk nedeni — checkout'te göster
- **Mobil UX** artık opsiyonel değil, zorunlu

---

### 5. E-ticaret Platform Trendleri 2026

**Mcmaster.com — "Best E-commerce Site I've Ever Used"** (1402 HN puan)

Neden övgü aldı?
- Hiçbir gereksiz element yok
- Endüstriyel satış için optimize edilmiş arama
- Stok durumu her zaman doğru
- Checkout akışı dakikalar değil saniyeler

**İlginç Açı:** Amazon 1-Click patenti kaybetti (2017). Bu, e-ticaret'te tek-tık ödeme için rekabetin arttığı anlamına geliyor. Küçük oyuncular artık Amazon'un avantajına erişebilir.

---

## Önceki Günlerden Devam Eden Bulgular

### E-ticaret AI Otomasyon Trendleri
- Instagram → WhatsApp → 1 dk'da sipariş sistemi en yüksek ROI'li workflow
- WhatsApp Business AI agent ile %10-15 terk edilmiş sepet kurtarma
- n8n + Claude Code workflow otomasyonu Türk pazarında henüz yeterince bilinmiyor

---

## Metrikler Özeti

| Metrik | Değer | Kaynak |
|--------|-------|--------|
| AI referral traffic büyüme (US retail) | %4,700 YoY | Adobe, mid-2025 |
| ChatGPT referral CVR | %15.9 | Ahrefs |
| Google organic CVR | %1.76 | Ahrefs |
| AI citation'daki URL'ler Google top 100'de değil | %80 | Ahrefs |
| AI + deneyimli mühendis verimliliği | 10x | PixelRipple deneyimi |
| AI + deneyimsiz developer | 3x + borç | PixelRipple deneyimi |
| Abandoned cart recovery (WhatsApp) | %10-15 ek dönüşüm | Industry avg |

---

## Türkiye'ye Uyarlanabilirlik

### Fırsatlar:
1. **GEO (Generative Engine Optimization)** — Türk e-ticaret siteleri AI agent dostu değil, erken adapte avantajı
2. **WhatsApp abandoned cart** — Türkiye'de WhatsApp kullanımı yüksek, 1s/24s/72s hatırlatma sistemleri
3. **Instagram → WhatsApp AI bot** — E-ticaret için en yüksek ROI'li workflow Türkiye'de henüz yeterince kullanılmıyor

### Engeller:
1. WhatsApp Business API maliyeti (Meta pricing değişken)
2. Türkçe NLP modelleri henüz İngilizce kadar güçlü değil
3. E-ticaret sitelerinin çoğu JavaScript-heavy → AI crawler zorlukları

---

## Kaynaklar

1. https://www.mersel.ai — GEO (ChatGPT/Perplexity readable websites)
2. https://www.pixelripple.ai — AI ads agent
3. https://octogen.ai — E-commerce capabilities for AI agents
4. https://github.com/finsilabs/awesome-ecommerce-skills — E-commerce skills for AI agents
5. https://www.qubit.com/sites/default/files/pdf/qubit_meta_analysis.pdf — E-commerce meta-analysis
6. https://hn.algolia.com/api/v1/search?query=ecommerce+AI+agent — HN data

---

*Son güncelleme: 2026-06-12 10:00*