# Beyaz Yakalı Ofis Otomasyonları — 2026-06-15

## Pazartesi — Email & Takvim Otomasyonları

**Araştırma Odaklı:** Email önceliklendirme, takvim yönetimi, toplantı notu alma ve otomatik takip sistemleri

---

## OTOMASYON 1: Meetily — "Toplantı Notlarını Artık Siz Yazmıyorsunuz"

**Kimler İçin:** Toplantı yoğun çalışanlar, proje yöneticileri, satış temsilcileri, yöneticiler

**Ne Yapıyor:** Toplantı sırasında canlı transkripsiyon yapıyor, konuşmacıları ayırt ediyor (speaker diarization), ve toplantı sonunda AI özeti çıkarıyor — tamamen ofis bilgisayarında, bulut yok

**Nasıl Yapılır:**
1. GitHub'dan Meetily'i indir (macOS/Windows, ücretsiz)
2. Kur ve Ollama'ya bağla (yerel LLM)
3. Toplantıda "Start recording" bas
4. Bittiğinde AI özet ve action items otomatik gelir

**Ne Kazandırıyor:** Haftada 4-6 saat toplantı notu yazma zamanı. Geçen hafta 5 toplantı yaptıysanız = 1 iş günü kazanç.

**Zorluk:** Kolay — kurulum 15 dakika, teknik bilgi gerektirmiyor

**Araçlar:** Meetily (Zackriya-Solutions/meetily — 12,733 ⭐ GitHub), Ollama (yerel LLM), Whisper (konuşma tanıma)

**Kaçırılan Nokta:** İnsanlar toplantı notunu "sonra yazmayı" erteliyor. Meetily notu anında yazıyor — ertesi gün hatırlamaya çalışmak yok. "100% local processing" denildiğinde şirket verisi dışarı çıkmıyor, BT departmanı da rahat ediyor.

---

## OTOMASYON 2: Jace AI Email Agent — "Email'inizi Sizin Adınıza Okuyan AI Asistan"

**Kimler İçin:** Yöneticiler, executive asistanlar, email trafiği yoğun profesyoneller

**Ne Yapıyor:** Gelen kutusunu analiz ediyor, önemli mailleri önceliklendiriyor, otomatik yanıt taslakları oluşturuyor, toplantı isteklerini takvime ekliyor

**Nasıl Yapılır:**
1. Jace.ai'a kaydol
2. Email hesabını bağla (IMAP/SMTP veya doğrudan entegrasyon)
3. AI'a "her sabah 8'de özet ver", "müşteri maillerini önceliklendir" gibi talimatlar ver
4. Jace otomatik çalışıyor

**Ne Kazandırıyor:** Günde 1-2 saat email tarama ve yanıt yazma zamanı

**Zorluk:** Kolay — web arayüzü üzerinden kurulum, kod yazmaya gerek yok

**Araçlar:** Jace AI (jace.ai), alternatif: Superhuman AI, Lavender

**Kaçırılan Nokta:** "Email answer" özelliği sadece yanıt taslağı değil — Jace maillerin bağlamını anlayıp "müşteri bu maili neden atmış" yorumu da ekliyor. Yani sadece "ne yazacağınızı" değil, "durumu nasıl çözümleyeceğinizi" de sunuyor.

---

## OTOMASYON 3: Microsoft Scout — "OpenClaw'dan İlham Alan Şirket İçi AI Agent"

**Kimler İçin:** Microsoft 365 kullanan şirketler, IT yöneticileri, departman şefleri

**Ne Yapıyor:** Şirket içi görevleri otomatik yapıyor — doküman tarama, takvim kontrolü, email yazma, veri toplama. OpenClaw framework'ü üzerine inşa edilmiş.

**Nasıl Yapılır:**
1. Microsoft 365 Copilot redesign 2026 ile gelen Scout eklentisini aktif et
2. IT yöneticisi şirket içi veri kaynaklarını (SharePoint, Teams, Outlook) bağlar
3. Çalışanlar "Scout, müşteri sözleşmesini bul ve özetle" gibi talimat verir

**Ne Kazandırıyor:** Haftada 5-8 saat doküman arama ve bilgi toplama zamanı

**Zorluk:** Orta — IT kurulumu gerekiyor, bireysel çalışan doğrudan kullanamaz

**Araçlar:** Microsoft 365 Copilot (Scout), OpenClaw framework

**Kaçırılan Nokta:** Scout "şirket context'ini" anlıyor. Normal ChatGPT'den farkı — şirketin kendi verileriyle çalışıyor, gizli bilgileri sızdırmıyor. Bugün (Haziran 2026) canlıya girdi, henüz çok az şirket kullanıyor = erken adapte avantajı var.

---

## OTOMASYON 4: AI Email Filtreleme — "Gereksiz Email'i AI Ayıklıyor"

**Kimler İçin:** Her ofis çalışanı, özellikle günde 50+ email alanlar

**Ne Yapıyor:** Gelen kutusundaki mailleri otomatik kategorize ediyor (müşteri/şirket içi/fatura/spam), önemli mailleri优先级 olarak işaretliyor, bültenleri tek bir klasöre topluyor

**Nasıl Yapılır:**
1. Google Workspace veya Microsoft 365'te AI özelliklerini aç
2. "otle.ai" veya "Clean Email" gibi araçlarla AI kuralları tanımla
3. "Müşterilerden gelen mailler = kırmızı, şirket içi = mavi" gibi kural koy
4. AI kendi kendine öğreniyor — 2 hafta sonra artık siz koymadan doğru分类 yapıyor

**Ne Kazandırıyor:** Günde 20-30 dakika gereksiz email okuma/tıklama zamanı

**Zorluk:** Kolay — 5 dakikada kurulur, 2 haftada AI öğrenir

**Araçlar:** Google Workspace AI, Microsoft Copilot Email, Otle.ai, Clean Email

**Kaçırılan Nokta:** İnsanlar email filtrelemesini "manuel" yapıyor — kurallar koyuyor. Oysa AI "spam olmayan ama okunmaya değmeyen" mailleri de yakalıyor. "Bana bu email'de ne soruluyor, ne istiyorlar?" sorusunu AI cevaplıyor ve siz sadece actionable olanlara bakıyorsunuz.

---

## OTOMASYON 5: Takvim AI Agent — "Toplantı Planlamayı AI Yapıyor"

**Kimler İçin:** CEO, yönetici, asistanlar, proje yöneticileri — randevu yoğunluğu olan herkes

**Ne Yapıyor:** Uygun toplantı zamanlarını otomatik buluyor, katılımcılara davet gönderiyor, toplantı öncesi gündem maddelerini paylaşıyor, takip notlarını dağıtıyor

**Nasıl Yapılır:**
1. Reclaim.ai veya Clockwise.abio.ai'a kaydol
2. Takviminizi bağla (Google Calendar veya Outlook)
3. "Her hafta Salı 14:00-16:00 odak çalışma zamanı blokla" gibi öncelikler ver
4. AI takviminizi otomatik düzenliyor

**Ne Kazandırıyor:** Haftada 2-3 saat toplantı koordinasyonu email'i yazma zamanı

**Zorluk:** Kolay — hesap aç, bağla, öncelikleri koy — 10 dakikada hazır

**Araçlar:** Reclaim.ai, Clockwise, Motion, Calendar

**Kaçırılan Nokta:** Reclaim.ai "conflict detection" yapıyor — siz toplantı ayarlamaya çalışırken AI anında uygun boşluk buluyor ve çakışma varsa alternatif öneriyor. Bu özellik "bana 1 saat boş zaman bul" diye email atan asistanlara olan ihtiyacı azaltıyor.

---

## Herkesin Kaçırdığı Nokta #1

**Microsoft Copilot Haziran'da 2 Kez Çöktü — Ama Bu AI'ın Değerini Artırıyor**

Microsoft Copilot bu ay (Haziran 2026) ardışık iki kez global çöküntü yaşadı. Enterprise müşteriler "AI'a bağımlı olduk" paniği yaşadı. Ama asıl ders şu: **AI kullanan şirketler, kullanmayanlara göre hâlâ 3-5x daha üretken.** Çöküş kısa süreliydi — 2-4 saat arası. Sonuç: şirketler "AI'a tam bağımlılık" yerine "AI + manuel backup" sistemi kurmaya başladı. **Otomasyon = kritik iş süreçlerini AI'a bırakmak değil, AI'ı destek olarak kullanmak.**

---

## Herkesin Kaçırdığı Nokta #2

**Microsoft AI CEO'su "12-18 Ayda Beyaz Yakalı İşler Otomatik Olacak" Dedi — Sonra Söyledikini Geri Aldı**

Mustafa Suleyman Haziran başında "Ofis işlerinin çoğu 12-18 ayda otomatik olacak" dedi. Ardından "ben işleri kastetmiştim, işleri değil" diye geri adım attı. Ama asıl kaçırılan nokta: **Süre değil, yön doğru.** 12-18 ay belki abartı. Ama 5-10 yıl içinde "email yönetimi, takvim koordinasyonu, basit doküman hazırlama" gibi görevlerin büyük kısmı AI'da olacak. Bugün email AI agent kullanan biri, 5 yıl sonra kimse email yönetmezse hazır olacak. **Kullanan kazanacak, bekleyen kaybedecek.**

---

## Haftalık Özet — Email & Takvim AI Araçları

| Otomasyon | Kazanım (Hafta) | Zorluk | Öne Çıkan Araç |
|-----------|-----------------|--------|----------------|
| Toplantı notu AI | 4-6 saat | Kolay | Meetily (12,733 ⭐) |
| Email AI agent | 5-10 saat | Kolay | Jace.ai |
| Şirket içi AI (Scout) | 5-8 saat | Orta | Microsoft 365 Copilot Scout |
| AI email filtreleme | 2-3 saat | Kolay | Google Workspace AI, Otle.ai |
| Takvim AI agent | 2-3 saat | Kolay | Reclaim.ai, Clockwise |

---

## Kaynaklar

- Meetily: https://github.com/Zackriya-Solutions/meetily
- Jace AI: https://www.jace.ai/
- Microsoft Scout: https://www.bing.com/news/search?q=Microsoft+Scout+AI+assistant+M365
- Reclaim.ai: https://reclaim.ai/
- Microsoft Copilot June outage: https://www.bing.com/news/search?q=Microsoft+Copilot+Fails+June+2026

---

## LinkedIn Post Fikri

**Başlık:** "Email'ınıza bakan biri var — ve o bir AI"

**Post:**
Email'ınızla ilgilenen bir "asistan" hayal edin:

• Gereksiz mailleri otomatik ayıklıyor
• Önemli müşteri maillerini优先级'laendiriyor
• Toplantı isteklerini takviminize bakarak otomatik yanıtlıyor
• Hatta taslak cevaplar yazıyor

Meetily toplantı notu için, Jace email önceliklendirme için, Reclaim.ai takvim koordinasyonu için. Hepsi aynı mantık: **tekrarlayan ofis işini AI alıyor, siz stratejik işe odaklanıyorsunuz.**

Bugün 5 toplantı yaptıysanız — haftada 1 iş günü kazancınız var.

Kullanıyor musunuz? Deneyimlerinizi paylaşın 👇

#AI #EmailOtomasyon #Takvim #OfisVerimliliği #AIAssistant

---

## Sonraki Gün — Salı: Doküman & Rapor Otomasyonları

Salı günkü otomasyon konusu: PDF okuma, rapor özetleme, doküman dönüştürme araçları. LLMWhisperer (belge AI'a hazırlama) ve benzeri araçlar incelenecek.
