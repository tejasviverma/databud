def calculate_health_score(profile):

    score = 100

    total_missing = sum(
        profile["missing_values"].values()
    )

    duplicates = profile["duplicate_rows"]

    score -= total_missing * 5

    score -= duplicates * 10

    score = max(score, 0)

    return score