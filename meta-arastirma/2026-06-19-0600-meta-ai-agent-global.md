# Meta AI Business Agent — Küresel Lansman ve Fiyatlandırma — 2026-06-19 06:00

## Özet Tablo

| Plan | Fiyat | Mesaj Başı | Hedef Kullanıcı |
|------|-------|------------|-----------------|
| Meta One (WhatsApp) | $7.99/ay | — | Bireysel işletme |
| Business Basic | $0.01/mesaj | $0.01 | Küçük işletme |
| Business Pro | $0.05/mesaj | $0.05 | Orta-büyük işletme |
| Enterprise | Custom | Custom | Büyük şirketler |

---

## Meta Business Agent Nedir?

Meta'nın AI Business Agent'ı, WhatsApp, Instagram ve Messenger'da çalışan 7/24 AI müşteri asistanı. İşletmelerin:
- Müşteri sorularını otomatik yanıtlama
- Sipariş takibi
- Ürün sorgulama
- Randevu rezervasyonu
- Satış sonrası destek

...tümünü AI ile yönetmesini sağlıyor.

---

## Küresel Lansman — Neden Şimdi?

**Arka plan:** Meta, 2025 sonlarında pilot program başlattı. İlk olarak Hindistan ve Brezilya'da test edildi. Şimdi (Haziran 2026) 150+ ülkede resmi olarak kullanıma açıldı.

**Türkiye dahil mi?** Evet — Business API erişimi olan tüm ülkelerde kullanılabilir durumda.

---

## Herkesin Kaçırdığı Nokta #1 — Asıl Gelir Kaynağı Mesaj Başı Değil

Herkes "$0.01/mesaj" rakamına odaklanıyor. Ama Meta'nın asıl hedefi:

**Veri.** Her AI agent etkileşiminden müşteri davranışı, tercih, satın alma pattern'i toplanıyor. Bu veri:
- Meta'nın reklam hedefleme motorunu güçlendirir
- Advantage+ kampanyalarını daha "akıllı" yapar
- Meta'nın reklam gelirini artırır (dolaylı)

Yani işletme $0.01/mesaj öderken, Meta $0.10-1.00 değerinde veri kazanıyor.

---

## Herkesin Kaçırdığı Nokta #2 — "Agent" mı Yoksa "Bot" mu?

Meta bunu "AI Business Agent" olarak pazarlıyor. Ama teknik olarak bu bir **LLM-powered FAQ bot** — yani genel soruları yanıtlıyor, karmaşık karar süreçlerini yönetemiyor.

**Fark:**
- Agent = otonom karar alır, eylem yapar (ödeme, sipariş değişikliği, iade başlatma)
- Bot = sorulan soruları yanıtlar, eyleme geçemez

Meta Business Agent şu anda %80 "bot", %20 "agent". Otonom eylem kapasitesi sınırlı.

---

## n8n + Claude Entegrasyonu — Alternatif Çözüm

Meta Business Agent'ın yerine açık kaynak alternatif:

```
[n8n Workflow]
→ WhatsApp Webhook (gelen mesaj)
→ Claude API (yanıt üret)
→ Koşul: "sipariş değişikliği" içeriyor mu?
  → Evet: ERP API çağır, sonucu döndür
  → Hayır: Claude yanıtı döndür
```

**Avantajları:**
- Mesaj başı ücret yok
- Özelleştirme sınırsız
- Kendi verisin üzerinde tam kontrol
- Claude Code ile geliştirme = 10x hız

---

## Türkiye İçin Değerlendirme

| Faktör | Meta Agent | n8n+Claude |
|--------|-----------|------------|
| Kurulum | 1-2 saat | 2-3 gün |
| Maliyet | $0.01/mesaj | Sunucu maliyeti ~$10/ay |
| Özelleştirme | Sınırlı | Sınırsız |
| Veri kontrolü | Meta'da | Kendi sunucunda |
| Türkiye desteği | Var | Yok (self-service) |

**Öneri:** Küçük işletme (günde <500 mesaj) = Meta Agent mantıklı. Büyük işletme veya veri hassasiyeti = n8n+Claude daha avantajlı.

---

## Kaynaklar

- TechCrunch: "Meta's AI agent for WhatsApp Business is now available globally"
- Meta for Business: WhatsApp Business API pricing
- VentureBeat: "Meta enters enterprise AI race with new business agent"

---

## LinkedIn Post Fikri

**Başlık:** Meta AI Agent: $0.01/mesaj mı, Yoksa Verdiğiniz Veri mi Gerçek Bedel?

**Hook:** Herkes "$0.01/mesaj çok ucuz" diyor. Ama Meta'nın asıl kazancı mesaj başı değil — veri.

**İçerik:**
- Meta Business Agent 150+ ülkede kullanıma açıldı
- Fiyat: $0.01-0.05/mesaj
- Asıl değer: Her etkileşimden toplanan müşteri verisi
- Alternatif: n8n + Claude ile aynı işlev, sadece $10/ay

**Görsel:** Meta logosu + para sembolleri + veri akışı görseli

#Meta #AI #WhatsApp #Business #Agent #n8n #Claude
