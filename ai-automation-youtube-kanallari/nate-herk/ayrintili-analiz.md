# Nate Herk — Detaylı Analiz

**Kanal:** Nate Herk | AI Automation  
**Abone Sayısı:** 822B  
**Tarama Tarihi:** 2026-06-22

---

## Video 1: Finally. Agent Loops Clearly Explained.
**Video ID:** EuzYhzB0vbI  
**Tarih:** 19 Haziran 2026  
**Süre:** ~14:33

### Özet
Agent loop mühendisliği hakkında yayınlanmış en net açıklama. Çoğu kişi agent loop'larını "kodcu işi" olarak görüyor, ancak Nate bunu aşıyor.

### Anahtartespitler
- Agent loop = **reason → act → observe → repeat** döngüsü
- **Verification step** (doğrulama adımı) mimariden daha kritik
- Agent loop kurarken "ne olursa başarısız olur" sorusunu sormak gerekiyor
- Agent fleet'ler çalıştıranlar için değil, **tek agent bile olsa** loop mantığı aynı

### Herkesin Kaçırdığı Nokta
Agent loop'ların gücü mimaride değil, **doğrulama mekanizmasında**. Çoğu eğitim videosu hangi modeli kullanacağınızı anlatıyor, ama başarının sırrı agent'ın çıktısını nasıl kontrol ettiğiniz.

### LinkedIn Post Fikri
> "Agent loop'ları sanıldığı kadar karmaşık değil. Dört adım var: reason, act, observe, repeat. Asıl mesele hangi mimariyi kullandığınız değil — çıktıyı nasıl doğruladığınız. Bugün agent'larınızın doğrulama adımı var mı, yoksa körü körüne mi çalışıyorlar?"

---

## Video 2: I Switched Claude Code to GLM 5.2 and Ran It All Day
**Video ID:** 2OD14-0cot4  
**Tarih:** 18 Haziran 2026

### Özet
GLM 5.2 (756 milyar parametreli açık kaynak model) Claude Code'a entegre ediliyor. Opus'a kıyasla ~5x ucuz, bilgi işi çoğu görevde yeterli performans.

### Anahtar Tespitler
- **GLM 5.2**: 756B parametre, açık kaynak, Z.ai üzerinden erişilebilir
- Claude Code harness'ına **per-proje** model seçimi mümkün
- Opus'a göre ~5x daha ucuz
- Bilgi işi/geliştirme görevlerinde Opus'a yakın performans
- Bazı durumlarda Opus'u geçiyor (özellikle kod üretimi)

### Herkesin Kaçırdığı Nokta
İnsanlar ya en pahalı modeli ya da en ünlü modeli seçiyor. GLM 5.2 gibi **güçlü açık kaynak alternatifler** Opus'a yaklaşık %80 performans sunuyor, maliyet sadece 1/5'i. Fiyat/performans hesabı yapmak yerine "en güçlü model" takıntısı paradan kaybettiriyor.

### LinkedIn Post Fikri
> "Claude Code'da GLM 5.2'ye geçtim. 756B açık kaynak model, Opus'un 1/5 fiyatı, bilgi işi görevlerinde yakın performans. Herkes en pahalı model peşinde koşuyor, kimse fiyat/performans hesabı yapmıyor. Bugün proje başına model seçimi yapıyorsanız, cüzdanınız zaten teşekkür ediyor."

---

## Video 3: The 5 Levels of a Claude Code Second Brain
**Video ID:** DTCyvo6cC54  
**Tarih:** 17 Haziran 2026  
**Süre:** ~33:00  
**Timestamp:** 0:00 | 3:25 | 4:19 | 8:11 | 13:03 | 19:27 | 25:25 | 28:48 | 30:41

### Özet
Beş seviyeli second-brain sistemi — basit CLAUDE.md router'dan otonom sürekli-çalışan sisteme kadar. Herkes "AI second brain" istiyor ama seviye seçimi yapılmıyor.

### Seviyeler
1. **Level 1:** CLAUDE.md ile yönlendirme (en basit)
2. **Level 2:** Görev başına context yönetimi
3. **Level 3:** Proje bazlı bellek sistemi
4. **Level 4:** Otonom ajan — sürekli çalışan, karar veren
5. **Level 5:** Tam otonomi — müdahale gerektirmeyen sistem

### Anahtar Tespit
"Amaç en üst seviyeye çıkmak değil — **size en az zahmetle en çok faydayı sağlayan seviyeyi bulmak**. Çoğu kişi Level 5'te olması gerektiğini düşünüyor ama Level 2-3 çoğu insan için yeterli."

### Herkesin Kaçırdığı Nokta
Herkes Level 5'te olmak istiyor, ama Level 2-3 çoğu iş için fazlasıyla yeterli. Fazla otomasyon = fazla karmaşıklık = daha çok hata. **En düşük seviye, probleminizi çözen seviye, doğru seviyedir.**

### LinkedIn Post Fikri
> "AI second brain inşa ederken çoğu kişi Level 5 hedefliyor. Yanlış soru bu. Doğru soru: 'Problemi çözen en basit sistem hangisi?' Çünkü her seviye artışı = karmaşıklık artışı = hata olasılığı artışı. Kendinize sorun: re-explaining things'i engelleyen ve ajanın nereye bakacağını bilen en basit sistem hangisi? Cevap muhtemelen Level 2."

---

## Video 4: Both AI Labs Want to Slow Down
**Video ID:** CvA8-aScqio  
**Tarih:** 16 Haziran 2026  
**Süre:** ~12:01  
**Timestamp:** 0:00 | 1:52 | 3:49 | 5:33 | 8:15 | 11:10 | 12:01

### Özet
Anthropic ve OpenAI'nin aynı anda "AI'ı yavaşlatma" çağrısı yapması, hem de IPO süreçlerinin hemen önünde. Nate, bu paradoksu çözüyor.

### Anahtar Tespitler
- Her iki lab da **kazanırlar listesinde** — en çok kazanacak olanlar yavaşlama istiyor
- Büyük lab'lar yavaşlatma çağrısı yaparken **küçük lab'lar hızlanıyor**
- Global yavaşlatma **işlevsel olarak imkansız** — rekabet uluslararası
- **Bireysel strateji:** Şirketlere değil, **kendi becerilerinize** yatırım yapın

### Herkesin Kaçırdığı Nokta
Yavaşlatma çağrısı yapan lab'ların IPO hazırlığı yapması tesadüf değil. Düzenleyici engeller, rakiplerin önünde olmanın en ucuz yolu. Bu arada küçük startup'lar hızla ilerliyor. "AI yavaşlasa bile" becerileriniz sizin kontrolünüzde.

### LinkedIn Post Fikri
> "Anthropic ve OpenAI aynı anda 'AI'ı yavaşlatalım' dedi. Tam IPO öncesi. Tesadüf mü? Büyük lab'lar düzenleyici engel koyarak rekabeti yavaşlatmak istiyor — bu onların en güçlü silahı. Ama siz bir şirkete değil, **kendi becerilerinize** yatırım yapın. Company'e değil, capability'ye bahis koyun."

---

## Video 5: 6 AI Skills to Futureproof Your Career
**Video ID:** 3XIGcM7VICc  
**Tarih:** 15 Haziran 2026  
**Timestamp:** 0:29 | 4:47 | 7:42 | 10:13 | 13:13 | 16:40

### Özet
AI'ın işleri şekillendireceği veya ortadan kaldıracağı bir dönemde, kariyer güvence altına almak için altı somut beceri.

### Altı Beceri
1. Ekipte **AI sorumlusu** olmak — "o kişi" olmak
2. Bir AI aracını **derinlemesine** öğrenmek (yüzeysel değil)
3. **Ne zaman AI gerekmediğini** bilmek
4. AI çıktısını **doğrulama** becerisi
5. AI ile **özerk çalışabilme** (bağımsız)
6. **Birden fazla gelir akışı** oluşturmak (kişisel "işsizlik sigortası")

### Herkesin Kaçırdığı Nokta
Beşinci beceri (birden fazla gelir akışı) çoğu profesyonelin hiç düşünmediği şey. AI sadece "ne iş yapıyorum" değil, "nasıl para kazanıyorum"ı da değiştirecek. Tek gelir akışı = AI'a karşı tek kırılganlık noktası.

### LinkedIn Post Fikri
> "AI geleceği 6 beceri gerektiriyor — ama altıncısı en kritik: birden fazla gelir akışı. AI'ın sizin rolünüzü değiştireceğini veya ortadan kaldıracağını varsayın. Tek gelir akışıyla ne olur? Çoklu gelir akışı = AI'a karşı kişisel kırılganlık sigortanız. Bu beceriyi kaç kişi listeleyerek geçiyor?"
