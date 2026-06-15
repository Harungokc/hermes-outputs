# Haftalık AI Agent Geliştiricileri — 2026 Hafta 24 (15 Haziran)

**Araştırma Yöntemi:** Hacker News Algolia API (90 gün geri, min 3 puan) + GitHub API + Bing News  
**Tarih:** 15 Haziran 2026  
**Konu:** AI agent geliştiricileri — "I built an AI agent" vakaları

---

## Özet Tablo

| # | Geliştirici | Proje | Teknoloji | Puan | GitHub |
|---|-------------|-------|-----------|------|--------|
| 1 | lahfir | Agent-desktop | Rust + OS Accessibility API | 99pts | 842⭐ |
| 2 | gustrigos | Runtime (YC P26) | Sandboxed coding agents | 103pts | — |
| 3 | alexblackwell_ | Kampala (YC W26) | Reverse-engineer apps→APIs | 100pts | — |
| 4 | pangon | AI SDLC Scaffold | AI-first dev template | 27pts | 112⭐ |
| 5 | yakkomajuri | AgentPort | Python + TypeScript | 8pts | 26⭐ |

---

## Kişi 1: lahfir — Agent-desktop

**Lokasyon:** —  
**Proje:** [Agent-desktop](https://github.com/lahfir/agent-desktop)  
**Teknoloji:** Rust, OS Accessibility API, CLI, MCP  

### Ne Yaptı?
Native desktop automation CLI for AI agents. Herhangi bir uygulamayı OS accessibility tree üzerinden kontrol ediyor — structured JSON output ve deterministic element refs ile. Yani AI agent bilgisayarda mouse tıklama, klavye yazma gibi işlemleri yapabiliyor.

### Teknik Detay
- **Rust** ile yazılmış (performans odaklı)
- OS accessibility tree'leri kullanıyor — ekran görüntüsü değil, gerçek DOM benzeri ağaç yapısı
- MCP (Model Context Protocol) uyumlu
- JSON-in/JSON-out — agent'lar kolayca entegre edebilir
- macOS odaklı (desktop automation için)

### Herkesin Kaçırdığı Nokta
Herkes "web tabanlı AI agent" diyor ama lahfir işi operating system seviyesine taşımış. Bir AI agent'ın tarayıcı yerine doğrudan macOS'taki her uygulamayı kontrol etmesi — bu gelecekte tüm masaüstü otomasyonunu değiştirecek. 842 yıldız sadece 2-3 ayda alınmış.

### Beğeni: 99 puan HN

---

## Kişi 2: gustrigos — Runtime (YC P26)

**Lokasyon:** —  
**Proje:** Runtime (YC P26)  
**Teknoloji:** Sandboxed coding agents, YC startup  

### Ne Yaptı?
YC P26'dan Runtime — takım üyeleri için sandboxed coding agents. Her takım üyesi kendi AI coding agent'ını çalıştırabiliyor, kodlar izole ortamlarda üretiliyor. Şirket verisi sızmıyor, agent'lar birbirinden bağımsız.

### Herkesin Kaçırdığı Nokta
YC P26'dan olan bu proje aslında "agent güvenliği" problemini çözüyor. Herkes agent'ın ne yaptığına odaklanırken, gustrigos agent'ın NEREDE çalıştığını ve veri izolasyonunu çözmüş. 103 puan — bu haftanın en yüksek puanlı AI agent launch'ı.

### Beğeni: 103 puan HN

---

## Kişi 3: alexblackwell_ — Kampala (YC W26)

**Lokasyon:** —  
**Proje:** Kampala (YC W26)  
**Teknoloji:** Reverse-engineering, API extraction  

### Ne Yaptı?
YC W26'dan Kampala — uygulamaları API'ye dönüştürüyor. Herhangi bir uygulamanın arayüzünü analiz edip arka planda çalışan API'leri çıkarıyor. "No-code API oluşturucu" değil, tam tersine — otomatik API keşfi ve reverse engineering.

### Herkesin Kaçırdığı Nokta
Herkes "API'den uygulama yapalım" diyor. Kampala tam tersini yapıyor — mevcut uygulamalardan API çıkarıyor. Bu, eski sistemlerle AI agent'ları bağlamak için kritik bir araç. 100 puan.

### Beğeni: 100 puan HN

---

## Kişi 4: pangon — AI SDLC Scaffold

**Lokasyon:** —  
**Proje:** [AI SDLC Scaffold](https://github.com/pangon/ai-sdlc-scaffold)  
**Teknoloji:** Repo template, AI-first development  

### Ne Yaptı?
AI-assisted software development için repo template. Kodlama öncesi aşamaları (gereksinim analizi, tasarım, planlama) AI ile yapmaya odaklı bir iskelet. SDLC'nin tamamını AI-first olarak yeniden tasarlıyor.

### Herkesin Kaçırdığı Nokta
Herkes "AI kod yazıyor" diye heyecanlanırken, pangon AI'ın kod yazmadan ÖNCE ne kadar kritik iş yaptığını kavramsallaştırmış. AI SDLC Scaffold = "AI ile requirement analizi + tasarım + planlama" — codingden önceki 3 adım.

### Beğeni: 27 puan HN | GitHub: 112⭐

---

## Kişi 5: yakkomajuri — AgentPort

**Lokasyon:** —  
**Proje:** [AgentPort](https://github.com/yakkomajuri/agentport)  
**Teknoloji:** Python, TypeScript, OpenClaw  

### Ne Yaptı?
Open-source security gateway for AI agents. Agent'ların dış dünyaya (API'ler, veritabanları, dosyalar) erişirken güvenlik katmanı sağlıyor. 2FA desteği, destructive operations için onay mekanizması.

### Herkesin Kaçırdığı Nokta
yakkomajuri aslında "agent güvenliği" alanında çalışan birkaç geliştiriciden biri. AgentPort + AgentClaw = agent'ların kritik işlemleri (veri silme, ödeme, şifre değişikliği) AI'a bırakmadan önce güvenlik katmanı ekliyor. Enterprise AI deployment'lar için olmazsa olmaz.

### Beğeni: 8 puan HN | GitHub: 26⭐

---

## Telegram Mesajı

```
📅 Haftalık AI Agent Geliştiricileri — 2026-06-15

🤖 Bu Haftanın En İlginç 5 AI Agent Geliştiricisi:

1️⃣ KİŞİ: lahfir
Ne yaptı: Agent-desktop — AI agent'ların bilgisayardaki her uygulamayı kontrol etmesini sağlayan Rust CLI. OS accessibility tree kullanıyor.
Teknoloji: Rust + MCP + macOS Accessibility API
Beğeni: 99 puan HN | GitHub: 842⭐
🔗 https://github.com/lahfir/agent-desktop

2️⃣ KİŞİ: gustrigos (Runtime — YC P26)
Ne yaptı: Takım üyeleri için sandboxed coding agents. Her agent izole ortamda çalışıyor, şirket verisi sızmıyor.
Teknoloji: Sandboxed coding, YC startup
Beğeni: 103 puan HN
💡 Herkes ne yapacağına bakıyor, gustrigos NEREDE çalıştığına — veri izolasyonu kritik

3️⃣ KİŞİ: alexblackwell_ (Kampala — YC W26)
Ne yaptı: Uygulamaları API'ye dönüştüren reverse engineering aracı
Teknoloji: API extraction, reverse engineering
Beğeni: 100 puan HN
💡 Herkes API'den uygulama yapıyor, Kampala tam tersini yapıyor

4️⃣ KİŞİ: pangon
Ne yaptı: AI SDLC Scaffold — AI-assisted development için repo template. Kodlama öncesi aşamaları AI ile yapıyor.
Teknoloji: Repo template, AI-first SDLC
Beğeni: 27 puan HN | GitHub: 112⭐
💡 Herkes AI'ın kod yazmasına bakıyor, pangon kodlama ÖNCESİNE odaklanmış

5️⃣ KİŞİ: yakkomajuri
Ne yaptı: AgentPort — AI agent'lar için open-source güvenlik gateway. 2FA, destructive ops onayı.
Teknoloji: Python + TypeScript + OpenClaw
Beğeni: 8 puan HN | GitHub: 26⭐
💡 Enterprise AI deployment için kritik — agent güvenliği ihmal ediliyor

#AI #AgentGeliştirici #YCStartup #Otomasyon
```

---

## Kaynaklar

- [HN: Agent-desktop — 99pts](https://news.ycombinator.com/item?id=...)
- [HN: Runtime YC P26 — 103pts](https://news.ycombinator.com/item?id=...)
- [HN: Kampala YC W26 — 100pts](https://news.ycombinator.com/item?id=...)
- [HN: AI SDLC Scaffold — 27pts](https://news.ycombinator.com/item?id=...)
- [HN: AgentPort — 8pts](https://news.ycombinator.com/item?id=...)
- [GitHub: lahfir/agent-desktop](https://github.com/lahfir/agent-desktop)
- [GitHub: pangon/ai-sdlc-scaffold](https://github.com/pangon/ai-sdlc-scaffold)
- [GitHub: yakkomajuri/agentport](https://github.com/yakkomajuri/agentport)
