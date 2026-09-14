# Contributing to Discuss

## Local setup

Use APM CLI 0.30.0. Atlas resolves through marketplace
`atlas` (`atlas@atlas`). Register that
marketplace by name before install; do not use alias `me` or default
`atlas-marketplace`. Public github.com installs do not need a consumer PAT.

```bash
apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
git submodule update --init --recursive
apm install --target agent-skills --no-policy
```

Optional tagged install for contributor checks (not the public README path):

```bash
apm install sergio-sisternes-epam/discuss#v0.4.0 --target agent-skills
```

Never commit credentials, `apm_modules/`, or generated `.agents/` dependency
copies. APM 0.30.0 lockfiles record resolved git coordinates for marketplace
plugins, so `apm install --frozen` and `apm audit --ci` look for
`_marketplace/atlas/atlas` and fail. Replay the committed
lock with a normal install and confirm `apm.lock.yaml` is unchanged.
Source and consumer CI use `apm audit --no-policy --no-fail-fast` plus that
replay, not `--ci` / `--frozen`.

Same-repository GitHub pull requests run the source, store, and consumer
private gates with `APM_READ_TOKEN`. Fork pull requests never receive that
credential; reproduce fork changes on a trusted internal branch first. The
exact-main ready-to-tag gate still runs on current `main` and from a release
tag after it has been proven to reference that exact main commit.

## Validate a change

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/release_readiness.py --commit "$(git rev-parse HEAD)"
apm audit --no-policy --no-fail-fast
```

Resolve the store root and run both graph gates:

```bash
atlas_root="$(atlas resolve github.com/sergio-sisternes-epam/discuss-atlas)"
atlas compile --root "$atlas_root"
python3 scripts/lint.py --root "$atlas_root"
```

Install the checked-out package into disposable consumers for
`agent-skills`, `copilot`, and `claude`. Each consumer must pass a second
normal install without changing its lockfile and then pass
`apm audit --no-policy --no-fail-fast`.

When `dependencies.apm` changes, run
`apm install --target agent-skills --no-policy` to regenerate
`apm.lock.yaml`; never edit the lockfile by hand. Inspect the resolved refs and
commits before committing it.

## Release handoff

Discuss uses semantic versioning and immutable annotated `vX.Y.Z` tags.
Prereleases use `vX.Y.Z-<identifier>`.

1. Update `apm.yml`, `SKILL.md`, the CONTRIBUTING tagged install
   command, and `CHANGELOG.md` together.
2. Merge through the normal review process after all required CI checks pass.
3. Run **Discuss CI** manually against the exact `main` commit intended for
   release. Its final job must report `pre_tag_decision=ready to tag`.
4. After separate approval, create and push the matching annotated tag against
   that exact commit.
5. The tag workflow reruns all gates, verifies the tag is newly created and
   fetches its authoritative annotated object into `refs/release-tags/`, peels
   it to the exact current `main` commit, runs every release gate against that
   commit, classifies stable versus prerelease, and creates the GitHub Release.

Never move, overwrite, or delete a pushed release tag. If validation fails
before release creation because of a source, workflow, or metadata defect,
fix `main`, increment the patch version, repeat readiness, and create a new
tag. If only a provider outage or corrected permission blocked release
creation, rerun the failed workflow for the unchanged tag.

The immutable annotated `v0.3.7` tag is a failed release attempt: its workflow
failed before release creation because checkout replaced the local tag-object
ref with its peeled commit. Preserve that remote tag and do not create a
`v0.3.7` GitHub Release; recovery continues with `v0.3.8`.

## Issues and pull requests

Use the GitHub issue templates in `.github/ISSUE_TEMPLATE/` for bugs and
feature requests. Do not file public issues for vulnerabilities; report them
through a private GitHub security advisory.

External substantive work needs a linked issue first. Maintainer-authored
small docs or maintenance may skip that wait. Open pull requests with
`.github/PULL_REQUEST_TEMPLATE.md`. Confirm human scope approval before agent
implementation, except for maintainer-authored small docs or maintenance. The
GitHub author owns the change, including any agent-generated diffs.

## Repository protection

After CI is present on `main`, require its metadata, source/store, and three
consumer checks; require branches to be current; and block direct pushes,
force pushes, and deletion. Protect `v*` tags by restricting creation to
release maintainers and blocking updates and deletion.

This repository currently has one owner and no organization team or second
eligible reviewer. Do not add an individual-only CODEOWNERS file or require an
approval that no independent reviewer can provide. Add team-backed ownership
and approval requirements only after a real owning team exists.
