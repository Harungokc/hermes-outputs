# 🛠️ Kurulum Rehberi

Hedef: ~1 saatte çalışır hale getirmek. İki yol var — **n8n (low-code)** veya **Python**.
Ortak ilk adım: Claude API key.

---

## 0. Ortak — Claude API Key

1. [console.anthropic.com](https://console.anthropic.com/settings/keys) → **Create Key**
2. Key'i kopyala (`sk-ant-...`).
3. Hesabına biraz kredi yükle ($5 başlangıç için fazlasıyla yeter — bkz. [COSTS.md](COSTS.md)).

---

## Yol A — n8n (low-code)

### A1. n8n'i çalıştır
```bash
# Docker ile (en kolay)
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
# Tarayıcıda: http://localhost:5678
```
Ya da `npx n8n` ile.

### A2. Claude credential'ı ekle
n8n → **Credentials** → **New** → **Header Auth**
- **Name:** `Anthropic API (x-api-key)`
- **Header Name:** `x-api-key`
- **Header Value:** `sk-ant-...` (key'in)

> Workflow'lardaki HTTP Request node'ları bu header auth credential'ını kullanır.
> `anthropic-version` ve `content-type` header'ları workflow içinde zaten tanımlı.

### A3. Google credential'ları ekle
İhtiyacın olan workflow'a göre:
- **Gmail OAuth2** (workflow 1, 3, 5)
- **Google Sheets OAuth2** (workflow 2, 3)
- **Google Drive OAuth2** (workflow 4)
- **Google Calendar OAuth2** (workflow 5)

Her biri için n8n'in OAuth akışını takip et (Credentials → New → ilgili Google node).
[n8n Google rehberi](https://docs.n8n.io/integrations/builtin/credentials/google/).

### A4. Workflow'u import et
**Workflows** → **Import from File** → `workflows/1-email-triage.json` seç.
İçe aktardıktan sonra:
- Her node'da `REPLACE` yazan credential'ları kendi credential'larınla eşle.
- `REPLACE_SHEET_ID`, `REPLACE_recipient@example.com` gibi yer tutucuları doldur.
- Sağ üstten **Test workflow** ile dene, sonra **Active** yap.

---

## Yol B — Python

### B1. Bağımlılıklar
```bash
cd office-ai-copilot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # ANTHROPIC_API_KEY gir
```

### B2. Hemen dene (Google gerekmeden)
```bash
echo "Merhaba, yarınki sunum için slaytları bugün gönderebilir misiniz? Acil." \
  | python src/email_triage.py
```
Triyaj sonucu + taslak cevabı görürsün. Diğerleri:
```bash
python src/meeting_notes.py --file ornek_transkript.txt
python src/file_finder.py "geçen ayki bütçe sunumu"
```

### B3. Google API'yi bağla (gerçek Gmail/Drive/Calendar/Sheets)
1. [Google Cloud Console](https://console.cloud.google.com) → yeni proje
2. **APIs & Services** → şu API'leri etkinleştir: Gmail, Drive, Calendar, Sheets
3. **OAuth consent screen** ayarla (Internal/External + test kullanıcısı = kendi mailin)
4. **Credentials** → **OAuth client ID** → **Desktop app** → `credentials.json` indir
5. Repo köküne koy (`.gitignore`'da, commit edilmez).
6. İlk çalıştırmada tarayıcı açılır, izin verirsin → `token.json` oluşur.

> Scriptlerdeki `# TODO` işaretli yerler (Gmail çekme, Sheets yazma, Calendar insert)
> Google istemcisiyle doldurulacak iskeletlerdir. `google-api-python-client` zaten kurulu.
> [Google Python quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python).

### B4. Zamanla (otomatik çalıştır)
**macOS (launchd)** veya **Linux (cron)** ile:
```cron
# Her gün 09:00 — email triyaj (gerçek Gmail entegrasyonundan sonra)
0 9 * * * cd /path/office-ai-copilot && .venv/bin/python src/email_triage.py
# Her Cuma 16:00 — haftalık rapor
0 16 * * 5 cd /path/office-ai-copilot && .venv/bin/python src/weekly_report.py --file hafta.txt
```

---

## ✅ Doğrulama

- Python: `python src/email_triage.py` bir test mailiyle JSON çıktı veriyor mu?
- n8n: workflow'u "Test" ettiğinde Claude node'u 200 dönüyor mu?
- API key yanlışsa Anthropic 401 döner — key'i ve header adını (`x-api-key`) kontrol et.

Takıldığın yerde repo'da issue aç.
