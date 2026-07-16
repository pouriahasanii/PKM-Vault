from __future__ import annotations

import argparse
import hashlib
import shutil
from datetime import datetime
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(source: Path, body: str) -> str:
    if body.startswith("---\n"):
        return body
    created = datetime.fromtimestamp(source.stat().st_mtime).isoformat(timespec="seconds")
    return (
        "---\n"
        f"id: import-{digest(source)[:12]}\n"
        "type: imported-note\n"
        "status: inbox\n"
        f"created: {created}\n"
        f"source: migration\n"
        f"original_path: \"{source.as_posix()}\"\n"
        "tags: [inbox, imported]\n"
        "summary_level: 0\n"
        "---\n\n"
        + body
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Safely stage Markdown files for PKM migration")
    parser.add_argument("source", type=Path)
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()

    destination = args.vault / "00 Inbox" / "Imports" / datetime.now().strftime("%Y-%m-%d")
    destination.mkdir(parents=True, exist_ok=True)
    seen = {digest(path) for path in destination.rglob("*.md")}

    imported = skipped = 0
    for source in args.source.rglob("*.md"):
        fingerprint = digest(source)
        if fingerprint in seen:
            skipped += 1
            continue
        target = destination / source.name
        counter = 2
        while target.exists():
            target = destination / f"{source.stem}-{counter}{source.suffix}"
            counter += 1
        target.write_text(frontmatter(source, source.read_text(encoding="utf-8-sig")), encoding="utf-8")
        seen.add(fingerprint)
        imported += 1

    print(f"Imported: {imported}; duplicate content skipped: {skipped}; destination: {destination}")


if __name__ == "__main__":
    main()
