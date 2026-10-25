#!/usr/bin/env python3
"""Check evals/evals.json and evals/triggers.json for the expected schema and counts.

Usage:
    python scripts/validate_evals.py [--evals PATH] [--triggers PATH]
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODES = {"quick", "full"}
MIN_EVALS = 6
MIN_SHOULD_TRIGGER = 8
MIN_SHOULD_NOT_TRIGGER = 5


def string_list(value) -> bool:
    return isinstance(value, list) and len(value) > 0 and all(isinstance(v, str) and v.strip() for v in value)


def check_evals(data, errors):
    evals = data.get("evals") if isinstance(data, dict) else None
    if not isinstance(evals, list):
        errors.append("evals.json: top-level 'evals' must be a list")
        return 0
    if len(evals) < MIN_EVALS:
        errors.append(f"evals.json: need at least {MIN_EVALS} evals, found {len(evals)}")
    seen = set()
    for i, case in enumerate(evals):
        where = f"evals.json: eval #{i + 1}"
        if not isinstance(case, dict):
            errors.append(f"{where} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{where}: 'id' must be a non-empty string")
        elif case_id in seen:
            errors.append(f"{where}: duplicate id {case_id!r}")
        else:
            seen.add(case_id)
            where = f"evals.json: {case_id}"
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{where}: 'prompt' must be a non-empty string")
        if case.get("mode") not in MODES:
            errors.append(f"{where}: 'mode' must be one of {sorted(MODES)}")
        for key in ("expected_behavior", "must_not"):
            if not string_list(case.get(key)):
                errors.append(f"{where}: '{key}' must be a non-empty list of strings")
    return len(evals)


def check_triggers(data, errors):
    counts = {}
    for key, minimum in (("should_trigger", MIN_SHOULD_TRIGGER), ("should_not_trigger", MIN_SHOULD_NOT_TRIGGER)):
        items = data.get(key) if isinstance(data, dict) else None
        if not string_list(items):
            errors.append(f"triggers.json: '{key}' must be a non-empty list of strings")
            counts[key] = 0
            continue
        counts[key] = len(items)
        if len(items) < minimum:
            errors.append(f"triggers.json: need at least {minimum} '{key}' phrases, found {len(items)}")
        if len(set(items)) != len(items):
            errors.append(f"triggers.json: '{key}' has duplicate phrases")
    if isinstance(data, dict):
        overlap = set(data.get("should_trigger") or []) & set(data.get("should_not_trigger") or [])
        if overlap:
            errors.append(f"triggers.json: phrases in both lists: {sorted(overlap)}")
    return counts


def load(path, errors):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{path}: file not found")
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON ({exc})")
    return None


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate the skill's evals and trigger phrases.")
    parser.add_argument("--evals", default=ROOT / "evals" / "evals.json", help="path to evals.json")
    parser.add_argument("--triggers", default=ROOT / "evals" / "triggers.json", help="path to triggers.json")
    args = parser.parse_args(argv)

    errors = []
    evals_data = load(args.evals, errors)
    triggers_data = load(args.triggers, errors)
    n_evals = check_evals(evals_data, errors) if evals_data is not None else 0
    counts = check_triggers(triggers_data, errors) if triggers_data is not None else {}

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    modes = {}
    for case in evals_data["evals"]:
        modes[case["mode"]] = modes.get(case["mode"], 0) + 1
    print(f"OK: {n_evals} evals ({', '.join(f'{k}: {v}' for k, v in sorted(modes.items()))})")
    print(f"OK: {counts['should_trigger']} should_trigger, {counts['should_not_trigger']} should_not_trigger phrases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
