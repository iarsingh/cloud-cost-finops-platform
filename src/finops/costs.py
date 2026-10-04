class InputError(ValueError):
    pass


def summarize(lines, budget=None):
    if not isinstance(lines, list) or not lines:
        raise InputError("lines must be a non-empty list")
    by_service = {}
    total = 0.0
    for line in lines:
        try:
            amount = float(line["cost"])
        except (KeyError, TypeError, ValueError) as exc:
            raise InputError("each line needs a numeric cost") from exc
        svc = str(line.get("service", "unknown"))
        by_service[svc] = by_service.get(svc, 0.0) + amount
        total += amount
    over = budget is not None and total > budget
    return {
        "total": round(total, 4),
        "by_service": {k: round(v, 4) for k, v in by_service.items()},
        "over_budget": over,
        "applied": False,
    }
