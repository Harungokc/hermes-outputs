"""
4) Dosya Bulucu — doğal dil tarifini Drive aramasına çevir.

Kullanım:
  python src/file_finder.py "geçen ayki bütçe sunumu"

İki adım:
  1) Claude (Haiku) tarifi yapılandırılmış sorguya çevirir.
  2) Bu sorgu Google Drive API'sine çevrilir, sonuçlar link olarak döner.

Adım 2'nin gerçek Drive entegrasyonu docs/SETUP.md'de. Burada Claude'un
ürettiği yapılandırılmış sorguyu gösteriyoruz + Drive sorgu dizesini kuruyoruz.
"""

import argparse

from claude_client import ask_json


def parse_query(natural_query: str) -> dict:
    """Doğal dil tarifini yapılandırılmış arama sorgusuna çevirir."""
    return ask_json("file_finder", natural_query)


def build_drive_query(parsed: dict) -> str:
    """Yapılandırılmış sorgudan Google Drive `q` parametresi üretir.

    Drive API sorgu dili: https://developers.google.com/drive/api/guides/search-files
    """
    clauses = []
    for kw in parsed.get("keywords", []):
        clauses.append(f"fullText contains '{kw}'")

    mime_map = {
        "presentation": "application/vnd.google-apps.presentation",
        "spreadsheet": "application/vnd.google-apps.spreadsheet",
        "document": "application/vnd.google-apps.document",
        "pdf": "application/pdf",
    }
    if parsed.get("mime_hint") in mime_map:
        clauses.append(f"mimeType = '{mime_map[parsed['mime_hint']]}'")

    return " and ".join(clauses) if clauses else ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Doğal dil dosya bulucu")
    parser.add_argument("query", help="Aradığın dosyayı tarif et (tırnak içinde)")
    args = parser.parse_args()

    parsed = parse_query(args.query)
    print("\n🔍 Anlaşılan sorgu:")
    print(f"  Anahtar kelimeler: {parsed.get('keywords')}")
    print(f"  Dosya tipi ipucu : {parsed.get('mime_hint')}")
    print(f"  Sahip ipucu      : {parsed.get('owner_hint')}")
    print(f"  Tarih ipucu      : {parsed.get('date_hint')}")

    drive_q = build_drive_query(parsed)
    print(f"\n🗂️  Drive sorgu dizesi:\n  {drive_q or '(boş)'}")
    print("\nℹ️  Bu sorguyu Drive API'ye gönder (docs/SETUP.md). Sonuçlar link olarak döner.")


if __name__ == "__main__":
    main()
