---
name: discuss/paths/from-conversation
description: Turn a live or past conversation into discussion fabric in an Atlas. Load before executing. Retrospective and live both use this path.
path_id: from-conversation
---

# Path: from-conversation

## When

A conversation already happened (this thread, a pasted transcript, or named Atlas pages) and should become a durable discuss graph. Also the activation path for “turn this talk into fabric”.

## Enter

Discuss card plus:

```text
path: from-conversation
path_module: references/paths/from-conversation.md
source: this-conversation | <atlas path> | <transcript>
```

`discussion_root` is the hub that will own the fabric. Create it if missing.

## Procedure

1. **Lock subject and objective.** If absent, infer a one-line candidate from the source and confirm. Do not invent a second objective mid-path.
2. **Query the target Atlas.** If a hub for this subject exists, reuse it. Else create `founding/hub.md` or `<slug>/hub.md` and set `discussion_root` and `current_branch` to it.
3. **Extract a batch** onto the hub (do not create a page per item yet):
   - claims / ideas
   - questions
   - counters
   - decisions already taken
   - open protostars (pendings)
4. **Offer 1-by-1.** Live: wait for the user to pick. Retrospective: treat items the conversation already engaged as picked; leave unengaged items listed on the hub.
5. **For each engaged item**, persist one page:
   - type `experience` (turns) or `document` (research)
   - `relates_to` the parent with the right kind (`follows`, `counters`, `contradicts`, `derived_from`, `backed_by`, `refuted_by`, `records`)
   - `kva: forming | alive` against the **original objective**. Exit ramps use path **terminate** and the SKILL.md enum (`deprecated` | `superseded` | `terminated`). Do not use `keep`, `expand`, or a sixth `kva` value.
   - `reality: current | alternative`
   - research that grounded a counter is its own page with a source URL or citation, linked `backed_by` or `refuted_by`
6. **Move `current_branch`** only onto an engaged forming or alive node. Root never moves.
7. **Lineage.** If the conversation ended in a conclusion or action, write a `records` node pointing back at the branches that produced it. That is not implement authority.
8. **Park leftovers through sprout.** Any item still pending after the retrospective pass is a protostar. Load `references/paths/sprout.md` and follow it. Do not leave surviving pendings as catalog bullets only.
9. **Compile green.** `atlas compile --root <atlas_root>` exit 0.

## Retrospective rules

- Do not copy a transcript verbatim. Distill claims.
- Do not create nodes for every utterance. Create nodes for engaged ideas, counters, refinements, residuals, and conclusions.
- Side frames that were parked (example: “make it a top-level skill” before the graph model settled) stay `reality: alternative`.
- Counters that were answered are not deleted. Path **terminate** sets `kva: terminated` and means “no longer a live blocker”, not “erase”.

## Non-goals

- Implement product behaviour discovered in the conversation.
- Mandatory consult of other Atlases.
- Replaying the whole thread as one page.
