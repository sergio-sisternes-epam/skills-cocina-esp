from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import release_readiness


class ReleaseReadinessTests(unittest.TestCase):
    def write_package(
        self,
        root: Path,
        version: str = "0.3.8",
        skill_version: str | None = None,
        install_version: str | None = None,
        changelog_versions: tuple[str, ...] | None = None,
    ) -> None:
        skill_version = skill_version or version
        install_version = install_version or version
        changelog_versions = changelog_versions or (version,)
        (root / "apm.yml").write_text(
            f"name: discuss\nversion: {version}\n", encoding="utf-8"
        )
        (root / "SKILL.md").write_text(
            f"---\nname: discuss\nmetadata:\n  version: \"{skill_version}\"\n---\n",
            encoding="utf-8",
        )
        (root / "CONTRIBUTING.md").write_text(
            "apm install sergio-sisternes-epam/discuss"
            f"#v{install_version} --target agent-skills\n",
            encoding="utf-8",
        )
        sections = "\n".join(
            f"## [{item}] - 2026-09-04" for item in changelog_versions
        )
        (root / "CHANGELOG.md").write_text(sections + "\n", encoding="utf-8")

    def test_stable_version_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_package(root)
            version, errors = release_readiness.validate_versions(root)
        self.assertEqual(version, "0.3.8")
        self.assertEqual(errors, [])
        self.assertFalse(release_readiness.is_prerelease(version))

    def test_prerelease_version_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_package(root, version="0.4.0-rc.1")
            version, errors = release_readiness.validate_versions(root)
        self.assertEqual(errors, [])
        self.assertTrue(release_readiness.is_prerelease(version))

    def test_malformed_semver_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_package(root, version="03.7")
            version, errors = release_readiness.validate_versions(root)
        self.assertIsNone(version)
        self.assertTrue(errors)

    def test_mismatched_surface_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_package(root, install_version="0.3.9")
            _, errors = release_readiness.validate_versions(root)
        self.assertTrue(any("CONTRIBUTING.md" in error for error in errors))

    def test_duplicate_changelog_entry_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_package(
                root, changelog_versions=("0.3.8", "0.3.8")
            )
            _, errors = release_readiness.validate_versions(root)
        self.assertTrue(any("found 2" in error for error in errors))

    def test_wrong_tag_is_rejected(self) -> None:
        self.assertEqual(
            release_readiness.validate_tag("v0.3.7", "0.3.8"),
            ["release tag v0.3.7 != v0.3.8"],
        )

    @patch.object(release_readiness, "current_commit", return_value="a" * 40)
    def test_wrong_commit_is_rejected(self, _mock_current_commit) -> None:
        self.assertEqual(
            release_readiness.validate_commit("b" * 40),
            [f"candidate commit {'b' * 40} != checked-out revision {'a' * 40}"],
        )


if __name__ == "__main__":
    unittest.main()
