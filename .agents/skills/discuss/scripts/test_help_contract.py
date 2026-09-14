from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_IDS = (
    "getting-started",
    "help",
    "speak",
    "from-conversation",
    "sprout",
    "terminate",
    "lint",
    "consolidate",
    "constellation",
)
PATH_ID_RE = re.compile(r"\|\s*\*\*([a-z0-9-]+)\*\*\s*\|")
TEXT_FENCE_RE = re.compile(r"```text\n(.*?)```", re.S)
VERSION_RE = re.compile(r"^version:\s*(\S+)\s*$", re.M)
SECTION_RE = re.compile(r"^## \[([^\]]+)\][^\n]*\n", re.M)


def _ids(text: str) -> list[str]:
    return PATH_ID_RE.findall(text)


def _flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def _current_version() -> str:
    match = VERSION_RE.search((ROOT / "apm.yml").read_text(encoding="utf-8"))
    if match is None:
        raise AssertionError("apm.yml: missing version")
    return match.group(1)


def _changelog_section(changelog: str, title: str) -> str:
    headings = list(SECTION_RE.finditer(changelog))
    for index, heading in enumerate(headings):
        if heading.group(1) == title:
            end = headings[index + 1].start() if index + 1 < len(headings) else len(
                changelog
            )
            return changelog[heading.end() : end]
    raise AssertionError(f"CHANGELOG.md: missing section [{title}]")


class HelpContractTests(unittest.TestCase):
    def test_path_modules_exist(self) -> None:
        for path_id in REGISTRY_IDS:
            path = ROOT / "references" / "paths" / f"{path_id}.md"
            self.assertTrue(path.is_file(), path)

    def test_skill_registry_lists_every_module(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        start = skill.index("## Path registry")
        end = skill.index("Default live loop")
        self.assertEqual(_ids(skill[start:end]), list(REGISTRY_IDS))

    def test_help_catalog_matches_registry(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        start = help_text.index("## Installed registry")
        end = help_text.index("## Named module")
        self.assertEqual(_ids(help_text[start:end]), list(REGISTRY_IDS))

    def test_readme_modules_table_names_help_and_getting_started(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        start = readme.index("## Modules")
        end = readme.index("## Related")
        table = readme[start:end]
        self.assertIn("| Getting started |", table)
        self.assertIn("| Help |", table)
        self.assertNotIn("activation path", table.lower())
        self.assertNotIn("activation path", readme.lower())

    def test_readme_install_stays_marketplace_only(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("apm install discuss@atlas", readme)
        self.assertNotIn("discuss#v", readme)
        self.assertNotIn("sergio-sisternes-epam/discuss#", readme)

    def test_help_explains_and_does_not_execute(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("Explain Discuss. Do not execute Discuss.", help_text)
        self.assertIn("## Explain, do not execute", help_text)
        for forbidden in (
            "mutates the discussion graph",
            "atlas mount",
            "runs from-conversation, sprout, terminate",
        ):
            self.assertIn(forbidden, help_text)
        self.assertIn("Do not emit `path: terminate`", help_text)
        self.assertIn("Do not `atlas mount`. Do not auto-mount.", help_text)

    def test_help_baseline_then_optional_readonly_atlas(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("## Bundled baseline first", help_text)
        self.assertIn("Help must work with no Atlas mounted.", _flat(help_text))
        self.assertIn("## Optional Atlas enrichment", help_text)
        self.assertIn("when it is already resolvable", _flat(help_text))
        self.assertIn("atlas_used", help_text)
        self.assertIn("intent", help_text)
        self.assertIn("help_status", help_text)
        self.assertIn("atlas_status", help_text)
        self.assertIn("read-only query times out, is denied, or", help_text)
        self.assertIn("successful no-hit search", help_text)
        self.assertIn("`help_status: limited`", help_text)
        self.assertIn("no eligible hit is a knowledge gap", help_text)
        self.assertIn("add `atlas_reason`", help_text)
        self.assertIn("`atlas search`", help_text)
        self.assertNotIn("path **query**", help_text)
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        unreleased = _changelog_section(changelog, "Unreleased")
        current = _changelog_section(changelog, _current_version())
        self.assertNotIn("v0.12.0", unreleased)
        self.assertNotIn("40e11c65", unreleased)
        self.assertIn("v0.12.0", current)
        self.assertIn("40e11c65", current)

    def test_unknown_target_lists_valid_choices(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("say it is unknown and list the valid module names", help_text)
        self.assertIn("Do not require a clarifying question just to list", help_text)
        self.assertIn("walk back", help_text)
        self.assertIn("picture of the pieces", help_text)
        self.assertIn("gaps and contradictions", help_text)
        self.assertIn("join what stands", help_text)
        self.assertIn("Unqualified “help” outside Discuss context must not activate", help_text)

    def test_activation_cards_are_fenced_text(self) -> None:
        for relative in (
            "references/paths/help.md",
            "references/paths/getting-started.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            cards = [
                card
                for card in TEXT_FENCE_RE.findall(text)
                if "path:" in card and "intent:" in card
            ]
            self.assertTrue(cards, relative)
            for card in cards:
                self.assertIn("intent:", card, relative)
                self.assertIn("atlas_used:", card, relative)
                self.assertIn("atlas_status:", card, relative)
                self.assertIn("help_status:", card, relative)
                self.assertIn("speak_loaded: yes", card, relative)
                self.assertNotIn("help_status: pending", card, relative)

    def test_getting_started_covers_first_journey(self) -> None:
        text = (ROOT / "references/paths/getting-started.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("### Purpose", text)
        self.assertIn("### Prerequisites", text)
        self.assertIn("### Shortest useful first journey", text)
        self.assertIn("“What does Discuss do?”", text)
        self.assertIn("discuss-atlas", text)
        self.assertIn("path **speak**", text)
        self.assertIn("apm install discuss@atlas", text)
        self.assertIn("must not run them as live setup", text)
        self.assertIn(
            "Optional enrichment below may `atlas resolve` an",
            text,
        )
        self.assertIn("Point the user at path **help**", text)
        self.assertIn("Refresh the card **before** the explanation.", text)
        self.assertIn("atlas_reason", text)
        self.assertIn("help_status: limited", text)
        journey = text[text.index("### Shortest useful first journey") :]
        self.assertLess(
            journey.index("loads **speak**"),
            journey.index("emits its live card"),
        )
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn(
            "Baseline-only help stays complete when the bundled references answer.",
            changelog,
        )
        self.assertNotIn(
            "that store is already resolvable; otherwise limited help plus the reason.",
            changelog,
        )

    def test_live_loop_does_not_create_hub_for_help(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        gate = skill.index("## Explain-only gate")
        enter = skill.index("## Enter")
        mount_if_missing = skill.index("mount if missing")
        create_hub = skill.index("create a hub page")
        mount_cmd = skill.index(
            "atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main"
        )
        self.assertLess(gate, enter)
        self.assertLess(gate, mount_if_missing)
        self.assertLess(gate, create_hub)
        self.assertLess(gate, mount_cmd)
        self.assertLess(enter, mount_cmd)
        self.assertIn("Live discussion only (not help or getting-started):", skill)
        self.assertIn("Do not run `atlas mount` for help or getting-started.", skill)
        self.assertNotIn(
            "Do not run `atlas mount` or `atlas resolve` for help or getting-started.",
            skill,
        )
        self.assertIn(
            "Optional read-only `atlas resolve` of an already-registered checkout",
            skill,
        )
        self.assertIn("then `atlas search` as the selected path describes", skill)
        self.assertNotIn(
            "Optional Atlas enrichment is read-only resolve of an already-registered checkout only.",
            skill,
        )
        self.assertIn("Do not activate Atlas path **mount**.", skill)
        self.assertIn("Do not create a hub or set `discussion_root`.", skill)
        self.assertIn("This bullet is live discussion only", skill)
        self.assertIn(
            "zero implement authority, no product writes outside this Atlas, "
            "no discussion-to-implement short-circuit.",
            skill,
        )
        self.assertIn("Unqualified help outside Discuss must not activate this skill.", skill)
        self.assertIn("help frobnicate", skill)
        desc = skill.split("---", 2)[1]
        self.assertIn("help <module>", desc)
        self.assertIn("In Discuss context also trigger on help", desc)
        self.assertIn("unknown names such as help frobnicate", desc)
        self.assertIn("I am new to Discuss", desc)
        self.assertIn("how does Discuss work", desc)
        self.assertIn("what does Discuss do", desc)
        self.assertIn("how do I start a durable discussion graph", desc)
        self.assertIn("useful first step with Discuss", desc)
        self.assertIn("first-use intent clearly about Discuss", desc)
        self.assertIn("how to start a durable discussion graph", skill)
        self.assertIn("asked for a useful first step with Discuss", skill)
        self.assertIn("first-use intent clearly about Discuss", skill)
        self.assertIn("said they are new to Discuss", skill)
        self.assertIn("asked how Discuss works", skill)
        self.assertIn("asked what Discuss does", skill)
        self.assertIn("“What can Discuss do?” stays on path **help**.", skill)
        self.assertIn("enter path **getting-started**", skill)
        self.assertIn("enter path **help**", skill)
        self.assertIn("Do not enter path **help**.", skill)
        self.assertIn("Do not enter path **getting-started**.", skill)
        self.assertIn("loads the selected module source", skill)
        self.assertIn("what can Discuss do?", skill)
        self.assertIn("explain terminate", skill)
        self.assertIn("what does sprout need?", skill)
        self.assertIn("Direct module commands", skill)
        self.assertIn("must not enter this gate", skill)
        self.assertNotIn(
            "`references/paths/help.md` or `references/paths/getting-started.md`",
            skill,
        )

    def test_named_help_card_is_complete_on_baseline(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertNotIn("help_status: pending", help_text)
        self.assertIn("help_status: complete", help_text)
        self.assertIn("No `pending` on", help_text)
        self.assertIn("keep `atlas_root: none`", help_text)
        self.assertIn("references/paths/consolidate.md", help_text)
        self.assertIn("Do not present `keep`, `expand`", help_text)
        from_conv = (ROOT / "references/paths/from-conversation.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("kva: keep | expand | terminate", from_conv)
        self.assertNotIn("KVA `terminate`", from_conv)
        self.assertIn("kva: forming | alive", from_conv)
        self.assertIn("kva: terminated", from_conv)

    def test_changelog_records_unreleased_modules(self) -> None:
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        unreleased = _changelog_section(changelog, "Unreleased")
        current = _changelog_section(changelog, _current_version())
        self.assertNotIn("getting-started", unreleased)
        self.assertNotIn("**help**", unreleased)
        self.assertIn("getting-started", current)
        self.assertIn("help", current)
        self.assertNotIn("activation path", current.lower())


if __name__ == "__main__":
    unittest.main()
