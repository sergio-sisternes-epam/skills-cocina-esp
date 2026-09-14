---
name: discuss/paths/speak
description: Always-on prefix path. Load before any human-facing discuss reply. Owns sentence shape. Not a public mode.
path_id: speak
---

# Path: speak

Mandatory prefix. Discuss has not entered until this file and `references/human-turn.md` are loaded.

## When

Every discuss activation. Live loop, getting-started, help, from-conversation, sprout, terminate, lint, consolidate, and constellation all go through speak first when the next output is for a human.

## Enter

Discuss card plus:

```text
path: speak
path_module: references/paths/speak.md
speak_loaded: yes
```

Missing load ⇒ `incomplete: missing speak`. The activation card must include `speak_loaded: yes`.

## Procedure

1. Load `references/human-turn.md`.
2. Shape the human reply using that file. Filing the Atlas is separate work.
3. Do not replace the reply with an activation card or a path table.

## Non-goals

- Not a third discussion mode.
- Does not write Atlas pages.
- Does not replace sprout, terminate, or lint.
- Cannot compile-check stacked sentences. That remains a later test.
