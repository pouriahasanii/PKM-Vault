---
id: zettelkasten-dashboard
type: dashboard
status: active
tags: [system, zettelkasten]
---

# Zettelkasten Dashboard

Permanent notes are atomic, written in your own words, and linked to at least one hub or related note.

```dataview
TABLE created, maturity, related
FROM "40 Zettelkasten"
WHERE type = "permanent-note"
SORT created DESC
```
