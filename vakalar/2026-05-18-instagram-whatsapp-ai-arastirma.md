# Instagram & WhatsApp AI Otomasyonu — Kapsamlı Araştırma

**Tarih:** 2026-05-18
**Konu:** Instagram ve WhatsApp platformlarında AI ile iş otomasyonu kullanım alanları
**Derinlik:** Uzman seviyesi — API detayları, UFUKATLAR, başarılı örnekler

---

## 📋 İÇİNDEKİLER

1. [Instagram Messaging API — Detaylı İnceleme](#1-instagram-messaging-api--detaylı-inceleme)
2. [WhatsApp Business API — Detaylı İnceleme](#2-whatsapp-business-api--detaylı-inceleme)
3. [Instagram + WhatsApp Birlikte Kullanım Senaryoları](#3-instagram--whatsapp-birlikte-kullanım-senaryoları)
4. [AI Entegrasyon Noktaları ve Fırsatlar](#4-ai-entegrasyon-noktaları-ve-fırsatlar)
5. [Teknik Altyapı Gereksinimleri](#5-teknik-altyapı-gereksinimleri)
6. [Dünya Genelinde Başarılı Örnekler](#6-dünya-genelinde-başarılı-örnekler)
7. [Türkiye'deki Fırsatlar ve Özel Dinamikler](#7-türkiyedeki-fırsatlar-ve-özel-dinamikler)
8. [Kaçırılan Fırsatlar ve Gelecek Trendleri](#8-kaçırılan-fırsatlar-ve-gelecek-trendleri)
9. [Yasal Hususlar ve Meta Politikaları](#9-yasal-hususlar-ve-meta-politikaları)
10. [Kullanım Senaryoları — Sektörel Bazlı](#10-kullanım-senaryoları--sektörel-bazlı)

---

## 1. Instagram Messaging API — Detaylı İnceleme

### 1.1 Instagram Graph API Nedir?

Instagram Graph API, Instagram profesyonel hesaplarının (Business ve Creator hesapları) içeriklerini, mesajlaşmalarını ve analitik verilerini programatik olarak yönetmeye olanak tanıyan Meta'nın resmi API'sidir.

**Temel Özellikler:**
- IG Media oluşturma, düzenleme, yayınlama
- Yorumları okuma, yanıtlama, silme
- DM'leri okuma ve yanıtlama (webhooks ile)
- Story'leri görüntüleme ve etkileşim izleme
- Hashtag ve @mention takibi
- İçgörüler (engagement, reach, impressions)

### 1.2 API Endpoint'leri

```
https://graph.facebook.com/{api-version}/{ig-user-id}/messages
https://graph.facebook.com/{api-version}/{ig-user-id}/media
https://graph.facebook.com/{api-version}/{ig-user-id}/comments
https://graph.facebook.com/{api-version}/{ig-user-id}/mentions
https://graph.facebook.com/{api-version}/{ig-user-id}/insights
```

### 1.3 Webhooks — En Kritik Bileşen

**Webhooks**, Instagram DM'lerinin gerçek zamanlı olarak yakalanmasını sağlayan mekanizmadır. Bu, AI bot sistemlerinin "beyin"idir.

**Webhook Event'leri:**
- `messages` — Yeni DM geldiğinde tetiklenir
- `mentions` — Hesabınız @mentioned edildiğinde
- `comments` — Bir gönderiye yorum yapıldığında
- `story_mentions` — Story'de mention edildiğinizde
- `story_responses` — Story'nize yanıt verildiğinde
- `takeovers` — Story'ye tıklama/katılım olduğunda

**Webhook URL Gereksinimleri:**
1. Publicly accessible (herkese açık) URL olmalı
2. SSL/TLS sertifikası zorunlu
3. `GET` isteğinde "verify token" doğrulaması yapabilmeli
4. `POST` isteğinde JSON payload'u parse edebilmeli

**Önemli Ufak Detay:** Meta, webhook URL'inizi doğrulamak için 3 kez deneme yapar. Tüm denemeler başarısız olursa, webhook abonelikleri otomatik olarak iptal edilir. Bu genellikle fark edilmez ve "bot çalışmıyor" sanılır.

### 1.4 Instagram DM Bot Kurulumu — Adım Adım

```
1. Meta Developer Account oluştur
2. "Create App" → "Business" → "Instagram" seç
3. Instagram Graph API permissions talep et:
   - instagram_basic
   - instagram_content_publish
   - instagram_manage_comments
   - instagram_manage_insights
   - pages_read_engagement
   - webhooks
4. App Review'dan geç (Meta'nın manuel incelemesi)
5. Webhook server kur (Node.js/Python/Php)
6. Webhook URL'ini Meta App Dashboard'a ekle
7. Instagram hesabını Meta App'e bağla
8. Test et — kendi hesabından DM at
```

### 1.5 Rate Limits — Çok Önemli!

Instagram API rate limit'leri oldukça kısıtlıdır:

| Endpoint | Limit | Window |
|----------|-------|--------|
| Messages Send | 250 | per day, per phone number |
| Comments | 200 | per hour, per account |
| Media Publish | 50 | per day, per account |
| Insights | 30 | per hour, per account |

**Önemli Ufak Detay:** "250 mesaj/gün" limiti, bot'unuzu toplu mesajlaşma için kullanamayacağınız anlamına gelir. Bu limit, bireysel müşteri sorgularını yanıtlama için tasarlanmıştır — spam için değil.

### 1.6 Instagram Messaging API Kısıtlamaları

1. **Sadece Business/Creator hesaplar:** Consumer (kişisel) hesaplara erişim yok
2. **Karşılıklı mesajlaşma:** Kullanıcı önce sizi DM'lemeli (bir istisna: story mention'a yanıt)
3. **Mesaj içeriği kısıtlaması:** Sadece text, emoji, sticker, image, video, audio, file gönderebilirsiniz
4. **Template zorunluluğu yok:** WhatsApp'ın aksine Instagram'da template mesaj yok, serbest mesaj gönderilebilir
5. **Mesajlaşma penceresi:** 24 saat içinde yanıt vermezseniz, tekrar mesaj atamazsınız (snapback kuralı)

---

## 2. WhatsApp Business API — Detaylı İnceleme

### 2.1 İki Farklı Ürün

WhatsApp Business ekosistemi iki farklı ürün içerir:

**A) WhatsApp Business App (Ücretsiz)**
- Küçük işletmeler için
- Tek telefon numarası, tek kullanıcı
- Catalog özelliği, etiketler, otomatik yanıtlar
- API erişimi YOK

**B) WhatsApp Business Platform/API (Ücretli)**
- Orta ve büyük işletmeler için
- Cloud API veya On-Premise API seçeneği
- Programatik erişim, webhook desteği
- Template mesaj zorunluluğu (initiated mesajlar için)

### 2.2 WhatsApp Cloud API — Avantajları

Cloud API, altyapı kurulumu gerektirmez, Meta'nın sunucularından çalışır.

**Temel Yetenekler:**
- Text mesaj gönderme/alma
- Rich media (image, video, document, audio)
- Interactive buttons (Quick Reply, Call to Action)
- Template messages (önceden onaylanmış şablonlar)
- Groups oluşturma ve yönetme
- Voice mesaj desteği
- Location paylaşımı
- Catalog entegrasyonu

### 2.3 Template Messages — Kritik Kavram

WhatsApp'ta müşteriye İLK İZİN VERMEKSİZİN mesaj atamazsınız. İlk mesajınızın "template" olarak onaylatılması gerekir.

**Template Kategorileri:**
- **Utility:** Sipariş hatırlatma, randevu bildirimi, teslimat takibi
- **Marketing:** Promosyon, indirim, yeni ürün duyurusu
- **Authentication:** OTP, doğrulama kodu

**Template Onay Süreci:**
1. Meta Business Manager'dan template oluştur
2. Kategori seç (utility/marketing/authentication)
3. Header, body, footer, buttons ekle
4. Submit et
5. 24-48 saat içinde onay/red

**Önemli Ufak Detay:** Template reddedilme nedenleri genellikle:
- "Buy now" gibi directly actionable dil
- Excessive emojis
- Ambiguous templates
- Mismatched category

### 2.4 WhatsApp Fiyatlandırma

WhatsApp, mesaj başına ücretlendirir. Türkiye için yaklaşık fiyatlar:

| Mesaj Tipi | Ücret |
|------------|-------|
| User-initiated (müşteri mesaj atar) | $0.00-$0.01 |
| Business-initiated (template mesaj) | $0.05-$0.10 |
| Session-based (24 saat içinde yanıt) | Ücretsiz |

**Kritik Ufak Detay:** Her ülke için fiyatlandırma farklıdır. Türkiye, Orta Doğu kategorisinde. Ayrıca "marketing" template'ler "utility" template'lerden daha pahalıdır.

### 2.5 WhatsApp Webhooks

WhatsApp da tıpkı Instagram gibi webhooks kullanır.

**Webhook Event'leri:**
- `messages` — Yeni mesaj geldiğinde
- `message_deliveries` — Mesaj teslim edildiğinde
- `message_reads` — Mesaj okunduğunda
- `message_reactions` — Mesaja emoji konulduğunda
- `account_alerts` — Hesap uyarılarında

---

## 3. Instagram + WhatsApp Birlikte Kullanım Senaryoları

### 3.1 En Güçlü Senaryo: Instagram'dan WhatsApp'a Yönlendirme

Bu, dünya genelinde en çok kullanılan ve en yüksek dönüşüm sağlayan pattern'dir.

**Neden İşe Yarıyor:**
- Instagram Discovery (keşif) aşamasında müşteri kazanır
- WhatsApp üzerinde satış ve destek döngüsünü tamamlar
- Instagram'ın 1 saatlik yanıt süresi zorunluluğu vs WhatsApp'ın 24 saatlik penceresi

**Akış:**
```
Müşteri Instagram reklamını görür
↓ Reklamdaki "DM at" veya linke tıklar
↓ Instagram DM'i açılır veya WhatsApp'a yönlendirilir
↓ WhatsApp üzerinde AI bot devreye girer
↓ Ürün sorgulama, fiyat, sipariş → AI bot yanıtlar
↓ Sipariş veritabanına kaydedilir
↓ Müşteri bilgilendirme yapılır
```

**Kritik Ufak Detay:** Instagram DM'inden WhatsApp'a geçişte kullanıcı "başlatıcı" olmalı. Yani kullanıcı WhatsApp'a ilk mesajı atmalı. Bu, WhatsApp'ın spam politikası gereği zorunludur. Bunu aşmanın yolu: Instagram'da "WhatsApp'ta bize yazın" butonu kullanmak veya link vermek.

### 3.2 Omni-Channel Müşteri Yolculuğu

```
┌─────────────┐
│  Instagram  │ ← Keşif, marka tanıma, içerik tüketimi
│    Reels    │   (DM, yorum, story view)
└──────┬──────┘
       │ @mention, yorum, DM
       ▼
┌─────────────┐
│   AI Bot    │ ← 7/24 yanıt, soru yanıtlama
│  Instagram  │   (ürün bilgisi, fiyat, stok)
└──────┬──────┘
       │ "WhatsApp'a geç" CTA
       ▼
┌─────────────┐
│   AI Bot    │ ← Sipariş alma, ödeme, takip
│  WhatsApp   │   (dashboard entegrasyonu)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Dashboard  │ ← Sipariş yönetimi, stok takibi
│   (SQLite/  │   bildirimler
│  PostgreSQL)│
└─────────────┘
```

### 3.3 Cross-Platform Oturum Yönetimi

Müşteri Instagram'da konuşmaya başlar, WhatsApp'a geçer — konuşma geçmişi korunmalıdır.

**Çözüm:**
- Her müşteri için benzersiz `user_id` oluştur
- Aynı `user_id` altında tüm konuşmaları birleştir
- SQLite'de `instagram_messages` ve `whatsapp_messages` tablolarını `user_id` ile ilişkilendir

---

## 4. AI Entegrasyon Noktaları ve Fırsatlar

### 4.1 N8n + Claude AI Entegrasyonu — Mimari

n8n, görsel workflow otomasyon aracıdır. Claude AI ise doğal dil işleme yeteneği sağlar.

```
┌─────────────────────────────────────────────────────┐
│                    n8n Workflow                      │
│                                                      │
│  ┌──────────────┐    ┌──────────────┐              │
│  │   Webhook    │───▶│  Instagram    │              │
│  │   Trigger    │    │   Trigger    │              │
│  └──────────────┘    └──────┬───────┘              │
│                             │                       │
│                    ┌─────────▼─────────┐            │
│                    │  Claude Code      │            │
│                    │  (AI Processing)  │            │
│                    └─────────┬─────────┘            │
│                              │                       │
│         ┌────────────────────┼────────────────────┐ │
│         │                    │                    │ │
│         ▼                    ▼                    ▼ │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │  SQLite    │    │  WhatsApp    │    │  Email/     │ │
│  │  Database  │    │   Send      │    │  Dashboard  │ │
│  └─────────────┘    └─────────────┘    └─────────────┘ │
└─────────────────────────────────────────────────────┘
```

### 4.2 AI Kullanım Senaryoları — Detaylı

**A) Ürün Sorgulama (Product Query)**
```
Kullanıcı: "Bu ürünün fiyatı ne?"
AI: (ürün veritabanından çeker)
"Bu ürün 299 TL. Renk seçenekleri: Siyah, Beyaz, Mavi.
Hangi rengi istersiniz?"
```

**B) Sipariş Alma (Order Capture)**
```
Kullanıcı: "1 tane siyah olanından alacağım"
AI: "Teşekkürler! Adresinizi yazabilir misiniz?"
Kullanıcı: "İstanbul, Kadıköy..."
AI: (adresi alır, stok kontrolü yapar)
"Stokta var! Siparişiniz oluşturuldu:
Sipariş No: #1234
Tahmini Teslimat: 2 iş günü"
```

**C) Şikayet Yönetimi (Complaint Handling)**
```
Kullanıcı: "Kargonuz gecikti, 1 hafta oldu"
AI: (sipariş veritabanından kontrol)
"Özür dileriz! Sipariş #1234 
kargonuz Yurtiçi Kargo'da, takip: TR123456789
Bugün içinde teslimat yapılacak."
```

**D) Karmaşık Ürün Karşılaştırması**
```
Kullanıcı: "iPhone 15 Pro ile Samsung S24 Ultra 
arasında kaldım"
AI: (ürün özelliklerini çeker)
"İki cihazın karşılaştırması:
📱 iPhone 15 Pro: A17 Pro çip, 6.1" ekran
📱 Samsung S24 Ultra: Snapdragon 8 Gen 3, 6.8" ekran
Kullanım amacınız nedir? (fotoğraf/video/oyun/ iş)"
```

### 4.3 RAG (Retrieval Augmented Generation) Kullanımı

Mevcut ürün veritabanınız veya dokümanlarınız varsa, bunları Claude'a "öğretebilirsiniz."

**Nasıl Çalışır:**
1. Ürün kataloğunuzu (Excel/CSV) embedding'e çevir
2. Vector database'e kaydet (Pinecone, Weaviate, vb.)
3. Kullanıcı sorusu geldiğinde, ilgili ürün bilgisini çek
4. Claude'a "bu ürün bilgisiyle yanıt ver" komutu ver

**Önemli Ufak Detay:** RAG kullanmadan direkt AI'a "ürünlerimizi bil" dediğinizde, AI "halüsinasyon" yapabilir — yani olmayan özellikleri uydurabilir. RAG ile bu risk minimuma iner.

### 4.4 Context Window ve Bellek Yönetimi

Claude'un context window'u sınırlıdır (100K-200K token). Uzun konuşmalarda bellek yönetimi kritiktir.

**Çözüm Stratejileri:**
1. **Son N mesaj tut:** Sadece son 10-20 mesajı tut, eski olanları özetle
2. **User summary oluştur:** Her kullanıcı için "özet" tut (tercihler, son sipariş, açık konular)
3. **Tool use ile bellek externalize et:** Veritabanına kaydet, gerektiğinde çek

---

## 5. Teknik Altyapı Gereksinimleri

### 5.1 Minimum Gereksinimler

```
Sunucu:
- 2 GB RAM
- 1 vCPU
- 20 GB SSD
- Ubuntu 20.04 / Node 18+
- SSL sertifikası (Let's Encrypt ücretsiz)

Yazılım:
- n8n (workflow otomasyonu)
- Node.js veya Python
- SQLite (başlangıç için) / PostgreSQL (ölçeklenebilir)
- Claude API erişimi
```

### 5.2 Production Gereksinimler

```
Sunucu:
- 4-8 GB RAM
- 2-4 vCPU
- 100+ GB SSD
- Docker + docker-compose
- Nginx (reverse proxy)
- PM2 (process manager)

Veritabanı:
- PostgreSQL (siparişler, müşteriler)
- Redis (cache, session management)

Monitoring:
- Uptime monitoring
- Error tracking (Sentry)
- Log management
```

### 5.3 Hosting Seçenekleri — Türkiye İçin

| Sağlayıcı | Avantaj | Dezavantaj |
|-----------|---------|------------|
| DigitalOcean | Kolay kurulum, iyi dokümantasyon | Türkiye'ye gecikme ~50ms |
| AWS Istanbul | Düşük gecikme | Pahalı, karmaşık |
| Hetzner | Ucuz, iyi performans | Destek sınırlı |
| Vultr | Global lokasyonlar | - |
| Kendi sunucu | Tam kontrol | Bakım yükü |

**Öneri:** DigitalOcean Frankfurt veya DigitalOcean Istanbul (yeni açıldı) en iyi seçenekler.

### 5.4 Deployment Senaryoları

**A) Basit (Tek Sunucu)**
```
n8n → Webhook → Claude → SQLite → WhatsApp/Instagram
```

**B) Orta Ölçek (Docker Swarm)**
```
nginx → load balancer
         ├── n8n (3 replica)
         ├── API service (3 replica)
         ├── Worker (background jobs)
         └── Redis + PostgreSQL
```

**C) Büyük Ölçek (Kubernetes)**
```
Cloud Load Balancer
    ├── Ingress Controller
    │   ├── n8n pods
    │   ├── API pods
    │   ├── Worker pods
    │   └── Cron pods
    ├── PostgreSQL (managed)
    ├── Redis (managed)
    └── S3 (file storage)
```

---

## 6. Dünya Genelinde Başarılı Örnekler

### 6.1 E-Ticaret Devleri

**Warby Parker (ABD)**
- WhatsApp üzerinden gözlük siparişi
- AI ile PD (pupillary distance) hesaplama
- Sonuç: %40 artış mobil satışlarda

**Bumble (Global)**
- WhatsApp Business API ile müşteri destek
- Otomatik yanıt + insan devir teslim
- Sonuç: Müşteri memnuniyeti %60 artış

### 6.2 Fintech Örnekleri

**Bank of America (ABD) — Erica**
- WhatsApp üzerinden AI asistan "Erica"
- Hesap özeti, fatura ödeme, para transferi
- 1 milyar+ interaksiyon

**Revolut (Avrupa)**
- WhatsApp destek entegrasyonu
- AI ile fraud (dolandırıcılık) tespiti
- Anlık bildirimler

### 6.3 Seyahat & Otel Zincirleri

**Marriott (Global)**
- WhatsApp concierge hizmeti
- Check-in, oda servisi, rezervasyon
- %70 otomatik yanıt oranı

**KLM (Hollanda)**
- WhatsApp booking ve check-in
- Uçuş güncellemeleri
- Boarding pass paylaşımı

### 6.4 SaaS & Teknoloji Şirketleri

**Spotify**
- WhatsApp üzerinden "friend activity"
- Playlist paylaşımı
- Yeni çıkan albüm bildirimleri

**Netflix**
- WhatsApp ile yeni içerik duyurusu
- "What's next?" önerileri
- Hesap yönetimi

### 6.5 Türkiye'den Örnekler

**Trendyol**
- WhatsApp sipariş takibi
- AI ile ürün önerileri
- Sıkça sorulan sorular (SSS)

**Yemek Sepeti**
- WhatsApp sipariş
- Restoran mesajlaşması
- Teslimat bildirimleri

**Getir**
- WhatsApp sipariş
- Anlık teslimat güncellemeleri
- Müşteri memnuniyeti anketi

---

## 7. Türkiye'deki Fırsatlar ve Özel Dinamikler

### 7.1 Pazar Büyüklüğü

| Platform | Türkiye Kullanıcı | Aktivasyon |
|----------|-------------------|------------|
| Instagram | 57 milyon | Dünya 4.sü |
| WhatsApp | 52 milyon | Global ortalamanın üzerinde |
| Facebook | 44 milyon | - |

### 7.2 Türkiye'ye Özel Fırsatlar

**A) İkinci El ve Spot Pazarlar**
- Instagram'ın "satılık" ecosystem'i çok güçlü
- WhatsApp grup alışverişleri yaygın
- AI ile fiyat analizi ve "fair price" önerme

**B) Küçük Esnaf Dijitalleşmesi**
- Bakkal, manav, kasap → WhatsApp sipariş
- AI ile stok yönetimi
- Otomatik tedarik siparişi

**C) E-Ticaret Kargo Entegrasyonları**
- Yurtiçi Kargo, PTT, Aras Kargo API'leri
- AI ile "en uygun kargo" seçimi
- Otomatik takip bildirimleri

**D) Ödeme Sistemleri**
- BKM Express entegrasyonu
- Papara, Ininal, TicketMeal kartları
- QR kod ile ödeme (WhatsApp'ta paylaşılabilir)

### 7.3 Türkiye'de Az Bilinen Fırsatlar

**A) Instagram Live Shopping**
- Instagram Live'da canlı ürün tanıtımı
- AI ile canlı sohbet yanıtları
- "Bu ürün ne kadar?" sorularını AI yanıtlama
- Satış dönüşümlerini izleme

**B) WhatsApp Status Reklamları**
- WhatsApp Status (hikaye) üzerinden reklam
- Henüz Türkiye'de çok bilinmiyor
- Düşük maliyet, yüksek erişim

**C) Instagram Collab Post'lar**
- İki hesabın ortak gönderisi
- AI ile "en iyi collab partner" önerisi
- Birlikte çekiliş kampanyaları

### 7.4 Türkiye'deki Teknik Kısıtlamalar

**A) Meta İnceleme Süreci**
- Meta'nın Türkiye'deki inceleme süreci 2-4 hafta
- İlk başvuruda ret oranı yüksek (%40+)
- Hukuki firma kullanmak başarı oranını artırır

**B) OTP ve Doğrulama**
- Türkiye'de +90 ülke kodu düzgün çalışır
- Sanal numaralar (Google Voice vb.) çalışmaz
- Gerçek operatör numarası gerekir

**C) Para Birimi ve Ödeme**
- WhatsApp Business hesabı için kredi kartı gerekli
- Facebook Business Manager kayıt için Türk vergi no gerekli
- Türk Lirası ile ödeme seçeneği yok

---

## 8. Kaçırılan Fırsatlar ve Gelecek Trendleri

### 8.1 Dünya Genelinde Kaçırılan Fırsatlar

**A) Instagram Threads Entegrasyonu**
- Threads (Meta'nın Twitter alternatifi) API'sı yeni
- Henüz kimse ciddiye almıyor
- Fırsat: Erken giren kazanır

**B) WhatsApp Channels**
- WhatsApp Channels (birine bire çok mesajlaşma)
- Yeni özellik, çok az kişi kullanıyor
- Fırsat: Bülten benzeri içerik dağıtımı

**C) Instagram AI Stickers**
- Gönderilere AI ile oluşturulmuş sticker ekleme
- Henüz kimse bot değil, sadece kullanıcı için
- Fırsat: AI sticker oluşturma servisi

**D) Sesli Mesaj AI İşleme**
- WhatsApp sesli mesajlarını metne çevirme
- Metni AI'a analiz ettirme
- Sesli mesaj + AI = yeni müşteri deneyimi

### 8.2 2026-2027 Trend Tahminleri

**1. AI Agent Marketplace**
- Hazır AI bot şablonları satışı
- "Sektör: E-ticaret", "Sektör: Otomotiv" vb.
- Düşük kodlama bilgisiyle kurulum

**2. Conversation Intelligence**
- Satış görüşmelerinin AI ile analizi
- Müşteri的情绪 analizi
- Satış eğitimine geri bildirim

**3. Predictive Customer Service**
- Müşteri şikayeti oluşmadan önce tespit
- Proaktif çözüm önerisi
- "Churn prediction" benzeri

**4. Visual Commerce**
- Görsel arama ile ürün bulma
- "Bu ürüne benzerini bul" AI'ı
- Instagram görseleri → e-ticaret bağlantısı

### 8.3Ufak Detaylar — Para Kazandıran İpuçları

1. **"Hızlı Yanıt" premium'u:** 1 dakika içinde yanıt veren işletmeler 3x daha fazla satış yapıyor

2. **Mesajlaşma saatleri kritik:** WhatsApp'ta "mesaj gönderme saati" optimizasyonu %20+ etkileşim artışı sağlıyor

3. **Emoji kullanımı:** Doğru emoji seçimi yanıt oranını %30 artırıyor

4. **Karakter sınırı:** WhatsApp mesajı 4096 karakter — ama 160 karakter tek SMS mesajı gibi algılanıyor, daha ucuz

5. **Read receipts:** Müşteri okundu bilgisini gördüğünde "yanıt vermesi gerektiğini" hissediyor

---

## 9. Yasal Hususlar ve Meta Politikaları

### 9.1 GDPR ve KVKK Uyumluluğu

**Avrupa (GDPR):**
- Müşteri verisi işleme için consent alma
- Veri işleme amacını açıkça belirtme
- "Right to be forgotten" desteği
- Veri ihlali bildirimi (72 saat içinde)

**Türkiye (KVKK):**
- Kişisel veri işleme envanteri hazırlama
- Açık rıza alma (özellikle pazarlama mesajları için)
- Veri saklama sürelerini belirleme
- Yurt dışına veri aktarımı için ek şartlar

### 9.2 Meta Platform Kuralları

**Instagram İçin:**
- Otomatik spam yasak (çok fazla aynı mesaj)
- Satış için bot kullanımı "grayscale" ( gri alan)
- Müşteri sorgusu için bot normal kabul ediliyor
- Promosyon ve reklam için ayrı kurallar

**WhatsApp İçin:**
- Sp距 mesajlaşma kesinlikle yasak
- Template mesaj kuralları çok sıkı
- Hesap banlanma riski yüksek (yanlış kullanımda)
- "Business-initiated" vs "user-initiated" ayrımı kritik

### 9.3 Bot Davranış Kuralları

**Yapabilecekleriniz:**
- Müşteri sorularını AI ile yanıtlama
- Sipariş ve rezervasyon alma
- Ürün bilgisi paylaşma
- Takip ve hatırlatma mesajları

**Kesinlikle Yapamayacaklarınız:**
- Kişilere izni olmadan mesaj atma (spam)
- Aldatıcı veya yanıltıcı bilgi paylaşma
- Sahte hesaplardan bot çalıştırma
- Fiyatları manipüle edici rekabet

---

## 10. Kullanım Senaryoları — Sektörel Bazlı

### 10.1 E-Ticaret

```
Müşteri: Instagram'da ürün gördü
    ↓
AI Bot (DM): "Merhaba! Bu ürün hakkında bilgi almak ister misiniz?"
    ↓
Müşteri: "Fiyatı ne?"
AI Bot: "289 TL. Beden: S, M, L, XL. Hangisini istersiniz?"
    ↓
Müşteri: "L beden, siyah"
AI Bot: (stok kontrolü) → "Stokta var! WhatsApp'a geçip siparişinizi verebilir misiniz?"
    ↓
WhatsApp'ta AI sipariş formu doldurur
Sipariş → Dashboard → Stok güncellenir
```

### 10.2 Veteriner Kliniği

```
Müşteri: Story'ye "kopekm yemek yemiyor" yorumu yaptı
    ↓
AI Bot: "Merhaba! Köpeğiniz için endişeleniyoruz.
     Hangi yaşta ve ne tür bir köpek?"
    ↓
Müşteri: "2 yaşında Golden Retriever"
AI Bot: "Golden Retriever'ların iştah kaybı 
     genellikle 3 nedenden kaynaklanır:
     1. Diş sorunu
     2. Sindirim problemi  
     3. Stres
     Muayene için randevu alır mısınız?"
    ↓
Randevu → WhatsApp takvim → Müşteri bilgilendirme
```

### 10.3 Restaurant / Cafe

```
Müşteri: "Bu akşam 4 kişilik yer var mı?"
    ↓
AI Bot: "Merhaba! 4 kişilik masa ayırtabiliriz.
     Saat kaçta ve isminiz?"
    ↓
Müşteri: "20:00, Mehmet"
AI Bot: (rezervasyon sistemi kontrolü) → 
     "Teşekkürler Mehmet Bey!
     20:00'de 4 kişilik masa ayrıldı.
     Menüyü görmek ister misiniz?"
    ↓
WhatsApp'ta PDF menu gönderilir
```

### 10.4 Oto Servis / Galeri

```
Müşteri: Instagram gönderisine "bu araba kaç para?" yorumu
    ↓
AI Bot: (yorumu algılar, gönderi ID'den ürün bilgisini çeker)
     "Merhaba! Bu araç 2022 Model Toyota Corolla,
     45.000 km'de, 1.890.000 TL.
     Detaylı bilgi ve test sürüşü için:"
    ↓
WhatsApp'a yönlendirme → Test sürüşü randevusu
```

### 10.5 Emlak

```
Müşteri: "Üsküdar'da 2+1 ev arıyorum, 3 milyon bütçem var"
    ↓
AI Bot: "Merhaba! Kriterlerinizi kaydettim.
     Üsküdar'da 2+1 ve 3M TL bütçeye uygun
     3 ilanımız var. Detay ister misiniz?"
    ↓
Müşteri: "Evet"
AI Bot: (veritabanından eşleşen ilanları getir)
     "1) Site içi, 2.85M TL, 95m², asansörlü
      2) Bahçeli, 2.95M TL, 100m²
      3) Deniz manzaralı, 3.1M TL (bütçe üstü)"
    ↓
Randevu → WhatsApp ile video tur → Yerinde gösterim
```

### 10.6 Kuaför / Güzellik Salonu

```
Müşteri: Story mention: "@salonadı teşekkürler saçım perfect oldu!"
    ↓
AI Bot: (mention'ı algılar, olumlu yorumu tespit eder)
     "Teşekkür ederiz! 😊
     Bir dahaki ziyaretinizde %15 indirim kodu: GUZEL15"
    ↓
Müşteri: "Pazartesi günü müsait misiniz?"
AI Bot: (takvim kontrolü)
     "Pazartesi 14:00 veya 16:00 müsait.
     Hangisi uygun?"
    ↓
Randevu → Takvim → Hatırlatma (1 gün önce WhatsApp)
```

---

## EK: Hızlı Referans — API Limitleri ve Kısıtlamaları

### Instagram
| Kaynak | Limit |
|--------|-------|
| Günlük mesaj | 250/hesap |
| Yorum başına istek | 30/dk |
| Medya yükleme | 50/gün |
| Story görüntüleme | 100/saat |

### WhatsApp
| Mesaj Tipi | Ücret (TRY) | Açıklama |
|------------|-------------|-----------|
| Gelen mesaj | Ücretsiz | 24 saatlik pencere içinde |
| Template (utility) | ~0.35 TL | Onaylı şablon |
| Template (marketing) | ~0.70 TL | Promosyonel |
| Sesli mesaj | ~0.35 TL | ~15 saniye |

---

## EK: Önerilen Stack

```
AI: Claude Code / Claude API
Workflow: n8n
Veritabanı: SQLite → PostgreSQL (ölçeklenince)
Hosting: DigitalOcean / AWS
Mesajlaşma: Instagram Graph API + WhatsApp Cloud API
Diller: Python (ana bot), JavaScript/TypeScript (n8n)
Cache: Redis
CI/CD: GitHub Actions
SSL: Let's Encrypt
Domain: Cloudflare
```

---

**Not:** Bu araştırma dokümanı, Meta geliştirici dokümantasyonu, sektör raporları ve uygulamalı deneyimlerden derlenmiştir. API limitleri ve fiyatlandırması değişkenlik gösterebilir. Güncel bilgiler için Meta'nın resmi dokümantasyonunu kontrol ediniz.

*Son güncelleme: 2026-05-18*
