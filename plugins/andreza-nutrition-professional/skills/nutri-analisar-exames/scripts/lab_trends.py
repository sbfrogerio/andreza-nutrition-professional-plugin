#!/usr/bin/env python3
"""Organizar tendências laboratoriais usando apenas referências fornecidas."""

import argparse
import collections
import datetime as dt
import json
import sys


def load_input(path):
    stream = sys.stdin if path == "-" else open(path, "r", encoding="utf-8")
    try:
        return json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def classify(value, low, high):
    if not numeric(value):
        return "indeterminado"
    if numeric(low) and value < low:
        return "abaixo_da_referencia_do_laudo"
    if numeric(high) and value > high:
        return "acima_da_referencia_do_laudo"
    if numeric(low) or numeric(high):
        return "dentro_da_referencia_do_laudo"
    return "sem_referencia_fornecida"


def calculate(payload):
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("records deve ser uma lista não vazia")
    groups = collections.defaultdict(list)
    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"records[{idx}] deve ser objeto")
        marker = str(record.get("marker", "")).strip()
        unit = str(record.get("unit", "")).strip()
        method = str(record.get("method", "")).strip()
        if not marker:
            raise ValueError(f"records[{idx}].marker é obrigatório")
        try:
            dt.date.fromisoformat(str(record.get("date")))
        except ValueError as exc:
            raise ValueError(f"records[{idx}].date deve usar YYYY-MM-DD") from exc
        item = dict(record)
        item["status_by_report_range"] = classify(
            item.get("value"), item.get("ref_low"), item.get("ref_high")
        )
        groups[(marker.casefold(), unit, method.casefold())].append(item)

    result = []
    for (_, unit, _), items in sorted(groups.items()):
        items.sort(key=lambda x: str(x.get("date", "")))
        values = [float(x["value"]) for x in items if numeric(x.get("value"))]
        trend = {
            "comparable_numeric_results": len(values),
            "first_last_delta": None if len(values) < 2 else round(values[-1] - values[0], 6),
            "direction": (
                "dados_insuficientes"
                if len(values) < 2
                else "aumento"
                if values[-1] > values[0]
                else "reducao"
                if values[-1] < values[0]
                else "sem_mudanca_numerica"
            ),
        }
        result.append(
            {
                "marker": items[0]["marker"],
                "unit": unit,
                "method": items[0].get("method"),
                "laboratories": sorted({str(x.get("laboratory", "")).strip() for x in items if x.get("laboratory")}),
                "records": items,
                "descriptive_trend": trend,
            }
        )
    return {
        "groups": result,
        "unit_conversion_performed": False,
        "different_methods_compared_directly": False,
        "diagnosis_generated": False,
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
