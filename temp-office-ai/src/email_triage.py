"""
1) Email Triyaj — gelen email'i oku, öncelik ver, taslak cevap öner.

Kullanım:
  echo "email metni" | python src/email_triage.py
  python src/email_triage.py --file ornek_email.txt

Gerçek Gmail entegrasyonu için fetch_unread() fonksiyonunu doldur
(docs/SETUP.md → Google API). Bu script demo amaçlı stdin/dosya okur.
"""

import argparse
import sys

from claude_client import ask_json


def triage(email_text: str) -> dict:
    """Bir email metnini triyajdan geçirir."""
    return ask_json("email_triage", email_text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Email triyaj asistanı")
    parser.add_argument("--file", help="Email metnini içeren dosya yolu")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            email_text = f.read()
    else:
        email_text = sys.stdin.read()

    if not email_text.strip():
        print("Hata: email metni boş. stdin veya --file ile metin ver.", file=sys.stderr)
        sys.exit(1)

    result = triage(email_text)

    print(f"\n📧 Öncelik : {result['priority']}")
    print(f"🏷️  Kategori: {result['category']}")
    print(f"📝 Özet    : {result['summary']}")
    if result.get("needs_reply") and result.get("draft_reply"):
        print("\n✍️  Taslak Cevap:\n" + "-" * 40)
        print(result["draft_reply"])
        print("-" * 40)
        print("\n⚠️  Bu bir TASLAKTIR. Gözden geçirip sen gönder.")
    else:
        print("\nℹ️  Cevap gerektirmiyor.")


if __name__ == "__main__":
    main()
