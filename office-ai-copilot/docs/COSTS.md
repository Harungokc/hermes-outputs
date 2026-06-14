# 💰 Maliyet Dökümü

Şeffaf olalım: bu kitin tek değişken maliyeti **Claude API**. n8n self-hosted
ücretsiz, Google Workspace zaten var.

---

## Claude API Fiyatları (1M token başına)

| Model              | Girdi  | Çıktı  | Ne için kullanılıyor                  |
|--------------------|--------|--------|----------------------------------------|
| **Haiku 4.5**      | $1     | $5     | Email triyaj, dosya sorgusu, takvim çıkarımı (yüksek hacim, ucuz) |
| **Sonnet 4.6**     | $3     | $15    | Toplantı özeti, haftalık rapor (kalite)|

> Fiyatlar Anthropic'in resmi listesinden (Haziran 2026). Güncel için:
> [anthropic.com/pricing](https://www.anthropic.com/pricing).

---

## Gerçekçi Aylık Senaryo

Orta yoğunlukta bir ofis çalışanı için kabaca hesap:

| İş                  | Hacim/ay     | Model   | ~Token/iş | ~Aylık maliyet |
|---------------------|--------------|---------|-----------|----------------|
| Email triyaj        | 600 mail     | Haiku   | ~1.5K     | ~$3            |
| Toplantı özeti      | 20 toplantı  | Sonnet  | ~8K       | ~$3            |
| Haftalık rapor      | 4 rapor      | Sonnet  | ~10K      | ~$1            |
| Dosya arama         | 100 sorgu    | Haiku   | ~0.5K     | ~$0.50         |
| Takvim çıkarımı     | 60 mail      | Haiku   | ~1K       | ~$0.50         |
| **Toplam**          |              |         |           | **~$8-12/ay**  |

Yoğun kullanımda (3-5x hacim) bile **~$30-50/ay** bandında kalır.

---

## Tasarruf Hesabı

```
Kazanılan zaman : haftada ~10 saat
Yıllık          : ~500 saat
Maliyet         : ~$10-50/ay  →  yılda ~$120-600

500 saat × (senin saatlik değerin) >>> $600
```

İşçilik maliyeti tarafında geri dönüş genelde **ilk haftada** kapanır.

---

## Maliyeti Düşürme İpuçları

1. **Doğru modeli seç.** Sınıflandırma/çıkarım işlerini Haiku'da tut; sadece
   gerçekten yazım kalitesi gereken işler (rapor, özet) Sonnet'e gitsin.
   `.env` içindeki `MODEL_FAST` / `MODEL_SMART` ile kontrol edersin.
2. **`max_tokens`'ı abartma.** Triyaj için 1500, rapor için 3000 yeterli.
3. **Prompt caching.** Aynı uzun system prompt'u tekrar tekrar gönderiyorsan
   Anthropic prompt caching ile girdi maliyetini ~%90 düşürebilirsin (ileri seviye).
4. **Batch API.** Acil olmayan toplu işlerde (ör. gecelik 100 mail triyajı)
   Batches API %50 indirim sağlar.

---

> Not: Rakamlar tahminidir; gerçek kullanımın token hacmine bağlıdır. İlk ay
> Anthropic konsolundan gerçek tüketimini izle, modeli ona göre ayarla.
