#!/usr/bin/env python3
"""discuss fabric lint. L1 hubs. L2–L6 KVA contract."""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

RESERVED = {"index.md", "log.md"}
LEGAL_KVA = {"forming", "alive", "deprecated", "superseded", "terminated"}
EXIT_KVA = {"deprecated": "kva_deprecate", "superseded": "kva_supersede", "terminated": "kva_terminate"}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
TYPE_RE = re.compile(r"^type:\s*[\"']?(\S+?)[\"']?\s*$", re.M)
KVA_RE = re.compile(r"^kva:\s*[\"']?(\S+?)[\"']?\s*$", re.M)
ROLE_RE = re.compile(r"^kva_role:\s*[\"']?(\S+?)[\"']?\s*$", re.M)
GROWTH_RE = re.compile(r"^growth:\s*[\"']?(\S+?)[\"']?\s*$", re.M)
CONS_RE = re.compile(r"^consolidation:\s*[\"']?(\S+?)[\"']?\s*$", re.M)
# Inbound kinds that a consolidate view may use on ideas (including protostars).
STANCE_KINDS = {
    "confirms",
    "refutes",
    "expands",
    "restates",
    "indexes",
    "defers",
    "absorbs",
    "feeds",
}
REL_RE = re.compile(
    r"-\s*path:\s*[\"']?([^\"'\n]+)[\"']?\s*\n\s*kind:\s*[\"']?([A-Za-z0-9_-]+)[\"']?",
    re.M,
)


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    fm = m.group(1) if m else ""
    rels = REL_RE.findall(fm)
    t = TYPE_RE.search(fm)
    k = KVA_RE.search(fm)
    role = ROLE_RE.search(fm)
    g = GROWTH_RE.search(fm)
    cons = CONS_RE.search(fm)
    return {
        "path": path,
        "type": (t.group(1) if t else ""),
        "kva": (k.group(1) if k else ""),
        "kva_role": (role.group(1) if role else ""),
        "growth": (g.group(1) if g else ""),
        "consolidation": (cons.group(1) if cons else ""),
        "rels": [(p.strip(), knd.strip()) for p, knd in rels],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    pages = []
    for p in root.rglob("*.md"):
        if p.name in RESERVED:
            continue
        if "templates" in p.parts or "staging" in p.parts:
            continue
        pages.append(load(p))

    rel = {}
    for page in pages:
        rel[str(page["path"].relative_to(root))] = page

    inbound = defaultdict(list)
    for rel_path, page in rel.items():
        for target, kind in page["rels"]:
            target = target.lstrip("./")
            inbound[target].append((rel_path, page["type"], kind))

    failures = []

    for rel_path, page in rel.items():
        if page["kva"] and page["kva"] not in LEGAL_KVA:
            failures.append(f"L2 {rel_path}: illegal kva {page['kva']!r}")
        if page["type"] == "protostar" and not page["kva"]:
            failures.append(f"L3 {rel_path}: protostar missing kva")
        if page["growth"] == "true" and page["kva"] != "forming":
            failures.append(f"L5 {rel_path}: growth true requires kva forming (have {page['kva']!r})")
        if page["kva"] in EXIT_KVA:
            want = EXIT_KVA[page["kva"]]
            matches = []
            for target, kind in page["rels"]:
                target = target.lstrip("./")
                if kind == want:
                    dest = rel.get(target)
                    if not dest:
                        failures.append(f"L4 {rel_path}: {want} target missing {target}")
                        continue
                    if dest.get("kva_role") != "exit-reason" or dest.get("kva") != "alive":
                        failures.append(
                            f"L4 {rel_path}: {want} target {target} must be kva_role exit-reason and kva alive"
                        )
                    else:
                        matches.append(target)
            if len(matches) != 1:
                failures.append(
                    f"L4 {rel_path}: {page['kva']} needs exactly one {want} to an exit-reason (have {matches})"
                )

    for target, ins in sorted(inbound.items()):
        proto = [(src, kind) for src, typ, kind in ins if typ == "protostar"]
        if not proto:
            continue
        dest = rel.get(target)
        shortcuts = []
        children = []
        for src, kind in proto:
            src_page = rel.get(src)
            if not src_page:
                shortcuts.append((src, kind))
                continue
            origins = [p.lstrip("./") for p, k in src_page["rels"] if k == "derived_from"]
            if target in origins:
                children.append(src)
            else:
                shortcuts.append((src, kind))
        if dest and dest["kva"] in EXIT_KVA:
            bad = [(src, kind) for src, kind in proto if kind != "derived_from"]
            if bad:
                failures.append(
                    f"L6 {target}: exit stub has protostar inbound other than derived_from {bad}"
                )
            continue
        if dest and dest.get("consolidation") == "true":
            # Partial consolidate views may be pointed at by many protostars
            # and may index them; they are snapshots, not origin hubs.
            continue
        shortcuts = [(src, kind) for src, kind in shortcuts if kind not in STANCE_KINDS]
        if len(shortcuts) >= 3:
            failures.append(
                f"L1 hub file {target}: {len(shortcuts)} protostar shortcuts (not derived_from this page) {shortcuts}"
            )

    if failures:
        print("discuss lint FAIL")
        for f in failures:
            print(f)
        return 1
    print("discuss lint PASS")
    print("L1 no hub files")
    print("L2–L6 KVA contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
