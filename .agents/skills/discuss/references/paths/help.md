---
name: discuss/paths/help
description: Explain Discuss modules without executing them. List the installed registry, or explain one named module from bundled references, with optional read-only Atlas enrichment.
path_id: help
---

# Path: help

Explain Discuss. Do not execute Discuss. Load this module for discovery or
for a named-module explanation. Reading another module to explain it is not
permission to run that module.

## When

In Discuss context only:

- no target: “help”, “what can Discuss do?”, “list modules”
- named module or topic: “explain terminate”, “what does sprout need?”
- unknown name: “help frobnicate”

Do not require a clarifying question just to list the registry.

Unqualified “help” outside Discuss context must not activate this skill or
hijack an unrelated task. “Terminate this branch” is path **terminate**, not
help. “Help me centre this CSS” is not Discuss.

## Enter

Load path **speak** first. Then emit this card as a fenced `text` block.
`path` stays `help` even when the topic is another module. `intent` is the
learning goal.

No-target example:

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: help
path_module: references/paths/help.md
intent: List every installed Discuss module
atlas_id: github.com/sergio-sisternes-epam/discuss-atlas
ref: main
atlas_root: none
atlas_status: baseline-only
atlas_used: []
help_status: complete
speak_loaded: yes
```

Named-module example (still path help):

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: help
path_module: references/paths/help.md
intent: Understand how terminate works without terminating a branch
atlas_id: github.com/sergio-sisternes-epam/discuss-atlas
ref: main
atlas_root: none
atlas_status: baseline-only
atlas_used: []
help_status: complete
speak_loaded: yes
```

Do not emit `path: terminate` (or sprout, or from-conversation) for an
explanation. Do not create `discussion_root`. If speak is missing ⇒
`incomplete: missing speak`.

Field contract:

- `intent` names the user’s learning goal, near the top.
- `atlas_id` / `atlas_root` are selected retrieval context, not proof of use.
  At Enter they may be `none`. Only an already-resolvable read-only resolve
  may fill `atlas_root`. Never fabricate a mount path.
- `atlas_status`: `not-queried` | `baseline-only` | `consulted` | `unavailable`.
  If `unavailable`, add short `atlas_reason`.
- `atlas_used` starts empty. List only store IDs whose eligible evidence
  contributed. A consulted miss stays empty.
- `help_status`: `complete` or `limited` on the final card. No `pending` on
  the card that accompanies the answer.
- If bundled references suffice and no retrieval occurred, the baseline-only
  card is enough. Do not duplicate identical cards.
- Card, citations, and prose must agree.

## Installed registry (bundled)

This table is the no-target answer. It matches the path registry in
`SKILL.md` for this package version. One line each. Do not load every
module file just to list.

| Module | Purpose |
|--------|---------|
| **getting-started** | First-use: purpose, prerequisites, shortest useful first journey |
| **help** | Explain modules without running them |
| **speak** | Always-on prefix; human narration before any human-facing reply |
| **from-conversation** | Turn a live or past conversation into graph fabric |
| **sprout** | Park a surviving pending as a protostar linked to its origin |
| **terminate** | KVA-terminate a wrong frame; write exit-reason; link living thesis |
| **lint** | Check fabric discipline. L1 hubs; L2–L6 KVA contract |
| **consolidate** | Partial dated view; stance edges. Informal: walk-back |
| **constellation** | Join cadence. Official picture of what stands. Synonym: checkpoint |

Aliases for lookup only: walk-back, walk back, picture of the pieces, gaps and contradictions → **consolidate**; checkpoint, join what stands → **constellation**.

After the list, say the user can ask for any one module by name. Do not
ask which to list.

## Named module or topic

1. Map the utterance to one `path_id` in the registry (or an alias above).
2. If it does not match, say it is unknown and list the valid module names
   from the registry table. Do not invent flags, CLI verbs, or extra modules.
3. Load **only** that module file (`references/paths/<path_id>.md`), plus
   files it explicitly names as required contract (for example
   `references/human-turn.md` when the topic is **speak**, and
   `references/paths/consolidate.md` when the topic is **constellation**).
   Do not load every module.
4. Explain from that source:
   - intent (what it is for)
   - inputs (Enter card fields)
   - prerequisites
   - examples
   - outputs
   - side effects
   - boundaries / non-goals
   KVA values and live-loop rules in `SKILL.md` override stale wording in a
   module file. The current enum is `forming | alive | deprecated |
   superseded | terminated`. Do not present `keep`, `expand`, or any other
   extra `kva` symbol as current capability.
5. Stop if that file answers the actual question. Set
   `atlas_status: baseline-only`, `atlas_used: []`, `help_status: complete`.

Topic overlap or fluent general knowledge is not enough. Mechanics do not
always explain design rationale. A partial answer is a gap.

## Explain, do not execute

Help never:

- mutates the discussion graph (no pages, edges, KVA writes, sprouts, exits)
- mounts, inits, installs, authenticates, or repairs Atlas
- runs from-conversation, sprout, terminate, lint, consolidate, or constellation
- compiles, remembers, commits, or pushes
- creates a hub because `discussion_root` is missing

Reading `references/paths/terminate.md` to explain terminate is not a
terminate ramp. Same for sprout and from-conversation.

## Bundled baseline first

Ship and use versioned references in this package. Help must work with no
Atlas mounted. If the loaded references answer the question, stop. Extra
enrichment is optional, not required.

## Optional Atlas enrichment

If references are absent, unreadable, irrelevant, or only partial:

1. Attempt **read-only** resolve of
   `github.com/sergio-sisternes-epam/discuss-atlas` when it is already
   resolvable (`atlas resolve`). Do not `atlas mount`. Do not auto-mount.
2. If resolve fails, or no registered checkout exists: limited help. Say
   that fuller knowledge lives in that store and why it was not queried
   (unmounted, denied, timeout, unknown). Baseline remains usable.
3. If resolve succeeds, search read-only with `atlas search` (1–3 pages,
   no index build, no write). Prefer published, applicable evidence. Do
   not treat unapproved proposals as installed capability. Do not load a
   Discuss path named **query**.
4. Refresh the card before the explanation. `atlas_used` lists only
   evidence that contributed. `help_status` is `complete` or `limited`.
   - `atlas_status: consulted` only after a successful resolve; then set
     `atlas_root` to the real resolved path.
   - If resolve succeeds but the read-only query times out, is denied, or
     errors: keep `atlas_status: consulted` and the real `atlas_root`, set
     `help_status: limited`, and add `atlas_reason`. That is not a
     successful no-hit search.
   - `atlas_status: unavailable` when resolve fails or no checkout exists;
     keep `atlas_root: none` and add `atlas_reason`. Never fabricate a path.

Suggested limited-help wording when retrieval fails:

> The bundled references do not cover this question fully, so my help is
> limited. I could not access the Discuss Atlas knowledge store, where
> fuller information is maintained, because [known reason]. I can explain
> [supported part], but I cannot confirm [missing part] from the available
> sources.

If nothing is supported, omit the partial explanation. A successful search
with no eligible hit is a knowledge gap, not unavailability: keep
`atlas_status: consulted`, `atlas_used: []`, and `help_status: limited`.
Never mount, authenticate, install, repair, or publish just to answer help.

## Non-goals

- A second catalog skill named help
- Visualise / Cartograph (out of scope for this package)
- Hijacking unqualified help outside Discuss
- Replacing speak, or running the live discuss loop
- Schema overlays or curated `help/` articles in this change
