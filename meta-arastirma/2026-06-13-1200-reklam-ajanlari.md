# Meta Platform — Reklam Ajansları Araştırması
**Tarih:** 2026-06-13 12:00
**Slot:** 1200

---

## 1. Özet Tablo

| Araç | Platform | Fiyat | Açıklama | Link |
|------|----------|-------|----------|------|
| AdEspresso | Meta Ads | $99-499/ay | Kapsamlı reklam yönetim platformu | adespresso.com |
| Revealbot | Facebook/Instagram Ads | $99-299/ay | Otomatik kurallar, A/B testing | revealbot.com |
| Madgicx | Meta Ads | $199-999/ay | AI destekli reklam optimizasyonu | madgicx.com |
| Social Flow | Meta Operations | Açık kaynak (ücretsiz) | n8n + Meta MCP Server entegrasyonu | GitHub |
| Meta MCP Server | Meta Business | Açık kaynak (ücretsiz) | 200+ araç, Facebook/Instagram/Ads | GitHub |
| Meta-Ads-Automation-n8n | n8n + Meta | Açık kaynak (ücretsiz) | AI-assisted campaign creation | GitHub |

---

## 2. Ticari Reklam Otomasyon Platformları

### AdEspresso
**Fiyat:** $99-499/ay (kullanıcı sayısına göre)
**Link:** https://adespresso.com

**Özellikler:**
- Facebook, Instagram, Google Ads tek panel
- A/B test otomasyonu
- Otomatik budget optimizasyonu
- Detaylı analitik dashboard
- Kampanya kopyalama ve şablonlar

**Artıları:** Kapsamlı, kurumsal düzeyde
**Eksileri:** Yüksek fiyat, küçük işletmeler için pahalı

---

### Revealbot
**Fiyat:** $99-299/ay
**Link:** https://revealbot.com

**Özellikler:**
- Otomatik kurallar (IFTTT benzeri)
- Kampanya durdurma/başlatma otomasyonu
- A/B test sonuçlarını otomatik analiz
- Slack/Discord entegrasyonu
- Raporlama otomasyonu

**Artıları:** Esnek kurallar, iyi fiyat/özellik oranı
**Eksileri:** AI özellikleri sınırlı

---

### Madgicx
**Fiyat:** $199-999/ay
**Link:** https://madgicx.com

**Özellikler:**
- AI destekli audience segmentasyonu
- Otomatik creative optimizasyonu
- Predictive analytics
- Full-funnel automation
- Landing page heatmap entegrasyonu

**Artıları:** AI özellikleri güçlü, otomatik karar verme
**Eksileri:** En pahalı seçeneklerden biri

---

## 3. Açık Kaynak Alternatifler

### Social Flow (144 ⭐)
**Link:** https://github.com/vishalgojha/social-flow

Meta işlemleri için rehber kontrol paneli. Ajanslar, büyüme ekipleri ve Meta operatörleri için tasarlanmış.

**Özellikler:**
- Facebook, Instagram, WhatsApp, Ads Manager workflow'ları
- Tek yerden kurulum, günlük çalıştırma, onaylar, raporlama
- Komutlar, gateway API'leri ve SDK üzerinden çalışır

**Fiyat:** Ücretsiz (açık kaynak)

---

### Meta MCP Server (15 ⭐)
**Link:** https://github.com/oliverames/meta-mcp-server

Meta'nın iş platformu için en kapsamlı MCP server. 200'den fazla araç içerir.

**Kapsam:**
- Facebook Pages
- Instagram
- Threads
- Ads Manager
- Commerce
- Conversions API
- Audiences
- Insights
- Ad Library

**Kullanım:** Claude Code, n8n veya herhangi bir MCP istemcisi ile

**Fiyat:** Ücretsiz (açık kaynak)

---

### Meta-Ads-Automation-n8n (9 ⭐)
**Link:** https://github.com/nikD305/Meta-Ads-Automation-n8n

n8n ile Meta reklam otomasyonu. Google Sheets ve Telegram ile entegre çalışır.

**Özellikler:**
- Ads Manager'a girmeden kampanya başlatma ve izleme
- AI-assisted campaign creation
- Canlı raporlama
- Telegram bildirimleri

**Fiyat:** Ücretsiz (n8n açık kaynak, kendi sunucunuzda çalışır)

---

## 4. Herkesin Kaçırdığı Nokta #1

**Madgicx'in "AI" iddiası aslında sadece segmentasyon.**

Herkes Madgicx'i "yapay zeka reklam aracı" olarak pazarlıyor ama gerçek şu: Temel yaptığı şey audience segmentasyonu ve lookalike audience oluşturma. Bu İŞE YARIYOR ama "AI agent" gibi özerk karar veren bir sistem değil. Hâlâ bir insan "accept" veya "reject" demesi gerekiyor.

**Gerçek AI agent reklam yönetimi için:** Meta MCP Server + n8n + Claude Code kombinasyonu daha özerk çalışabilir — örneğin kampanya performansına göre otomatik bid ayarlama, durma/baslama kararları.

---

## 5. Herkesin Kaçırdığı Nokta #2

**Açık kaynak alternatifler ticari platformlardan daha esnek.**

AdEspresso, Revealbot, Madgicx hep "kullanıcı başına" fiyatlandırılır. 10 kişilik ajans = $1000-5000/ay. Ama Social Flow + Meta MCP Server + n8n kombinasyonu:
- Sunucu maliyeti: ~$20-50/ay
- n8n: Ücretsiz (kendi sunucu)
- Meta MCP Server: Ücretsiz

**Toplam:** ~$50-100/ay = Tüm ticari platformlardan 10-50x ucuz.

---

## 6. Adım Adım Yapım Rehberi

### n8n + Meta MCP Server ile Reklam Otomasyonu

**Gerekenler:**
1. Meta Business Manager hesabı
2. n8n kurulumu (self-hosted veya cloud)
3. Meta MCP Server (GitHub'dan)
4. Claude Code veya benzeri AI aracı

**Kurulum:**

1. **Meta MCP Server kur:**
```bash
npx -y @meta-mcp/server
```

2. **n8n'de workflow oluştur:**
```
[AI Agent Node]
  ↓
[Meta Ads Manager API]
  - Kampanya oluştur
  - Audience seç
  - Budget ayarla
  ↓
[Slack/Telegram bildirim]
```

3. **Otomatik karar kuralları:**
   - ROAS < 2x → kampanya durdur
   - CTR > 5% → budget %20 artır
   - Frequency > 4 → audience daralt

---

## 7. Kaynaklar

1. https://adespresso.com
2. https://revealbot.com
3. https://madgicx.com
4. https://github.com/vishalgojha/social-flow (144 ⭐)
5. https://github.com/oliverames/meta-mcp-server (15 ⭐)
6. https://github.com/nikD305/Meta-Ads-Automation-n8n (9 ⭐)