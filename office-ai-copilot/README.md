# 🤖 Office AI Copilot

> Ofis çalışanlarının en çok zaman harcadığı **5 işi** otomatikleştiren, açık kaynak AI agent kiti.
> **n8n + Claude API + Google Workspace.** Kur, çalıştır, haftada 10+ saat geri kazan.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude API](https://img.shields.io/badge/Claude-Haiku%204.5%20%7C%20Sonnet%204.6-orange)](https://www.anthropic.com)
[![n8n](https://img.shields.io/badge/n8n-self--hosted-EA4B71)](https://n8n.io)

---

> 🔬 **Bu kit nasıl tasarlandı?** Önce alandaki mevcut açık kaynak projeler detaylı
> tarandı, iki ana yaklaşım ve aradaki boşluk tespit edildi. Tüm araştırma ve tasarım
> gerekçeleri: [`docs/ARASTIRMA.md`](docs/ARASTIRMA.md)

---

## 🚀 Sıfırdan Kurulum (Adım Adım)

Bu repo bir **AI Agent Kurulum Merkezi**. İçinde, sıfır bilgiyle kendi bilgisayarına
kurabileceğin **iki sistem** var:

| Sistem | Ne işe yarar | Sıfırdan rehber |
|--------|--------------|------------------|
| 🏢 **Office AI Copilot** | 5 ofis işini otomatikleştirir (n8n + Claude + Google) | 👉 [`docs/KURULUM-OFIS.md`](docs/KURULUM-OFIS.md) |
| 🤖 **Hermes Agent** | Eski bilgisayarı 7/24 kişisel ajana çevirir (Telegram + GitHub) | 👉 [`docs/KURULUM-HERMES.md`](docs/KURULUM-HERMES.md) |

Her iki rehber de hiç terminal kullanmamış biri için, adım adım yazıldı (Windows + Linux/VPS).
Geliştirmek / kendi agent'ını eklemek istersen: 👉 [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 🎯 Çözdüğümüz Problem

Bir araştırmaya göre ofis çalışanları zamanlarının büyük kısmını tekrarlayan işlere harcıyor:

| #  | İş                       | Harcanan Zaman      | Bu Kit Ne Yapıyor                         |
|----|--------------------------|---------------------|-------------------------------------------|
| 1  | 📧 Email okuma/cevaplama | Günde 2-3 saat      | AI okur → öncelik verir → taslak cevap yazar |
| 2  | 📝 Toplantı notu yazma   | Haftada 3-5 saat    | Transkript → özet + action items → Sheets |
| 3  | 📊 Rapor hazırlama       | Haftada 2-4 saat    | Haftalık veriyi toplar → rapor yazar → mailler |
| 4  | 🔍 Dosya arama           | Günde 30-60 dakika  | Doğal dille Drive'da arar → linki getirir |
| 5  | 📅 Takvim yönetimi       | Günde 30 dakika     | Mail thread → takvim daveti oluşturur     |

**Toplam:** Haftada 1.5-2 günlük iş. **Bu kit ile:** Sen sadece kontrol ediyorsun.

```
Email geliyor    →  AI okur      →  Öncelik + taslak cevap
Toplantı biter   →  AI özetler   →  Action items → Sheets
Hafta sonu       →  AI rapor     →  Otomatik gönderir
```

---

## 💰 Maliyet & Geri Dönüş

| Kalem                      | Tutar (aylık)  |
|----------------------------|----------------|
| n8n (self-hosted)          | **$0** (kendi sunucun) |
| Claude API (Haiku + Sonnet)| **~$15-50**    |
| Google Workspace           | Zaten var      |
| **Toplam**                 | **~$15-50/ay** |

**Tasarruf:** Haftada 10+ saat → yılda 500+ saat. Detaylı döküm: [`docs/COSTS.md`](docs/COSTS.md)

> Neden Claude? Haiku 4.5 ($1/$5 per 1M token) triyaj/sınıflandırma gibi yüksek hacimli işlerde
> çok ucuz; Sonnet 4.6 ($3/$15) rapor/özet gibi kalite gerektiren işlerde devreye giriyor.

---

## 📦 İki Yol — Senin Tercihin

Bu repo aynı 5 işi **iki ayrı şekilde** sunuyor. İhtiyacına göre seç:

### 🟢 Yol A — n8n Workflow'ları (low-code, önerilen)
`workflows/` klasöründeki JSON'ları n8n'e import et, Claude API key'ini gir, çalıştır.
Kod yazmana gerek yok. Görsel, bakımı kolay, herkese açık.

### 🔵 Yol B — Python Scriptleri (developer)
`src/` klasöründeki standalone Python scriptleri. n8n gerektirmez,
cron/launchd ile zamanla, CI'ya göm. Tam kontrol.

> İkisi de aynı `prompts/` klasöründeki Claude system prompt'larını kullanır — tek kaynaktan beslenir.

---

## 🗂️ Repo Yapısı

```
office-ai-copilot/
├── workflows/                  # 🟢 Yol A: n8n JSON export'ları
│   ├── 1-email-triage.json        Email oku → öncelik + taslak cevap
│   ├── 2-meeting-notes.json       Transkript → özet + action items → Sheets
│   ├── 3-weekly-report.json       Sheets verisi → rapor → mail
│   ├── 4-file-finder.json         Drive doğal dil arama
│   └── 5-calendar-agent.json      Mail thread → takvim daveti
├── src/                        # 🔵 Yol B: Python scriptleri
│   ├── claude_client.py            Ortak Claude API yardımcısı
│   ├── email_triage.py
│   ├── meeting_notes.py
│   ├── weekly_report.py
│   ├── file_finder.py
│   └── calendar_agent.py
├── prompts/                    # 📜 Claude system prompt'ları (tek kaynak)
│   ├── email_triage.md
│   ├── meeting_notes.md
│   ├── weekly_report.md
│   ├── file_finder.md
│   └── calendar_agent.md
├── CONTRIBUTING.md             # 🤝 Geliştirenler için: yeni agent ekleme, PR süreci
├── docs/
│   ├── KURULUM-OFIS.md             🏢 Office kiti — sıfırdan adım adım kurulum
│   ├── KURULUM-HERMES.md           🤖 Hermes Agent — sıfırdan kişisel ajan kurulumu
│   ├── SETUP.md                    Hızlı kurulum özeti (Google API, n8n credential)
│   ├── COSTS.md                    Şeffaf maliyet dökümü
│   ├── ARCHITECTURE.md             Mimari + akış diyagramları
│   └── ARASTIRMA.md                GitHub manzara araştırması + tasarım gerekçeleri
├── .env.example
├── requirements.txt
└── LICENSE
```

---

## 🚀 Hızlı Başlangıç (5 dakika)

```bash
# 1. Repo'yu klonla
git clone https://github.com/Harungokc/office-ai-copilot.git
cd office-ai-copilot

# 2. Ortam değişkenlerini ayarla
cp .env.example .env
# .env içine ANTHROPIC_API_KEY değerini gir

# 3a. Yol B (Python) için:
pip install -r requirements.txt
python src/email_triage.py --help

# 3b. Yol A (n8n) için:
# n8n arayüzünde Workflows → Import from File → workflows/1-email-triage.json
```

Tam kurulum (Google API key'leri, n8n credential'ları, ilk çalıştırma):
👉 [`docs/SETUP.md`](docs/SETUP.md)

---

## 👀 Nasıl Görünüyor (Örnek Çıktı)

**Girdi** — gelen bir email:
```
Konu: Yarınki sunum
Merhaba, yarın saat 10'daki müşteri sunumu için slaytları
bugün akşama kadar gönderebilir misiniz? Biraz acil.
```

**Çıktı** — Email Triyaj agent'ı (Haiku):
```json
{
  "priority": "ACİL",
  "category": "İç Talep / Deadline",
  "summary": "Yarınki müşteri sunumu için slaytlar bugün akşama isteniyor.",
  "needs_reply": true,
  "draft_reply": "Merhaba, slaytları bugün [saat] gibi tamamlayıp göndereceğim.
Eklemek istediğiniz bir konu varsa iletin. İyi çalışmalar."
}
```
→ n8n bu taslağı Gmail'de **taslak** olarak bırakır; sen tek tıkla gönderirsin.

Diğer agent'ların ne döndürdüğü: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

---

## ⚠️ Güvenlik & Sınırlar

- **İnsan onayı:** Email gönderme ve takvim daveti gibi geri alınamaz işlemler **taslak** olarak hazırlanır; göndermeden önce sen onaylarsın. Tam otomatik gönderim opsiyoneldir ve varsayılan olarak kapalıdır.
- **API key'ler:** `.env` dosyası `.gitignore`'da — asla commit etme.
- **Veri:** Mailler ve dökümanlar yalnızca Claude API'ye gider (Anthropic, API verisini model eğitimi için kullanmaz). Kendi n8n sunucunda çalışır, üçüncü bir aracı yok.

---

## 🛠️ Kullanılan Teknolojiler

- **[Claude API](https://www.anthropic.com)** — Haiku 4.5 (triyaj) + Sonnet 4.6 (rapor/özet)
- **[n8n](https://n8n.io)** — açık kaynak workflow otomasyonu (Zapier alternatifi)
- **Google Workspace API** — Gmail, Drive, Calendar, Sheets
- **Python 3.10+** — standalone scriptler için

---

## 📄 Lisans

MIT — dilediğin gibi kullan, değiştir, dağıt. Bkz. [LICENSE](LICENSE).

---

> Bu proje bir **şablon/başlangıç kiti**. Kendi iş akışına göre prompt'ları ve workflow'ları
> uyarlaman beklenir. Sorular ve katkılar için issue açmaktan çekinme.
