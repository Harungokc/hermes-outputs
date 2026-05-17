# AI Günlük Haberleri

## Yapı

- `YYYY-MM-DD-gunluk.md` - Günlük özetler
- `raw/` - Ham veriler (saatlik toplanan)
- `stanford/` - Stanford video analizleri

## Aktif Cron Jobs

1. **Her saat başı (00:00):** Kaynak tarama ve veri toplama
   - Job ID: d64cb45723f7
   - 24 kez tekrarla (günlük döngü)

2. **Her gün 09:00:** Günlük özet oluşturma ve Telegram
   - Job ID: d5d9b3d65c6c
   - Süresiz

## İçerik Formatı

Her haber için:
- Başlık
- Özet (1-2 cümle)
- "Herkesin kaçırdığı ilginç nokta"
- LinkedIn post formatı
- Kaynak linki
- Görsel önerisi

## Kaynaklar

### YouTube
- Nate Herk: youtube.com/@nateherk
- Matt Wolfe: youtube.com/@mreflow
- Wes Roth: youtube.com/@WesRoth
- Stanford Online: youtube.com/@StanfordOnline

### LinkedIn
- Pascal Bornet
- Andrew Ng
- Andrej Karpathy
- Allie K. Miller

### Google
- "AI agent news today"
- "AI automation news today"