from app.services.statistics import (
    get_numeric_summary
)


class StatisticsAgent:

    def run(self, state):

        print("Statistics Agent Running...")

        stats = get_numeric_summary(
            state["df"]
        )

        state["stats"] = stats

        return state