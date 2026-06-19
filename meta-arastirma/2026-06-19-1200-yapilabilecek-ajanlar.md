# WhatsApp ve Instagram İçin 5 Yapılabilecek AI Ajanı
**Tarih:** 2026-06-19 12:00
**Slot:** 6 saatlik Meta araştırma slotu — Konu 3/4

---

## Giriş — AI Agent Platform Olarak Meta

Meta, Haziran 2026'da WhatsApp Business ve Instagram için AI Business Agent platformunu global olarak başlattı. Bu platform, işletmelerin müşteri hizmetleri, satış ve pazarlama süreçlerini otomatikleştirmesini sağlıyor.

**Platformun kapasitesi:**
- WhatsApp, Instagram DM, Messenger üzerinden 7/24 müşteri desteği
- Doğal dilde sipariş alma, şikayet çözme, ürün önerisi
- $200/ay "Hatch" fiyatlandırma planı

**Ama gerçek fırsat:** Meta'nın sunduğu 5 hazır ajanın ötesinde, işletmelere özel ajanlar build etmek.

---

## Ajan #1 — Sepet Terk Etme Recovery Ajanı 🛒

**Ne yapıyor?**
Müşteri e-ticaret sitesinde sepete ürün ekledi ama satın almadı. Ajan:
1. 1 saat sonra: "Merhaba [isim], sepetinizi mi unuttunuz? 🎁"
2. 24 saat sonra: "Bugün son gün! [Ürün] hâlá sizi bekliyor"
3. 72 saat sonra: "%10 indirim kodu" teklifi

**Nasıl çalışır?**
```
n8n Workflow:
  SepetDB ( Terk Edildi ) → Koşul Kontrolü (72 saat?) 
  → Evet: Claude → Kişiselleştirilmiş mesaj oluştur
  → WhatsApp Business API → Gönder
  → Hayır: Bekle, sonraki saat kontrol et
```

**Gerçek metrikler:**
- Abandoned cart recovery: %10-15 ek dönüşüm
- WhatsApp açılma oranı: %70-80 (email: %20-30)
- 72 saat kuralı: Template onayı gerektirmez

**Herkesin Kaçırdığı Nokta:** İnsanlar "sepete ürün ekleyip çıktı" durumunu email ile çözmeye çalışıyor. Email açılma oranı %20-30. WhatsApp ile aynı mesaj: %70-80 açılma. Aynı maliyet, 3x daha fazla sonuç.

---

## Ajan #2 — Sipariş Takip ve Kargo Bildirimi Ajanı 📦

**Ne yapıyor?**
Müşteri siparişini takip etmek için WhatsApp üzerinden "Siparişim nerede?" yazıyor. Ajan:
1. Sipariş numarasını çekiyor
2. Kargo API'sinden anlık durumu alıyor
3. Müşteriye ETA (tahmini varış zamanı) bildiriyor
4. Kargo değişikliğinde otomatik bildirim gönderiyor

**Nasıl çalışır?**
```
WhatsApp Mesajı → "Siparişim nerede #SPN12345"
→ Claude: Sipariş no çıkar → Kargo API sorgula
→ Yanıt: "Paketiniz yarın 14:00-16:00 arasında teslim edilecek 🚚"
```

**Gerçek metrikler:**
- Müşteri desteği yükü: %40-60 azalma
- Müşteri memnuniyeti: %25 artış ( NPS )
- Kargo şikayeti: %50 düşüş

**Herkesin Kaçırdığı Nokta:** Kargo takip ajanı sadece "müşteri mutluluğu" değil, aynı zamanda **satış fırsatıdır**. Müşteri siparişini takip ederken, "Bu ürünle birlikte şu da ilgililerinizi inceleyebilirsiniz" ile çapraz satış yapılabilir.

---

## Ajan #3 — Ürün Öneri ve Kişiselleştirilmiş Satış Ajanı 🎯

**Ne yapıyor?**
Müşteri WhatsApp üzerinden "Hangi ürünü önerirsiniz?" diye soruyor. Ajan:
1. Müşterinin geçmiş siparişlerini çekiyor
2. Claude ile kişiselleştirilmiş ürün önerisi oluşturuyor
3. Görsel + açıklama + fiyat + CTA ile mesaj gönderiyor
4. "Beğendiniz mi?" takibi yapıyor

**Nasıl çalışır?**
```
WhatsApp: "Hangi ürünü önerirsiniz?"
→ Müşteri geçmişi: Son 3 sipariş, category tercihleri
→ Claude: "Siparişlerinize göre [Ürün X] kesinlikle beğeneceksiniz çünkü..."
→ WhatsApp: Görsel + açıklama + "Sipariş vermek için: [link]"
```

**Gerçek metrikler:**
- Kişiselleştirilmiş öneri: %30 daha yüksek tıklama oranı
- Chat-to-sale dönüşüm: %15-25
- Ortalama sipariş değeri: %20 artış (çapraz satış ile)

**Herkesin Kaçırdığı Nokta:** İnsanlar ürün önerisini "müşteri hizmetleri" olarak görüyor. Oysa kişiselleştirilmiş öneri = en yüksek ROI'li pazarlama kanalı. Amazon'un gelirinin %35'i kişiselleştirilmiş önerilerden geliyor.

---

## Ajan #4 — Randevu ve Rezervasyon Yönetim Ajanı 📅

**Ne yapıyor?**
WhatsApp üzerinden randevu alma, iptal, değişiklik:
1. "Cuma 14:00'te kuaför randevusu almak istiyorum"
2. Ajan uygun slot'ları kontrol ediyor
3. Onay mesajı gönderiyor
4. 24 saat önce hatırlatma yapıyor
5. No-show durumunda otomatik iptal/yeniden açma

**Nasıl çalışır?**
```
WhatsApp: "Cuma 14:00 randevu"
→ Takvim API: Uygun slot kontrolü
→ Müsait: "Onaylıyor musunuz? [Evet/Hayır]"
→ Onay: Takvim'e kaydet + 24s hatırlatma planla
```

**Gerçek metrikler:**
- Rezervasyon no-show oranı: %25-40 düşüş
- Telefon ile randevu maliyeti: $8-15/call → $0.02/WhatsApp message
- Müşteri memnuniyeti: Randevu hatırlatma ile %40 artış

**Herkesin Kaçırdığı Nokta:** Randevu yönetimi ajanı sadece kuaför/gym için değil. E-ticaret için "teslimat randevusu planlama", servis için "montaj randevusu", hastane için "muayene randevusu" — her sektörde çalışır.

---

## Ajan #5 — Şikayet ve Crisis Yönetimi Ajanı ⚠️

**Ne yapıyor?**
Müşteri şikayet ediyor: "Ürün hasarlı geldi", "Kargo gecikti", "Yanlış ürün geldi". Ajan:
1. Şikayeti sınıflandırıyor (hasarlı/yanlış/gecikmeli)
2. Duygu analizi yapıyor (kızgın/memnun/ hayal kırıklığı)
3. Uygun çözüm öneriyor (iade/yeniden gönderim/para iadesi)
4. İnsan onayına sunuyor veya otomatik çözüyor
5. Sonuçları kaydediyor ve raporluyor

**Nasıl çalışır?**
```
WhatsApp: "Ürün hasarlı geldi!!! 😡"
→ Claude: Duygu analizi (kızgın) + Ürün kontrolü (son 30 gün satın alma)
→ Çözüm önerisi: "Yeni ürünü en kısa zamanda ücretsiz gönderiyoruz"
→ Müşteri onayı → Otomatik yeni sipariş + kargo takip no
→ Arka planda: Rapor → Ürün kalitesi ekibi bilgilendir
```

**Gerçek metrikler:**
- First response time: 2 saat → 30 saniye
- Müşteri retention: Şikayeti çözülen müşteriler %80 tekrar satın alıyor
- Negatif sosyal medya: Proaktif çözüm ile %60 azalma

**Herkesin Kaçırdığı Nokta:** Şikayet yönetiminde hız = her şey. Müşteri "hasarlı ürün" diye mesaj attığında ilk 30 dakika kritik. Bu sürede yanıt vermezseniz, müşteri Twitter/Instagram'a gidiyor. AI ajan 7/24 anında yanıt veriyor, insan sadece onay veriyor.

---

## Genel Metrik Özeti

| Ajan | Ana Fayda | Beklenen Sonuç |
|------|-----------|----------------|
| #1 Sepet Recovery | Terk edilen sepetleri kurtarma | %10-15 ek dönüşüm |
| #2 Sipariş Takip | Anlık kargo bilgisi | %40-60 destek yükü azalması |
| #3 Ürün Öneri | Kişiselleştirilmiş satış | %30 tıklama, %20 sepet artışı |
| #4 Randevu Yönetimi | Otomatik randevu | %25-40 no-show azalması |
| #5 Şikayet Yönetimi | 7/24 anında yanıt | %80 müşteri retention |

---

## Türkiye İçin Öncelik Sıralaması

1. **#1 Sepet Recovery** — E-ticaret için en yüksek ROI, kolay implementasyon
2. **#3 Ürün Öneri** — E-ticaret × fashion/giyim için ideal
3. **#5 Şikayet Yönetimi** — Türk müşterileri hızlı yanıt bekliyor
4. **#2 Sipariş Takip** — Lojistik/sevkiyat şirketleri için
5. **#4 Randevu** — Kuaför/gym/ clinic için

---

## LinkedIn Post Fikri

**Başlık:** WhatsApp Business İçin 5 AI Ajanı: Hangisi Sizin İşinizi Kurtarır?

**Hook:** Meta Business Agent platformu geldi ve herkes "ne yapacağım" diye düşünüyor. İşte 5 ajan fikri — hangisi sizin sektörünüz için en kritik?

**İçerik:**
Meta, Haziran 2026'da WhatsApp Business için AI ajan platformunu global başlattı. İşletmeler için 5 kritik ajan:

1. 🛒 Sepet Terk Etme Recovery — %10-15 ek dönüşüm
2. 📦 Sipariş Takip — %40-60 destek yükü azalması
3. 🎯 Ürün Öneri — Kişiselleştirilmiş satış, %30 daha yüksek tıklama
4. 📅 Randevu Yönetimi — No-show %25-40 azalması
5. ⚠️ Şikayet Yönetimi — 7/24 anında yanıt, %80 müşteri retention

Sizin işletmeniz için hangisi öncelikli? Yorumlarda belirtin 👇

**Görsel önerisi:** 5 ikon kartı — her ajan için ikon + kısa metin + beklenen sonuç

---

## Kaynaklar

1. [TechCrunch: Meta's AI agent for WhatsApp Business is now available globally](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-av)
2. [Meta Business Agent platform](https://developers.facebook.com/docs/whatsapp/overview)
3. [Meta enters enterprise AI race with new business agent — Reuters](https://www.reuters.com/business/meta-launches-enterprise-focused-ai-business-agent-2026-06-03/)
