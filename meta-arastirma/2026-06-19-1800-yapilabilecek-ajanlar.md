# WhatsApp ve Instagram İçin 5 Yapılabilecek AI Ajanı

**Tarih:** 19 Haziran 2026, 18:00
**Slot:** Her 6 saatte bir (1800)
**Konu:** Yapılabilecek Ajanslar

---

## 1. Özet Tablo

| Ajan # | İsim | Görev | Verimlilik Kazanı |
|--------|------|-------|-------------------|
| 1 | Sipariş Bot | WhatsApp üzerinden sipariş alma, stok sorgulama | +40% dönüşüm |
| 2 | Randevu Hatırlatıcı | Otomatik randevu teyidi, hatırlatma, iptal yönetimi | -60% no-show |
| 3 | Sepet Terk Bot | Sepeti bırakan müşteriye 1s/24s/72s hatırlatma | +%10-15 dönüşüm |
| 4 | Kargo Takip Bot | Kargo durumu sorgulama, tahmini teslimat bildirimi | -70% destek talebi |
| 5 | Sadakat/Müşteri Ödül Bot | Puan sorgulama, ödül kullanımı, VIP müşteri yönetimi | +25% tekrar satın alma |

---

## 2. Ajan #1 — Sipariş Bot (En Yüksek ROI)

**Ne yapıyor?**
Müşteri WhatsApp'tan "1 numara menusü, 2 adet kola" yazıyor → AI bot siparişi alıp sisteme kaydediyor, stok kontrolü yapıyor, ödeme linki gönderiyor.

**Workflow:**
```
Müşteri DM → Claude/n8n → Stok API → Ödeme Linki → Sipariş Onayı
```

**Kimler için:**
- E-ticaret markaları
- Restaurant/cafe'ler
- Kuaför/güzellik salonları
- Küçük perakende

**Maliyet:** WhatsApp Business API mesaj başına ~$0.01-0.05 + Claude API ~$0.001/mesaj

---

## 3. Ajan #2 — Randevu Hatırlatıcı Bot

**Ne yapıyor?**
Müşteri randevu alıyor → 24 saat önce otomatik hatırlatma → randevu günü tekrar hatırlatma → iptal durumunda boşluğu doldurma

**Workflow:**
```
Randevu API → 24s önce WhatsApp hatırlatma → Teyit beklet → 
Teyit yoksa 2s önce tekrar hatırlatma → İptal → Bekleme listesine bildirim
```

**Kimler için:**
- Kuaför/güzellik salonları
- Klinik/estetik merkezleri
- Avukat/muhasebe ofisleri
- Eğitim/kurs merkezleri

**Metrik:** No-show oranı %60'a kadar düşüyor (sektöre göre değişir)

---

## 4. Ajan #3 — Sepet Terk Bot (E-ticaret İçin En Değerli)

**Ne yapıyor?**
Müşteri sepet ekleyip ayrılıyor → 1 saat sonra kişiselleştirilmiş hatırlatma → 24 saat sonra indirim teklifi → 72 saat sonra son hatırlatma

**Workflow:**
```
Sepet terk → 1s: "Sepetinizi unuttunuz mu?" + ürün görseli
→ 24s: "%10 indirim kodu" teklifi
→ 72s: "Son fırsat" + azalan stok uyarısı
```

**Kimler için:**
- Tüm e-ticaret markaları
- Özellikle moda, aksesuar, elektronik

**Metrik:** Abandoned cart recovery rate %10-15 artış (sektöre göre)

**Herkesin Kaçırdığı Nokta:** Türkiye'de WhatsApp kullanım oranı çok yüksek. E-posta kampanyaları %5-10 açılırken, WhatsApp mesajları %70+ açılıyor. Aynı abandoned cart stratejisi WhatsApp'ta 10x daha etkili.

---

## 5. Ajan #4 — Kargo Takip Bot

**Ne yapıyor?**
Müşteri kargo numarası gönderiyor → AI bot kargo durumunu sorguluyor → tahmini teslimat tarihini bildiriyor → teslimat günü sabahı hatırlatma

**Workflow:**
```
Kargo no gönder → Kargo API entegrasyonu → Durum özeti → 
Tahmini teslimat → Gecikme varsa neden bildirimi → Teslimat günü sabahı hatırlatma
```

**Kimler için:**
- E-ticaret markaları
- Lojistik şirketleri
- Marketplace platformları

**Metrik:** Müşteri destek talebi %70 azalıyor

---

## 6. Ajan #5 — Sadakat/Müşteri Ödül Bot

**Ne yapıyor?**
Müşteri puan sorguluyor → AI bot puan durumunu söylüyor → Yeni ödül/ kampanya bildirimi gönderiyor → VIP müşterilere özel teklifler

**Workflow:**
```
Puan sorgusu → Mevcut puan + yetersizse kaç puan gerektiği → 
Yeni kampanya bildirimi → VIP müşteriye özel indirim → Doğum günü tebriği
```

**Kimler için:**
- Restaurant/zincir mağazalar
- E-ticaret markaları
- Kuaför/güzellik salonları
- Seyahat şirketleri

**Metrik:** Tekrar satın alma oranı %25 artış

---

## 7. Teknik Altyapı — n8n + Claude Code

**Entegrasyon:**
```
WhatsApp Business API → n8n → Claude Code → Yanıt Üretimi → WhatsApp
                              ↓
                        Stok/Sipariş/Randevu API'leri
```

**Gerekli araçlar:**
- WhatsApp Business API (Cloud API)
- n8n (workflow otomasyonu)
- Claude Code / Claude API
- Entegre edilecek iş sistemleri (stok, sipariş, randevu)

**Kullanıcının avantajı:** n8n + Claude Code + Instagram/WhatsApp API konusunda uzmanlaşmış — bu ajanları kurmak için ideal konumda.

---

## 8. LinkedIn Post Fikri

**Başlık:** WhatsApp İçin 5 AI Ajanı Fikri — E-ticaret, Restoran ve Hizmet Sektörü İçin

**Hook:** Herkes büyük AI ajanlardan bahsediyor. Ama küçük işletmeler için en değerli ajanlar sade ve spesifik.

**İçerik:**
WhatsApp Business API + AI ajanları ile yapılabilecek 5 şey:

1. **Sipariş Bot** — WhatsApp'tan direkt sipariş, +40% dönüşüm
2. **Randevu Hatırlatıcı** — No-show oranı %60 düşüyor
3. **Sepet Terk Bot** — E-ticaret için en yüksek ROI, +%10-15 dönüşüm
4. **Kargo Takip Bot** — Destek talebi %70 azalır
5. **Sadakat Bot** — Tekrar satın alma %25 artar

En önemli keşif: Türkiye'de WhatsApp açılma oranı %70+. E-posta kampanyalarından 10x daha etkili.

Siz hangi ajanı kurmak istersiniz?

#WhatsAppBusiness #AIBot #Ecommerce #Automation #n8n

**Görsel Önerisi:** 5 madde listesi olan carousel veya tek görselde 5 ajan ikonu

---

## 9. Kaynaklar

1. [WhatsApp Business Platform - Developers](https://developers.facebook.com/docs/whatsapp/overview)
2. [n8n.io - Workflow Automation](https://n8n.io)
3. [NotFair - Claude Code Meta Ads](https://github.com/nowork-studio/NotFair)
