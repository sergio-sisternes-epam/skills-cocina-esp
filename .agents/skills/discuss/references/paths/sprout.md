---
name: discuss/paths/sprout
description: Park anything still pending as a protostar linked to the originating conversation node. Load before executing.
path_id: sprout
---

# Path: sprout

## When

A refine, question, counter, probe, tension, or later action is still pending at the end of a turn. Live discuss and from-conversation both park through this path. Do not invent a second filing habit.

## Enter

Discuss card plus:

```text
path: sprout
path_module: references/paths/sprout.md
origin_node: <atlas-relative page that originated the pending>
```

If `origin_node` is missing, use `current_branch`, then `discussion_root`. Never create a protostar with no origin edge.

## Procedure

1. **Still pending?** If the item died in this turn (answered, dropped, typo), leave it as a batch line on the parent. No page.
2. **Not every utterance.** One protostar per surviving pending. Flood is forbidden.
3. **Write the protostar** beside the origin node (same folder as that page, or the work-hub folder). Never create a `residuals/` bucket.
   - `type: protostar`
   - `status: open`
   - `kva: forming`
   - `growth: true`
   - `star_kind: refine | question | counter | probe | tension | action`
   - `work_id` of the source work when one exists
   - `relates_to` origin with `kind: derived_from` (add `follows` if it also continues that thread)
   - `relates_to` the work hub (`work/<work_id>.md` or `autogenesis/work/<work_id>.md`) with `kind: implements` when `work_id` exists
4. **KVA at birth.** Default `forming`. Exit ramps use the SKILL final-node rule, not this path.
5. **No protostar hub.** Required edges are origin_node (`derived_from`) and, when `work_id` exists, the work hub (`implements`). A folder index may list the file. A concept catalog that every star points at is forbidden.
6. **No implement authority.** `star_kind: action` is lineage of a later do-something. It does not start Autogenesis implement.
7. **Compile green.**

## Non-goals

- Todo app
- Leaf per sentence
- Orphan protostars
- Implementing because a protostar exists
