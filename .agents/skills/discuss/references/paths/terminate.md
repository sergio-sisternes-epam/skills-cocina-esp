---
name: discuss/paths/terminate
description: KVA-terminate a wrong discussion frame. Persist the dead branch, write an alive exit-reason node, link it to the living thesis. Load before executing.
path_id: terminate
---

# Path: terminate

## When

The user explicitly kills a frame (“wrong comparison”, “that is not what this is”, “terminate this branch”, “KVA terminate”). The branch was never fit or is out of scope. Not for reshape of an alive page. Not for supersede of a frame that *was* fit.

## Enter

Discuss card plus:

```text
path: terminate
path_module: references/paths/terminate.md
subject_node: <atlas-relative page of the wrong frame>
living_node: <atlas-relative alive vision or correct thesis, or CREATE>
```

If `subject_node` is missing, use `current_branch` only when that node *is* the wrong frame. Do not terminate `discussion_root` by accident.

Trigger must be explicit in the user turn. No silent terminate.

## Procedure

1. **Query first.** Atlas query on `atlas_root`. Read `subject_node`, `discussion_root`, and any living vision / correct-thesis page. Confirm the subject is the frame being killed.
2. **Classify the ramp.**
   - Still useful and in-scope, text is just wrong → reshape the alive page. Stop this path.
   - Was fit; a successor exists → `kva: superseded` + `kva_supersede`. Same artefact shape as terminate; different kind.
   - Never fit or out of scope → continue as terminate.
3. **Living thesis.** If `living_node` is missing, write an alive document that states the corrected frame (vision, comparison, or decision) *before* claiming the exit complete. That page is `kva: alive`.
4. **Subject page.** Set `kva: terminated`, `growth: false` if present. Do not delete. Do not flip an older terminated page back to forming. Add `relates_to` the exit node with `kind: kva_terminate`. Optionally `contradicts` the living thesis.
5. **Exit-reason node** (required). New or reused `type: document` with:
   - `kva_role: exit-reason`
   - `kva: alive`
   - body: what was terminated, against which objective, why terminate not supersede, pointers to living pages
   - `relates_to` subject with `kind: records`
   - `relates_to` `living_node` with `kind: related`
   - `relates_to` work hub with `kind: implements` when `work_id` exists
6. **Archive debris.** Facts that remain true may live on sibling pages with `reality: archive` and `kva: alive`. They must not present the dead frame as current identity.
7. **Move orbit.** Set `current_branch` to `living_node` (or the exit node if the living page is only a pointer). Do not keep talking on the terminated subject.
8. **Lint L4.** `terminated` must have exactly one `kva_terminate` to an alive exit-reason page. Use path lint when a lint script exists; otherwise check the two pages by read.
9. **Compile green** on `atlas_root`.

## Reactivation

A later forming page may `derived_from` the terminated stub. Never edit `kva` on the stub back to forming.

## Non-goals

- Auto-terminate from model disagreement alone
- Deleting pages
- Re-implementing KVA inside Atlas remember (remember only loads this path)
- Using this path for ordinary sprout/park
