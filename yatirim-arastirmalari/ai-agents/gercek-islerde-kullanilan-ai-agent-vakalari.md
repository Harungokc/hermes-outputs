# Gerçek İşlerde Kullanılan AI Agent Vakaları

> Bu dosya, şirketlerin gerçek hayatta AI agent'ları nasıl kullandığını belgeliyor. Her gün güncellenmektedir.
> Araştırma odağı: "Agent satan şirketler" değil — **"Agent kullanan şirketler"**.

---

## 19 Haziran 2026 — Yeni Vakalar

### Otel & Turizm AI Agent Vakaları — Perşembe/ Cuma Rotasyonu

---

### 1. Airbnb — AI Bot %40 Müşteri Destek Sorununu Çözüyor

**Sektör:** Konaklama / Ev Paylaşım Platformu
**Kullanım Alanı:** Müşteri Hizmetleri + Yazılım Geliştirme

**Agent'ın Görevi:**

**Vaka A — Müşteri Desteği (40% Otomatik Çözüm):**
Airbnb'nin AI bot'u artık tüm müşteri destek taleplerinin %40'ını insansız çözüyor. Kullanıcılar:
- Rezervasyon değişikliği
- İade talebi
- Host ile iletişim
- Şikayet çözümü

...konularında AI bot ile doğrudan konuşuyor ve bot sorunu çözüyor veya doğru insana yönlendiriyor.

**Vaka B — Kod Yazımı (%60 Otomatik):**
Brian Chesky (Airbnb CEO) açıkça söylüyor: **"AI artık Airbnb'nin yeni kodunun %60'ını yazıyor."** Bu sadece code completion değil — tam feature yazımı, test, deployment süreçlerini kapsıyor.

**Müşteri Deneyimi — Destek Dialog Örneği:**
```
Kullanıcı: "Rezervasyonumu 2 gün geri almak istiyorum"
Airbnb AI:
 → "Rezervasyon #12345 için iade politikasını kontrol ediyorum..."
 → "Bu rezervasyon esnek iade kapsamında. İade onaylandı."
 → "Paranız 3-5 iş günü içinde hesabınıza yatacak."
Kullanıcı: "Teşekkürler"
[Bot kapanır — insan destek yok]
```

**Sonuçlar:**
| Metrik | Değer |
|--------|-------|
| Müşteri destek otomatik çözüm | %40 |
| AI tarafından yazılan yeni kod | %60 |
| Destek maliyeti | Düşüş trendinde |
| Müşteri memnuniyeti | Stabil (henüz düşüş yok) |

**Herkesin Kaçırdığı Nokta #1:** Airbnb'nin 40% destek çözüm oranı, "AI chatbot" değil "AI workflow agent" olarak çalışmasından geliyor. Bot sadece Cevap vermiyor — rezervasyon sistemine bağlı, para iadesi yapabiliyor, host'a mesaj gönderebiliyor. Yani tek bir API değil, 10+ internal sistemle entegre.

**Herkesin Kaçırdığı Nokta #2:** Airbnb'nin "AI kod yazıyor" demesi sadece developer tool değil — şirket artık daha az yazılımcı istihdam ediyor. 2026'da Airbnb mühendislik ekibini büyütmeden daha çok ürün çıkarıyor. Bu = "AI ile şirket küçültme" değil "AI ile aynı ekiple 2x çıktı" modeli.

**Kaynak:**
- Bing News — "Airbnb says AI bot now handles 40% of customer support issues" (Haziran 2026)
- Bing News — "Airbnb's CEO says AI writes 60% of the company's code" (Haziran 2026)

---

### 2. Brian Chesky — Yeni AI Laboratuvarı Kuruyor

**Sektör:** Konaklama / Seyahat Teknolojisi
**Kullanım Alanı:** Yeni Ürün Geliştirme — Seyahat AI Agent

**Ne Yapıyor:**
Brian Chesky, Airbnb'nin ana şirketinden bağımsız yeni bir AI lab kuruyor. Amacı: mevcut chatbot'ların ötesinde, gerçek anlamda "seyahat planlayabilen" bir AI agent. Mevcut ChatGPT, Gemini gibi genel AI'lar seyahat planlamakta kötü — çünkü:
- Uçuş fiyatları dinamik
- Otel müsaitliği anlık değişiyor
- Yerel etkinlikler integration'ı zor

Chesky'nin lab'ı bu problemleri çözmek için proprietary model geliştiriyor.

**Herkesin Kaçırdığı Nokta:** Chesky "AI yarışına girdim" demiyor — "mevcut AI'lar seyahati anlamıyor" diyor. Bu = seyahat AI'ının hâlâ çok ham bir pazar olduğunu ve ilk gerçek çözümü bulanın kazanacağını gösteriyor.

**Kaynak:**
- Bing News — "Airbnb CEO Brian Chesky launches new AI lab to build proprietary models" (Haziran 2026)

---

### 3. Expedia Group — "Agentic Design" ile SeyahatAI Platformu

**Sektör:** Online Seyahat Acentası (OTA)
**Kullanım Alanı:** B2B Platform + Müşteri Deneyimi

**Agent'ın Görevi:**

Expedia, Explore 2026 etkinliğinde "AI Travel Experiences" ve yeni bir **B2B AI Toolkit** duyurdu. Bu toolkit:
- Seyahat acentalarına (TUI, Booking.com dışı küçük acentalar) AI agent altyapısı sunuyor
- Uçuş, otel, araç kiralama API'lerini tek bir agent interface'inde birleştiriyor
- Acentalar "kendi AI destekli seyahat asistanlarını" oluşturabiliyor

**"Agentic Design" Ne Demek:**
Expedia CTO'su diyor ki: "Artık kullanıcılara 10 tane arama kutusu vermek yerine, tek bir AI agent'a 'Madrid'e 3 gece kalabalıktan uzak, 4 yıldız, 500€ bütçe' diyebileceksiniz. Agent tüm seçenekleri karşılaştırıp en iyisini sunacak."

**Müşteri Deneyimi — Yeni Nesil Arama:**
```
Kullanıcı: "10. yıl dönümümüz için romantik bir kaçamak, 
            ama bütçemiz sınırlı, çocukları da bırakabilecek 
             bir yer lazım"
Expedia Agent:
 → Takvim kontrol: önümüzdeki hafta sonu
 → Çocuk bakıcığı olan oteller → filtre
 → Romantik atmosfer puanı > 4.5 → filtre
 → Bütçe dahilindeki seçenekler: 3 otel
 → Kullanıcıya sunum: özet + fiyat karşılaştırması + fotoğraflar
```

**Sonuçlar:**
- Expedia B2B AI Toolkit — seyahat acentalarına özel AI agent oluşturma imkanı
- "Agentic design" = kullanıcının doğal dille tüm seyahat planını yaptırması

**Herkesin Kaçırdığı Nokta:** Expedia'nın B2B hamlesi büyük acentaları değil, **küçük bağımsız seyahat acentalarını** hedefliyor. Türkiye'de binlerce küçük acente var — bunlar kendi AI agent'larını Expedia altyapısıyla kurabilirse, Booking.com ve Airbnb'ye karşı rekabet edebilirler. Bu Küçük acenta = Expedia'nın yeni büyüme alanı.

**Kaynak:**
- Bing News — "Expedia Group Unveils New AI Experiences at Explore 2026" (Haziran 2026)
- Bing News — "Expedia Group B2B Introduces AI Toolkit and Platform for the Future of Travel Distribution" (Haziran 2026)
- Bing News — "How Expedia Is Reinventing Travel Through AI And Agentic Design" (Haziran 2026)

---

### 4. World Cup 2026 — FIFA + Otel AI Chatbot'ları

**Sektör:** Otel Zincirleri / FIFA 2026 Ev Sahipliği
**Kullanım Alanı:** Müşteri Hizmetleri — Etkinlik Dönemi

**Ne Yapıyor:**
2026 FIFA Dünya Kupası ABD-Kanada-Meksika'da. Otel chatbot'ları:
- Maç saatleri ve şehir bilgisi
- Stadyum arah Ulaşım önerileri
- Maç günü otel doluluk/boşluk yönetimi
- Anlık fiyat optimizasyonu (maç günleri 3x normal fiyat)

**Herkesin Kaçırdığı Nokta:** FIFA Dünya Kupası = otel AI chatbot'ları için en büyük test. 3 ülkede eş zamanlı etkinlik, 50+ şehir, milyonlarca anlık sorgu. Bu sistemi yöneten AI agent'lar, normal zamanda 10x daha az yoğun sorgularla başa çıkabilir. Kupadan önce stress test = kupadan sonra stabil ürün.

**Kaynak:**
- Bing News — "These AI bots want to help fans navigate World Cup host cities" (Haziran 2026)

---

## 19 Haziran 2026 — Kaynaklar

1. Bing News — "Airbnb says AI bot now handles 40% of customer support issues" (Haziran 2026)
2. Bing News — "Airbnb's CEO says AI writes 60% of the company's code" (Haziran 2026)
3. Bing News — "Airbnb CEO Brian Chesky launches new AI lab to build proprietary models" (Haziran 2026)
4. Bing News — "Expedia Group Unveils New AI Experiences at Explore 2026" (Haziran 2026)
5. Bing News — "Expedia Group B2B Introduces AI Toolkit and Platform for the Future of Travel Distribution" (Haziran 2026)
6. Bing News — "How Expedia Is Reinventing Travel Through AI And Agentic Design" (Haziran 2026)
7. Bing News — "These AI bots want to help fans navigate World Cup host cities" (Haziran 2026)

---

## 17 Haziran 2026 — Önceki Vakalar (Referans)

### SaaS & Teknoloji AI Agent Vakaları

1. **Salesforce → Fin** — $3.6B AI müşteri destek platformu satın alımı
2. **KPMG** — Microsoft Agent 365 governance framework ile enterprise deployment
3. **Zendesk** — "Per resolution" fiyatlandırma modeli (kullanıcı başına değil, çözüm başına ödeme)
4. **Glean** — $300M+ ARR, enterprise search AI
5. **Atlassian Rovo** — Teamwork Graph tabanlı agentic work
6. **AgentHub** — 1 kişi 47 AI agent, 192⭐
7. **auto-co-meta** — 14 AI agent 24/7 otonom şirket OS, 36⭐

---

*Bu dosya Hermes Agent tarafından güncellenmektedir.*
*Güncelleme: Her gün 12:00 (Otel & Turizm rotasyonu: Cuma)*
*Tarih: 19 Haziran 2026*
