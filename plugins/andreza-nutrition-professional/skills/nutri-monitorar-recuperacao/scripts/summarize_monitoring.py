#!/usr/bin/env python3
"""Resumir métricas recentes sem aplicar limiares clínicos."""

import argparse
import datetime as dt
import json
import statistics
import sys


METRICS = (
    "training_minutes",
    "srpe",
    "sleep_hours",
    "hrv_ms",
    "rest_hr_bpm",
    "weight_kg",
    "intake_kcal",
    "adherence_pct",
    "fatigue_0_10",
)


def load_input(path):
    stream = sys.stdin if path == "-" else open(path, "r", encoding="utf-8")
    try:
        return json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def metric_summary(records, metric):
    dated = [(str(r.get("date", "")), float(r[metric])) for r in records if numeric(r.get(metric))]
    dated.sort(key=lambda item: item[0])
    values = [value for _, value in dated]
    if not values:
        return {"count": 0, "missing": len(records)}
    return {
        "count": len(values),
        "missing": len(records) - len(values),
        "mean": round(statistics.fmean(values), 3),
        "median": round(statistics.median(values), 3),
        "min": round(min(values), 3),
        "max": round(max(values), 3),
        "first": round(values[0], 3),
        "last": round(values[-1], 3),
        "first_last_delta": round(values[-1] - values[0], 3),
    }


def calculate(payload):
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("records deve ser uma lista não vazia")
    normalized = []
    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"records[{idx}] deve ser objeto")
        item = dict(record)
        try:
            item["date"] = dt.date.fromisoformat(str(item.get("date"))).isoformat()
        except ValueError as exc:
            raise ValueError(f"records[{idx}].date deve usar YYYY-MM-DD") from exc
        for metric in METRICS:
            value = item.get(metric)
            if value is not None and not numeric(value):
                raise ValueError(f"records[{idx}].{metric} deve ser numérico")
            if numeric(value) and value < 0:
                raise ValueError(f"records[{idx}].{metric} não pode ser negativo")
        if numeric(item.get("srpe")) and item["srpe"] > 10:
            raise ValueError(f"records[{idx}].srpe deve estar entre 0 e 10")
        if numeric(item.get("adherence_pct")) and item["adherence_pct"] > 100:
            raise ValueError(f"records[{idx}].adherence_pct deve estar entre 0 e 100")
        duration = item.get("training_minutes")
        srpe = item.get("srpe")
        if numeric(duration) and numeric(srpe):
            item["session_load"] = round(float(duration) * float(srpe), 3)
        normalized.append(item)
    summaries = {metric: metric_summary(normalized, metric) for metric in METRICS}
    summaries["session_load"] = metric_summary(normalized, "session_load")
    return {
        "records": len(normalized),
        "period_start": min(str(r.get("date", "")) for r in normalized),
        "period_end": max(str(r.get("date", "")) for r in normalized),
        "metrics": summaries,
        "automatic_risk_classification": False,
        "dates_validated": True,
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
