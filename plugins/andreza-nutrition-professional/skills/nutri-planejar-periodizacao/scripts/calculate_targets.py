#!/usr/bin/env python3
"""Conferir metas nutricionais fornecidas; não definir conduta clínica."""

import argparse
import json
import sys


def load_input(path):
    stream = sys.stdin if path == "-" else open(path, "r", encoding="utf-8")
    try:
        return json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()


def number(value, field, required=False):
    if value is None and not required:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} deve ser numérico")
    if value < 0:
        raise ValueError(f"{field} não pode ser negativo")
    return float(value)


def calculate(payload):
    weight = number(payload.get("weight_kg"), "weight_kg", required=True)
    if weight == 0:
        raise ValueError("weight_kg deve ser maior que zero")
    days = payload.get("days")
    if not isinstance(days, list) or not days:
        raise ValueError("days deve ser uma lista não vazia")

    output_days = []
    for index, day in enumerate(days):
        if not isinstance(day, dict):
            raise ValueError(f"days[{index}] deve ser objeto")
        carb_rate = number(day.get("carb_g_per_kg"), f"days[{index}].carb_g_per_kg")
        protein_rate = number(day.get("protein_g_per_kg"), f"days[{index}].protein_g_per_kg")
        fat_rate = number(day.get("fat_g_per_kg"), f"days[{index}].fat_g_per_kg")
        target_energy = number(day.get("energy_kcal"), f"days[{index}].energy_kcal")

        carb_g = None if carb_rate is None else round(carb_rate * weight, 2)
        protein_g = None if protein_rate is None else round(protein_rate * weight, 2)
        fat_g = None if fat_rate is None else round(fat_rate * weight, 2)
        macro_energy = None
        if None not in (carb_g, protein_g, fat_g):
            macro_energy = round(carb_g * 4 + protein_g * 4 + fat_g * 9, 2)

        result = {
            "date": day.get("date"),
            "day_type": day.get("day_type"),
            "weight_kg": weight,
            "carb_g": carb_g,
            "protein_g": protein_g,
            "fat_g": fat_g,
            "energy_from_macros_kcal": macro_energy,
            "target_energy_kcal": target_energy,
            "energy_delta_kcal": (
                None
                if macro_energy is None or target_energy is None
                else round(macro_energy - target_energy, 2)
            ),
        }
        output_days.append(result)

    return {
        "status": "calculo_descritivo",
        "clinical_targets_selected_by_script": False,
        "days": output_days,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="-", help="JSON ou - para stdin")
    args = parser.parse_args()
    try:
        print(json.dumps(calculate(load_input(args.input)), ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()

