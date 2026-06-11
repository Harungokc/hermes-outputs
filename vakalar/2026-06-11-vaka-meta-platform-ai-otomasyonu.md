# Meta Platformları AI Otomasyonu —11 Haziran 2026

## Tarih: 2026-06-11
## Konu: Instagram + WhatsApp Business API + AI Bot Sistemleri

---

## 1. Instagram Graph API — AI Otomasyonu İmkanları

### Instagram Messaging API Nedir?
Instagram Graph API, işletme hesaplarının DM'lerini, yorumlarını ve story mention'larını programatik olarak yönetmeye yarıyor.

### Temel Özellikler
- **DM Okuma/Yazma:** Gelen mesajları oku, otomatik yanıt ver
- **Yorum Yanıtlama:** Gönderi yorumlarına otomatik yanıt
- **Story Mention:** Story'de etiketlenince otomatik DM atma
- **Webhooks:** Yeni mesaj geldiğinde bildirim alma

### AI Entegrasyonu
```
Instagram DM geliyor
    ↓ Webhook tetikleniyor
n8n / Cloud Functions
    ↓ Claude API'ye gönderiyor
"Müşteri ne istiyor?"
    ↓
AI yanıt üretiyor
    ↓
Instagram DM gönderiyor
```

### Herkesin Kaçırdığı Nokta
**Instagram Messaging API rate limit aslında çok düşük — günde sadece 250 mesaj/hesap.** Bu yüzden "her DM'e AI yanıt" yerine "önemli DM'leri AI ile yanıtla" stratejisi daha doğru. Veya birden fazla hesap kullan.

### Rate Limits (Güncel)
| Limit | Değer |
|-------|-------|
| Günlük mesaj | 250/hesap |
| Yorum başına istek | 30/dk |
| Medya yükleme | 50/gün |
| Yanıt penceresi | 24 saat |

### Instagram → WhatsApp Yönlendirme
**En güçlü kullanım senaryosu:**
```
1. Müşteri Instagram reklamını görür
2. "DM at" veya "WhatsApp'a geç" butonuna tıklar
3. Instagram DM açılır — AI bot "Merhaba! WhatsApp'a geçerseniz daha hızlı yardımcı olabilirim" der
4. Müşteri WhatsApp'a geçer (kendi isteğiyle — spam değil)
5. WhatsApp'ta AI bot devreye girer
6. Sipariş, sorgulama, şikayet → hepsi WhatsApp'ta
```

**Kritik not:** WhatsApp'a ilk mesajı müşteri kendisi atmalı. Spam politikası bunu gerektiriyor.

---

## 2. WhatsApp Business API — AI Müşteri Asistanı

### WhatsApp Business API Nedir?
WhatsApp'ın işletmeler için sunduğu API. Büyük ölçekli müşteri iletişimi, otomatik yanıtlar, template mesajları.

### Template (Onaylı Mesaj) Sistemi
WhatsApp'ta ilk mesaj mutlaka onaylı template olmalı. Template'ler 3 kategori:

| Kategori | Kullanım | Maliyet (TL) |
|----------|----------|---------------|
| **Utility** | Sipariş takibi, randevu hatırlatma | ~0.35 |
| **Marketing** | Kampanya, tanıtım | ~0.70 |
| **Authentication** | Doğrulama kodları | ~0.35 |

### Template Onay Süreci
1. Template oluştur (Meta Business panel)
2. Meta onay bekliyor (24-48 saat)
3. Onay gelirse kullanmaya başla
4. **Ret oranı yüzde 40+** — ilk denemede onaylanmayabilir

### AI Bot Entegrasyonu
```
Müşteri WhatsApp'a mesaj atıyor
    ↓ Cloud API'ye geliyor
Webhook tetikleniyor
    ↓
n8n / server — AI kararı alıyor
    ↓ Claude API
"Ne istiyor? Neye yanıt vereyim?"
    ↓
AI yanıt üretiyor
    ↓
Müşteriye gönderiliyor
```

### Gerçek Kullanım Senaryoları

#### E-Ticaret
- "Siparişim ne zaman gelir?" → Stok sorgusu → AI yanıt
- "Bu ürünün fiyatı ne?" → Ürün veritabanı → AI yanıt
- "İade yapmak istiyorum" → İade akışı başlat → AI yönlendirme

#### Veteriner
- "Köpeğim yemek yemiyor" → Semptom analizi → AI öneri
- "Randevu almak istiyorum" → Takvim kontrolü → Saat önerisi
- "İlaç dozu ne?" → Uzman yönlendirme (AI değil, gerçek veteriner)

#### Restaurant
- "Rezervasyon yapmak istiyorum" → Tarih/saat kontrolü → Onay
- "Menüde ne var?" → AI menü okuyup öneriyor
- "Hesap ne kadar?" → AI hesap bilgisi veriyor

### Herkesin Kaçırdığı Nokta
**WhatsApp Business API'yi sadece "müşteri hizmetleri" için düşünmeyin.** Gerçek fırsat:
- **Satış hunisi:** Instagram'dan çeken müşteriyi WhatsApp'ta siparişe dönüştürme
- **Upsell:** "Bu ürüne baktın, benzeri olan X de var" gibi AI önerileri
- **Sepet terk önleme:** "Sepetinizdeki ürünler duruyor, yardımcı olalım mı?" mesajı

---

## 3. Meta AI Genel Bakış — WhatsApp ve Instagram'daki Yeni Özellikler

### Meta AI Nedir?
Meta'nın AI assistant'ı. WhatsApp, Instagram, Messenger'da doğrudan kullanılabiliyor.

### WhatsApp'ta Meta AI
- Sohbet etmek için AI ile doğrudan konuşabiliyorsunuz
- Görsel üretim özellikleri var
- Web araması yapabiliyor

### Herkesin Kaçırdığı Nokta
**Meta AI işletmeler için değil, bireysel kullanıcılar için.** Yani:
- Müşteriniz Meta AI'a soru sorabilir
- Ama işletme hesabınızdan Meta AI kullanamazsınız
- Meta AI ile işletme bot'u yapamazsınız (henüz)

**Gerçek kullanım:** Rakip analizi için Meta AI'ı kullanabilirsiniz — "Bana X markasının WhatsApp'taki bot'unu analiz et" gibi.

---

## 4. Instagram Threads API — Erken Fırsat

### Threads API Nedir?
Instagram Threads için programatik erişim. 2024 sonunda çıktı, henüz çok yeni.

### Özellikler
- Thread oluşturma/güncelleme
- Beğeni ve yanıt yönetimi
- Profil bilgisi çekme

### Herkesin Kaçırdığı Nokta
**Threads API henüz beta aşamasında ve rekabet düşük.** Kimse ciddi Threads bot'ları yazmıyor çünkü:
- API yeni ve dokümantasyon sınırlı
- Kullanıcı tabanı henüz büyüyor
- Erken giren kazanır durumda

### Potansiyel Kullanım
- Otomatik thread paylaşımı (içerik yayınlama)
- Thread'lere otomatik yanıt
- Trend topic takibi

---

## 5. Webhook Kurulumu — Teknik Detaylar

### Webhook URL Gereksinimleri
1. **Publicly accessible** — Meta'nın erişebileceği URL
2. **SSL/TLS zorunlu** — HTTPS olmalı
3. **GET destekli** — Verify token doğrulaması için
4. **POST destekli** — Mesajları almak için

### Meta Verify Süreci
Meta webhook'u doğrulamak için 3 kez deneme yapıyor:
- 3 başarısız deneme = webhook iptal
- Her denemede farklı bir challenge gönderiyor
- Doğru yanıt vermek gerekiyor

### Yerel Geliştirme için Ngrok
```
1. ngrok indir
2. ./ngrok http3000
3. HTTPS URL'ini al
4. Meta Developer Portal'a URL'i kaydet
5. Webhook URL'ini test et
```

---

## 6. Türkiye'de Meta Platform Kullanımı — Özel Durumlar

### Türkiye'ye Özel Kısıtlamalar
- **Meta inceleme süreci 2-4 hafta** — Ret oranı yüzde 40+
- **Sanal numaralar çalışmaz** — Gerçek operatör numarası gerekli
- **Türk Lirası ile ödeme yok** — USD/EUR gerekli

### Türkiye'de WhatsApp Kullanım İstatistikleri
- Aktif WhatsApp kullanıcısı: 55M+
- WhatsApp Business kullanıcısı: 5M+
- Ortalama günlük mesaj: 30+

### Fırsatlar
1. **WhatsApp Channels** — Henüz çok az kişi kullanıyor
2. **Instagram Collab Post'lar** — Birlikte çekiliş kampanyaları
3. **Instagram Live Shopping** — AI ile canlı sohbet yanıtları

---

## 7. Entegrasyon Mimarisi — Tam Sistem

### Sistem Diyagramı
```
[Instagram]
    ↓ DM / Yorum / Story Mention
[Instagram Graph API]
    ↓ Webhook
[n8n Workflow]
    ↓ HTTP / MCP
[Claude API]
    ↓ Yanıt
[n8n Workflow]
    ↓
[WhatsApp Cloud API]
    ↓
[Müşteri WhatsApp]
```

### Veritabanı Akışı
```
Müşteri sipariş veriyor (WhatsApp)
    ↓
n8n: Veritabanına kaydet (SQLite/PostgreSQL)
    ↓
Stok güncelle
    ↓
Dashboard'a ekle
    ↓
Müşteriye onay mesajı
```

### Stack (Önerilen)
```
AI: Claude Code / Claude API
Workflow: n8n
Veritabanı: SQLite (local) → PostgreSQL (scale)
Hosting: DigitalOcean Istanbul / Frankfurt
Mesajlaşma: Instagram Graph API + WhatsApp Cloud API
Diller: Python (bot), JavaScript/TypeScript (n8n)
Cache: Redis (opsiyonel)
```

---

## Kaynaklar
- Meta for Developers — Instagram Messaging API docs
- Meta for Developers — WhatsApp Business API docs
- n8n.io — MCP integration blog
- WhatsApp Business API rate limits (2026)

---

*Bu dosya 2026-06-11 tarihinde manuel araştırma ile oluşturuldu.*
*GitHub: Harungokc/hermes-outputs/vakalar/*
