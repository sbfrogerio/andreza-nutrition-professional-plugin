#!/usr/bin/env python3
"""Padronizar e comparar planos alimentares fornecidos."""

import argparse
import json
import sys


FIELDS = ("energy_kcal", "carb_g", "protein_g", "fat_g", "adherence_pct")


def load_input(path):
    stream = sys.stdin if path == "-" else open(path, "r", encoding="utf-8")
    try:
        return json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()


def valid_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def calculate(payload):
    plans = payload.get("plans")
    if not isinstance(plans, list) or not plans:
        raise ValueError("plans deve ser uma lista não vazia")
    normalized = []
    for idx, plan in enumerate(plans):
        if not isinstance(plan, dict):
            raise ValueError(f"plans[{idx}] deve ser objeto")
        item = {
            "name": plan.get("name"),
            "start": plan.get("start"),
            "end": plan.get("end"),
            "objective": plan.get("objective"),
            "weight_kg": plan.get("weight_kg"),
        }
        weight = plan.get("weight_kg")
        if weight is not None and (not valid_number(weight) or weight <= 0):
            raise ValueError(f"plans[{idx}].weight_kg inválido")
        for field in FIELDS:
            value = plan.get(field)
            if value is not None and (not valid_number(value) or value < 0):
                raise ValueError(f"plans[{idx}].{field} inválido")
            if field == "adherence_pct" and valid_number(value) and value > 100:
                raise ValueError(f"plans[{idx}].adherence_pct deve estar entre 0 e 100")
            item[field] = value
        for macro in ("carb_g", "protein_g", "fat_g"):
            item[f"{macro}_per_kg"] = (
                None
                if not valid_number(item.get(macro)) or not valid_number(weight)
                else round(item[macro] / weight, 4)
            )
        normalized.append(item)
    normalized.sort(key=lambda x: str(x.get("start", "")))

    changes = []
    for previous, current in zip(normalized, normalized[1:]):
        delta = {}
        for field in FIELDS:
            left, right = previous.get(field), current.get(field)
            delta[field] = (
                round(float(right) - float(left), 4)
                if valid_number(left) and valid_number(right)
                else None
            )
        changes.append({"from": previous.get("name"), "to": current.get("name"), "delta": delta})
    return {
        "plans": normalized,
        "consecutive_changes": changes,
        "prescription_treated_as_actual_intake": False,
        "causality_inferred": False,
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
