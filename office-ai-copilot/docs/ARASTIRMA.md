# 🔬 GitHub Manzara Araştırması

Bu kit sıfırdan tasarlanmadı. Önce "ofis otomasyonu AI agent" alanındaki mevcut
açık kaynak projeler detaylı tarandı, iki ana yaklaşım tespit edildi, aralarındaki
boşluk bulundu ve bu kitin tasarımı o boşluğu doldurmak üzere kuruldu.

Bu dosya o araştırmanın kaydıdır — neden bu mimari, neden n8n+Claude, neden hibrit.

---

## 1. Yöntem

5 ofis işinin (email, toplantı notu, rapor, dosya arama, takvim) her biri için
ayrı ayrı, çok açılı arama yapıldı:
- Email otomasyonu + Claude API + açık kaynak
- Toplantı notu / transkript özetleyici (self-hosted)
- Zapier alternatifi + rapor üretimi + Google Sheets
- Kişisel AI asistanı (takvim/email/ajan)
- n8n workflow şablon koleksiyonları

Üst sıradaki ~15 repo incelendi; en alakalı 4'ünün mimarisi (stack, klasör yapısı,
yıldız, tasarım deseni) GitHub sayfalarından derinlemesine okundu.

---

## 2. Bulgu: Alan İki Uca Ayrılıyor

### Uç 1 — Ağır Multi-Agent Sistemler (Python / LangGraph / LangChain)

| Repo | Stack | Yıldız | Değerlendirme |
|------|-------|--------|----------------|
| [berkyalkn/ai-personal-assistant](https://github.com/berkyalkn/ai-personal-assistant) | FastAPI + LangGraph + Next.js + Docker + K8s | ~1 ⭐ | Enterprise-grade mimari (supervisor + 5 alt-ajan, OAuth, checkpoint state, OpenShift manifest). Çok sağlam ama kurması saatler sürer; "kopyala-çalıştır" değil. |
| [AIXerum/personal-ai-assistant](https://github.com/AIXerum/personal-ai-assistant) | LangGraph supervisor, 5 alt-ajan (email/calendar/notion/slack/researcher) | ~4 ⭐ | Telegram/Slack/WhatsApp arayüzü. Çok katmanlı; soyut, somut ROI vaadi yok. |
| [JoelKong/PersonalAgents](https://github.com/JoelKong/PersonalAgents) | Çok ajanlı email+calendar+scraper | düşük | Benzer desen, benzer kurulum yükü. |

**Ortak sorun:** Teknik olarak etkileyici ama **erişilemez**. Düşük yıldız sayıları
da bunu doğruluyor — kimse kurup kullanamıyor. Net bir problem/ROI çerçevesi yok.

### Uç 2 — n8n Şablon Koleksiyonları (Yüksek Yıldız, Düşük Kod)

| Repo | İçerik | Neden popüler |
|------|--------|----------------|
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 280+ hazır workflow (Gmail, Slack, OpenAI, Claude…) | Kopyala-import-çalıştır; anında değer |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Claude ile n8n workflow üretimi (MCP) | Erişilebilir, pratik |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Privacy-first toplantı notu (local Whisper+Ollama, Rust) | Net problem, net çözüm |

**Ortak güç:** Erişilebilir, pratik, yüksek yıldız. **Ortak sınır:** Ya tek bir işe
odaklı (meetily sadece toplantı), ya da odaksız bir şablon yığını (280 template
arasında kaybolursun) — uçtan uca "şu 5 işi şu ROI ile çöz" diyen bir kit yok.

---

## 3. Boşluk (Bu Kitin Var Olma Sebebi)

Hiçbir repo, hedeflediğimiz spesifik çerçeveyi sunmuyor:

> **5 net ofis işi → ~$15-50/ay → haftada 10+ saat → 1 saatte kurulabilir.**

- LangGraph sistemleri → çok karmaşık (kimse kuramıyor, düşük yıldız).
- n8n yığınları → çok dağınık (odak ve ROI hikayesi yok).
- meetily gibi tekil araçlar → sadece 1 işi çözüyor.

**Fırsat:** Net problem + net maliyet + kurulabilirlik + iki kitleye (low-code & developer)
hitap. Erişilebilirliği n8n'den, somut problem/ROI çerçevesini ise eksik olan yerden alıyoruz.

---

## 4. Araştırmadan Çıkan Tasarım Kararları

| Karar | Gerekçe (araştırmaya dayalı) |
|-------|------------------------------|
| **n8n + Claude (Zapier değil)** | Zapier kapalı SaaS → repo olarak paylaşılamaz. n8n açık kaynak → JSON export herkes import eder. En yüksek-yıldızlı repo'lar bu formatta. |
| **Hibrit (n8n + Python)** | Uç 2 (n8n) erişilebilirliği, Uç 1 (Python) developer kitlesini yakalar. Tek repo iki kitleye hitap eder. |
| **Tek-çağrı mimarisi (LangGraph değil)** | Uç 1'in düşük yıldızı, ağır framework'ün benimsenmeyi öldürdüğünü gösteriyor. Çoğu ofis işi için "tek görev → tek prompt → yapılandırılmış çıktı" yeterli ve ucuz. |
| **Haiku + Sonnet model ayrımı** | Maliyet odaklı: ucuz işler (triyaj/çıkarım) Haiku, kaliteli işler (rapor/özet) Sonnet. ROI hikayesini gerçekçi tutar. |
| **İnsan-döngüde (taslak varsayılan)** | Mevcut sistemlerin çoğu otomatik gönderim yapıyor (risk). Geri alınamaz işlemleri (mail/davet) taslak bırakmak sorumlu otomasyon imajı verir. |
| **Net problem + ROI çerçevesi** | Boşluğun ta kendisi. README'yi problem tablosu + maliyet dökümüyle açmak, soyut "AI asistanı" repo'larından ayrışmanın yolu. |

---

## 5. Kaynaklar

İncelenen repo ve referanslar:
- https://github.com/berkyalkn/ai-personal-assistant
- https://github.com/AIXerum/personal-ai-assistant
- https://github.com/JoelKong/PersonalAgents
- https://github.com/enescingoz/awesome-n8n-templates
- https://github.com/czlonkowski/n8n-mcp
- https://github.com/Zackriya-Solutions/meetily
- https://github.com/alexkroman/opennotes
- https://github.com/AlexisBalayre/AI-Powered-Meeting-Summarizer
- https://github.com/ethanplusai/harvey
- [Activepieces — açık kaynak Zapier alternatifi](https://www.activepieces.com/blog/zapier-alternatives)
- [Anthropic Claude API & fiyatlandırma](https://www.anthropic.com/pricing)

---

> Bu araştırma Haziran 2026'da yapıldı. Alan hızlı değişiyor; yeni repo'lar
> çıktıkça bu analiz güncellenebilir. Katkı/güncelleme için issue açabilirsin.
