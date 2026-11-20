def assess(answers):
    scores = {}
    for area, answer in answers:
        if answer == "y":
            scores[area] = scores.get(area, 0) + 1

    if not scores:
        return {"area": "Explore", "score": 0, "scores": {}}

    area = max(scores, key=scores.get)
    return {"area": area.title(), "score": scores[area], "scores": scores}
