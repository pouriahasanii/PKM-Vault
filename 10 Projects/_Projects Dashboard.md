---
id: projects-dashboard
type: dashboard
status: active
tags: [system, project]
---

# Projects Dashboard

```dataview
TABLE status, outcome, next_action
FROM "10 Projects"
WHERE type = "project" AND status != "archived"
SORT file.name ASC
```

```clojure
{{query (and (property type project) (not (property status archived)))}}
```
