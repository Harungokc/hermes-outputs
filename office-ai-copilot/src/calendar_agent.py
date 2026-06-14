"""
5) Takvim Ajanı — mail thread'inden takvim daveti çıkar.

Kullanım:
  python src/calendar_agent.py --file thread.txt

Geri alınamaz işlem (davet gönderme) olduğu için:
  - Claude `confident: false` derse, etkinlik OLUŞTURULMAZ.
  - AUTO_SEND=false (varsayılan) ise davet TASLAK olarak gösterilir, sen onaylarsın.
"""

import argparse
import os
import sys

from claude_client import ask_json

TIMEZONE = os.getenv("TIMEZONE", "Europe/Istanbul")
AUTO_SEND = os.getenv("AUTO_SEND", "false").lower() == "true"


def extract_event(thread_text: str) -> dict:
    """Mail thread'inden takvim etkinliği çıkarır.

    Kullanıcının saat dilimini mesaja ekliyoruz ki Claude varsayımını ona göre yapsın.
    """
    content = f"Kullanıcının saat dilimi: {TIMEZONE}\n\n--- Mail thread ---\n{thread_text}"
    return ask_json("calendar_agent", content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Mail thread → takvim daveti")
    parser.add_argument("--file", help="Mail thread dosyası")
    args = parser.parse_args()

    thread = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    if not thread.strip():
        print("Hata: thread boş.", file=sys.stderr)
        sys.exit(1)

    event = extract_event(thread)

    if not event.get("confident"):
        print("\n🤔 Net bir tarih/saat çıkaramadım. Lütfen netleştir.")
        print("   (Claude tahmin yürütmedi — yanlış davet oluşturmaktansa sormayı tercih etti.)")
        sys.exit(0)

    print("\n📅 Önerilen Etkinlik (TASLAK):")
    print(f"  Başlık     : {event['title']}")
    print(f"  Başlangıç  : {event['start']} ({TIMEZONE})")
    print(f"  Bitiş      : {event['end']}")
    print(f"  Katılımcılar: {', '.join(event.get('attendees', [])) or '—'}")
    print(f"  Yer        : {event.get('location') or '—'}")
    print(f"  Not        : {event.get('notes') or '—'}")

    if AUTO_SEND:
        print("\n⚙️  AUTO_SEND=true — Calendar API ile davet oluşturuluyor...")
        # TODO: Google Calendar API ile events.insert çağrısı (docs/SETUP.md).
    else:
        print("\n⚠️  Bu bir TASLAKTIR. Onaylamak için Calendar'a sen ekle "
              "veya .env'de AUTO_SEND=true yap.")


if __name__ == "__main__":
    main()
