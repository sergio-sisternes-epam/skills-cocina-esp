---
name: discuss/paths/getting-started
description: First-use orientation for Discuss. Purpose, prerequisites, and the shortest useful first journey. Explain; do not execute.
path_id: getting-started
---

# Path: getting-started

First-use for Discuss. Load when the user is new to Discuss, asks how it works,
or wants a useful first step. This path explains. It does not start a discussion
graph, mount a store, or run another module.

## When

- “I am new to Discuss”
- “How does Discuss work?”
- “What does Discuss do?”
- “How do I start a durable discussion graph?”
- First-use intent clearly about Discuss

Do not steal an unrelated “getting started” task. If the user is not asking
about Discuss, leave this path unloaded.

## Enter

Load path **speak** first. Then emit this card as a fenced `text` block.
Keep `intent` as the user’s learning goal, not an operation to run.

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: getting-started
path_module: references/paths/getting-started.md
intent: Learn what Discuss does and take a first useful step
atlas_id: github.com/sergio-sisternes-epam/discuss-atlas
ref: main
atlas_root: none
atlas_status: baseline-only
atlas_used: []
help_status: complete
speak_loaded: yes
```

Do not create `discussion_root`. Do not ask for a discussion subject or
objective just to orient. If speak is missing ⇒ `incomplete: missing speak`.

Field contract (same as path **help**):

- `intent` is the learning goal.
- `atlas_id` / `atlas_root` name the retrieval context, not proof it was used.
- `atlas_status`: `not-queried` | `baseline-only` | `consulted` | `unavailable`.
  If `unavailable`, add short `atlas_reason`.
- `atlas_used` lists only store IDs whose evidence actually contributed.
- `help_status`: `complete` or `limited`.
- Final cards contain no `pending` placeholders.

If this file answers the question, stop. Keep `atlas_status: baseline-only`
and `atlas_used: []`. Do not duplicate an identical card.

## Bundled baseline (this package, this version)

Answers here are for the installed Discuss package. They do not need
`discuss-atlas` to be mounted.

### Purpose

Discuss runs a discussion as a durable, agent-maintained Atlas graph. The
graph is a high-fidelity record and navigation aid. New ideas come from the
human–AI conversation. The graph persists that work, amortises
discarded-session cost, and accelerates human connections.

This package is not for implementation. Autogenesis Discussion mode still
applies when called from Autogenesis: zero implement authority, no product
writes outside the companion store, no discussion-to-implement short-circuit.

### Prerequisites

1. APM CLI (see `CONTRIBUTING.md` for the version this checkout expects).
2. Marketplace install, not a git-tag install in consumer docs:

   ```bash
   apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
   apm install discuss@atlas
   ```

3. Atlas is the knowledge substrate. Discuss depends on it; do not invent a
   parallel store.
4. Persistence uses the companion store
   `github.com/sergio-sisternes-epam/discuss-atlas`. That store is All Rights
   Reserved knowledge, not an APM dependency of this package. Installing
   Discuss does not mount it.
5. A git repository is required before Atlas will persist. Getting-started
   does not create one.

### Shortest useful first journey

1. **Name the work.** A clear subject and a one-line objective. Discuss will
   ask for these when you actually start a discussion, not during this
   orientation.
2. **Companion store, when you will persist.** In the project git repo, mount
   and resolve if the store is not already resolvable. Show these commands;
   this path must not run them as live setup on the user's behalf:

   ```text
   atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main
   atlas resolve github.com/sergio-sisternes-epam/discuss-atlas
   ```

   Do not `atlas mount`. Optional enrichment below may `atlas resolve` an
   already-registered checkout when the bundled answer is incomplete.

3. **Start discussing.** Ask to discuss the subject with that objective. Discuss
   loads **speak** and `human-turn.md` first, then emits its live card, and
   talks in plain British English. Chat is the shared picture; the Atlas is
   usually invisible.
4. **Let the agent file.** Query first, stay on one conversation orbit, batch
   questions, persist engaged items, sprout leftovers as protostars, compile
   green. You do not file nodes by hand.
5. **Then use module help.** For what each module does, load path **help**.
   No-target help lists the installed registry. Named help explains one
   module without running it.

### Human narration

Every live turn must make visible: where we are after the last pin, what the
live distinction is, what was set aside when that still matters, then the ask.
Activation cards do not replace that prose. Path **speak** owns the register.

## Optional Atlas enrichment

If this file does not answer the actual question, follow path **help**’s
read-only retrieval rule against
`github.com/sergio-sisternes-epam/discuss-atlas`. Attempt resolve only when
already registered. Never mount, init, remember, compile, or write to answer
getting-started. Baseline above remains usable.

Refresh the card **before** the explanation. Do not leave the Enter
`baseline-only` / `help_status: complete` card in place after enrichment.

- Successful resolve and contributing evidence: `atlas_status: consulted`,
  real `atlas_root`, `atlas_used` listing those store IDs,
  `help_status: complete` or `limited`.
- Resolve fails or no checkout exists: `atlas_status: unavailable`,
  `atlas_root: none`, `atlas_used: []`, `help_status: limited`, and
  `atlas_reason` with the known cause. Limited help plus that reason.

## Next modules

Point the user at path **help** for the installed registry, then at a named
module if they already know which one they need. Typical next reads:

- **speak** — how Discuss talks
- **from-conversation** — turn talk into fabric
- **sprout** — park a surviving pending
- **terminate** — close a wrong frame

## Non-goals

- Starting a discussion or creating a hub
- Mounting or repairing `discuss-atlas`
- Running sprout, terminate, lint, consolidate, or constellation
- Teaching Atlas CLI as if it were Discuss
- Hijacking a getting-started request that is not about Discuss
