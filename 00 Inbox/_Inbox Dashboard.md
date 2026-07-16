---
id: inbox-dashboard
type: dashboard
status: active
tags: [system, inbox]
---

# Inbox Dashboard

Everything enters here before classification.

## Obsidian Dataview

```dataview
TABLE source, content_type, created
FROM "00 Inbox"
WHERE file.name != "_Inbox Dashboard"
SORT created ASC
```

## Logseq query

```clojure
{{query (and (property status inbox) (not (page "Inbox Dashboard")))}}
```
