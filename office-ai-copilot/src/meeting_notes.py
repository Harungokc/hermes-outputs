"""
2) Toplantı Notu — transkripti özet + action item'lara çevir.

Kullanım:
  python src/meeting_notes.py --file transkript.txt
  cat transkript.txt | python src/meeting_notes.py

Çıktı: ekrana yazılır + (GOOGLE_SHEET_ID verilmişse) Sheets'e satır eklenir.
Sheets entegrasyonu docs/SETUP.md'de anlatılır; burada iskelet bırakıldı.
"""

import argparse
import sys

from claude_client import ask_json


def summarize(transcript: str) -> dict:
    """Transkripti yapılandırılmış toplantı notuna çevirir (Sonnet)."""
    return ask_json("meeting_notes", transcript, smart=True, max_tokens=3000)


def main() -> None:
    parser = argparse.ArgumentParser(description="Toplantı notu özetleyici")
    parser.add_argument("--file", help="Transkript dosyası")
    args = parser.parse_args()

    transcript = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    if not transcript.strip():
        print("Hata: transkript boş.", file=sys.stderr)
        sys.exit(1)

    notes = summarize(transcript)

    print(f"\n📋 {notes['title']}\n" + "=" * 50)
    print("\n📌 Özet:")
    for item in notes["summary"]:
        print(f"  • {item}")
    if notes.get("decisions"):
        print("\n✅ Kararlar:")
        for d in notes["decisions"]:
            print(f"  • {d}")
    print("\n🎯 Action Items:")
    for a in notes["action_items"]:
        owner = a.get("owner") or "—"
        due = a.get("due") or "—"
        print(f"  • {a['task']}  (sorumlu: {owner}, tarih: {due})")

    # TODO: GOOGLE_SHEET_ID verilmişse her action item'ı Sheets'e satır olarak ekle.
    #       Bkz. docs/SETUP.md → "Sheets'e yazma".


if __name__ == "__main__":
    main()
