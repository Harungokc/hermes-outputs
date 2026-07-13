# Nate Herk — Detaylı Analiz

**Son Tarama:** 2026-07-13

---

## Video 1: Claude Code for Normal People (jdbOVepEtUE)

** yayınlanma:** 2026-07-11 | **Süre:** 5.5 saat

### Özet
5.5 saatlik kapsamlı kurs — hiç kodlama geçmişi gerektirmeyen, AI native olma yolculuğu. İlk prompt'tan beceri oluşturma, alt-ajanlar, ikinci beyin ve bulutta çalışan otomasyonlara kadar.

### Herkesin Kaçırdığı Nokta
**"Beceriler, Alt-ajanlar ve Hafıza" üçlüsü birbirinden ayrı satılıyor ama aslında aynı sistemin parçaları.** Beceriler = tekrar eden görevler için hazır prompt'lar. Alt-ajanlar = becerileri kullanan bağımsız çalışanlar. Hafıza = onların geçmişinden öğrenen sistem. Birlikte çalıştığında, AI aslında bir ekip gibi oluyor.

### LinkedIn Post Fikri
> 5.5 saat harcadım ve tek bir şey öğrendim: AI'ı yanlış kullanıyoruz. Çoğu insan AI'a "bana bir şey yap" diyor. Doğru kullanım: AI'ına görev vermek, araç vermek ve onu tekrarlayan işlerden kurtulmak. Claude Code'la başladım — 6 saat sonra ilk otomasyonum çalışıyordu.

### İçerik Kapsamı
- 12 Mindset Shift (düşünce kalıpları değişimi)
- AI Operating System kurulumu (claude.md, settings.json, .env)
- Skills deep dive (beceriler = tekrar kullanılabilir prompt'lar)
- Sub-agents (alt-ajanlar = bağımsız çalışan AI)
- Second brain (5 seviye: Dosyalama → Özetleme → Analiz → Senaryo → Karar)
- Token management & prompt caching
- Scheduled automations (cron job benzeri)
- Google Workspace MCP entegrasyonu

---

## Video 2: Sol vs Fable: Manager vs Worker (EthxaDswUFo)

** yayınlanma:** 2026-07-09 | **Süre:** ~20 dakika

### Özet
GPT-5.6 Sol ve Claude Fable 5'i gerçek iş görevlerinde head-to-head test. Codex ve Claude Code üzerinde browser oyunları, interaktif websiteler ve API testleri.

### Herkesin Kaçırdığı Nokta
**Sol "ucuz ve hızlı worker" olarak konumlanıyor ama asıl değer proposition'ı maliyet/performans oranı değil — orchestration'a hazır olması.** Sol, agentic workflows için optimize edilmiş. Yani tek başına "daha iyi kod yazıyor" değil, "bir ekibin parçası olarak çalışmaya daha uygun."

### Test Sonuçları
| Test | Fable | Sol |
|------|-------|-----|
| Browser Bike Game | Daha yaratıcı | Daha hızlı |
| Scroll-Stopping Website | Daha iyi UX | Hızlı shipping |
| Five Visual Worlds | Daha rafine | Yüksek hacim |
| API One-Off | Daha tutarlı | 2-3x daha hızlı, %60 ucuz |

### Final Verdict
- **Fable = Manager model** (stratejik, yaratıcı, kalite kontrol)
- **Sol = Worker model** (hızlı, ucuz, agentic)
- **Hybrid yaklaşım en mantıklı** — Fable'a strateji, Sol'a execution

---

## Video 3: Sol Made This Video (J_jswzXhYJA)

** yayınlanma:** 2026-07-09 | **Süre:** ~5 dakika

### Özet
GPT-5.6 Sol'a tek bir prompt verip arkanı dönüyor. Sol araştırdı, script yazdı, ElevenLabs'la audio, HeyGen'le avatar, HyperFrames'de düzenledi ve her frame'i kendi kontrol etti.

### Herkesin Kaçırdığı Nokta
**"Ultra effort" = pahalı yanlış anlaşılıyor.** Sol'un çalıştığı ultra = yüksek token tüketimi, bu da maliyeti artırıyor. Asıl mesele: "High effort" ile "Ultra" arasındaki fark kaliteden çok kontrolden geliyor. Ultra = AI daha fazla iterasyon yapıyor, daha fazla şeyi kendi düzeltiyor.

### Pipeline
1. Research → 2. Script (Nate'in ses tonunda) → 3. ElevenLabs audio → 4. HeyGen avatar → 5. HyperFrames edit → 6. Self-review

### Maliyet
- Base video: ~$8
- Ultra effort: yüksek token tüketimi
- High effort daha makul maliyet

---

## Video 4: LLM Wiki Second Brain (hQvwMj7IJe4)

** yayınlanma:** 2026-07-03 | **Süre:** ~15 dakika

### Özet
Andrej Karpathy'nin LLM Wiki konseptini uygulama. Tüm YouTube videolarını AI OS'ye aktarıp cross-linked wiki pages oluşturma. Claude Code + Obsidian ile 5 dakikada kurulum.

### Herkesin Kaçırdığı Nokta
**Flat vs Structured wiki seçimi çoğu insanın gözden kaçırdığı bir tradeoff.** Flat = hızlı başlangıç, kolay bakım. Structured = daha zengin bağlantılar ama daha fazla bakım. Nate'in önerisi: başlangıçta flat, sonra ihtiyaca göre structured'a geçiş — MVP mentalitesi.

### Kurulum Adımları
1. Vault oluşturma (Obsidian)
2. Schema yazma
3. Routing kuralları tanımlama
4. PDF/URL/YouTube ingestion
5. AI parsing + chunking + cross-link

---

## Genel Değerlendirme

### Nate Herk'in Bu Haftaki Teması
- **Multi-model orchestration** — tek model değil, model kombinasyonları
- **Agentic workflows** — AI'ın ajan olarak çalışması
- **AI OS kavramı** — kişisel AI sistemi kurma
- **Maliyet/hız dengesi** — Sol vs Fable tartışması

### Çıkarılacak Dersler
1. Manager/Worker ayrımı artık standart — Fable strateji, Sol execution
2. Beceriler + Alt-ajanlar + Hafıza = birbirine bağlı sistemler
3. "Naked pipeline" — AI'ın tek başına tam iş üretmesi mümkün ama maliyet önemli
4. LLM Wiki = ikinci beyin için pratik uygulama

### LinkedIn Post Önerileri
1. "AI ajanı = manager + worker. Fable strateji veriyorum, Sol execution'a veriyorum. Maliyet 40% düştü, hız 2x arttı."
2. "5.5 saat harcadım: AI'ı yanlış kullanıyormuşum. AI'a görev vermek, araç vermek, onu tekrarlayan işlerden kurtarmak = doğru kullanım."
3. "LLM Wiki: 5 dakikada kurdum, 200+ videom var. Artık 'hangi videoda X'ten bahsetmiştim' yerine AI'ıma soruyorum."
