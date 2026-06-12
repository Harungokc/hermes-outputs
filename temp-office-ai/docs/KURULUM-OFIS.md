# 🏢 Office AI Copilot — Sıfırdan Kurulum Rehberi

> Bilgisayarında daha önce hiç terminal/kod kullanmamış olsan bile takip edebileceğin,
> adım adım kurulum. Sonunda 5 ofis işini (email, toplantı notu, rapor, dosya arama,
> takvim) otomatikleştiren agent'ların kendi makinende çalışıyor olacak.
>
> İki yol var: **Yol A (n8n, low-code — kod yazmadan)** ve **Yol B (Python)**.
> Yeni başlıyorsan **Yol A** ile başla.

**Hazırlayan:** Harun Gökçe — [LinkedIn](https://linkedin.com/in/harun-gokce-08843a298)

---

## İçindekiler
1. [Sistem Gereksinimleri](#1-sistem-gereksinimleri)
2. [Ortak Adım — Claude API Key](#2-ortak-adım--claude-api-key-zorunlu)
3. [Yol A — n8n Kurulumu (low-code)](#3-yol-a--n8n-kurulumu-low-code)
4. [Yol B — Python Kurulumu](#4-yol-b--python-kurulumu)
5. [Google Workspace Bağlama](#5-google-workspace-bağlama-gerçek-gmaildrive)
6. [Otomatik Çalıştırma (zamanla)](#6-otomatik-çalıştırma-zamanla)
7. [Sık Karşılaşılan Hatalar](#7-sık-karşılaşılan-hatalar)

---

## 1. Sistem Gereksinimleri

Ağır bir donanım gerekmiyor — AI işlemleri Claude API üzerinde (bulutta) gerçekleşir.

|                | Minimum            | Önerilen           |
|----------------|--------------------|--------------------|
| İşletim Sistemi| Windows 10 / macOS 12 / Ubuntu 20.04 | Güncel sürümler |
| RAM            | 4 GB               | 8 GB+              |
| Depolama       | 2 GB boş alan      | 10 GB+            |
| İnternet       | Sabit bağlantı     | —                  |

> 7/24 çalışsın istiyorsan ucuz bir VPS (Hetzner ~€4, DigitalOcean ~$6) da kullanabilirsin —
> bkz. [`KURULUM-HERMES.md`](KURULUM-HERMES.md) Bölüm 3 (sunucu kurulumu aynı mantık).

---

## 2. Ortak Adım — Claude API Key (zorunlu)

Her iki yol da Claude'a ihtiyaç duyar. Önce bunu hallet:

1. [console.anthropic.com](https://console.anthropic.com/settings/keys) → giriş yap / kayıt ol
2. **Settings → API Keys → Create Key** → key'i kopyala (`sk-ant-...`)
3. **Billing → Add credits** → ~$5 yükle (başlangıç için fazlasıyla yeter;
   neden bu kadar ucuz: [`COSTS.md`](COSTS.md))

> ⚠️ Bu key bir şifredir. Kimseyle paylaşma, kod içine yazma, GitHub'a commit etme.
> Sadece `.env` dosyasına veya n8n credential'ına gir.

---

## 3. Yol A — n8n Kurulumu (low-code)

n8n, görsel bir workflow otomasyon aracı (açık kaynaklı Zapier alternatifi). Kod yazmadan,
hazır JSON'ları import edip çalıştırırsın.

### Adım 1 — Docker'ı kur (en kolay yol)
n8n'i çalıştırmanın en temiz yolu Docker. Yoksa:
- **Windows/macOS:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) indir, kur, başlat.
- **Linux:** `curl -fsSL https://get.docker.com | sh`

> Docker istemiyorsan alternatif: `npx n8n` (önce [Node.js](https://nodejs.org) kur).

### Adım 2 — n8n'i başlat
Terminal/PowerShell aç ve şunu çalıştır:
```bash
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
Tarayıcıda aç: **http://localhost:5678** → ilk girişte bir hesap oluştur (yerel, ücretsiz).

### Adım 3 — Bu repo'yu indir
```bash
git clone https://github.com/Harungokc/office-ai-copilot.git
```
> Git yoksa: GitHub'da repo sayfasında **Code → Download ZIP** ile de indirebilirsin.

### Adım 4 — Claude credential'ı ekle
n8n arayüzünde: **Credentials → Add credential → "Header Auth"**
- **Name:** `Anthropic API (x-api-key)`
- **Header Name:** `x-api-key`
- **Header Value:** `sk-ant-...` (senin key'in)
- Kaydet.

### Adım 5 — İlk workflow'u import et
**Workflows → Import from File** → repo'daki `workflows/1-email-triage.json` dosyasını seç.

İçe aktardıktan sonra workflow'da `REPLACE` yazan yerleri düzelt:
- Her node'daki credential'ı kendi credential'ınla eşle (Claude için Header Auth, Gmail için Gmail OAuth).
- `REPLACE_SHEET_ID`, `REPLACE_recipient@...` gibi yer tutucuları doldur.

### Adım 6 — Test et ve aktif et
Sağ üstten **Test workflow** → Claude node'u yeşil (200) dönerse çalışıyor demektir.
Sonra workflow'u **Active** yap — artık otomatik tetiklenir.

### Adım 7 — Diğer workflow'ları ekle
Aynı şekilde `2-meeting-notes.json` … `5-calendar-agent.json` dosyalarını import et.
Sadece ihtiyacın olanları kurman yeterli — hepsi bağımsız çalışır.

> Google credential'larının (Gmail/Sheets/Drive/Calendar) nasıl ekleneceği: [Bölüm 5](#5-google-workspace-bağlama-gerçek-gmaildrive).

---

## 4. Yol B — Python Kurulumu

Kod tarafını tercih edersen, n8n gerekmeden scriptleri doğrudan çalıştırabilirsin.

### Adım 1 — Python 3.10+ kur
- **Windows:** [python.org/downloads](https://www.python.org/downloads/) → kurarken
  **"Add Python to PATH"** kutusunu işaretle.
- **macOS:** `brew install python` (veya python.org).
- **Linux:** genelde kuruludur; `python3 --version` ile kontrol et.

### Adım 2 — Repo'yu indir ve sanal ortam kur
```bash
git clone https://github.com/Harungokc/office-ai-copilot.git
cd office-ai-copilot
python3 -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

### Adım 3 — Ortam değişkenlerini ayarla
```bash
cp .env.example .env      # Windows: copy .env.example .env
```
`.env` dosyasını bir metin editörüyle aç, `ANTHROPIC_API_KEY=sk-ant-...` satırını doldur.

### Adım 4 — Hemen dene (Google gerekmeden)
```bash
echo "Yarın 10'daki sunum için slaytları bugün gönderir misiniz? Acil." | python src/email_triage.py
```
Triyaj sonucu + taslak cevabı görürsün. Diğerleri:
```bash
python src/meeting_notes.py --file ornek_transkript.txt
python src/file_finder.py "geçen ayki bütçe sunumu"
```

> Bu adımda scriptler stdin/dosya okur — gerçek Gmail/Drive bağlamak için Bölüm 5.

---

## 5. Google Workspace Bağlama (gerçek Gmail/Drive)

Agent'ların gerçek mail/dosya/takvimle çalışması için Google'a bir kez yetki vermen gerekir.

### Yol A (n8n) için
n8n'de her Google node'u için **Credentials → Add → ilgili Google OAuth2** akışını takip et:
- Gmail OAuth2 (workflow 1, 3, 5)
- Google Sheets OAuth2 (workflow 2, 3)
- Google Drive OAuth2 (workflow 4)
- Google Calendar OAuth2 (workflow 5)

n8n sana adım adım gösterir; "Sign in with Google" deyip izin vermen yeterli.
Detay: [n8n Google rehberi](https://docs.n8n.io/integrations/builtin/credentials/google/).

### Yol B (Python) için
1. [Google Cloud Console](https://console.cloud.google.com) → **yeni proje** oluştur
2. **APIs & Services → Library** → şunları etkinleştir: Gmail, Drive, Calendar, Sheets
3. **OAuth consent screen** ayarla → test kullanıcısı olarak kendi mailini ekle
4. **Credentials → Create → OAuth client ID → Desktop app** → `credentials.json` indir
5. Bu dosyayı repo köküne koy (`.gitignore`'da, commit edilmez)
6. Scripti ilk çalıştırdığında tarayıcı açılır, izin verirsin → `token.json` otomatik oluşur

> Scriptlerdeki `# TODO` işaretli yerler (Gmail çekme, Sheets yazma, Calendar insert)
> bu Google istemcisiyle doldurulacak iskeletlerdir. `google-api-python-client` zaten kurulu.
> Referans: [Google Python quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python).

---

## 6. Otomatik Çalıştırma (zamanla)

### Yol A (n8n)
Workflow'ları **Active** yapman yeterli — Gmail Trigger yeni mail geldiğinde, Schedule
Trigger ise belirlenen saatte (ör. Cuma 16:00 rapor) otomatik tetiklenir.

### Yol B (Python) — cron / Görev Zamanlayıcı
**macOS/Linux (cron):**
```cron
0 9 * * *   cd /yol/office-ai-copilot && .venv/bin/python src/email_triage.py
0 16 * * 5  cd /yol/office-ai-copilot && .venv/bin/python src/weekly_report.py --file hafta.txt
```
**Windows:** Görev Zamanlayıcı (Task Scheduler) ile `.venv\Scripts\python.exe src\...` çalıştır.

---

## 7. Sık Karşılaşılan Hatalar

### ❗ HTTP 401 — API Key Hatası
- `.env`'de `ANTHROPIC_API_KEY` doğru mu? Başında/sonunda boşluk olmamalı.
- n8n'de Header adı tam olarak `x-api-key` mi?
- Anthropic konsolunda krediniz var mı?

### ❗ "ANTHROPIC_API_KEY not found" (Python)
- `.env` dosyasını oluşturdun mu? (`cp .env.example .env`)
- Scripti repo kökünden çalıştırıyor musun?
- Sanal ortam aktif mi? (`source .venv/bin/activate`)

### ❗ n8n: "Could not connect / ECONNREFUSED"
- Docker çalışıyor mu? `docker ps` ile kontrol et.
- http://localhost:5678 yerine başka port verdin mi?

### ❗ Claude geçerli JSON dönmedi
- Nadiren olur. `max_tokens` çok düşükse çıktı yarıda kesilir — workflow/script'te artır.
- Aynı girdiyle tekrar dene; prompt'lar JSON şemasını net belirtir.

### ❗ Google "Access blocked / app not verified"
- OAuth consent screen'de uygulamayı **Testing** modunda bıraktıysan, kendi mailini
  **Test users** listesine eklemen gerekir.

---

> Takıldığın yerde [repo'da issue aç](https://github.com/Harungokc/office-ai-copilot/issues)
> veya [LinkedIn](https://linkedin.com/in/harun-gokce-08843a298)'den ulaş.
