---
name: discuss/paths/lint
description: Check discussion fabric for discipline breaks. L1 hubs; L2–L6 KVA contract. Load before executing.
path_id: lint
---

# Path: lint

## When

After a sprout or from-conversation pass, or when the user asks to lint the discussion graph.

## Enter

```text
path: lint
path_module: references/paths/lint.md
atlas_root: <store>
```

## Rules

### L1 — no hub files

A **hub file** is a concept page used as a connector across disconnected topics: many nodes (especially protostars) `relates_to` it even though they do not share that page as their originating conversation.

Forbidden: catalog / rim / “all protostars live here” pages.

Allowed:

- reserved `index.md` and `log.md` (file lists, not fabric)
- an exit stub (`kva: terminated|deprecated|superseded`) with **no new inbound** from protostars except `derived_from` reactivation children
- a real origin node that several children of **the same conversation** point at
- a final-reason document that several subjects of **the same exit event** point at with `kva_*` kinds
- a page with `consolidation: true` (partial dated consolidate view). Protostar `indexes` / `defers` / other stance inbound does not make it a hub.

Pass: every protostar’s required edge is its origin conversation node, not a shared rim catalog.

A page that several protostars `derived_from` because it *is* their origin is not a hub. A page that three or more protostars attach to without that origin edge is a hub.

### L2 — kva enum

If `kva` is present it must be one of: `forming`, `alive`, `deprecated`, `superseded`, `terminated`.

### L3 — protostar requires kva

Every `type: protostar` page must have `kva`.

### L4 — exit edge

`deprecated` | `superseded` | `terminated` must have exactly one matching edge:

- `kva_deprecate` | `kva_supersede` | `kva_terminate`
- target page `kva_role: exit-reason` and `kva: alive`

### L5 — growth match

`growth: true` only when `kva: forming`.

### L6 — exit stubs

`terminated` | `deprecated` | `superseded` pages must not collect new protostar inbound except `derived_from` reactivation children.

## Procedure

1. Load this module.
2. Run `python3 <discuss>/scripts/lint.py --root <atlas_root>`.
3. If a rule fails, list the pages. Do not “fix” L1 by adding another hub.
4. Fix, then lint again.
5. Record pass/fail on the work or a short experience if the lint was requested as its own turn.

## Non-goals

- Inventing more rules in this file without a new design
- Treating compile as lint (compile is structure; lint is discussion discipline)
