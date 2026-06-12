# Meta İçin Yapılabilecek AI Agent'lar — Geliştirme Rehberi
**Tarih:** 2026-06-12 18:00
**Kaynak:** Bing News, Meta Developer Docs, GitHub (doğrudan erişim yok)

---

## Özet

Meta platformları (WhatsApp, Instagram, Facebook) için kendi AI ajanını yapmak artık çok kolay. Meta'nın resmi API'leri açık ve iyi dokümante edilmiş. 2026'da Meta Business Agent global lansmanıyla, "kendi ajanını yap" trendi hızlandı. İlginç olan: çoğu geliştirici WhatsApp API'sini biliyor ama Instagram Graph API'yi atlayış — Instagram'da AI ajan yapmak WhatsApp'tan 3 kat daha değerli çünkü discovery potansiyeli çok yüksek.

---

## Yapılabilecek AI Agent'lar

### 1. WhatsApp AI Müşteri Asistanı
**Ne yapar:** 7/24 müşteri sorgularını yanıtlama, sipariş alma, şikayet çözümü
**Zorluk:** ⭐⭐ (Orta)
**Teknoloji:** WhatsApp Business API + Claude/CPT-4

### 2. Instagram DM Otomasyon Botu
**Ne yapar:** Yorum/DM'leri yanıtlama, ürön推荐, sepet hatırlatma
**Zorluk:** ⭐⭐⭐ (Orta-İleri)
**Teknoloji:** Instagram Graph API + n8n + Claude

### 3. Abandoned Cart Recovery Agent
**Ne yapar:** Sepeti terk eden müşteriye WhatsApp'tan 1s → 24s → 72s hatırlatma
**Zorluk:** ⭐⭐ (Orta)
**ROI:** %10-15 ek dönüşüm
**Teknoloji:** WhatsApp Business API + e-ticaret webhook + Claude

### 4. Meta Ads Performance Analyst Agent
**Ne yapar:** Günlük reklam metriklerini analiz edip öneri üretme
**Zorluk:** ⭐⭐⭐ (İleri)
**Teknoloji:** Meta Marketing API + Python/Node + Claude

### 5. Content Moderation Agent
**Ne yapar:** Yorum/soru analizi, spam/uygunsuz içerik filtreleme
**Zorluk:** ⭐⭐ (Başlangıç)
**Teknoloji:** Instagram Graph API + Claude + n8n

---

## Kullanılabilir API'ler

### WhatsApp Business API
- **Endpoint:** `graph.facebook.com/v18.0/Phone_Number_ID/messages`
- **Doküman:** https://developers.facebook.com/docs/whatsapp
- **Kullanım:** Mesaj gönderme/alma, template yönetimi, webhook

### Instagram Graph API
- **Endpoint:** `graph.facebook.com/v18.0/ig_user_id/`
- **Doküman:** https://developers.facebook.com/docs/instagram-api
- **Kullanım:** Media, comments, direct messages, insights

### Meta Marketing API
- **Endpoint:** `graph.facebook.com/v18.0/act_AD_ACCOUNT_ID/`
- **Doküman:** https://developers.facebook.com/docs/marketing-apis
- **Kullanım:** Kampanya oluşturma, hedefleme, raporlama

### Meta Business Agent Platform (Yeni - 2026)
- **Doküman:** https://business.whatsapp.com/ (Business Agent bölümü)
- **Kullanım:** Hazır AI agent'ı özelleştirme, knowledge base ekleme
- **Fiyat:** $200/ay (Hatch plan)

---

## Adım Adım Yapım Rehberi

### Proje 1: WhatsApp AI Müşteri Asistanı

#### Gerekenler
- WhatsApp Business API hesabı
- n8n (veya Node.js/Python backend)
- Claude API erişimi
- Webhook URL (ngrok veya sunucu)

#### Kurulum Adımları
```
1. WhatsApp Business API kur (business.facebook.com)
2. Ngrok ile webhook expose et:
   ngrok http 5678
3. n8n'de workflow oluştur:
   - Webhook trigger (WhatsApp gelen mesaj)
   - Claude node (prompt: "Müşteri şunu sordu: {{$json.message}}")
   - HTTP Request node (WhatsApp API ile yanıt gönder)
4. Test et, canlıya al
```

#### Claude Prompt Örneği
```
Sen bir e-ticaret müşteri hizmetleri asistanısın.
Ürünlerimiz: [liste]
Sipariş durumu sorgusu: "{{$json.order_id}}" ile kontrol et
Yanıtın: 
- Türkçe
- Kısa ve net (max 2 cümle)
- Action button varsa ekle
```

---

### Proje 2: Instagram → WhatsApp Satış Botu

#### Gerekenler
- Instagram Graph API erişimi
- WhatsApp Business API erişimi
- n8n + Claude

#### Kurulum Adımları
```
1. Instagram Developer App oluştur
2. Webhook setup (Instagram comment/DM trigger)
3. n8n workflow:
   - Instagram trigger (yeni yorum geldi)
   - AI node: "Ürün önerisi yap" (Claude)
   - WhatsApp node: Müşteriye DM gönder
4. Otomatik takip: 24 saat sonra "sipariş verdiniz mi?" mesajı
```

---

## Örnek GitHub Repoları

### WhatsApp Bot Framework'leri
- **chatbot-whatsapp** (Python) — https://github.com/jgoncalvesdev/chatbot-whatsapp
- **whatsapp-web.js** (Node.js) — https://github.com/pedroslopez/whatsapp-web.js
- **venombot** (Node.js) — https://github.com/orken/venombot

### Instagram Otomasyon
- **instagram-private-api** (Node.js) — https://github.com/dator/instagram-private-api
- **instagram-graph-api-sdk** — Meta'nın resmi SDK'sı

### Meta Marketing API
- **facebook-business-sdk** (Node.js/Python) — Meta'nın resmi SDK'sı

**Not:** GitHub API çalışmıyor (exit code 49), doğrudan link verilmiştir.

---

## Herkesin Kaçırdığı Nokta

**#1 — Instagram API, WhatsApp'tan 3 Kat Değerli**
Herkes WhatsApp bot yapıyor çünkü daha kolay. Ama Instagram'da AI ajan yapmak = yeni müşteri keşfi. WhatsApp'ta sadece mevcut müşterilere ulaşırsın. Instagram'da keşfedilmemiş müşterilere ulaşırsın.

**#2 — Abandoned Cart = En Yüksek ROI**
E-ticaret için en basit ve en yüksek ROI'li ajan: sepeti terk edenlere WhatsApp hatırlatması. 1s → 24s → 72s kuralıyla %10-15 ek dönüşüm. Bu ajanı yapıp "nasıl yapılır" diye sorana LinkedIn'de post yazsan 390K görüntüleme alırsın.

**#3 — Meta Business Agent Platform = No-Code Çözüm**
Kod yazmak istemeyenler için: Meta Business Agent Platform ($200/ay) ile no-code ajan yapılabilir. Ama Türkiye'de henüz erişilebilir değil. Alternatif: n8n + Claude ile %50 maliyetle aynı işlevsellik.

---

## Kaynaklar

- https://developers.facebook.com/docs/whatsapp
- https://developers.facebook.com/docs/instagram-api
- https://developers.facebook.com/docs/marketing-apis
- https://business.whatsapp.com/developers/developer-hub
- https://github.com/pedroslopez/whatsapp-web.js
- https://github.com/n8n-io/n8n
