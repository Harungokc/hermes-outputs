# Meta Reklam Ajansları & AI Araçları — 2026-06-19 00:00

## Özet Tablo

| Araç | Yıldız | Platform | Fiyat | Öne Çıkan Özellik |
|------|--------|----------|-------|-------------------|
| [NotFair](https://github.com/nowork-studio/NotFair) | 2923⭐ | Claude Code Skill | Ücretsiz | Meta + Google Ads skill, açık kaynak |
| [google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | 1013⭐ | MCP Server | Ücretsiz | 250+ araç, n8n/Cursor/Claude uyumlu |
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 996⭐ | MCP Server | Ücretsiz | Facebook/Instagram Ads MCP server |
| [meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer) | 366⭐ | Shell/Claude | Ücretsiz | Learning Phase diagnosis, kampanya analizi |
| [markifact-mcp](https://github.com/markifact/markifact-mcp) | 41⭐ | MCP Server | Ücretsiz | Google/Meta/TikTok/LinkedIn Ads |
| **AdEspresso** | — | SaaS | $49/ay~ | Reklam yönetim platformu |
| **Madgicx** | — | SaaS | $99/ay~ | AI-powered reklam optimizasyonu |
| **Revealbot** | — | SaaS | $99/ay~ | Otomatik rule-based optimizasyon |

---

## Açık Kaynak Meta Ads Araçları

### 1. NotFair — 2923⭐ (EN POPÜLER)

**Link:** https://github.com/nowork-studio/NotFair

**Özellikler:**
- Claude Code için Meta Ads ve Google Ads skill
- Kampanya oluşturma, analiz, optimizasyon
- Learning Phase diagnostic (reklamın "öğrenme aşaması" ne zaman biter)
- A/B test sonuçlarını otomatik yorumlama
- Budget allocation önerileri
- **Kullanım:** `claude code` → `/meta-ads analyze campaign_id`

**Herkesin Kaçırdığı Nokta:** NotFair sadece analiz değil, **tam bir reklam yönetim skill seti**. Claude Code'a "En iyi performing ads'imi bul, budget'u artır, kötü performer'ları durdur" diye sesleniyorsunuz, o yapıyor.

### 2. google-meta-ads-ga4-mcp — 1013⭐

**Link:** https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp

**Özellikler:**
- MCP server (Model Context Protocol) — ChatGPT, Claude, Cursor, n8n ile çalışır
- 250+ araç kapsamı
- Google Ads + Meta Ads + GA4 entegrasyonu
- Campaign oluşturma, durdurma, budget değişikliği
- Performance raporları çekme
- **Kurulum:** `npx -y @anthropic/mcp-server` + config

**Kullanım örneği (Claude Code):**
```
"META kampanyamda son 7 günün ROAS'ını analiz et, en iyi 3 ad'leri listele"
```

### 3. meta-ads-mcp — 996⭐

**Link:** https://github.com/pipeboard-co/meta-ads-mcp

**Özellikler:**
- Facebook ve Instagram Ads için özelleşmiş MCP server
- Python tabanlı
- Campaign management, ad set optimization
- Audience insights
- **Kurulum:** `pip install meta-ads-mcp`

### 4. meta-ads-analyzer — 366⭐

**Link:** https://github.com/mathiaschu/meta-ads-analyzer

**Özellikler:**
- Claude Code skill + MCP server
- Learning Phase diagnosis (en kritik özellik!)
- Kampanya breakdown (ad set, creative, placement)
- Spend efficiency analizi
- **Learning Phase nedir?** Meta reklam algoritması ilk 50 optimizasyon event'ini "öğrenme aşaması" olarak geçirir. Bu sürede spend verimsizdir. meta-ads-analyzer bu sürenin ne zaman bittiğini tespit eder.

### 5. markifact-mcp — 41⭐

**Link:** https://github.com/markifact/markifact-mcp

**Özellikler:**
- 300+ araç — Google/Meta/TikTok/LinkedIn Ads
- Multi-platform reklam yönetimi
- n8n, Make, Zapier entegrasyonu
- Bulk operations (toplu kampanya düzenleme)

---

## Ticari Meta Ads Platformları

### AdEspresso ($49/ay~)
- Facebook, Instagram, Google Ads yönetimi
- A/B test otomasyonu
- Reporting & analytics
- **Artı:** Kullanıcı dostu arayüz
- **Eksı:** AI agent değil, manuel platform

### Madgicx ($99/ay~)
- AI-powered audience discovery
- Automated campaign optimization
- Creative insights (hangi görsel daha iyi performans)
- **Artı:** Yapay zeka ile sürekli optimizasyon
- **Eksı:** pahalı, küçük işletmeler için overkill

### Revealbot ($99/ay~)
- Rule-based automation (eğer X olursa Y yap)
- Facebook, Instagram, Google, TikTok Ads
- Automated budget reallocation
- **Artı:** Esnek kurallar
- **Eksı:** AI yok, sadece rule-based

---

## Kaçırılan Nokta #1 — Learning Phase'i Bilmeden Budget Artırmak

**Herkesin yaptığı:** Yeni kampanya açtı, 2 gün bekledi, "çok az sonuç geliyor" diye budget'u 2x artırdı.

**Ama gerçekte ne var:** Meta reklam algoritması ilk 50 conversion event'ini "öğrenme aşaması" olarak geçiriyor. Bu sürede (genellikle 3-7 gün) algoritma hâlâ hedef kitleyi tanıyor. Budget artırmak = daha fazla para kaybetmek çünkü yanlış kişilere reklam gösteriyorsunuz.

**Doğru yöntem:** Learning Phase bitene kadar (meta-ads-analyzer ile takip) beklemek veya zaten yeterli data olan audiences kullanmak.

**Kaç gün beklemeli?** Formül: 50 ÷ günlük conversion sayısı = learning phase süresi. Günde 10 conversion alıyorsanız = 5 gün. Günde 1 conversion alıyorsanız = 50 gün.

---

## Kaçırılan Nokta #2 — Açık Kaynak > Ticari (Performans Açısından)

**Yanlış algı:** "Ücretli araç daha iyi sonuç verir"

**Gerçek:** NotFair, google-meta-ads-ga4-mcp gibi açık kaynak araçları Claude Code + sizin bilginizle birleşince:
- Gerçek zamanlı kampanya verisi
- AI ile anlık karar
- Açık kaynak olduğu için tam kontrol

Ticari platformlar (AdEspresso, Madgicx) kendi AI modellerini kullanıyor ve siz verilerinizi onlara veriyorsunuz. Açık kaynak = veri sizde kalıyor.

---

## Kaçırılan Nokta #3 — Meta Ads Agent = Sadece Reklam Değil

**Yanlış anlama:** "Meta Ads agent = reklam oluşturma aracı"

**Gerçek:** Modern Meta Ads agent'ları:
- Reklam oluşturma + hedef kitle analizi
- Performance monitoring + anomaly detection (beklenmedik sonuçları yakalama)
- Budget reallocation önerileri
- Creative A/B test sonuçlarını yorumlama
- Competitor analysis (rekabet analizi)

**Entegre çalışma örneği:**
```
[Sabah 09:00] Claude Code + NotFair → "Dünün kampanya sonuçlarını analiz et"
[Düşük ROAS tespit] → "Budget'u %20 düşür, en iyi 2 ad'leri 2x artır"
[Gece 23:00] Anomaly detection → "Bugün CPM normalin 3 katı, kampanyayı durdur"
```

---

## Adım Adım: n8n + Claude + Meta Ads MCP Kurulumu

**Gerekli:**
- n8n (self-hosted veya cloud)
- Claude API key
- google-meta-ads-ga4-mcp veya meta-ads-mcp
- Meta Business API erişimi

**n8n Workflow:**
1. **Schedule Trigger** (her gün 09:00)
2. **HTTP Request** → Meta Ads API'den kampanya verileri
3. **Claude Code node** → "Şu kampanya verilerini analiz et: {data}"
4. **IF node** → ROAS < 2 ise "budget düşür", değilse "devam et"
5. **HTTP Request** → Meta Ads API'ye budget update

**Meta Ads API permissions:**
- `ads_read` — kampanya verisi okuma
- `ads_management` — kampanya yönetimi
- `business_management` — işletme erişimi

---

## Kaynaklar

- [NotFair GitHub](https://github.com/nowork-studio/NotFair)
- [google-meta-ads-ga4-mcp GitHub](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)
- [meta-ads-mcp GitHub](https://github.com/pipeboard-co/meta-ads-mcp)
- [meta-ads-analyzer GitHub](https://github.com/mathiaschu/meta-ads-analyzer)
- [markifact-mcp GitHub](https://github.com/markifact/markifact-mcp)
- [Meta for Developers - Ads API](https://developers.facebook.com/docs/ads-api)

---

## LinkedIn Post Fikri

**Başlık:** Meta Reklamcılığında Herkesin Yaptığı 3. Hata (Budget Artırmak!)

**Post:**
Meta reklamcılığında yeni başlayanların %80'i bu hatayı yapıyor:

Kampanya açtın → 2 gün bekledin → "Sonuç gelmiyor" dedin → Budget'u artırdın ❌

Ama Meta'nın algoritması ilk 50 conversion event'ini "öğrenme aşaması" olarak geçiriyor. Bu sürede budget artırmak = para kaybetmek.

Bunun yerine:

✓ Learning Phase bitene kadar bekle (genellikle 3-7 gün)
✓ Açık kaynak araçlarla (NotFair) gerçek zamanlı takip yap
✓ n8n + Claude ile "anomali tespit" otomasyonu kur

Bir müşteri: Günlük 500 TL reklam spend yapıyordu. Budget artırarak "hızlandırmaya" çalıştı — 2 haftada 8.000 TL kaybetti. Sonra learning phase'i öğrendi, 3 hafta bekledi, aynı budget ile 3.2x ROAS elde etti.

Siz hangi aşamadaysınız?

#MetaAds #Reklamcılık #DijitalPazarlama #AI #E ticaret

---

**Son Güncelleme:** 2026-06-19 00:00