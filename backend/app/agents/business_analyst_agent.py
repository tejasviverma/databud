from app.services.insights import (
    generate_insights
)

from app.services.ai_analyst import (
    generate_ai_analysis
)


class BusinessAnalystAgent:

    def run(self, state):

        print(
            "Business Analyst Agent Running..."
        )

        profile = state["profile"]
        stats = state["stats"]

        insights = generate_insights(
            profile,
            stats
        )

        ai_analysis = generate_ai_analysis(
            profile,
            stats,
            insights
        )

        state["insights"] = insights
        state["ai_analysis"] = ai_analysis

        return state