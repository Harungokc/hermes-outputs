# Meta Araştırması — Yapılabilecek Meta AI Agent'lar
**Tarih:** 19 Haziran 2026 12:00
**Slot:** 06:00 — 12:00 arası

---

## Özet

Meta ekosisteminde (WhatsApp, Instagram, Messenger, Facebook Ads) kendi AI agent'ını yapmak için onlarca açık kaynak proje, MCP server ve API var. Bu slot'ta 11 farklı agent fikri ve bunları destekleyen GitHub repoları derlendi.

---

## Yapılabilecek Agent'lar

### 1. Müşteri Hizmetleri Agent — WhatsApp/Instagram

**Yapı:**
- Gelen mesajları AI ile analiz et (satış mı, şikayet mi, bilgi talebi mi?)
- Intent'e göre yönlendir veya otomatik yanıt ver
- Şikayetleri önceliklendir, Slack/Email'e bildirim gönder

**Kullanılan Teknoloji:**
- `pipeboard-co/meta-ads-mcp` (997⭐) — Meta Graph API
- `manu14357/tota-agent` (7⭐) — 11 LLM provider desteği
- Claude Code — Intent classification

**Agent Örneği — Sepet Terk Bildirimi:**
```
Müşteri: "Ürünü beğendim ama fiyat yüksek"
↓
Agent: Fiyat karşılaştırması yap, indirim kuponu var mı kontrol et
↓
Yanıt: "Bu üründe %15 indirim var, kupon: HOSGELDIN15"
```

### 2. Otomatik Randevu Agent — WhatsApp Business

**Yapı:**
- Müşteri uygun tarih seçer
- AI takvim kontrol eder
- Randevuyu onaylar ve hatırlatma gönderir

**Kullanılan Teknoloji:**
- WhatsApp Business API
- Google Calendar API
- n8n workflow

**GitHub Referansı:**
- `prempatkar936-lang/MPPRS-AI-Agent` — WhatsApp, Instagram & Messenger AI agent

### 3. Abandoned Cart Recovery Agent — WhatsApp

**Yapı:**
- Sepeti terk eden müşterilere 1, 24, 72 saat sonra hatırlatma
- Claude ile kişiselleştirilmiş mesaj üret
- Görsel + fiyat bilgisi gönder

**Kullanılan Teknoloji:**
- E-ticaret webhook (Shopify/WooCommerce)
- Claude Code — mesaj üretimi
- WhatsApp Business API — gönderim

**Herkesin Kaçırdığı Nokta #1:**
Abandoned cart recovery = e-ticaret için en yüksek ROI'li otomasyon. Sepet terk oranı %70, WhatsApp hatırlatma ile %10-15 ek dönüşüm. 72 saat kuralı bu workflow için aslında avantaj — ilk 24 saat en kritik.

### 4. Reklam Performans Monitoring Agent

**Yapı:**
- Campaign performansını her saat kontrol et
- Anomali tespit et (CTR düşüşü, spend artışı)
- Otomatik action veya bildirim gönder

**Kullanılan Teknoloji:**
- `mellowmir94/meta-ads-langgraph-agent` (yeni, LangGraph tabanlı) — 2026-06-19
- `mathiaschu/meta-ads-analyzer` (367⭐) — Learning Phase diagnosis
- NotFair (2924⭐) — Claude Code Meta Ads skill

**GitHub Referansları:**
- LangGraph ile monitoring: `meta-ads-langgraph-agent`
- Claude Code skill: `meta-ads-analyzer` + NotFair

### 5. Lead Scoring Agent — Instagram/Messenger

**Yapı:**
- Yeni follower/dm'leri analiz et
- Satın alma niyeti skorla
- Yüksek skorluları CRM'e kaydet

**Kullanılan Teknoloji:**
- Instagram Graph API
- Claude Code — conversation analysis
- Google Sheets / Airtable

### 6. İçerik Otomasyon Agent — Instagram

**Yapı:**
- Haftalık içerik planı oluştur
- Görsel + caption üret (AI ile)
- Zamanlı yayınlama planla

**Kullanılan Teknoloji:**
- Instagram Graph API — post scheduling
- Claude Code — caption generation
- DALL-E / Midjourney — görsel üretimi

### 7. A/B Test Otomasyon Agent — Meta Ads

**Yapı:**
- Birden fazla creative oluştur (Claude)
- A/B test kampanyası kur
- Performansa göre kazananı seç
- Loser'ı durdur, winner'ın bütçesini artır

**Kullanılan Teknoloji:**
- Meta Ads API — campaign creation
- Claude Code — creative generation
- n8n + meta-ads-mcp

### 8. Sipariş Takip Agent — WhatsApp

**Yapı:**
- Sipariş verildi → Kargo takip numarası gönder
- Kargo güncellendi → Müşteriye bildirim
- Teslimat sonrası → Memnuniyet anketi

**Kullanılan Teknoloji:**
- Shopify/WooCommerce webhook
- Kargo API (MNG, Yurtiçi, PTT)
- WhatsApp Business API

### 9. Stok Uyari Agent — E-ticaret

**Yapı:**
- Stok azaldığında bildirim
- Kritik stok seviyesinde kampanya durdur
- Yeni stok geldiğinde satışa aç

**Kullanılan Teknoloji:**
- E-ticaret API (Shopify, WooCommerce)
- Claude Code — uyarı mesajı üretimi
- Telegram/Slack — bildirim

### 10. FAQ Bot Agent — WhatsApp/Instagram

**Yapı:**
- Sık sorulan soruları AI ile yanıtla
- Bilinmeyen soruları insan operator'e yönlendir
- Bilgi tabanını güncelle

**Kullanılan Teknoloji:**
- WhatsApp Business API
- Claude Code — Q&A
- Google Sheets — bilgi tabanı

### 11. Çok Dilli Müşteri Hizmetleri Agent

**Yapı:**
- Gelen mesajı algıla (Türkçe, İngilizce, Arapça...)
- Doğru dilde yanıt ver
- Türkçe bilmeyen müşteriye otomatik çeviri

**Kullanılan Teknoloji:**
- `manu14357/tota-agent` (7⭐) — 11 LLM provider
- Claude Code — çeviri + yanıt
- WhatsApp Business API — çoklu dil desteği

---

## Adım Adım Yapım Rehberi — Minimal Viable Agent

### Proje: Otomatik Yanıt Agent (WhatsApp)

**Gerekenler:**
- WhatsApp Business API hesabı
- n8n (veya Node.js)
- Claude API key
- OpenClaw veya MCP server

**Kod (Node.js basit hali):**
```javascript
// WhatsApp webhook handler
app.post('/webhook', async (req, res) => {
  const { from, body } = req.body.entry[0].changes[0].value.messages[0];
  
  // Claude ile intent analizi
  const intent = await claude.analyze(body);
  
  if (intent === 'order_inquiry') {
    await whatsapp.send(from, "Sipariş numaranızı verin, kontrol edeyim.");
  } else if (intent === 'complaint') {
    await slack.notify(`Şikayet var: ${body}`);
  } else {
    await whatsapp.send(from, "En kısa sürede dönüş yapacağız.");
  }
  
  res.sendStatus(200);
});
```

### n8n Workflow Kurulumu

```
[WhatsApp Webhook]
↓
[Claude Code Node] → Intent classification
↓
[Switch Node] → order_inquiry / complaint / other
↓
[WhatsApp Send Node] / [Slack Node] / [Email Node]
```

---

## Yeni GitHub Keşifleri — Agent Yapımı İçin

| Repo | ⭐ | Kapsam |
|------|-----|--------|
| [waberyhq/cli](https://github.com/waberyhq/cli) | — | WhatsApp flow CLI + MCP |
| [Kenneth0416/whatsapp-agent](https://github.com/Kenneth0416/whatsapp-agent) | — | TypeScript WhatsApp Web agent (MCP uyumlu) |
| [manu14357/tota-agent](https://github.com/manu14357/tota-agent) | 7⭐ | 11 LLM provider — agent framework |
| [prempatkar936-lang/MPPRS-AI-Agent](https://github.com/prempatkar936-lang/MPPRS-AI-Agent) | — | WhatsApp/Instagram/Messenger birleşik agent |
| [mellowmir94/meta-ads-langgraph-agent](https://github.com/mellowmir94/meta-ads-langgraph-agent) | — | LangGraph Meta Ads monitoring |

---

## Herkesin Kaçırdığı Nokta #2:

Meta Business Agent ($200/ay) yerine kendi agent'ını yapmak:
- **Maliyet:** $0 (sabit) vs $200/ay
- **Kontrol:** Tamamen senin elinde
- **Esneklik:** İstediğin workflow'u kurarsın
- **Öğrenme:** Pazarın en talepkar becerisi

Bir kez öğren = sonsuz uygulama.

---

## Kaynaklar

1. [Meta Graph API — Resmi Dokümantasyon](https://developers.facebook.com/docs/graph-api)
2. [WhatsApp Business API — Resmi Dokümantasyon](https://developers.facebook.com/docs/whatsapp)
3. [NotFair — Claude Code Meta Ads Skill](https://github.com/nowork-studio/NotFair)
4. [tota-agent — 11 LLM Provider](https://github.com/manu14357/tota-agent)
5. [meta-ads-langgraph-agent — LangGraph Monitoring](https://github.com/mellowmir94/meta-ads-langgraph-agent)
6. [Prempatkar MPPRS AI Agent](https://github.com/prempatkar936-lang/MPPRS-AI-Agent)
7. [WhatsApp Agent TypeScript](https://github.com/Kenneth0416/whatsapp-agent)

---

## LinkedIn Paylaşımı

**Post Taslağı:**

```
Meta için AI agent yapmak sandığın kadar zor değil.

11 farklı agent fikri, hepsi açık kaynak araçlarla yapılabilir:

1️⃣ Abandoned Cart Recovery — Sepet terk edene 1 saat sonra mesaj
2️⃣ Lead Scoring — Kimin alacağını AI bilir
3️⃣ A/B Test Otomasyonu — Kazananı seçer, kaybedeni durdurur
4️⃣ Stok Uyarı — Bittiğinde anında bilgi
5️⃣ Çok Dilli Destek — 11 dilde otomatik cevap

Bunların hepsi:

✓ WhatsApp Business API
✓ Claude Code
✓ n8n
✓ Açık kaynak MCP server'lar

$200/ay Meta Business Agent yerine = $0.

Tek ihtiyacın olan: 1 hafta kurulum.

Yatırım geri dönüşü: 1 ay.

Sence hangisi mantıklı? 👇

#AI #Meta #WhatsApp #Otomasyon
```

---

*Son güncelleme: 2026-06-19 12:00*
