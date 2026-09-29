#!/usr/bin/env python3
"""Deterministic gate derivation for an initiative folder.

Applies the G1–G10 rules from docs/interaction-model.md to the artifacts
in one or more initiative folders and prints phase, passed gates, the
blocker, status-file discrepancies (claimed passed, not backed) and
gates the artifacts satisfy but STATUS.md leaves open.

Usage:  python3 evals/derive_gates.py initiatives/<slug> [...]
        python3 evals/derive_gates.py evals/gate-fixtures/*/   (--check compares with expected.md)

/navigate status runs the same rules by reading; this script is the
checkpoint that keeps the reading honest. A rule change goes here and
in the interaction model together.
"""
import pathlib, re, sys

ORDER = [f"G{i}" for i in range(1, 11)]

def txt(p): return p.read_text() if p.exists() else ""

def derive(d):
    d = pathlib.Path(d); g = {}
    js = re.compile(r"When (my|I|a|the)[^\n]*?,? I want to[^\n]*?, so (that )?I can", re.I)
    g["G1"] = any(js.search(txt(d/p)) for p in ["discovery/brainstorm.md", "discovery/synthesis.md", "problems/problems.md"])
    led = txt(d/"ledger.md")
    ra = re.search(r"\*\*Riskiest assumption \(exactly one\):\*\* (.+)", led)
    ct = re.search(r"\*\*Its cheapest test:\*\* (.+)", led)
    g["G2"] = bool(ra and ct and "not yet named" not in ra.group(1) and "not yet named" not in ct.group(1))
    g["G3"] = bool(re.search(r"Verdict:\s*\**Yes", txt(d/"problems/problems.md"))) or ("persevere" in txt(d/"discovery/synthesis.md"))
    sc = txt(d/"problems/gap-scorecard.md")
    scores = [int(m.group(1)) for m in re.finditer(r"^\| \d \| [^|]+ \| (\d) \|", sc, re.M)]
    g["G4"] = len(scores) == 5 and min(scores) >= 3 and "dated" in sc
    vp = txt(d/"experiments/value-proposition.md")
    g["G5"] = bool(re.search(r"We [^\n]+ by [^\n]+", vp)) and "Statement" in vp
    ex = d/"experiments"
    cards = (list(ex.glob("*-card.md")) + list(ex.glob("*-readout.md"))) if ex.exists() else []
    g["G6"] = any(all(k in txt(c) for k in ["Found out that", "Decision", "Expected", "Would disprove"]) for c in cards)
    opts = list((d/"options").glob("*.md")) if (d/"options").exists() else []
    g["G7"] = any(re.search(r"status:\s*chosen", txt(o)) for o in opts)
    g["G8"] = any(all(k in txt(o) for k in ["CD3", "Deferred", "Class"]) for o in opts if o.name.endswith("-v1.md"))
    g["G9"] = bool(re.search(r"(Verdict|verdict):\s*(build|iterate|kill|park)", txt(d/"prfaq/prfaq.md")))
    g["G10"] = "counter-metric" in txt(d/"metrics/metric-tree.md").lower()
    phase = "Opportunity Discovery"
    if g["G2"]: phase = "Problem Validation"
    if g["G4"]: phase = "Solution Validation"
    blocker = next((x for x in ORDER[:9] if not g[x]), None)
    st = txt(d/"STATUS.md")
    claimed = {m.group(1): m.group(2) for m in re.finditer(r"^\| (G\d+) \| [^|]+ \| (\w+) \|", st, re.M)}
    disc = [x for x in ORDER if claimed.get(x) == "passed" and not g[x]]
    unmarked = [x for x in ORDER if g[x] and claimed.get(x) != "passed"]
    return dict(phase=phase, passed=[k for k in ORDER if g[k]], blocker=blocker, discrepancies=disc, unmarked=unmarked)

def main(argv):
    check = "--check" in argv
    paths = [a for a in argv if not a.startswith("--")]
    ok = 0; n = 0
    for p in paths:
        r = derive(p); n += 1
        print(f"== {p}\n   phase={r['phase']} · passed={r['passed']} · blocker={r['blocker']} · discrepancies={r['discrepancies']} · unmarked={r['unmarked']}")
        exp = pathlib.Path(p)/"expected.md"
        if check and exp.exists():
            e = exp.read_text()
            want_phase = re.search(r"Phase: \*\*([^*]+)\*\*", e).group(1)
            want_block = re.search(r"Blocker: \*\*(G\d+)\*\*", e).group(1)
            want_disc = re.findall(r"Discrepancies: \*\*(G\d+)", e)
            good = (r["phase"] == want_phase and r["blocker"] == want_block and set(r["discrepancies"]) == set(want_disc))
            ok += good; print("   expected:", "MATCH" if good else f"MISMATCH (phase {want_phase}, blocker {want_block}, discrepancies {want_disc})")
    if check: print(f"\n{ok}/{n} fixtures match")
    return 0 if not check or ok == n else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
