# WhatsApp Business API — Toplu Mesaj ve Otomasyon Durumu

## 2026-06-19 İtibarıyla Durum

### Template Message Zorunluluğu
WhatsApp Business API'de toplu mesaj göndermek için **onaylı template** şart. Template'lar:
- Müşteri adına kişiselleştirilebilir (ad, sipariş no, ürün adı)
- 72 saat içinde yanıt alınmayan konuşmalarda zorunlu
- Her template için ayrı onay gerekiyor (Meta tarafından inceleniyor)

### 72 Saat Kuralı — En Kritik Kısıtlama
Müşteriyle son mesajlaşmadan **72 saat sonra** serbest mesaj gönderilemez. Bu süre geçtikten sonra:
- Ya template kullanılacak
- Ya da müşterinin bot'a kendisi mesaj atması beklenilecek

**Pratik uygulama:** n8n ile otomatik takip mesajları planlanırken 72 saat kuralı kritik. Abandoned cart hatırlatması 1sa, 24sa, 72sa şeklinde gönderilmeli.

### Kişiselleştirilmiş Toplu Mesaj
Her mesajı müşteriye özel göndermek mümkün:
```
Ahmet Bey, #2453 numaralı siparişiniz kargoya verildi → [kargo takip]
```
Bunun için:
- n8n + Claude + WhatsApp Business API entegrasyonu
- Her mesaj ayrı API çağrısı (toplu değil, sıralı)
- Gönderim hızı: ~60 mesaj/dakika (WhatsApp limit)

## GitHub Toplu Mesaj Repoları

| Repo | ⭐ | Platform | Not |
|------|----|---------|-----|
| nikhilmuz/WhatsApp-Bulk-Sender | 284 | Android/Web | Açık kaynak |
| SaeidJavadi/Advanced-WhatsApp-Sender | 213 | Web | Görsel desteği |
| mubashir-786/n8n-whatsapp-automation | 106 | n8n | Sipariş otomasyonu |
| DarshanParbadiya/WhatsApp-Automation | 55 | Web | Kişi listesi |

## En İyi Uygulama — Sepet Terk Önleme

```
1. saat:  "Sepetinizde unuttuğunuz ürünler var!"
24. saat: "Bugün özel %10 indirim kodu"
72. saat: "Son şans! Sepetinizdeki ürünler 2 gün içinde silinecek"
```

Bu zincir WhatsApp'ta %85 açılma oranıyla email'in 10 katı etkili.

## Herkesin Kaçırdığı Nokta
**"Toplu mesaj = spam" algısı yanlış.** Kişiselleştirilmiş, değer veren, zamanında gönderilen mesajlar spam değil — müşteri hizmeti. Türk işletmelerinin %90'ı bunu karıştırıyor ve WhatsApp'ın sunduğu yüksek etkileşim oranından yararlanamıyor.

## Türkiye İçin Kullanım Alanları
1. **E-ticaret:** Sepet hatırlatma, kargo takip, iade süreci
2. **Randevu:** Kuaför, dişçi, araç servisi — otomatik hatırlatma
3. **Restoran:** Sipariş teyidi, özel gün tebrikleri
4. **Otel:** Check-in hatırlatma, concierge hizmeti

## Kaynaklar
- https://business.whatsapp.com/developers/developer-hub
- https://developers.facebook.com/docs/whatsapp
