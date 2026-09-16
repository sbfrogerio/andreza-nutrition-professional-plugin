#!/usr/bin/env python3
"""Agregar sessões por semana sem classificar risco ou prescrever treino."""

import argparse
import collections
import datetime as dt
import json
import statistics
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


def parse_date(value, field):
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError as exc:
        raise ValueError(f"{field} deve usar YYYY-MM-DD") from exc


def calculate(payload):
    sessions = payload.get("sessions")
    if not isinstance(sessions, list) or not sessions:
        raise ValueError("sessions deve ser uma lista não vazia")
    weeks = collections.defaultdict(list)
    for idx, session in enumerate(sessions):
        if not isinstance(session, dict):
            raise ValueError(f"sessions[{idx}] deve ser objeto")
        day = parse_date(session.get("date"), f"sessions[{idx}].date")
        duration = session.get("duration_min")
        srpe = session.get("srpe")
        if duration is not None and (not numeric(duration) or duration < 0):
            raise ValueError(f"sessions[{idx}].duration_min inválido")
        if srpe is not None and (not numeric(srpe) or srpe < 0 or srpe > 10):
            raise ValueError(f"sessions[{idx}].srpe inválido")
        iso_year, iso_week, _ = day.isocalendar()
        item = dict(session)
        item["_date"] = day
        item["session_load"] = (
            round(float(duration) * float(srpe), 3)
            if numeric(duration) and numeric(srpe)
            else None
        )
        weeks[(iso_year, iso_week)].append(item)

    output = []
    for (year, week), items in sorted(weeks.items()):
        duration_total = sum(float(x["duration_min"]) for x in items if numeric(x.get("duration_min")))
        loads = [float(x["session_load"]) for x in items if numeric(x.get("session_load"))]
        weekly_load = sum(loads)
        monday = dt.date.fromisocalendar(year, week, 1)
        daily = [0.0] * 7
        for item in items:
            if numeric(item.get("session_load")):
                daily[(item["_date"] - monday).days] += float(item["session_load"])
        mean_daily = statistics.fmean(daily)
        sd_daily = statistics.pstdev(daily)
        monotony = None if sd_daily == 0 else mean_daily / sd_daily
        strain = None if monotony is None else weekly_load * monotony
        output.append(
            {
                "iso_week": f"{year}-W{week:02d}",
                "sessions": len(items),
                "sessions_with_load": len(loads),
                "duration_min": round(duration_total, 3),
                "session_rpe_load": round(weekly_load, 3),
                "daily_load_mean": round(mean_daily, 3),
                "daily_load_sd": round(sd_daily, 3),
                "monotony_descriptive": None if monotony is None else round(monotony, 3),
                "strain_descriptive": None if strain is None else round(strain, 3),
            }
        )
    return {
        "weeks": output,
        "risk_thresholds_applied": False,
        "training_recommendation_generated": False,
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

