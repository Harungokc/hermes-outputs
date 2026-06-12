# Beyaz Yakalı Ofis Çalışanları İçin AI Otomasyon Rehberi 🚀

> **Ofisteki en çok zaman alan 5 işi AI'ye bırak, haftada 10+ saat kazan**

**Yazar:** Harun Gökce  
**GitHub:** [Harungokc/hermes-outputs](https://github.com/Harungokc/hermes-outputs)  
**Tarih:** 15 Haziran 2026  
**Son Güncelleme:** 15 Haziran 2026  

---

## 📋 İçindekiler

1. [Neden Bu Rehber?](#neden-bu-rehber)
2. [Popüler GitHub Repoları](#popüler-github-repoları)
3. [Email Otomasyonu](#1-email-otomasyonu)
4. [Takvim & Toplantı Otomasyonu](#2-takvim--toplantı-otomasyonu)
5. [Doküman İşleme](#3-doküman-i̇şleme)
6. [Veri Girişi Otomasyonu](#4-veri-girişi-otomasyonu)
7. [Raporlama Otomasyonu](#5-raporlama-otomasyonu)
8. [Hızlı Başlangıç](#hızlı-başlangıç)
9. [Maliyet & Araçlar](#maliyet--araçlar)

---

## Neden Bu Rehber?

Ofis çalışanları günde ortalama **2-3 saat** ofis işlerine harcıyor:

- Email okuma/yazma: 1-2 saat
- Toplantı planlama ve notları: 30-60 dk
- Veri girişi ve raporlama: 30-60 dk
- Dosya organizasyonu: 15-30 dk

**Bu rehber, en popüler GitHub otomasyon repolarından derlenmiş, adım adım kurulum talimatlarıyla birlikte sunuluyor.**

---

## Popüler GitHub Repoları

Bu rehberdeki otomasyonların temelini oluşturan açık kaynak projeler:

| Repo | Yıldız | Ne İşe Yarar? |
|------|--------|---------------|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | ⭐ 192k | Workflow otomasyon platformu |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | ⭐ 64k | Claude AI yetenekleri ve otomasyonları |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | ⭐ 53k | Görsel AI ajanı oluşturma |
| [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) | ⭐ 38k | İç uygulama ve dashboard oluşturma |
| [emretasss/AI-Workflow-Hub-2000-](https://github.com/emretasss/AI-Workflow-Hub-2000-) | ⭐ 262 | 2000+ N8N şablonu |

---

## 1. Email Otomasyonu

### Otomasyon #1: Email Önceliklendirme + Otomatik Yanıt

**Kimler İçin:** CEO, Yönetici, Satış temsilcisi, Müşteri hizmetleri  
**Zaman Tasarrufu:** Günde 1-2 saat  
**Zorluk:** ⭐ Kolay  

#### Kurulum

**Adım 1: N8N Kurulumu**
```bash
# Docker ile kurulum
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

**Adım 2: Gmail Entegrasyonu**
1. N8N'ye giriş yap (http://localhost:5678)
2. "Credentials" → "New" → "Gmail OAuth2"
3. Google Cloud Console'da OAuth2 key oluştur
4. Yetkilendirme yap

**Adım 3: Workflow Oluşturma**
```
[Gmail Trigger] → [AI - Intent Analizi] → [Koşul:
  - Toplantı isteği → Takvim kontrolü → Yanıt
  - Fiyat sorusu → Ürün bilgisi → Satış ekibi bildirimi
  - Şikayet → Öncelikli etiket → İnsan devreye girsin
  - Basit soru → AI otomatik yanıt]
```

#### Kaynak Repolar
- **N8N Workflow:** [emretasss/AI-Workflow-Hub-2000-](https://github.com/emretasss/AI-Workflow-Hub-2000-) - 2000+ şablon
- **Email AI:** [kaymen99/langgraph-email-automation](https://github.com/kaymen99/langgraph-email-automation) - LangGraph tabanlı email otomasyonu

#### Örnek AI Yanıtı
```
Gelen Email: "Merhaba, ürününüzün fiyatını öğrenmek istiyorum"

AI Yanıtı:
"Merhaba, ilgilendiğiniz için teşekkür ederiz.
Ürün fiyatlarımız modele göre 1.500 - 5.000 TL arasında.
Detaylı bilgi için satış ekibimiz 15 dakika içinde 
sizinle iletişime geçecektir."
```

---

### Otomasyon #2: Email Takip Hatırlatıcı

**Kimler İçin:** Satış temsilcisi, Account manager  
**Zaman Tasarrufu:** Haftada 2-3 saat  
**Zorluk:** ⭐ Kolay  

#### Kurulum

**Adım 1: Zapier/Make.com'da yeni workflow oluştur**

**Adım 2: Trigger ayarla**
```
Trigger: Email gönderildi (Gmail - specific label)
```

**Adım 3: Delay ve kontrol ekle**
```
Delay: 48 saat bekle
↓
[Gmail - Email exists?] 
  → Evet: İkinci hatırlatma gönder (96 saat)
  → Hayır: Workflow bitir
↓
[Slack/Teams bildirimi]
```

**Kullanılabilecek Araçlar:**
- [Zapier Follow-up Emails](https://zapier.com/apps/email/integrations)
- [Mailtrack](https://mailtrack.io/) - Email takip
- [Yet Another Mail Merge](https://yamm.com/) - Toplu email takip

---

## 2. Takvim & Toplantı Otomasyonu

### Otomasyon #3: Otomatik Toplantı Planlama

**Kimler İçin:** Yönetici asistanı, CEO, Proje yöneticisi  
**Zaman Tasarrufu:** Haftada 2-4 saat  
**Zorluk:** ⭐ Kolay  

#### Kurulum

**Adım 1: Calendly Kurulumu**
```bash
# Web üzerinden kayıt ol: https://calendly.com
# Gmail hesabı ile giriş yap
```

**Adım 2: Entegrasyonlar**
1. Calendly → Google Calendar bağlantısı
2. Calendly → Zoom/Google Meet bağlantısı
3. Bildirim ayarları: "Yeni toplantı oluştuğunda email gönder"

**Adım 3: Davetiye emaili özelleştir**
```
Toplantı talebiniz alındı.
Uygun saatlerim:
- Salı 14:00-15:00
- Çarşamba 10:00-11:00
- Perşembe 16:00-17:00

Lütfen tercih ettiğiniz saati yanıtlayın.
Onayınızdan sonra toplantı linki gönderilecektir.
```

#### Popüler Araçlar
| Araç | Fiyat | Özellik |
|------|-------|---------|
| [Calendly](https://calendly.com/) | Ücretsiz / $12/ay | En popüler |
| [x.ai](https://x.ai/) | $39/ay | AI tabanlı |
| [Clockwise](https://www.getclockwise.com/) | Ücretsiz / $10/ay | Takvim optimizasyonu |

---

### Otomasyon #4: Toplantı Özeti Otomatik Üretimi

**Kimler İçin:** Herkes (toplantı yapan herkes)  
**Zaman Tasarrufu:** Haftada 3+ saat  
**Zorluk:** ⭐⭐ Orta  

#### Kurulum

**Adım 1: Fireflies.ai / Otter.ai kayıt**
```bash
# Fireflies.ai'ye kayıt ol
# Google Calendar veya Zoom bağlantısı yap
```

**Adım 2: Otomatik transkript aktif et**
1. "Meetings" → "Auto Record" seç
2. "AI Summary" → "Action Items" seç
3. "Notifications" → Slack veya email seç

**Adım 3: Action items'ları CRM'e aktar (opsiyonel)**
```
N8N veya Zapier ile:
[Fireflies API] → [AI - Action Items çıkar] → [Notion/HubSpot/Todoist]
```

#### Sonuçlar
| Metrik | Önce | Sonra |
|--------|------|-------|
| Toplantı notu yazma | 15 dk/kişi | 0 dk |
| Action item takip | %40 | %90+ |
| "Ne konuştuk?" sorusu | Sık | Hiç |

---

## 3. Doküman İşleme

### Otomasyon #5: Fatura/Fiş Okuma ve Kaydetme

**Kimler İçin:** Muhasebe, Ofis yöneticisi, KOBİ sahibi  
**Zaman Tasarrufu:** %95 (15 dk → 30 sn)  
**Zorluk:** ⭐ Kolay  

#### Kurulum

**Adım 1: Rossum veya Google Cloud Vision API**
```bash
# Rossum (Kolay - No-code)
# https://rossum.ai/ adresinde kayıt ol
# Fatura email adresi al
```

**Adım 2: Email ile fatura gönderme**
```
Fatura fotoğrafı çek
↓
Rossum'un verdiği email adresine gönder
↓
AI okur, veritabanına kaydeder
↓
Muhasebe onay emaili alır
```

**Adım 3: Muhasebe yazılımına aktarım (N8N ile)**
```
[Rossum Webhook] → [N8N] → [Logo/Muhasebe/Excel]
```

#### Araçlar
| Araç | Fiyat | Özellik |
|------|-------|---------|
| [Rossum](https://rossum.ai/) | €3/fatura | En doğru |
| [ABBYY](https://www.abbyy.com/) | Kurumsal | Enterprise |
| [Google Cloud Vision](https://cloud.google.com/vision) | Pay-as-you-go | Esnek |

---

### Otomasyon #6: Sözleşme Analizi (Hızlı Okuma)

**Kimler İçin:** Hukuk departmanı, İK, Satın alma  
**Zaman Tasarrufu:** %70 (60 dk → 18 dk)  
**Zorluk:** ⭐⭐ Orta  

#### Kurulum

**Adım 1: Claude API veya OpenAI API**
```bash
# Claude API key al
# https://console.anthropic.com/

# Environment variable ayarla
export ANTHROPIC_API_KEY="sk-ant-xxxxx"
```

**Adım 2: Python script oluştur**
```python
# contract_analyzer.py
import anthropic
import sys

client = anthropic.Anthropic()

def analyze_contract(pdf_path):
    with open(pdf_path, 'rb') as f:
        content = f.read()
    
    message = client.messages.create(
        model="claude-opus-4-20241114",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"""Bu sözleşmeyi analiz et:
            1. Ana maddeler neler?
            2. Riskli maddeler (kırmızı işaretle)
            3. Eksik maddeler (sarı işaretle)
            4. Standart maddeler (yeşil işaretle)
            
            Sözleşme içeriği:
            {content.decode('utf-8', errors='ignore')[:10000]}"""
        }]
    )
    return message.content

if __name__ == "__main__":
    result = analyze_contract(sys.argv[1])
    print(result)
```

**Adım 3: Çalıştır**
```bash
python contract_analyzer.py "sozlesme.pdf"
```

---

## 4. Veri Girişi Otomasyonu

### Otomasyon #7: Web Form Verilerini Otomatik CRM'e Kaydetme

**Kimler İçin:** Pazarlama, Satış, CRM ekibi  
**Zaman Tasarrufu:** %100 (5 dk → 0)  
**Zorluk:** ⭐ Kolay  

#### Kurulum (N8N)

**Adım 1: Webhook oluştur**
```
N8N → Workflow → New → Trigger → Webhook
Endpoint: https://siten.com/webhook/form
```

**Adım 2: Form backend (basit PHP veya Node.js)**
```php
<?php
// form-handler.php
$data = json_decode(file_get_contents('php://input'), true);

// N8N'ye gönder
$ch = curl_init('https://your-n8n.com/webhook/form');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_exec($ch);
curl_close($ch);

// CRM'e kaydet (HubSpot API)
$hubspot = [
    'properties' => [
        'email' => $data['email'],
        'firstname' => $data['name'],
        'phone' => $data['phone'],
        'company' => $data['company']
    ]
];
// HubSpot API call...
?>
```

**Adım 3: N8N Workflow**
```
[Webhook] → [AI - Veri temizleme] → [HubSpot CRM - Create/Update Contact]
                                    → [Email - Otomatik yanıt]
                                    → [Slack - Yeni lead bildirimi]
```

---

### Otomasyon #8: Excel/Google Sheets Otomatik Güncelleme

**Kimler İçin:** Analist, Satış, Pazarlama, Lojistik  
**Zaman Tasarrufu:** Haftada 3-5 saat  
**Zorluk:** ⭐ Kolay (No-code) veya ⭐⭐ Orta (API)  

#### Kurulum (Zapier)

**Adım 1: Zap oluştur**
```
Trigger: Schedule (Her gün 09:00)
↓
Action: Google Sheets - Read Rows
↓
Action: AI - (OpenAI/Claude) - Analiz ve düzenleme
↓
Action: Google Sheets - Update Row
↓
Action: Email - Bildirim
```

**Adım 2: Google Sheets API etkinleştir**
```bash
# Google Cloud Console'da:
# APIs & Services → Enable → Google Sheets API
# Credentials → Create OAuth2 Client ID
```

---

## 5. Raporlama Otomasyonu

### Otomasyon #9: Haftalık Satış Raporu

**Kimler İçin:** Satış müdürü, CEO, KOBİ sahibi  
**Zaman Tasarrufu:** %90 (3 saat → 15 dk)  
**Zorluk:** ⭐⭐ Orta  

#### Kurulum

**Adım 1: N8N Workflow**
```
[Schedule: Her Cuma 17:00]
↓
[HubSpot/Gmail/Google Sheets - Veri çek]
↓
[AI - Rapor oluştur]
  - Bu hafta kaç satış?
  - Kaç teklif gönderildi?
  - Kaçı onaylandı?
  - En çok satan ürünler?
  - Funnel darboğazı nerede?
↓
[Email - PDF rapor gönder]
```

**Adım 2: Rapor template (Claude Prompt)**
```
Aşağıdaki verilerden haftalık satış raporu oluştur:

VERİLER:
- Bu hafta satış: {satış_data}
- Geçen hafta satış: {geçen_hafta_data}
- Bekleyen teklifler: {teklif_data}

RAPOR FORMATI:
1. Özet (2-3 cümle)
2. Bu hafta vs geçen hafta karşılaştırması
3. En iyi performans gösteren ürünler
4. Dikkat edilmesi gereken noktalar
5. Önümüzdeki hafta önerileri
```

#### Araçlar
| Araç | Kullanım | Fiyat |
|------|----------|-------|
| [N8N](https://n8n.io/) | Workflow otomasyon | Ücretsiz (self-hosted) |
| [Google Data Studio](https://datastudio.google.com/) | Dashboard | Ücretsiz |
| [Power BI](https://powerbi.microsoft.com/) | Raporlama | Ücretsiz / $10/ay |
| [Metabase](https://www.metabase.com/) | Açık kaynak BI | Ücretsiz |

---

## Hızlı Başlangıç

### 1. Hafta: Email Otomasyonu
```bash
# N8N kur (en kolay başlangıç)
docker run -d --name n8n -p 5678:5678 n8nio/n8n

# Gmail entegrasyonu yap
# İlk workflow: Email önceliklendirme
```

### 2. Hafta: Takvim Otomasyonu
```bash
# Calendly kayıt ol
# Google Calendar bağla
# İlk toplantı planla
```

### 3. Hafta: Toplantı Özeti
```bash
# Fireflies.ai kayıt ol
# Zoom bağla
# İlk toplantını kaydet
```

### 4. Hafta: Raporlama
```bash
# N8N'ye veri kaynaklarını bağla
# Haftalık schedule ayarla
# İlk otomatik raporu al
```

---

## Maliyet & Araçlar

### No-Code Otomasyon Platformları

| Platform | Güçlü Yön | Fiyat |
|----------|-----------|-------|
| [Zapier](https://zapier.com/) | 5000+ uygulama | Ücretsiz başlangıç, $20+/ay |
| [Make.com](https://make.com/) | Görsel akış | Ücretsiz, $9+/ay |
| [n8n](https://n8n.io/) | Açık kaynak, esnek | Kendi sunucunda ücretsiz |
| [Power Automate](https://flow.microsoft.com/) | Office 365 entegrasyonu | Office ile ücretsiz |
| [IFTTT](https://ifttt.com/) | Basit otomasyonlar | Ücretsiz |

### AI API Servisleri

| Servis | Kullanım | Fiyat |
|--------|----------|-------|
| [Claude API](https://console.anthropic.com/) | Doküman analizi, yazı | $0.001-0.01/istek |
| [OpenAI API](https://platform.openai.com/) | Yazı, analiz | $0.001-0.06/istek |
| [Google AI](https://cloud.google.com/ai) | Çeviri, OCR | Pay-as-you-go |
| [Azure AI](https://azure.microsoft.com/ai) | Kurumsal çözümler | Kurumsal |

### Email & Takvim

| Araç | Kullanım | Fiyat |
|------|----------|-------|
| [Mailtrack](https://mailtrack.io/) | Email takip | Ücretsiz/$8/ay |
| [Calendly](https://calendly.com/) | Toplantı planlama | Ücretsiz/$12/ay |
| [Otter.ai](https://otter.ai/) | Toplantı transkript | Ücretsiz/$10/ay |
| [Fireflies.ai](https://fireflies.ai/) | Toplantı AI analizi | Ücretsiz/$10/ay |

---

## Sonuç

Bu rehberdeki 9 otomasyonu uygulayarak:

- **Haftalık tasarruf:** 10-15 saat
- **Email okuma süresi:** -%60
- **Toplantı notu:** -%100
- **Rapor hazırlama:** -%90
- **Veri girişi hatası:** -%80

**Başlangıç:** En kolay olanla başla (email otomasyonu veya takvim). 1 hafta içinde sonuç görürsün.

---

## Katkıda Bulunma

Bu rehber açık kaynak olarak geliştirilmektedir. Katkıda bulunmak için:
1. Fork edin
2. Yeni workflow'lar ekleyin
3. Pull request açın

## Lisans

MIT License - Ticari ve kişisel kullanım için ücretsiz.

---

*Bu rehber, en yıldızlı GitHub repolarından derlenmiştir. Tüm araçlar açık kaynak veya ücretsiz başlangıç planı sunmaktadır.*