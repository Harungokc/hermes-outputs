"""
Ortak Claude API yardımcısı.

5 scriptin de kullandığı tek giriş noktası. Prompt'ları `prompts/` klasöründen
okur, Claude'u çağırır, JSON çıktıyı parse eder.

Model seçimi .env'den gelir:
  MODEL_FAST  = claude-haiku-4-5   (triyaj, sınıflandırma, çıkarım — ucuz)
  MODEL_SMART = claude-sonnet-4-6  (özet, rapor — kalite)
"""

import json
import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv()

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"

MODEL_FAST = os.getenv("MODEL_FAST", "claude-haiku-4-5")
MODEL_SMART = os.getenv("MODEL_SMART", "claude-sonnet-4-6")

# anthropic.Anthropic() ANTHROPIC_API_KEY'i ortamdan otomatik okur.
_client = anthropic.Anthropic()


def load_prompt(name: str) -> str:
    """prompts/<name>.md dosyasını system prompt olarak okur.

    Markdown başlık/açıklama satırlarını da içerir — Claude bunları
    yönerge olarak değerlendirir, sorun olmaz.
    """
    path = PROMPTS_DIR / f"{name}.md"
    return path.read_text(encoding="utf-8")


def ask(prompt_name: str, user_content: str, *, smart: bool = False,
        max_tokens: int = 2000) -> str:
    """Claude'a tek seferlik bir istek atar, düz metin döner.

    smart=True -> Sonnet (rapor/özet), aksi halde Haiku (triyaj/çıkarım).
    """
    model = MODEL_SMART if smart else MODEL_FAST
    resp = _client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=load_prompt(prompt_name),
        messages=[{"role": "user", "content": user_content}],
    )
    return next((b.text for b in resp.content if b.type == "text"), "")


def ask_json(prompt_name: str, user_content: str, *, smart: bool = False,
             max_tokens: int = 2000) -> dict:
    """ask() ile aynı, ama çıktıyı JSON olarak parse eder.

    Claude bazen JSON'u ```json ... ``` bloğu içinde döner; onu temizler.
    """
    raw = ask(prompt_name, user_content, smart=smart, max_tokens=max_tokens)
    text = raw.strip()
    if text.startswith("```"):
        # ```json ... ``` veya ``` ... ``` bloğunu soy
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude geçerli JSON dönmedi:\n{raw}") from e
