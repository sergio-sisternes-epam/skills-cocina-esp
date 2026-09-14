---
name: discuss/paths/consolidate
description: Write a partial dated consolidate view over an existing discussion graph. Stance edges name what the snapshot does to each idea. Informal name: walk-back. Load before executing.
path_id: consolidate
---

# Path: consolidate

Informal name: **walk-back**. Formal `path_id`: **consolidate**.

## When

The user asks to consolidate, walk back the graph, draw a picture of the pieces, or list gaps and contradictions. Also when Autogenesis discussion explicitly requests a picture.

If the user asked for a constellation or a checkpoint, enter path **constellation** instead of this one. Constellation already loads this file for the view contract; do not bounce back here to change path.

Not the default live loop. Not a substitute for `from-conversation` (ingest) or `lint` (discipline).

## Enter

Discuss card plus:

```text
path: consolidate
path_module: references/paths/consolidate.md
discussion_root: <existing hub>
view_page: <slug>/consolidate-YYYY-MM-DD-<slug>.md
prior_view: <optional earlier consolidate page>
```

## Page contract

- `type: document`
- `consolidation: true`
- `kva: alive`
- `reality: current`
- Filename `consolidate-YYYY-MM-DD-<slug>.md` under the discussion folder
- New file per consolidate unless the user names an existing file to refresh

A view is a **partial, dated stance** over the graph. Several views may exist on one `discussion_root`. Later views `derived_from` and `feeds` from earlier views.

## Stance vocabulary (view → idea)

KVA on the idea page is unchanged. A refute does not terminate.

| Kind | This snapshot… |
|------|----------------|
| `confirms` | takes the idea as standing here |
| `refutes` | rejects it here; page remains |
| `expands` | grows or re-scopes it |
| `restates` | same claim, tighter wording |
| `indexes` | points at it, no truth claim (default for protostar gaps) |
| `defers` | known, out of this snapshot |
| `absorbs` | folds it into another idea named on this view |
| `feeds` | this view is input to a later view (view → view) |

Do not use `records` as a fake `confirms`. Idea↔idea kinds stay `follows`, `related`, `derived_from`, `records`, `contradicts`, `counters`, `backed_by`, `refuted_by`, KVA ramps.

## Procedure

1. Query the hub, existing consolidate views, and pages with `kva` set.
2. Write the view body: picture, confirmed, refuted, expanded, deferred, gaps, contradictions.
3. Put stance edges **on the view**. Every idea mentioned in the body gets one stance kind.
4. Protostars: `indexes` or `defers` only. Their `derived_from` origin stays the real conversation node.
5. If `prior_view` exists, add `derived_from` that page and `feeds` from prior → this view (prior page gains a `feeds` edge, or this page notes the feed in body and `derived_from` prior).
6. Also `derived_from` the hub and `implements` the work hub when one exists.
7. Set `current_branch` to this view.
8. `atlas compile` then discuss `lint`. A `consolidation: true` page is not an L1 hub.
9. In chat, name what was confirmed / refuted / expanded / deferred. Offer one contradiction or one gap cluster.

## Non-goals

- Overwriting the only view on every call
- Flattening contradictions into one current reality
- Deleting or KVA-exiting an idea because this snapshot refuted it
- Running this path every discuss turn
