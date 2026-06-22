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

## 20 Haziran 2026 — Yeni Vakalar

### Otel & Turizm AI Agent Vakaları — Cuma Rotasyonu (Devam)

---

### 1. Zendesk — "Per Resolution" AI Agent Fiyatlandırma Modeli

**Sektör:** Customer Service SaaS
**Kullanım Alanı:** Müşteri Hizmetleri — AI Agent Fiyatlandırma

**Ne Yapıyor:**
Zendesk, Mayıs 2026'da Relate 2026 konferansında "Autonomous Service Workforce" vizyonunu duyurdu. Yenilikçi özellik: **AI agent'lar artık "koltuk başına" değil, "çözüm başına" faturalandırılıyor.**

Müşteriler sadece AI tarafından başarıyla çözülen destek talepleri için ödeme yapıyor. Bu büyük bir shift: geleneksel SaaS "kullanıcı başına" modelinden "outcome-based" modele geçiş.

**Müşteri Deneyimi — Dialog Örneği:**
```
Müşteri: "Siparişim gecikti, ne zaman gelir?"
Zendesk AI Agent:
 → Sipariş veritabanını kontrol eder
 → Kargo API'sinden canlı takip bilgisi çeker
 → Müşteriye kesin teslimat tarihi verir
 → Sorun çözüldü → "1 resolution" olarak sayılır
 → Şirket sadece bu çözüm için öder
Müşteri: [Sorun çözüldü, memnuniyet puanı verir]
```

**Sonuçlar:**
| Metrik | Değer |
|--------|-------|
| Fiyatlandırma modeli | Koltuk başına → Çözüm başına |
| AI platform genişlemesi | ChatGPT, Gemini, voice, messaging |
| Desteklenen dil | 60+ dil |
| Hedef | AI = emek birimi olarak tanımlanıyor |

**Herkesin Kaçırdığı Nokta #1:** "Per resolution" fiyatlandırma sadece bir pricing yeniliği değil — AI agent'ların performansını ölçmenin yeni standardı. Artık şirketler "kaç tane bot çalıştırıyoruz" değil, "bot kaç problem çözüyor" diye bakıyor. Bu = AI agent ROI'sini kanıtlama zorunluluğu.

**Herkesin Kaçırdığı Nokta #2:** Zendesk'in 60+ dil desteği, global şirketler için kritik. Türk şirketleri de İngilizce bilmeyen müşterilerine aynı AI kalitesini verebiliyor — bu daha önce lükstü, şimdi standart olacak.

**Kaynak:**
- Bing News — "At Relate 2026, Zendesk Launches AI Agents Priced on Resolutions, Not Seats" (19.05.2026)
- Bing News — "Zendesk links AI pricing to verified resolution outcomes" (22.05.2026)
- Bing News — "Zendesk expands AI agents across ChatGPT, Gemini, voice and messaging" (21.05.2026)

---

### 2. Titan Brands Hospitality Group + AgenticFlo — Agentic AI Core Operations

**Sektör:** Otel & Konaklama / Las Vegas
**Kullanım Alanı:** Operasyonlar — Temizlik, Bakım, Kat Hizmetleri

**Ne Yapıyor:**
Titan Brands Hospitality Group (Las Vegas merkezli otel operatörü), AgenticFlo ile ortaklık kurdu. AgenticFlo'nun agentic AI çözümlerini otel operasyonlarına entegre ediyor.

Operasyonel alanlar:
- Oda temizlik triyajı (hangı oda önce temizlenecek, hangi kat personeli atanacak)
- Bakım taleplerinin akıllı yönlendirmesi
- Envanter yönetimi ve otomatik sipariş
- Enerji optimizasyonu (oda sıcaklığı, aydınlatma AI kontrolü)

**Herkesin Kaçırdığı Nokta:** Las Vegas otel operatörleri = en rekabetçi pazar. Kumarhaneler, resort'lar, boutique oteller bir arada. Agentic AI burada başarılı olursa, her otel grubuna satılık ürün hazır demek. Türkiye'deki otel zincirleri de benzer operasyonel maliyet sorunları yaşıyor — bu teknoloji doğrudan uygulanabilir.

**Kaynak:**
- Bing News — "Titan Brands Hospitality Group Deploys Agentic AI Across Core Operations" (Nevada Business Magazine, Mayıs 2026)

---

### 3. Accor — 4 Stratejik AI Bahsi

**Sektör:** Otel Zincirleri (Global)
**Kullanım Alanı:** Stratejik Planlama — Dağıtım, Sadakat, Operasyonlar

**Ne Yapıyor:**
Accor (Novotel, Ibis, Raffles, Fairmont gibi markaların sahibi) CEO düzeyinde AI vizyonunu açıkladı. 4 stratejik bahis:

1. **Marka Dağıtımı** — AI ile dinamik fiyatlandırma ve tedarikçi yönetimi
2. **Sadakat Programları** — AI-driven personalizasyon, üye deneyimi
3. **Operasyonlar** — Oda doluluk tahmini, персонал planlama, enerji yönetimi
4. **Guest Experience** — AI concierge, talep tahmini

**Herkesin Kaçırdığı Nokta:** Accor gibi dev şirketler AI'yı "müşteri chatbot'undan" çok operasyonel verimliliğe odaklı görüyor. Türkiye'deki 5 yıldızlı oteller de aynı operasyonel maliyet sorunları yaşıyor — ama henüz bu ölçekte AI adoption yok. 1-2 yıl içinde erken adapte eden oteller ciddi rekabet avantajı yakalayacak.

**Kaynak:**
- Bing News — "4 Bets Accor Is Making on AI and the Future of Hospitality" (Skift, Mayıs 2026)

---

### 4. HN Insight — "Trillions of Dollars Spent Just to Work on Customer Services"

**Sektör:** Genel — Müşteri Hizmetleri Ekonomi
**Kullanım Alanı:** Pazar Büyüklüğü — AI Agent Fırsatı

**Ne Yapıyor:**
Bir HN kullanıcısı, müşteri hizmetlerine harcanan paradan bahsetti. Rakamlar çarpıcı: Küresel müşteri hizmetleri pazarı **trilyonlarca dolar** seviyesinde. AI agent'lar bu pazarda devrim yaratma potansiyeli taşıyor.

**Metrik:**
| Alan | Değer |
|------|-------|
| Küresel müşteri hizmetleri pazarı | Trilyonlarca $ |
| AI otomasyon potansiyeli | %30-60 maliyet düşüşü |
| En büyük fırsat alanı | Sepeti terk eden müşteriler, basit talep triyajı |

**Herkesin Kaçırdığı Nokta:** "Trilyonlarca dolar" denilince insanlar B2C customer service'i düşünüyor. Ama asıl fırsat B2B. Kurumsal şirketlerin müşteri hizmetleri (technical support, onboarding, renewals) = daha yüksek marj, daha az rekabet. Türk SaaS şirketleri için bu alan = yüksek değerli Müşteri destek AI agent'ları.

**Kaynak:**
- HN — "Trillions of dollars spent just to work on customer services?" (8 points, 19.06.2026)

---

## 20 Haziran 2026 — Kaynaklar

1. Bing News — "At Relate 2026, Zendesk Launches AI Agents Priced on Resolutions, Not Seats" (19.05.2026)
2. Bing News — "Zendesk links AI pricing to verified resolution outcomes" (22.05.2026)
3. Bing News — "Zendesk expands AI agents across ChatGPT, Gemini, voice and messaging" (21.05.2026)
4. Bing News — "Titan Brands Hospitality Group Deploys Agentic AI Across Core Operations" (Nevada Business Magazine, Mayıs 2026)
5. Bing News — "4 Bets Accor Is Making on AI and the Future of Hospitality" (Skift, Mayıs 2026)
6. HN — "Trillions of dollars spent just to work on customer services?" (8 points, 19.06.2026)

---

## 19 Haziran 2026 — Önceki Vakalar (Referans)
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
*Güncelleme: Her gün 12:00 (Cumartesi/Pazar: Genel Araştırma — YC Launches + Enterprise Deployments)*
*Tarih: 21 Haziran 2026*

---

## 21 Haziran 2026 — Yeni Vakalar

### Genel Araştırma — YC Launches + Enterprise Deployments (Cumartesi/Pazar Rotasyonu)

---

### 1. Walmart — AI Kullanımına Maliyet Üst Limitleri Geliyor

**Sektör:** Perakende / Süpermarket Zinciri
**Kullanım Alanı:** İç Operasyonlar — AI Maliyet Kontrolü

**Ne Yapıyor:**
Walmart, çalışanlarının kullandığı AI araçlarına **maliyet üst limiti** koymaya başladı. Şirket yetkilileri, AI araçlarına olan talebin beklenmedik şekilde yüksek olduğunu ve maliyetlerin hızla arttığını belirtiyor.

**Neden Önemli:**
Amazon'dan sonra Walmart da AI kullanımını kısıtlama kararı aldı. Her iki şirket de çalışanlarına "AI kullanmak için AI kullanmayın" mesajı veriyor.

**Herkesin Kaçırdığı Nokta #1:** Amazon ve Walmart'ın bu kararı, AI agent'ların "fırsat maliyeti" henüz tam anlaşılamadığını gösteriyor. Çalışanlar AI'yı kullanıyor ama tam olarak verimli kullanıp kullanmadıkları ölçülmüyor. Sonuç: şirketler AI maliyetini kontrol edemez hale geliyor.

**Herkesin Kaçırdığı Nokta #2:** Bu haber aslında AI'ın ne kadar hızlı benimsendiğinin kanıtı. 1-2 yıl önce "çalışanlar AI kullanmıyor" şikayeti vardı. Şimdi "çok kullanıyorlar" şikayeti geliyor. Sorun = AI'ın kendisi değil, AI kullanımını yönetme kapasitesinin eksikliği.

**Kaynak:**
- Bing News — "AI getting too expensive? Walmart starts putting cap on AI use for employees after rising cost" (Haziran 2026)
- Bing News — "Amazon, Walmart and Uber curb employee AI use as costs surge" (Haziran 2026)

---

### 2. Amazon — "Tokenmaxxing": AI Kullanım Metriklerini Şişiren Çalışanlar

**Sektör:** E-ticaret / Teknoloji
**Kullanım Alanı:** İç Gözetim — AI Kullanım Metrikleri

**Ne Yapıyor:**
Amazon, çalışanları arasında **"tokenmaxxing"** olarak adlandırılan bir fenomen ile karşı karşıya. Şirket, AI kullanım metriklerini yüksek göstermek için çalışanların gereksiz AI sorguları oluşturduğunu tespit etti. Sonuç: şirket içi **token leaderboard** kapatıldı.

| Olgu | Değer |
|------|-------|
| Tokenmaxxing nedeni | Performans değerlendirmesi / bonus beklentisi |
| AI kullanım metrikleri | Yapay olarak şişirildi |
| Sonuç | Token leaderboard kapatıldı |

**Herkesin Kaçırdığı Nokta #1:** AI kullanım metrikleri = yeni "sahte KPI". Çalışanlar gerçek iş sonuçları yerine "kaç token harcadım" üzerinden değerlendirilince, her token'ı gereksiz yere kullanıyorlar. Bu = total maliyet patlaması.

**Herkesin Kaçırdığı Nokta #2:** Amazon ve Walmart'ın AI kullanım kısıtlamaları, AI agent'ların ROI'sini ölçmenin hâlâ çözülmemiş bir problem olduğunu gösteriyor. Şirketler AI'ı benimsiyor ama "ne kadar değer üretiyor" sorusunu cevaplayamıyor.

**Kaynak:**
- Bing News — "Amazon cracks down on AI tokenmaxxing after rising cost, tells employees don't use AI just to use AI" (Haziran 2026)
- Bing News — "Amazon joins Microsoft in sending shocking message to employees" (Haziran 2026)

---

### 3. Viktor — $75M Yatırım, Slack ve Teams İçinde "AI Coworker"

**Sektör:** Enterprise AI / Çalışan Üretkenliği
**Kullanım Alanı:** İç İletişim + İş Akışı Otomasyonu

**Ne Yapıyor:**
Viktor, Accel'den $75 milyon yatırım alarak Slack ve Teams içinde çalışan bir **AI coworker** ürünü gelştiriyor. Ürünün iddiası: "Her çalışanın 7/24 ulaşabileceği, işleri otomatik yapan bir AI meslektaş."

**Özellikler:**
- Slack/Teams içinde doğal dil ile iletişim
- Toplantı özetleri çıkarma
- E-posta ve mesaj trafiğini yönetme
- İş akışları oluşturma (IT ticket, onboarding, etc.)
- Şirket içi bilgi tabanlarından yanıt verme

**Herkesin Kaçırdığı Nokta #1:** Viktor'ın $75M alması = Accel'in bu alana olan güveni. Enterprise AI coworker = yeni "killer app". Microsoft'un Copilot'u kurumsal, Viktor ise "her boyuttaki şirket için" konumlanıyor.

**Herkesin Kaçırdığı Nokta #2:** Slack/Teams içinde AI coworker = en doğal adoption modeli. Çalışan yeni bir uygulama öğrenmek zorunda değil — aynı Slack'te @Viktor diyerek iş yaptırıyor. Bu = sıfır learning curve.

**Kaynak:**
- Bing News — "Exclusive: AI startup Viktor raises $75 million to put a virtual 'coworker' in Slack and Teams" (Haziran 2026)

---

### 4. Microsoft Scout — OpenClaw Tabanlı, "Hiç Uyumayan" AI Agent

**Sektör:** Enterprise SaaS / Microsoft Ekosistemi
**Kullanım Alanı:** Microsoft 365 — Otonom İş Otomasyonu

**Ne Yapıyor:**
Microsoft, Build 2026'da **Scout** adlı yeni AI agent'ı duyurdu. Scout:
- OpenClaw tabanlı (Microsoft'un açık kaynak agent framework'ü)
- Microsoft 365 içinde "always-on" çalışıyor
- Kullanıcı adına e-postaları yanıtlıyor, toplantıları planlıyor, belgeleri düzenliyor
- "Autopilot" serisinin ilk ürünü

**Maliyet:** $200/ay (Microsoft 365 Copilot üzerine ek)

**Herkesin Kaçırdığı Nokta #1:** Microsoft Scout = Microsoft'un "agentification" stratejisinin merkezi. Copilot = assistant (insan istiyor), Scout = agent (insan istemeden yapıyor). Bu = enterprise AI'da büyük paradigm shift.

**Herkesin Kaçırdığı Nokta #2:** OpenClaw tabanlı olması = Microsoft artık sadece kendi AI modelini değil, açık kaynak agent framework'lerini de kullanıyor. Bu = gelecekte Anthropic, OpenAI modelleri de Scout içinde çalışabilir demek.

**Kaynak:**
- Bing News — "Microsoft unveils Scout, an autonomous AI agent built on OpenClaw" (Build 2026, Haziran 2026)
- Bing News — "Microsoft launches new personal AI agent, Microsoft Scout" (Haziran 2026)

---

### 5. Norm AI — Microsoft 365 Copilot İçin Compliance Agent

**Sektör:** Compliance / Regülasyon Teknolojisi
**Kullanım Alanı:** Hukuk & Uyum — Otomatik Regülasyon Kontrolü

**Ne Yapıyor:**
Norm AI, Microsoft 365 Copilot içinde çalışan bir **compliance agent** duyurdu. Agent:
- Şirket içi e-postaları ve belgeleri tarıyor
- Regülasyon ihlali risklerini işaretliyor
- Yasal uyumluluk kontrollerini otomatik yapıyor
- Risk raporları üretiyor

**Kullanım Alanları:**
- Bankacılık ve finans sektörü (KYC/AML kontrolleri)
- Sağlık sektörü (HIPAA uyumu)
- Hukuk firmaları (client privilege kontrolleri)

**Herkesin Kaçırdığı Nokta #1:** Compliance = genellikle "engel" olarak görülür. Norm AI'ın yaklaşımı = compliance'ı agent workflow'una entegre etmek. Her e-posta gönderildiğinde veya belge paylaşıldığında arka planda compliance kontrolü çalışıyor.

**Herkesin Kaçırdığı Nokta #2:** Norm AI + Microsoft 365 Copilot = her çalışanın cebinde bir compliance asistanı. Daha önce sadece hukuk departmanı erişebilirdi, şimdi satış temsilcisi bile "bu sözleşme riskli mi?" diye sorabiliyor.

**Kaynak:**
- Bing News — "Norm Ai Launches Compliance Agent for Microsoft 365 Copilot" (Haziran 2026)

---

### 6. KPMG — Microsoft Agent 365 ile Global AI Agent Governance

**Sektör:** Danışmanlık / Big Four
**Kullanım Alanı:** Kurumsal Yönetişim — AI Agent Denetimi

**Ne Yapıyor:**
KPMG ve Microsoft, Agent 365 ve Copilot'u KPMG'nin global iş gücüne yaygınlaştırmak için ortaklık kurdu. KPMG'nin odak noktası: **AI governance** — şirket içinde kaç agent çalışıyor, kimler kullanıyor, hangi verilere erişiyor.

| Alan | Değer |
|------|-------|
| Kapsam | KPMG global iş gücü |
| Platform | Microsoft Agent 365 + Copilot |
| Odak | AI governance ve denetim |

**Herkesin Kaçırdığı Nokta #1:** KPMG'nin AI governance'a odaklanması = AI agent'ların şirket içinde "controlsız" büyümesi problemi. Her departman kendi agent'ını yapıyor, kimse kimseyi bilmiyor. KPMG = ilk büyük danışmanlık şirketi olarak bu alanda structured çözüm sunuyor.

**Herkesin Kaçırdığı Nokta #2:** Microsoft Agent 365 governance özellikleri = gelecekte tüm enterprise AI deployment'ların标配 olacak. Şirketler sadece "agent yapmak" değil "agent'ları yönetmek" için de platforma ihtiyaç duyuyor.

**Kaynak:**
- Bing News — "KPMG Deploys Microsoft Agent 365 to Govern AI Agents Across Its Global Firms" (Haziran 2026)
- Bing News — "KPMG and Microsoft scale trusted, enterprise AI agents globally" (Haziran 2026)

---

## 21 Haziran 2026 — Kaynaklar

1. Bing News — "AI getting too expensive? Walmart starts putting cap on AI use for employees after rising cost" (Haziran 2026)
2. Bing News — "Amazon cracks down on AI tokenmaxxing after rising cost" (Haziran 2026)
3. Bing News — "Exclusive: AI startup Viktor raises $75 million to put a virtual 'coworker' in Slack and Teams" (Haziran 2026)
4. Bing News — "Microsoft unveils Scout, an autonomous AI agent built on OpenClaw" (Build 2026, Haziran 2026)
5. Bing News — "Norm Ai Launches Compliance Agent for Microsoft 365 Copilot" (Haziran 2026)
6. Bing News — "KPMG Deploys Microsoft Agent 365 to Govern AI Agents Across Its Global Firms" (Haziran 2026)

---

## 22 Haziran 2026 — Yeni Vakalar

### Seyahat & Ulaşım AI Agent Vakaları — Perşembe Rotasyonu

---

### 1. SITA — Havayolu AI Stratejisi İki Katı Hızlandı

**Sektör:** Havacılık Teknolojisi / B2B Altyapı
**Kullanım Alanı:** Operasyonlar — Uçuş Kesinti Yönetimi + Veri Analitiği

**Ne Yapıyor:**
SITA (havayolları ve havaalanları için teknoloji sağlayıcısı), 2026'da AI stratejisini hızlandıran iki satın alma yaptı:

1. **Big Blue Analytics** — Havayolları için AI tabanlı analitik platform. Uçuş gecikmeleri, kapasite planlama, yakıt optimizasyonu için makine öğrenimi modelleri sunuyor.

2. **AI-Based Disruption Platform** — Uçuş aksamalarında (hava durumu, teknik arıza, slot sıkıntısı) otomatik çözüm üreten agent. Geleneksel sistem: insan operatör 10-30 dakikada çözüm buluyor. SITA'nın platformu: 2-3 dakikada otomatik re-routing, ekip yönlendirme, yolcu bildirimi.

**Müşteri Deneyimi — Kesinti Senaryosu:**
```
Senaryo: Frankfurt Havalimanı'nda yoğun sis, 40 uçuş rötar riski
SITA Agent:
 → Havalimanı operasyon verilerini real-time çekiyor
 → 40 uçuşu öncelik sırasına koyuyor (varış süresi, bağlantı, yolcu sayısı)
 → Alternatif slot tahsislerini simüle ediyor
 → En optimal çözümü buluyor (2 dakika)
 → Havalimanı operatörlerine öneri sunuyor
 → Onay sonrası tüm sistemlere otomatik güncelleme
```

**Herkesin Kaçırdığı Nokta #1:** SITA havayollarına "tek başına AI satmıyor" — komple operasyonel workflow satıyor. Kesinti yönetimi = havayolu şirketlerinin en pahalı operasyonel maliyeti. 1 saatlik gecikme = ortalama $50,000-$200,000 kayıp (uçak, mürettebat, yolcu bağlantıları). Bu rakamla AI'ın ROI'si tartışmasız.

**Herkesin Kaçırdığı Nokta #2:** SITA 100+ ülkede havalimanı teknolojisi sağlıyor. Big Blue Analytics ve Disruption Platform'u entegre edince, küresel ölçekte "hava yolu AI network'ü" oluşuyor. Bir havayolu şirketinin kesinti çözümü = diğer havayolları için learning. Bu = AI'ın network efekti.

**Kaynak:**
- Bing News — "SITA expands airline AI strategy with Big Blue Analytics acquisition" (Haziran 2026)
- Bing News — "SITA Acquires AI-Based Disruption Platform" (Haziran 2026)

---

### 2. Southwest Airlines + AWS — 2028'e Kadar Tam Cloud AI Geçişi

**Sektör:** Havayolu / ABD İç Hat
**Kullanım Alanı:** Altyapı Modernizasyonu — AI-Driven Operations

**Ne Yapıyor:**
Southwest Airlines, Amazon Web Services (AWS) ile ortaklık kurarak 2028'e kadar tüm operasyonel altyapısını bulut tabanlı AI sistemlerine taşıyor. Kapsam:
- Müşteri hizmetleri AI agent'ları (rezervasyon değişikliği, iade, şikayet)
- Uçuş operasyonları AI optimizasyonu
- Bakım tahmini (predictive maintenance — uçak parçaları)
- Kabin ekibi planlaması AI tabanlı

**Herkesin Kaçırdığı Nokta #1:** Southwest = ABD'nin en büyük iç hat havayolu. Bu kadar büyük bir şirketin AWS'e geçişi, havacılık sektöründe "cloud-first" trendinin artık geri dönülmez olduğunu gösteriyor. 2028 deadline = 2 yıl içinde karar.

**Herkesin Kaçırdığı Nokta #2:** Havayolu AI'ında en büyük fırsat = predictive maintenance. Uçak motorları, iniş takımları, kabin sistemleri — arıza öncesi parça değişimi = 0 uçuş aksamásı, 0 yolcu mağduriyeti. Southwest'in AWS AI'ı bu alanda uzmanlaşacak. Türk Havayolları ve Pegasus için de aynı model uygulanabilir.

**Kaynak:**
- Bing News — "Southwest Airlines Partners with Amazon Web Services (AWS) to Accelerate AI Capabilities and Technology Modernization" (Haziran 2026)
- Bing News — "Southwest Airlines partners with AWS to modernize systems, expand AI use, and move to a fully cloud-based environment by 2028" (Haziran 2026)

---

### 3. Digi Yatra — 10 Crore Yolculuk, 65 Havalimanına Genişleme

**Sektör:** Havacılık / Biyometrik Kimlik + Dijital Kimlik
**Kullanım Alanı:** Yolcu Deneyimi — Kimlik Doğrulama + Güvenlik

**Ne Yapıyor:**
Digi Yatra (Hindistan'ın merkezi havacılık biyometrik kimlik platformu), 2026'da 10 crore (100 milyon) yolculuk barajını aştı. Sistem:
- Yüz tanıma ile boarding (pasaport/kimlik kartı gerekmiyor)
- Havalimanı girişinden uçağa binerken tek biometric kimlik
- Self-boarding gate (insansız kapı geçişi)
- Future: otel check-in, duty-free alışveriş, uçuş rezervasyonu = tek kimlik

**Genişleme:** 2027'ye kadar 65 havalimanına yayılma hedefi. Hindistan = dünya'nın en kalabalık 3. havacılık pazarı.

**"Extensible Digital Identity" Vizyonu:**
Digi Yatra kurucuları artık "sadece havacılık için değil" diyor. Amaç: dijital kimlik = güvenilir kimlik kanıtı. Banka hesabı açma, otel check-in, araba kiralama — her yerde aynı biometric kimlik. Bu = WhatsApp + Instagram kimlik doğrulama gibi, ama gerçek dünya için.

**Herkesin Kaçırdığı Nokta #1:** 100 milyon yolculuk = dünya ölçeğinde en büyük biyometrik havacılık deployment'u. ABD'de TSA PreCheck ve CLEAR daha küçük ölçekli. Hindistan'ın altyapı avantajı = her şey dijital-first, eski sistem yükü yok.

**Herkesin Kaçırdığı Nokta #2:** Digi Yatra'nın "extensible identity" vizyonu = AI kimlik doğrulama agent'ları için yeni kullanım alanı. Havalimanında sadece boarding değil — para çekme, otel girişi, araba kiralama da aynı AI kimlik sistemi ile yapılabilir. Türkiye'de İstanbul Airport'un Digi Yatra benzeri bir sisteme geçişi = hem güvenlik hem konfor artışı.

**Kaynak:**
- Bing News — "Digi Yatra crosses 10 crore journeys, set to expand to 65 airports by next year" (Haziran 2026)
- Bing News — "Beyond Aviation: Digi Yatra eyes role as extensible digital identity layer" (Haziran 2026)
- Bing News — "Biometric boarding goes mainstream as Digi Yatra hits 10-crore mark" (Haziran 2026)

---

### 4. CargoAi — AI-Native Hava Kargo İşlem Platformu

**Sektör:** Lojistik / Hava Kargo
**Kullanım Alanı:** Operasyonlar — Kargo Booking + Fiyatlandırma + Takip

**Ne Yapıyor:**
CargoAi, hava kargo sektöründe AI-native teknoloji şirketi. CargoMART marketplace'ini tüm AI platformlarına entegre etti. Bu ne demek:
- Kargo göndericileri (fabrikalar, e-ticaret şirketleri) AI asistanlarından "en ucuz + en hızlı hava kargo seçeneği" sorabiliyor
- AI, CargoMART verilerini gerçek zamanlı fiyatlandırma, kapasite, transit time ile birleştiriyor
- Sonuç: sadece fiyat değil, "bu kargoyu Çarşamba günü Şangay'dan İstanbul'a 2 günde ulaştıran en ucuz seçenek" gibi spesifik sonuçlar

**Kullanım Alanı:**
- E-ticaret: Çin'den Türkiye'ye hızlı kargo için AI ile en optimal rota
- Otomotiv: Acil yedek parça = hava kargo AI agent'ı anlık çözüm sunuyor
- İlaç: Soğuk zincir gerektiren ilaçlar için uygun kapasite arama

**Herkesin Kaçırdığı Nokta #1:** Hava kargo = küresel ticaretin omurgası ama teknoloji olarak en geri kalmış sektör. Hâlâ e-posta ve telefon ile rezervasyon yapılıyor. CargoAi'ın AI-native yaklaşımı = bu sektörde ilk gerçek dijital dönüşüm.

**Herkesin Kaçırdığı Nokta #2:** Türkiye İstanbul Airport = küresel hava kargo hub'ı. Turkish Cargo = önemli oyuncu. Türk lojistik şirketleri için CargoAi modeli = doğrudan uygulanabilir. AI agent + hava kargo booking = 10x hızlı rezervasyon, 0 telefon trafiği.

**Kaynak:**
- Bing News — "CargoAi Connects CargoMART Air Cargo Intelligence to Every AI Platform" (Haziran 2026)

---

## 22 Haziran 2026 — Kaynaklar

1. Bing News — "SITA expands airline AI strategy with Big Blue Analytics acquisition" (Haziran 2026)
2. Bing News — "SITA Acquires AI-Based Disruption Platform" (Haziran 2026)
3. Bing News — "Southwest Airlines Partners with Amazon Web Services (AWS) to Accelerate AI Capabilities and Technology Modernization" (Haziran 2026)
4. Bing News — "Southwest Airlines partners with AWS to modernize systems, expand AI use, and move to a fully cloud-based environment by 2028" (Haziran 2026)
5. Bing News — "Digi Yatra crosses 10 crore journeys, set to expand to 65 airports by next year" (Haziran 2026)
6. Bing News — "Beyond Aviation: Digi Yatra eyes role as extensible digital identity layer" (Haziran 2026)
7. Bing News — "Biometric boarding goes mainstream as Digi Yatra hits 10-crore mark" (Haziran 2026)
8. Bing News — "CargoAi Connects CargoMART Air Cargo Intelligence to Every AI Platform" (Haziran 2026)

---

*Bu dosya Hermes Agent tarafından güncellenmektedir.*
*Güncelleme: Her gün 12:00 (Cumartesi/Pazar: Genel Araştırma — YC Launches + Enterprise Deployments)*
*Tarih: 22 Haziran 2026*
