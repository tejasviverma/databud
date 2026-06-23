def generate_insights(profile, statistics):

    insights = []

    duplicate_rows = profile["duplicate_rows"]

    if duplicate_rows > 0:
        insights.append(
            f"Dataset contains {duplicate_rows} duplicate rows."
        )

    for column, stats in statistics.items():

        insights.append(
            f"{column} averages {stats['mean']:.2f}."
        )

        insights.append(
            f"{column} ranges from "
            f"{stats['min']:.2f} to "
            f"{stats['max']:.2f}."
        )

    return insights