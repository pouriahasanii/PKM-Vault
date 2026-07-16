# Executive Summary

PKM-Vault is a local-first Markdown knowledge system that combines PARA, Johnny Decimal, Zettelkasten, LATCH, progressive summarization, and atomic-note practice. PARA decides responsibility; numeric areas stabilize paths; Zettelkasten turns reusable ideas into atomic notes; LATCH supplies navigation views; progressive summarization controls reading effort. Obsidian is the primary editor, GitHub is version history, and Logseq is a future block-oriented interface over the same canonical Markdown.

# Detailed Folder/Directory Structure (as a tree diagram in text)

```text
PKM-Vault/
├── 00 Inbox/                 temporary, unclassified captures
│   ├── Imports/              migration staging by date
│   ├── Telegram/
│   ├── Web/
│   ├── Clipboard/
│   └── _Inbox Dashboard.md
├── 10 Projects/              finite outcomes and project hubs
├── 20 Areas/                 ongoing responsibilities
├── 30 Resources/             topic-oriented reference material
├── 40 Zettelkasten/          atomic evergreen notes
├── 50 Visual Lab/            diagram-centric project workspaces
│   └── Projects/<project-id>/
├── 60 Journal/               daily and periodic notes
├── 70 Maps of Content/       curated LATCH navigation
├── 80 Archive/               inactive material
├── 90 System/                templates, scripts, guides, logs
├── assets/                   binary files; excluded from Git
├── logseq/                   Logseq configuration
└── .obsidian/                portable Obsidian configuration
```

# Core Principles and PKM Methodology Explanation

1. **One canonical note:** a concept, project, or area has one authoritative page.
2. **PARA for actionability:** Projects and Areas answer what deserves attention; Resources and Archive prevent inactive material from polluting active work.
3. **Johnny Decimal for durable paths:** decade prefixes remain stable while substructure evolves.
4. **Zettelkasten for synthesis:** valuable source notes produce atomic permanent notes in your own words. Source notes remain evidence; permanent notes become reusable thinking.
5. **LATCH for retrieval:** Maps of Content expose location, alphabet, time, category, and hierarchy without duplicating files.
6. **Progressive summarization:** `summary_level` advances from 0 raw capture, to 1 cleaned, 2 highlighted, 3 executive summary, and 4 evergreen synthesis.
7. **Atomic notes:** one clear claim per permanent note; split rather than accumulate unrelated ideas.
8. **Properties before uncontrolled tags:** `type`, `status`, `project_id`, `area`, `source`, and `maturity` drive workflow. Tags describe cross-cutting themes only.

This combination is superior to a folder-only system because action state, subject, maturity, and source are independent dimensions. A note moves physically only when its responsibility changes; other views are generated from properties and links.

# Logseq Integration Guide

Markdown is canonical. Use ISO dates, UTF-8, simple YAML scalars/lists, stable `id`, and Obsidian-style wiki links. Avoid Dataview inline fields as canonical metadata; they are an Obsidian view layer only.

Namespace conventions:

- `Projects/<project-id>` for project page titles
- `Areas/<area-name>` for responsibility pages
- `Knowledge/<concept>` for permanent notes
- `Sources/<source-type>/<title>` for source notes
- `Journal/YYYY-MM-DD` for daily notes

The `title` property carries the logical namespace even when the physical file uses a readable filename. Shared properties are `id`, `title`, `type`, `status`, `created`, `updated`, `project_id`, `area`, `source`, `source_url`, `tags`, `aliases`, and `maturity`.

Use native Logseq queries for workflow and Dataview only as an Obsidian projection. Example Logseq query:

```clojure
{{query (and (property type project) (property status active))}}
```

Recommended initial Obsidian plugins are Dataview, Templater, QuickAdd, and Excalidraw. Recommended optional Logseq plugins after stabilization are Tabs, Bullet Threading, and Git. Native features remain the baseline so plugin failure cannot make knowledge inaccessible.

# Diagram-Centric Project Workspace Specification

Every visual project uses `50 Visual Lab/Projects/<project-id>/`. The brief declares the question and outcome; the Visual Index links portable Mermaid diagrams plus optional Obsidian Canvas, Excalidraw, and Logseq Whiteboard surfaces; Decisions converts visual exploration into durable text.

The project hub in `10 Projects` and every Visual Lab note share the same `project_id`. Visual artifacts are working surfaces, not the only record. Conclusions become decision-log entries or atomic notes, ensuring ideas discovered visually remain searchable and portable.

# Knowledge Transfer Workflows with Examples

**Existing Markdown:** run `migrate_notes.py D:\OldVault`. Files enter `00 Inbox/Imports/<date>/`, receive stable IDs when missing, and duplicate content is skipped. Review then moves a project plan to `10 Projects`, a responsibility to `20 Areas`, a reference article to `30 Resources`, or a synthesized idea to `40 Zettelkasten`.

Example: `OldVault/AI/Prompting.md` → `00 Inbox/Imports/2026-07-15/Prompting.md` → clean metadata → keep source in `30 Resources/AI/Prompting.md` → extract `40 Zettelkasten/Constraints improve prompt reliability.md` → link both from `70 Maps of Content/AI.md`.

**PDF or image:** binary → `assets/Documents` or `assets/Images`; reference note → `00 Inbox`; after review the note moves to Resources while the binary link remains stable.

**New project:** create project hub from the Project template → assign `project_id` → create matching Visual Lab folder → brainstorm in Mermaid/Canvas/Whiteboard → copy decisions to the project hub → extract reusable insights into Zettelkasten.

**Telegram/Web/Clipboard:** capture to source subfolder in Inbox with `status: inbox`; daily triage applies one of four actions: delete, defer, attach to active project, or process into Resource/Permanent Note.

# Implementation Steps (numbered)

1. Clone the private GitHub repository to `C:\PKM\PKM-Vault`.
2. Copy this package into the clone, preserving `.git` from the clone.
3. Open the folder as an Obsidian Vault and confirm attachment/template paths.
4. Install the minimal Obsidian plugin set and configure QuickAdd capture.
5. Run `validate_vault.py`; inspect GitHub Desktop to ensure `.env` and assets are absent.
6. Commit the architecture as `Initialize PKM architecture v2` and push.
7. Pilot manual capture for one week before enabling Telegram or scheduled processing.
8. Import old notes in dated batches of no more than 100; review each batch before the next.
9. Enable separate encrypted backup for `assets/`.
10. Pilot Logseq read/annotation use after the Obsidian workflow is stable; expand only after a conflict-free test period.

# Potential Risks and Mitigations

- **Simultaneous edits:** Obsidian, Logseq, sync software, and Git can conflict. Use one active editor per note and commit before switching devices.
- **Plugin lock-in:** Dataview, Canvas, and Whiteboards may not render elsewhere. Keep decisions and canonical metadata in Markdown.
- **Secret exposure:** tokens must live in `.env`; validation checks for Telegram-token patterns before commit.
- **Binary repository growth:** assets are Git-ignored and backed up separately.
- **Over-classification:** Inbox triage uses a small controlled vocabulary; tags are not folders.
- **Broken links during migration:** Obsidian automatic link updates remain enabled; migrations stage before final moves.
- **Duplicate notes:** migration uses content hashes and stable IDs; merge intentionally rather than deleting automatically.
- **Logseq format drift:** use a pilot branch/backup, simple properties, ISO dates, and native Markdown before adopting plugin-specific syntax.
