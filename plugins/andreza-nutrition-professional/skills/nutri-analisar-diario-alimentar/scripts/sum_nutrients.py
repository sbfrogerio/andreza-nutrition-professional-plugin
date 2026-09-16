#!/usr/bin/env python3
"""Somar somente nutrientes informados e relatar cobertura."""

import argparse
import collections
import datetime as dt
import json
import sys


NUTRIENTS = ("energy_kcal", "carb_g", "protein_g", "fat_g", "fiber_g")


def load_input(path):
    stream = sys.stdin if path == "-" else open(path, "r", encoding="utf-8")
    try:
        return json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()


def calculate(payload):
    entries = payload.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("entries deve ser uma lista não vazia")
    totals = {key: 0.0 for key in NUTRIENTS}
    counts = {key: 0 for key in NUTRIENTS}
    confidence = collections.Counter()
    by_date = collections.defaultdict(lambda: {key: 0.0 for key in NUTRIENTS})
    by_date_counts = collections.defaultdict(lambda: {key: 0 for key in NUTRIENTS})
    for idx, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"entries[{idx}] deve ser objeto")
        confidence[str(entry.get("confidence", "nao_informada"))] += 1
        date = entry.get("date")
        if date is not None:
            try:
                date = dt.date.fromisoformat(str(date)).isoformat()
            except ValueError as exc:
                raise ValueError(f"entries[{idx}].date deve usar YYYY-MM-DD") from exc
        else:
            date = "data_nao_informada"
        nutrients = entry.get("nutrients") or {}
        if not isinstance(nutrients, dict):
            raise ValueError(f"entries[{idx}].nutrients deve ser objeto")
        for key in NUTRIENTS:
            value = nutrients.get(key)
            if value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"entries[{idx}].nutrients.{key} inválido")
            totals[key] += float(value)
            counts[key] += 1
            by_date[date][key] += float(value)
            by_date_counts[date][key] += 1
    return {
        "entry_count": len(entries),
        "totals": {k: round(v, 3) for k, v in totals.items()},
        "coverage": {
            k: {"entries_with_value": counts[k], "entries_total": len(entries)}
            for k in NUTRIENTS
        },
        "confidence_counts": dict(confidence),
        "totals_by_date": {
            date: {
                "totals": {key: round(values[key], 3) for key in NUTRIENTS},
                "coverage": {
                    key: {
                        "entries_with_value": by_date_counts[date][key],
                        "entries_total": sum(1 for item in entries if str(item.get("date") or "data_nao_informada") == date),
                    }
                    for key in NUTRIENTS
                },
            }
            for date, values in sorted(by_date.items())
        },
        "missing_values_treated_as_zero": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="-")
    args = parser.parse_args()
    try:
        print(json.dumps(calculate(load_input(args.input)), ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
