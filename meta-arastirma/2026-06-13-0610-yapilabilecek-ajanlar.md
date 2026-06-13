# Meta İçin Yapılabilecek AI Ajansları Araştırması — 2026-06-13-0610

## Özet

Meta platformları için özel AI ajanları geliştirmek artık her zamankinden kolay. Meta'nın kendi siteleri (developers.facebook.com, business.whatsapp.com) bot koruması olmadan çalışıyor ve açık kaynak MCP server'lar ile Claude AI entegrasyonu çok basit. 200+ API endpoint'i ile Facebook Pages, Instagram, WhatsApp Business, Ads Manager'ın hepsi programatik olarak yönetilebiliyor.

**Herkesin Kaçırdığı Nokta:** Bugün açıklanan Meta 8.000 kişilik işten çıkarma haberleri aslında bir fırsat. Her kesinti demek otomasyona olan yatırımın artması demek. Zuckerberg'in "AI transformation mistakes" itirafı, şirketin daha fazla açık kaynak ve API erişimi sunmak zorunda kalacağını gösteriyor. Bu da bağımsız geliştiriciler için büyük fırsat.

---

## Bulunan Araçlar ve Linkler

### 1. oliverames/meta-mcp-server
| Özellik | Değer |
|---------|-------|
| **Stars** | 15 |
| **Link** | https://github.com/oliverames/meta-mcp-server |
| **Açıklama** | Claude AI ile Meta Business verilerine doğal dil sorgulama |
| **Özellik** | 200+ tools, Insights, Audiences, Ad Library |
| **Dil** | TypeScript |

### 2. Lifecycle-Innovations-Limited/claude-ops ⭐18
| Özellik | Değer |
|---------|-------|
| **Stars** | 18 |
| **Link** | https://github.com/Lifecycle-Innovations-Limited/claude-ops |
| **Açıklama** | Business operating system for Claude Code — 25 skills, 13 agents, smart daemon. Unified inbox (WhatsApp, email, Slack) |
| **Özellik** | WhatsApp, email, Slack entegrasyonu, AI agent orchestration |
| **Dil** | Shell/Claude Code |

### 3. meensinaai-ai/meensinaai-meta-ads-department ⭐0
| Özellik | Değer |
|---------|-------|
| **Link** | https://github.com/contatomeensinaai-ai/meensinaai-meta-ads-department |
| **Açıklama** | Meta Ads uzmanı 10 AI ajanından oluşan ekip (Andromeda 2026) |
| **Özellik** | Knowledge base versiyonlama, ads optimization |
| **Dil** | Bilinmiyor |

### 4. thanhauco/harness-next ⭐0
| Özellik | Değer |
|---------|-------|
| **Link** | https://github.com/thanhauco/harness-next |
| **Açıklama** | Business hedefinden otomatik kampanya üreten, deploy eden ve izleyen meta-platform |
| **Özellik** | End-to-end kampanya otomasyonu |
| **Dil** | Bilinmiyor |

---

## Açık Kaynak Alternatifler

| Araç | Dil | Özellik | GitHub |
|------|-----|---------|--------|
| meta-mcp-server | TypeScript | Claude + Meta Business entegrasyonu | oliverames/meta-mcp-server |
| claude-ops | Shell | Business OS for Claude Code | Lifecycle-Innovations-Limited/claude-ops |
| chat-to-ads-engine | Python | WhatsApp → Advantage+ köprü | dousheng34/chat-to-ads-engine |
| facebook-ads-library-mcp | Python | Claude + FB Ads Library | proxy-intell/facebook-ads-library-mcp |

---

## Adım Adım Yapım Rehberi

### Meta WhatsApp AI Agent Oluşturma

**1. Gerekli Araçlar:**
```
- WhatsApp Business API hesabı
- Meta Developer uygulaması
- n8n (workflow otomasyonu)
- Claude AI veya OpenAI API
- Cloud hosting (VPS veya Heroku)
```

**2. Mimari:**
```
[Kullanıcı WhatsApp mesajı]
    ↓
[WhatsApp Business API Webhook]
    ↓
[n8n Workflow]
    ↓
[Claude AI API - Yanıt üretimi]
    ↓
[WhatsApp Business API - Yanıt gönder]
```

**3. n8n Workflow Adımları:**
```javascript
// 1. Webhook node: WhatsApp'tan gelen mesajları yakala
// 2. HTTP Request node: Claude API'ye istek at
// 3. WhatsApp Send Message node: Yanıtı gönder
```

**4. Güvenlik Önlemleri:**
- Input sanitization (prompt injection'a karşı)
- Rate limiting (spam koruması)
- User authentication (kimlik doğrulama)
- Audit logging (tüm konuşmaları kaydet)

---

## Kaynaklar

- https://github.com/oliverames/meta-mcp-server
- https://github.com/Lifecycle-Innovations-Limited/claude-ops
- https://github.com/dousheng34/chat-to-ads-engine
- https://business.whatsapp.com/developers/developer-hub
- https://developers.facebook.com/docs/marketing-apis
