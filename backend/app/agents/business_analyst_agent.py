from app.services.insights import (
    generate_insights
)

from app.services.ai_analyst import (
    generate_ai_analysis
)


class BusinessAnalystAgent:

    def run(
        self,
        profile,
        stats
    ):

        print(
            "Business Analyst Agent Running..."
        )

        insights = generate_insights(
            profile,
            stats
        )

        ai_analysis = generate_ai_analysis(
            profile,
            stats,
            insights
        )

        return {
            "insights": insights,
            "ai_analysis": ai_analysis
        }