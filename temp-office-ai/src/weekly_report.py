"""
3) Haftalık Rapor — haftanın ham verisini okunabilir rapora çevir.

Kullanım:
  python src/weekly_report.py --file hafta_verisi.txt

Tipik akış: Google Sheets'ten haftanın satırlarını çek → Claude'a ver →
rapor üret → REPORT_RECIPIENT_EMAIL'e gönder. Sheets okuma ve mail gönderme
iskeleti docs/SETUP.md'de; burada metin girdisiyle çalışır.
"""

import argparse
import sys

from claude_client import ask


def build_report(week_data: str) -> str:
    """Ham haftalık veriyi Markdown rapora çevirir (Sonnet)."""
    return ask("weekly_report", week_data, smart=True, max_tokens=3000)


def main() -> None:
    parser = argparse.ArgumentParser(description="Haftalık rapor üretici")
    parser.add_argument("--file", help="Hafta verisini içeren dosya")
    args = parser.parse_args()

    data = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    if not data.strip():
        print("Hata: hafta verisi boş.", file=sys.stderr)
        sys.exit(1)

    report = build_report(data)
    print(report)

    # TODO: AUTO_SEND=true ve REPORT_RECIPIENT_EMAIL verilmişse Gmail ile gönder.
    #       Varsayılan: ekrana basar, sen kopyalayıp gönderirsin.


if __name__ == "__main__":
    main()
