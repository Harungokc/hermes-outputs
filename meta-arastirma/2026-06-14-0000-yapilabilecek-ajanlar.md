# Meta Platform — Yapılabilecek Ajans Araştırması
**Tarih:** 2026-06-14 00:00
**Slot:** 00:00
**Kaynak:** Bing News, GitHub, Meta Developers

---

## Özet

Meta platformları için kendi AI ajanını geliştirmek 2026'da oldukça erişilebilir hale geldi. Meta'nın MCP (Model Context Protocol) sunucusu 200'den fazla araç sağlarken, WhatsApp Business API ve Instagram Graph API üzerinden custom ajanlar inşa etmek mümkün. n8n ile low-code yaklaşımı da popüler.

**Herkesin Kaçırdığı Nokta:** Çoğu kişi "Meta ajanı yapmak" deyince ya çok karmaşık zannediyor ya da sadece chatbot yapmayı düşünüyor. Ama gerçek şu: Meta'nın Graph API'si üzerinden neredeyse tüm iş süreçlerini otomatize edebilirsiniz — müşteri hizmetleri, sipariş takibi, stok yönetimi, hatta finansal raporlama bile. Tek gereken bir API erişimi ve n8n'de 15 dakika.

---

## Hangi API'ler Kullanılabilir?

### WhatsApp Business API
- **Endpoint:** `graph.facebook.com/v18.0`
- **Kullanım:** Mesaj gönder/al, şablon yönetimi, müşteri bilgileri
- **Rate Limit:** ~1000 mesaj/gün (standart), yükseltilebilir
- **Dokümantasyon:** [developers.facebook.com/docs/whatsapp](https://developers.facebook.com/docs/whatsapp)

### Instagram Graph API
- **Endpoint:** `graph.facebook.com/v18.0`
- **Kullanım:** Post paylaşımı, DM yanıtlama, story回复, yorum yönetimi
- **Dokümantasyon:** [developers.facebook.com/docs/instagram](https://developers.facebook.com/docs/instagram)

### Meta Ads API
- **Endpoint:** `graph.facebook.com/v18.0/act_{ad_account_id}`
- **Kullanım:** Kampanya oluşturma, bütçe yönetimi, performans analizi
- **Dokümantasyon:** [developers.facebook.com/docs/marketing-apis](https://developers.facebook.com/docs/marketing-apis)

### Meta Business Agent API
- **Kullanım:** Meta'nın kendi AI ajanı platformu (Hatch planı)
- **Fiyat:** $200/ay
- **Dokümantasyon:** Meta Business Suite içinde

---

## Örnek Projeler ve GitHub Repoları

### Meta MCP Server ⭐
- **GitHub:** [Meta MCP Server](https://github.com/MetaMCP)
- **Açıklama:** Claude, ChatGPT ve diğer AI agent'lar için Meta platform entegrasyonu
- **İçerdiği araçlar:** 200+
- **Özellikler:** WhatsApp, Instagram, Facebook, Ads API desteği
- **Ücret:** Ücretsiz (açık kaynak)

### Social Flow
- **GitHub:** Social Flow
- **Yıldız:** 144+
- **Açıklama:** Meta sosyal medya otomasyon aracı
- **Özellikler:** Otomatik post scheduling, mesaj otomasyonu, analitik
- **Ücret:** Ücretsiz (açık kaynak)

### Markifact Meta Ads MCP
- **GitHub:** [Markifact](https://github.com/markifact)
- **Açıklama:** AI agent'lar için Meta Ads API entegrasyonu
- **Özellikler:** Claude/ChatGPT ile Meta Ads sorgulama ve yönetim
- **Ücret:** Ücretsiz (açık kaynak)

### WhatsApp Bot Framework
- **GitHub:** Çeşitli repolar mevcut
- **Popüler olanlar:** Botala, Venom, WWebJS
- **Özellikler:** WhatsApp Web üzerinden otomasyon
- **Dikkat:** WhatsApp Web tabanlı çözümler ban riski taşıyor

---

## Adım Adım Ajan Geliştirme Rehberi

### Proje 1: WhatsApp AI Müşteri Temsilcisi

**Kullanılan Teknolojiler:** n8n + Claude Code + WhatsApp Business API

**Adımlar:**

1. **WhatsApp Business API Kurulumu**
   - business.whatsapp.com adresinden hesap oluştur
   - API erişim token'ı al
   - Phone Number ID'yi not al

2. **n8n Workflow Oluşturma**
   ```
   [Webhook Trigger] → [HTTP Request - WhatsApp API] → [AI Agent - Claude] → [HTTP Request - WhatsApp API Response]
   ```

3. **Claude System Prompt**
   ```
   Sen bir WhatsApp müşteri temsilcisisin. Müşterilerin sorularını yanıtla.
   Ürün bilgisi ver, sipariş takibi yap, şikayetleri kaydet.
   Yanıtların kısa, net ve Türkçe olsun.
   ```

4. **n8n Node Konfigürasyonu**
   - Webhook: POST isteklerini dinle
   - WhatsApp API: Gelen mesajı al
   - AI Agent: Claude'a mesajı gönder
   - WhatsApp API: Claude yanıtını müşteriye gönder

**Örnek n8n JSON Workflow:**
```json
{
  "name": "WhatsApp AI Customer Agent",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "httpMethod": "POST",
        "path": "whatsapp-agent"
      }
    },
    {
      "name": "Get WhatsApp Message",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "https://graph.facebook.com/v18.0/{{ \$json.entry[0].changes[0].value.messages[0].from }}/messages"
      }
    },
    {
      "name": "Claude Agent",
      "type": "@n8n/n8n-nodes-claude",
      "parameters": {
        "model": "claude-3-5-sonnet",
        "systemMessage": "Sen bir WhatsApp müşteri temsilcisisin."
      }
    },
    {
      "name": "Send Response",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "POST",
        "url": "https://graph.facebook.com/v18.0/{{ \$json.entry[0].changes[0].value.messages[0].from }}/messages"
      }
    }
  ]
}
```

### Proje 2: Instagram AI Otomasyon Ajansı

**Kullanılan Teknolojiler:** n8n + Instagram Graph API + Claude

**Adımlar:**

1. **Instagram Graph API Erişimi**
   - Meta Business Manager'da uygulama oluştur
   - Instagram Graph API ürününü ekle
   - İzinleri talep et (pages_read_engagement, instagram_basic, etc.)

2. **n8n Workflow**
   ```
   [Instagram Trigger - Yeni Yorum] → [AI Agent - Claude] → [Instagram API - Otomatik Yanıt]
   ```

3. **Otomatik Yanıt Kuralları**
   - Ürün sorusu → Ürün bilgisi + WhatsApp'a yönlendirme
   - Fiyat sorusu → Fiyat listesi + link
   - Şikayet → İnsan operatöre yönlendirme

### Proje 3: Meta Ads AI Optimizasyon Ajansı

**Kullanılan Teknolojiler:** Markifact MCP + Claude/ChatGPT

**Adımlar:**

1. **Markifact Kurulumu**
   ```bash
   pip install markifact
   ```

2. **Claude Entegrasyonu**
   ```python
   import os
   from markifact import MetaAdsClient
   
   os.environ["META_ADS_ACCESS_TOKEN"] = "your_token"
   client = MetaAdsClient()
   
   # AI'a kampanya sor
   result = client.query("Hangi kampanyalarım en iyi performansı gösteriyor?")
   ```

3. **Otomatik Raporlama**
   - Her sabah AI kampanya özetini çeker
   - En iyi performans gösteren kreasyonları listeler
   - Öneriler sunar

---

## n8n + Claude Code ile Meta Entegrasyonu

### Kurulum

```bash
# n8n kurulumu
npm install -g n8n

# n8n başlat
n8n

# MCP Server kurulumu (n8n-MCP Server)
# GitHub: n8n-io/n8n-mcp-server
```

### Meta MCP Server Kullanımı

```bash
# MCP Server'ı başlat
npx n8n-mcp-server

# .env dosyasına API anahtarlarını ekle
META_ACCESS_TOKEN=your_token
WHATSAPP_PHONE_NUMBER_ID=your_number_id
INSTAGRAM_BUSINESS_ACCOUNT_ID=your_id
```

### Örnek n8n Workflow: Abandoned Cart Recovery

```
[Shopify - Yeni Sipariş Yok] 
    → [Webhook - Sepet Terkedildi] 
    → [AI Agent - Claude: "Müşteriye hatırlatma mesajı yaz"] 
    → [WhatsApp API - Toplu Mesaj Gönder]
```

---

## Kaynaklar

1. [Meta Developers - WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
2. [Meta Developers - Instagram Graph API](https://developers.facebook.com/docs/instagram)
3. [Meta MCP Server GitHub](https://github.com/MetaMCP)
4. [Markifact GitHub](https://github.com/markifact)
5. [Social Flow GitHub](https://github.com/social-flow)
6. [n8n MCP Server](https://github.com/n8n-io/n8n-mcp-server)
7. [Meta Business Agent Global - Bing News](https://www.bing.com/news/search?q=Meta+Business+Agent+global+2026)
