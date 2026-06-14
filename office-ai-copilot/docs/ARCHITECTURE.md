# 🏗️ Mimari

Bu kit basit ve kasıtlı olarak "ince" bir mimari kullanır: ağır framework yok,
her iş **tek bir Claude çağrısı** etrafında kuruludur. Karmaşık multi-agent
orkestrasyonu yerine "tek görev → tek prompt → yapılandırılmış çıktı" yaklaşımı.

---

## Genel Akış

```
                    ┌─────────────────────────────┐
   Tetikleyici  →   │  Veriyi hazırla (kaynak)     │
 (mail/zaman/      └──────────────┬──────────────┘
  webhook/CLI)                    │
                                  ▼
                    ┌─────────────────────────────┐
                    │  Claude API (system prompt) │   prompts/ klasöründen
                    │  Haiku = ucuz işler         │
                    │  Sonnet = kaliteli işler    │
                    └──────────────┬──────────────┘
                                   │  yapılandırılmış JSON / Markdown
                                   ▼
                    ┌─────────────────────────────┐
                    │  Çıktıyı yönlendir           │
                    │  (Sheets / mail / taslak /   │
                    │   takvim / kullanıcı)        │
                    └─────────────────────────────┘
```

---

## 5 İşin Akışı

| # | İş            | Tetik          | Model  | Kaynak → Hedef                          |
|---|---------------|----------------|--------|------------------------------------------|
| 1 | Email triyaj  | Gmail (yeni)   | Haiku  | Gmail → öncelik + Gmail taslak           |
| 2 | Toplantı notu | Webhook/dosya  | Sonnet | Transkript → Sheets (action items)       |
| 3 | Haftalık rapor| Zaman (Cuma)   | Sonnet | Sheets → mail                            |
| 4 | Dosya bulucu  | Webhook/bot    | Haiku  | Doğal dil → Drive arama → link           |
| 5 | Takvim ajanı  | Gmail (yeni)   | Haiku  | Mail thread → Calendar daveti            |

---

## Tek Kaynak: `prompts/`

Hem n8n workflow'ları hem Python scriptleri **aynı mantıksal system prompt'ları**
kullanır. `prompts/*.md` insan-okunabilir kaynaktır:
- **Python** bu dosyaları doğrudan okur (`claude_client.load_prompt`).
- **n8n** workflow JSON'larına gömülü prompt taşır (n8n tek dosya import edilebilsin diye).
  Prompt'u değiştirirsen iki yeri de güncelle (veya n8n'de bir "Set" node'una taşı).

---

## Tasarım İlkeleri

1. **Yapılandırılmış çıktı.** Claude'dan hep belirli bir JSON şeması (veya rapor için
   Markdown) isteriz. Bu, çıktıyı kodun güvenle işlemesini sağlar.
2. **Uydurma yok.** Prompt'lar Claude'a bilmediği detayı uydurmamasını, `null`
   bırakmasını söyler. Özellikle tarih/sorumlu/metrik konularında.
3. **İnsan döngüde (geri alınamaz işlerde).** Email gönderme ve takvim daveti
   varsayılan olarak **taslak**tır. `AUTO_SEND` ile açılır ama bilinçli bir tercihtir.
4. **Maliyet bilinci.** Model seçimi işin niteliğine göre — ucuz iş Haiku, kaliteli iş Sonnet.
5. **Bağımsız parçalar.** 5 iş birbirine bağımlı değil; sadece ihtiyacın olanı kur.

---

## Genişletme Fikirleri

- **Slack/Telegram bot** → dosya bulucu ve triyaj için arayüz.
- **Vektör arama** → dosya bulucuyu içerik-tabanlı semantik aramaya çevir.
- **Prompt caching** → uzun system prompt'larda girdi maliyetini düşür.
- **Onay adımı** → kritik mail/davetlerde Slack üzerinden tek tık onay.
- **Çoklu kullanıcı** → her kullanıcı için ayrı credential + Sheets sekmesi.

---

> Bu mimari kasıtlı olarak sade. Daha karmaşık ihtiyaçlar (durum yönetimi, uzun
> süreli ajanlar, araç kullanımı) için Claude'un tool use / agent SDK'sına geçebilirsin —
> ama çoğu ofis otomasyonu için tek-çağrı yaklaşımı yeterli ve ucuzdur.
