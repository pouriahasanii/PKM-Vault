from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r"\b\d{8,12}:[A-Za-z0-9_-]{30,}\b")


def main() -> None:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8-sig")
        if TOKEN.search(text):
            errors.append(f"Possible Telegram token: {path.relative_to(ROOT)}")
        match = re.search(r"^id:\s*[\"']?([^\n\"']+)", text, re.MULTILINE)
        if match:
            note_id = match.group(1).strip()
            if note_id in ids:
                errors.append(f"Duplicate id {note_id}: {ids[note_id]} and {path}")
            ids[note_id] = path
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Vault validation passed: {len(ids)} unique note IDs")


if __name__ == "__main__":
    main()
