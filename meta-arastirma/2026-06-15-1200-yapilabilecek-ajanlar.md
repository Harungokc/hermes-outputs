# Meta Platform Araştırması — Yapılabilecek Ajans — 2026-06-15 12:00

## Özet

Meta platformları için kendi AI ajanını geliştirmek artık çok kolay. MCP (Model Context Protocol) server'lar sayesinde kod yazmadan, sadece Claude Code + n8n ile Meta Ads ajanı, WhatsApp müşteri ajanı veya Instagram otomasyon ajanı yapılabiliyor. Açık kaynak repolardan (NotFair 2851⭐, meta-ads-mcp 987⭐) başlayıp, kendi özel ajanını 1-2 hafta içinde çalıştırmak mümkün.

---

## Hangi API'ler Kullanılabilir

### WhatsApp Business API

| Endpoint | Ne İşe yarar | Dökümantasyon |
|----------|--------------|---------------|
| `POST /messages` | Mesaj gönder | developers.facebook.com/docs/whatsapp/business-platform |
| `GET /messages` | Mesajları oku |Webhook ile anlık bildirim |
| `POST /media` | Medya gönder (görsel, doküman) | Max 100MB |
| `GET /phone_numbers` | Kayıtlı telefonları listele | Business account yönetimi |

**Gereksinimler:**
- WhatsApp Business Platform hesabı
- Phone Number ID
- Access Token (Permanent token gerekiyor)
- WABA (WhatsApp Business Account) onayı

### Instagram Graph API

| Endpoint | Ne İşe Yapar | Gereksinim |
|---------|--------------|------------|
| `POST /{ig-user-id}/messages` | DM gönder | Instagram Business hesabı |
| `GET /{ig-user-id}/messages` | Gelen DM'leri oku | Webhook gerekiyor |
| `POST /{media-id}/children` | Carousel post oluştur | Fotoğraf/video ID'leri |
| `GET /{ig-user-id}/insights` | Etkileşim metrikleri | Instagram Professional |

### Meta Ads API

| Endpoint | Ne İşe Yapar |
|---------|--------------|
| `GET /act_{ad-account-id}/ads` | Reklam kampanyalarını listele |
| `POST /act_{ad-account-id}/ads` | Yeni reklam oluştur |
| `GET /{ad-id}/insights` | Reklam metrikleri |
| `PUT /{ad-id}` | Reklam güncelle/durdur |

---

## Adım Adım: Meta Ads Agent Yapımı

### Adım 1: MCP Server Kurulumu (30 dakika)

```bash
# NotFair — Claude Code Meta Ads becerileri
git clone https://github.com/nowork-studio/NotFair.git
cd NotFair

# veya google-meta-ads-ga4-mcp — n8n uyumlu
git clone https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp.git
```

### Adım 2: Claude Code Entegrasyonu (1 saat)

```
1. Claude Code'u aç
2. NotFair klasörünü project olarak aç
3. /meta-ads — Meta Ads komutlarını kullan
4. Örnek: "/meta-ads create-campaign name=Summer-Sale budget=500"
```

### Adım 3: n8n Workflow Kurulumu (2 saat)

```
n8n Workflow:
Trigger (Zamanlı veya Webhook)
→ HTTP Request (Meta Ads API)
→ Claude Code Node (karar)
→ Koşul (if/else)
→ Sonuç döndür
```

### Adım 4: Tam Otomasyon (1 gün)

```
Tam Sistem:
1. Her sabah 08:00 → n8n Meta Ads verilerini çeker
2. Claude kampanya performansını analiz eder
3. Anomali varsa Slack/WhatsApp alert
4. ROAS < %15 ise kampanya durdurur veya bütçeyi azaltır
5. Haftalık raporu otomatik oluşturur
```

---

## Yapılabilecek 5 Farklı Meta Ajansı

### 1. WhatsApp Müşteri Hizmetleri Ajansı
- **Ne yapar:** 7/24 AI yanıt, sipariş takibi, şikayet çözümü
- **Kullanılan:** WhatsApp Business API + Claude + n8n
- **Maliyet:** $200/ay (Meta Business Agent) veya kendi API + sunucu ~$50/ay
- **Gelir potansiyeli:** Müşteri başına $500-2000/ay

### 2. Instagram Satış Ajansı
- **Ne yapar:** Yorum otomasyonu, DM yanıtı, story mention takibi, otomatik satış
- **Kullanılan:** Instagram Graph API + Claude + n8n
- **Maliyet:** Sunucu ~$20/ay + Instagram Business hesabı
- **Gelir potansiyeli:** Müşteri başına $300-1000/ay

### 3. Meta Ads Yönetim Ajansı
- **Ne yapar:** Kampanya oluşturma, optimizasyon, A/B test, raporlama
- **Kullanılan:** Meta Ads API + NotFair/Claude + n8n
- **Maliyet:** Açık kaynak (sadece sunucu + API maliyeti)
- **Gelir potansiyeli:** Reklam bütçesinin %10-20'si

### 4. Sepet Terk Kurtarma Ajansı
- **Ne yapar:** e-ticaret sitelerinde sepeti terk edenlere otomatik WhatsApp hatırlatma
- **Kullanılan:** WhatsApp Business API + n8n + e-ticaret webhook
- **Maliyet:** ~$100/ay
- **Gelir potansiyeli:** Dönüşüm başına %10-15 komisyon

### 5. Çoklu Marka Yönetim Ajansı
- **Ne yapar:** Birden fazla markanın tüm Meta platformlarını tek merkezden yönetim
- **Kullanılan:** Meta Business Suite API + n8n + Claude
- **Maliyet:** ~$200-500/ay
- **Gelir potansiyeli:** Marka başına $1000-5000/ay

---

## Örnek GitHub Projeleri (Başlangıç Noktası)

| Repo | Yıldız | Ne işe yarar |
|------|--------|--------------|
| [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) | 2851⭐ | Meta Ads + Google Ads Claude Code becerileri |
| [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | 1010⭐ | n8n/Cursor/Claude uyumlu Ads MCP |
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 987⭐ | Facebook/Instagram Ads MCP server |
| [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) | 365⭐ | Learning Phase diagnosis |
| [markifact/markifact-mcp](https://github.com/markifact/markifact-mcp) | 40⭐ | 300+ araç — çoklu platform |

---

## Herkesin Kaçırdığı Nokta #1

**MCP server'lar ile sıfırdan kod yazmaya gerek yok.** Çoğu geliştirici Meta API entegrasyonunu sıfırdan yazmaya çalışıyor ama 3000+ yıldızlı açık kaynak repolar zaten çözülmüş problemleri sunuyor. NotFair'i Clone'la → Claude Code'a yükle → Meta Ads komutlarını kullan. Bu kadar basit.

## Herkesin Kaçırdığı Nokta #2

**Meta Business Agent ($200/ay) yerine kendi ajanınızı kurmak 10x daha ucuz ve daha esnek.** Meta'nın ajanı sadece Meta platformlarında çalışıyor. Kendi ajanınız = WhatsApp + Instagram + e-posta + CRM + stok sistemi + muhasebe yazılımı hepsi bir arada. Başlangıç maliyeti: Sunucu ($20/ay) + Claude API (~$50/ay) = ~$70/ay.

## Herkesin Kaçırdığı Nokta #3

**"Satış ajansı" fırsatı çok büyük ama kimse bakmıyor.** Türkiye'de 100binlerce KOBİ WhatsApp Business kullanıyor ama %95'i sadece manuel mesajlaşma yapıyor. Onlara "AI destekli WhatsApp satış ajansı" satmak = Müşteri başına 500-2000TL/ay. 10 müşteri = 5000-20000TL/ay ek gelir. Büyük fırsat: E-ticaret dışı sektörler (restaurant, kuaför, avukat, eczane).

---

## Kaynaklar

- [NotFair](https://github.com/nowork-studio/NotFair) — 2851⭐
- [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) — 1010⭐
- [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) — 987⭐
- [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/business-platform)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [Meta Ads API](https://developers.facebook.com/docs/marketing-api)
- [Meta Business Agent Global](https://www.bing.com/news/search?q=Meta+Business+Agent+available+globally+2026)
