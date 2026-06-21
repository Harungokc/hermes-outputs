# Nate Herk — Ayrıntılı Analiz (2026-06-19)

---

## Video 1: GLM 5.2 in Claude Code is Blowing My Mind
**Video ID:** 2OD14-0cot4 | **Tarih:** 18 Haz 2026 | **Görüntülenme:** 101,842

### Özet
GLM 5.2 (756B parametre açık kaynak model) Claude Code'da Opus yerine kullanılabiliyor, ~5x ucuz. Nate bunu gün boyu test etmiş.

### Ana Noktalar
- GLM 5.2 çoğu bilgi işi için Opus kadar iyi performans gösteriyor
- Z.ai API üzerinden路由,Claude Code harness'ına entegre
- Kreatif one-shot buildler, storm research için ideal
- Açık kaynak olması "rent vs own" tartışmasını değiştiriyor

### Herkesin Kaçırdığı Nokta
**GLM 5.2'i kiralamak yerine kendiniz barındırabileceğiniz gibi, model seçimini proje bazlı yapmak da mümkün.** Her görev için en iyi modeli seçmek yerine, bütçe/kalite dengesini proje bazlı ayarlamak maliyeti düşürür.

### LinkedIn Post Fikri
"Açık kaynak model + Claude Code = 5x tasarruf. GLM 5.2'i Opus yerine kullanmak çoğu bilgi işi görevi için yeterli. Tek yapmanız gereken: .claude/settings.local.json'da modeli değiştirmek. Bu kadar basit."

---

## Video 2: How to Build Effective Claude Code Agents in 2026
**Video ID:** RzLV8sfFdMM | **Tarih:** 18 Haz 2026 | **Görüntülenme:** 30,619

### Özet
Cole Medin ile 1 saatlik sohbet: Binlerce saat Claude Code deneyiminden çıkarılan pratik dersler.

### Ana Noktalar
- **Vibe coding yerine yönlendirme**: Agentı yönetmek, sadece prompt yazmaktan farklı
- **Planlama > Build**: Her modelin "dumb zone"ı var — belli bir noktadan sonra sadece deneyim yardımcı oluyor
- **Verification system**: Agentın çalışmasını kanıtlaması gerekiyor
- **Security problem**: Herkes bunu atlıyor, ama kritik

### Herkesin Kaçırdığı Nokta
**"Dumb zone" kavramı** — her model belli bir karmaşıklık seviyesinde temel hatalar yapmaya başlıyor. Bunu bilmek, agent görevlerini doğru boyutlara bölmek için kritik.

### LinkedIn Post Fikri
"Claude Code'da 1000+ saat geçirdikten sonra öğrendiğim en önemli şey: Her modelin bir 'dumb zone'ı var. Belli bir karmaşıklıktan sonra model sadece hata yapıyor, siz de debug ile uğraşıyorsunuz. Çözüm: görevi daha küçük parçalara bölmek."

---

## Video 3: We Might Actually Need to Stop AI
**Video ID:** CvA8-aScqio | **Tarih:** 16 Haz 2026 | **Görüntülenme:** 37,349

### Özet
Anthropic ve OpenAI'nin "AI'ı yavaşlatın" çağrısı ile halka arz planları arasındaki çelişki analiz ediliyor.

### Ana Noktalar
- Her iki şirket de halka arza hazırlanıyor
- Aynı anda "AI'ı yavaşlatın" çağrısı yapıyorlar
- Küresel yavaşlatma mümkün mü? Hayır.
- **Betiğiniz: AI'ı değil, AI kullanma becerinizi geliştirin**

### Herkesin Kaçırdığı Nokta
Şirketler yarışı durduramaz çünkü rekabet onları zorluyor. Ama **siz kendi AI becerilerinizi geliştirmeye odaklanabilirsiniz** — bu, hiçbir şirketin sizden alamayacağı bir şey.

### LinkedIn Post Fikri
"OpenAI ve Anthropic 'AI'ı yavaşlatın' diyor, sonra halka arza hazırlanıyorlar. Çelişki değil — onlar yarışı durduramaz. Siz ne yapabilirsiniz? AI kullanma becerinizi geliştirmeye odaklanın. Bu sizin elinizde."

---

## Video 4: Every Level of a Claude Second Brain Explained
**Video ID:** DTCyvo6cC54 | **Tarih:** 17 Haz 2026 | **Görüntülenme:** 76,829

### Özet
5 seviyeli second brain sistemi, en düşük seviyeden (CLAUDE.md) en yükseğe (otonom agent).

### Ana Noktalar
- **Seviye 1**: CLAUDE.md ile yönlendirme
- **Seviye 3**: Dosya tabanlı memory sistemi
- **Seviye 5**: Sürekli çalışan otonom agent
- Hedef seviye 5'e çıkmak değil, **en düşük seviyeyi bulmak** ki bu sadece sorununuzu çözsün

### Herkesin Kaçırdığı Nokta
**Seviye 5 her zaman en iyi çözüm değil.** Sürekli çalışan bir agent, daha fazla maliyet ve karmaşıklık getirir. Amaç, "re-explaining things"i durdurmak — bunun için seviye 2 veya 3 yeterli olabilir.

### LinkedIn Post Fikri
"Second brain sistemleri 5 seviyeli — ama amaç en üst seviyeye çıkmak değil. En düşük seviyeyi bulmak ki bu sadece sorununuzu çözsün. Gereksiz karmaşıklık = gereksiz maliyet."

---

## Video 5: From Zero to Head of AI in 1 Year (as a regular person)
**Video ID:** diY71x7GUjI | **Tarih:** 12 Haz 2026 | **Görüntülenme:** 19,229

### Özet
Ailin: 15 yıl email developer, 39 yaşında işten çıkarıldı, 1 yıl sonra 15 markalı şirkette Head of AI.

### Ana Noktalar
- n8n ve Claude Code sıfırdan öğrendi
- Herkese açık şekilde building yapıyordu
- Mülakatta "ne inşa ettin?" sorusu her şeyi değiştirdi
- Teknik AI geçmişi yok — ama portföyü vardı

### Herkesin Kaçıldığı Nokta
**"Ne inşa ettin?" sorusu, CV'lerin yerini aldı.** AI çağında diploma ve unvan yerine, ne yaptığınızı göstermeniz gerekiyor. Ailin'in hikayesi bunun kanıtı.

### LinkedIn Post Fikri
"39 yaşında, 15 yıl email developer, işten çıkarıldı. 1 yıl sonra Head of AI oldu. Nasıl? CV yerine portföy gösterdi. 'Ne inşa ettin?' sorusu artık her mülakatın ilk sorusu — ve en önemlisi."

---

## Video 6: Finally. Agent Loops Clearly Explained.
**Video ID:** EuzYhzB0vbI | **Tarih:** 19 Haz 2026 | **Görüntülenme:** 41,597

### Özet
Agent loop (reason, act, observe, repeat) ve loop engineering'in gerçekte ne anlama geldiği.

### Ana Noktalar
- Loop = reason + act + observe + repeat
- **Verification adımı** mimariden daha önemli
- "Done" kriteri agentın anlayabileceği şekilde tanımlanmalı
- 5 agent çalıştırmak = iyi sonuç değil

### Herkesin Kaçırdığı Nokta
**Çoğu kişi loop mimarisine odaklanıyor, verification'a değil.** Agentın ne zaman "bitti" olduğunu bilmesi, kaç agent çalıştırdığınızdan çok daha kritik. Bu basit ama güçlü fark, üretkenliği 10x artırabilir.

### LinkedIn Post Fikri
"Agent loop engineering = 5 agent çalıştırmak değil. Agentın ne zaman 'bitti' olduğunu bilmesi = en kritik adım. Bu tek fark, üretkenliği 10x artırabilir. Çoğu kişi bunu atlıyor."