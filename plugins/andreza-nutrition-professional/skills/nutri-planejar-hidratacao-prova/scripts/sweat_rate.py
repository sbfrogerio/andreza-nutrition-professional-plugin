#!/usr/bin/env python3
"""Calcular taxa de sudorese observada a partir de entradas explícitas."""

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


def positive(payload, key, allow_zero=False):
    value = payload.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} deve ser numérico")
    value = float(value)
    if value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"{key} fora do intervalo permitido")
    return value


def calculate(payload):
    pre = positive(payload, "pre_weight_kg")
    post = positive(payload, "post_weight_kg")
    fluid = positive(payload, "fluid_intake_l", allow_zero=True)
    urine = positive(payload, "urine_l", allow_zero=True)
    duration = positive(payload, "duration_hours")
    body_mass_change = pre - post
    net_loss = body_mass_change + fluid - urine
    return {
        "body_mass_change_kg": round(body_mass_change, 4),
        "body_mass_change_pct": round(body_mass_change / pre * 100, 4),
        "estimated_sweat_loss_l": round(net_loss, 4),
        "observed_sweat_rate_l_per_hour": round(net_loss / duration, 4),
        "assumption": "1 kg de variação de massa corporal equivale aproximadamente a 1 L",
        "clinical_target_selected_by_script": False,
        "warning": "Resultado negativo ou contexto incompatível exige revisão das medições.",
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

