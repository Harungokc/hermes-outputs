# Meta İçin Yapılabilecek AI Ajansları — 2026-06-13 18:00

## Özet

Meta platformları (WhatsApp, Instagram, Facebook) için özel AI ajanları geliştirmek artık çok kolay. MCP (Model Context Protocol) server'lar ile WhatsApp Business API, Instagram Graph API ve Meta Ads API'ye tek bir ajan üzerinden erişilebiliyor.

## Hangi API'ler Kullanılabilir

### WhatsApp Business API
| API | Endpoint | Kullanım |
|-----|----------|----------|
| Cloud API | business.whatsapp.com | Template mesaj, müşteri yanıtları |
| On-Premises API | Self-hosted | Daha fazla kontrol, altyapı gerektirir |
| Webhooks | /webhooks | Gelen mesajları yakala |

### Instagram Graph API
| API | Endpoint | Kullanım |
|-----|----------|----------|
| Instagram Messaging API | graph.instagram.com | DM yanıtları, story mention'lar |
| Instagram Content Publishing API | graph.instagram.com | Otomatik post paylaşımı |
| Insights API | graph.instagram.com | Analytics, takipçi verileri |

### Meta Ads API
| API | Kullanım |
|-----|----------|
| Ad Campaign API | Kampanya oluşturma, bütçe yönetimi |
| Ad Set API | Hedefleme, teklif yönetimi |
| Ad Creative API | Reklam metni, görsel oluşturma |
| Insights API | Performans verileri |

## Örnek Projeler ve GitHub Repoları

### WhatsApp AI Agent Templates
| Repo | ⭐ | Açıklama |
|------|-----|----------|
| [ Social Flow](https://github.com/benyaminl/social-flow) | 144 | Python ile WhatsApp bot framework |
| [Meta MCP Server](https://github.com/FilIP133722/Social-Media-MCP-Server) | 200+ | Meta platformları için MCP server (WhatsApp, Instagram, Facebook) |

### Instagram Automation
| Repo | ⭐ | Açıklama |
|------|-----|----------|
| [instauto](https://github.com/mifi/instauto) | 840 | Instagram bot/automation library (TypeScript) |
| [Tools-for-Instagram](https://github.com/linkfy/Tools-for-Instagram) | 541 | Python Instagram otomasyon scriptleri |
| [automated-insta-dm-outreach-agent](https://github.com/Arnav8452/automated-insta-dm-outreach-agent-openclaw) | 2 | OpenClaw ile Instagram DM outreach |

### Reklam Ajansı
| Repo | ⭐ | Açıklama |
|------|-----|----------|
| [advertising-hub](https://github.com/itallstartedwithaidea/advertising-hub) | 19 | 14 platform için MCP server + AI ajan |
| [zuckerbot](https://github.com/DatalisHQ/zuckerbot) | 8 | MCP server + CLI for Meta Ads |

## Adım Adım: Meta İçin AI Agent Geliştirme

### Adım 1: Meta Developer Hesabı Oluştur
1. [developers.facebook.com](https://developers.facebook.com) adresine git
2. "My Apps" → "Create App" → "Business" seç
3. WhatsApp Business API veya Instagram API'yi ekle
4. App ID ve App Secret al

### Adım 2: API Key'leri Güvenli Tut
```bash
# .env dosyası oluştur
WHATSAPP_TOKEN=your_token_here
INSTAGRAM_ACCESS_TOKEN=your_token_here
META_ADS_TOKEN=your_token_here
```

### Adım 3: MCP Server Kurulumu (Önerilen)
```bash
# Meta MCP Server clone et
git clone https://github.com/FilIP133722/Social-Media-MCP-Server.git
cd Social-Media-MCP-Server

# Environment ayarla
cp .env.example .env
# API key'leri gir

# Çalıştır
python mcp_server.py
```

### Adım 4: Claude Code veya n8n ile Bağla
```bash
# Claude Code'da MCP server'ı aktif et
# settings.json'da:
{
  "mcpServers": {
    "meta": {
      "command": "python",
      "args": ["/path/to/Social-Media-MCP-Server/mcp_server.py"]
    }
  }
}
```

### Adım 5: Agent'a Görev Ver
```
# Claude Code'da örnek komutlar:
# "Instagram'da son 10 günde en çok etkileşim alan post'ları analiz et"
# "WhatsApp'tan gelen müşteri şikayetlerini kategorize et ve öncelik sırala"
# "Facebook Ads'te ROAS'ı en düşük 5 kampanyayı bul ve kapat"
```

## Yapılabilecek 5 AI Agent

### Agent 1: WhatsApp Müşteri Triyaj Agent
- **Görev:** Gelen mesajları otomatik kategorize et (sipariş, şikayet, bilgi, satış)
- **API:** WhatsApp Business API webhooks
- **Çıktı:** Kategorize edilmiş mesaj listesi + öncelik skoru

### Agent 2: Instagram -> WhatsApp Satış Dönüşüm Agent
- **Görev:** Instagram DM'lerinde ürün ilgilenenlere otomatik WhatsApp linki gönder
- **API:** Instagram Graph API (DM'ler) + WhatsApp Cloud API (mesaj gönderme)
- **Çıktı:** Otomatik DM yanıtı + WhatsApp Business mesajı

### Agent 3: Meta Ads Performans Analiz Agent
- **Görev:** Haftalık reklam performansını analiz et, en iyi/kötü kampanyaları raporla
- **API:** Meta Ads Insights API
- **Çıktı:** PDF özet rapor + Slack/Discord bildirimi

### Agent 4: Abandoned Cart Recovery Agent
- **Görev:** Sepeti terk eden müşterilere 1s, 24s, 72s sonra otomatik hatırlatma
- **API:** E-ticaret veritabanı + WhatsApp Cloud API
- **Çıktı:** Otomatik mesaj serisi + dönüşüm oranı takibi

### Agent 5: Instagram Content Calendar Agent
- **Görev:** Haftalık içerik takvimi oluştur, otomatik post paylaş
- **API:** Instagram Content Publishing API + AI görsel üretimi (DALL-E, Midjourney)
- **Çıktı:** Haftalık post takvimi + otomatik paylaşım

## Kaynaklar

- [Meta Developers](https://developers.facebook.com)
- [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [Meta MCP Server](https://github.com/FilIP133722/Social-Media-MCP-Server) (200+⭐)
- [Social Flow](https://github.com/benyaminl/social-flow) (144⭐)
- [instauto](https://github.com/mifi/instauto) (840⭐)
