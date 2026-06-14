# 🤝 Katkı & Geliştirme Rehberi

Bu repo bir **AI agent başlangıç kiti / şablonu**. Kendi ihtiyacına göre uyarlaman,
yeni agent'lar eklemen ve geri katkı yapman beklenir. Bu rehber, geliştirmek isteyenler
için repo'nun nasıl çalıştığını ve nasıl genişletileceğini anlatır.

---

## 🧭 Önce Mimariyi Anla

Repo iki sistemi barındırır:
1. **Office AI Copilot** — 5 ofis işini otomatikleştiren n8n + Python kiti (`workflows/`, `src/`, `prompts/`).
2. **Hermes Agent rehberi** — eski bir bilgisayarı kişisel ajana çeviren sıfırdan kurulum dökümanı (`docs/KURULUM-HERMES.md`).

Tasarım felsefesi kasıtlı olarak **ince**: ağır framework yok, her iş **tek bir Claude
çağrısı** etrafında kurulu. Detay: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
Neden böyle tasarlandı: [`docs/ARASTIRMA.md`](docs/ARASTIRMA.md).

```
prompts/   ← Claude system prompt'ları (TEK KAYNAK — mantık burada)
   ↓
src/       ← Python: prompt'u okur, Claude'u çağırır, çıktıyı yönlendirir
workflows/ ← n8n: aynı mantık, görsel workflow olarak (prompt JSON'a gömülü)
```

---

## 🛠️ Geliştirme Ortamı Kurulumu

```bash
git clone https://github.com/Harungokc/office-ai-copilot.git
cd office-ai-copilot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # ANTHROPIC_API_KEY gir
python src/email_triage.py --help   # çalıştığını doğrula
```

Tam kurulum (Google, n8n): [`docs/KURULUM-OFIS.md`](docs/KURULUM-OFIS.md).

---

## ➕ Yeni Bir Agent Nasıl Eklenir?

Mevcut 5 agent'ın deseni nettir. 6. bir agent (örnek: "fatura çıkarımı") eklemek için:

### 1. Prompt yaz — `prompts/<isim>.md`
- En üste model seçimini yaz (ucuz iş → `claude-haiku-4-5`, kaliteli iş → `claude-sonnet-4-6`).
- Claude'a net bir görev ve **yapılandırılmış çıktı** (JSON şeması veya Markdown) iste.
- "Bilmediğini uydurma, `null` bırak" kuralını ekle.

### 2. Python scripti — `src/<isim>.py`
Mevcut bir scripti şablon al. Ortak yardımcıyı kullan:
```python
from claude_client import ask_json   # veya ask() düz metin için

def process(metin: str) -> dict:
    return ask_json("<isim>", metin, smart=False)  # smart=True → Sonnet
```
`claude_client.py` model seçimini, prompt okumayı ve JSON parse'ı zaten halleder.

### 3. (Opsiyonel) n8n workflow — `workflows/N-<isim>.json`
- Mevcut bir JSON'u şablon al; HTTP Request node'unun `jsonBody` alanına aynı prompt'u göm.
- Import edilebilir kalması için tek dosya tut, credential'ları `REPLACE` ile bırak.

### 4. Doğrula
```bash
python -m py_compile src/<isim>.py                       # Python derleniyor mu?
python3 -c "import json; json.load(open('workflows/N-<isim>.json'))"   # JSON geçerli mi?
```

### 5. Dökümana ekle
`README.md` ve `docs/ARCHITECTURE.md`'deki tabloya yeni agent'ı satır olarak ekle.

---

## ✅ Kod Standartları

- **Python:** standart kütüphane + mevcut bağımlılıklar yeterli; gereksiz paket ekleme.
  Açıklayıcı docstring + Türkçe yorum (repo dili Türkçe).
- **Prompt'lar:** tek kaynak `prompts/`. n8n'e gömülü kopyayı değiştirdiysen `prompts/`'u da güncelle.
- **Güvenlik:** API key / token asla commit edilmez (`.gitignore`'da). Geri alınamaz
  işlemler (mail gönder, takvim daveti) varsayılan **taslak** kalmalı — `AUTO_SEND` opt-in.
- **Maliyet:** doğru modeli seç. Sınıflandırma/çıkarım Haiku, üretim/özet Sonnet.

---

## 🔁 Katkı Süreci (Pull Request)

1. Repo'yu **fork**'la.
2. Yeni bir dal aç: `git checkout -b ozellik/yeni-agent`
3. Değişikliği yap, yukarıdaki doğrulamaları çalıştır.
4. Anlamlı bir commit mesajı yaz (Türkçe ok): `git commit -m "feat: fatura çıkarımı agent'ı"`
5. Dalını push'la ve **Pull Request** aç. PR açıklamasında ne eklediğini ve nasıl test
   edileceğini yaz.

Küçük düzeltmeler (yazım, döküman, prompt iyileştirmesi) için doğrudan PR açabilirsin.
Büyük değişikliklerde önce bir **issue** açıp tartışmak iyi olur.

---

## 💡 Genişletme Fikirleri (katkıya açık)

- Slack/Telegram bot arayüzü (dosya bulucu + triyaj için)
- Vektör arama ile semantik dosya bulucu
- Prompt caching ile girdi maliyetini düşürme
- Kritik işlemlerde Slack üzerinden tek-tık onay adımı
- Çoklu kullanıcı desteği (kullanıcı başına credential + Sheets sekmesi)
- Yeni sektör/iş için agent (CRM güncelleme, sosyal medya, müşteri destek triyajı…)

---

## 📜 Lisans

Katkıların [MIT lisansı](LICENSE) altında yayımlanacağını kabul etmiş olursun.

> Sorular için [issue](https://github.com/Harungokc/office-ai-copilot/issues) aç veya
> [LinkedIn](https://linkedin.com/in/harun-gokce-08843a298)'den ulaş.
