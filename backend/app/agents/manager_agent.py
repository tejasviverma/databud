from app.agents.profiler_agent import (
    ProfilerAgent
)

from app.agents.statistics_agent import (
    StatisticsAgent
)

from app.agents.visualization_agent import (
    VisualizationAgent
)

from app.agents.business_analyst_agent import (
    BusinessAnalystAgent
)

from app.agents.report_writer_agent import (
    ReportWriterAgent
)

from app.services.health_score import (
    calculate_health_score
)


class ManagerAgent:

    def __init__(self):

        self.profiler = ProfilerAgent()

        self.statistics = StatisticsAgent()

        self.visualizer = VisualizationAgent()

        self.business = BusinessAnalystAgent()

        self.reporter = ReportWriterAgent()

    def run(self, df):

        # Shared state (currently only used by ProfilerAgent)
        state = {
            "df": df,
            "profile": None,
            "stats": None,
            "charts": None,
            "insights": None,
            "ai_analysis": None,
            "health_score": None,
            "report": None
        }

        # ProfilerAgent now writes into shared state
        state = self.profiler.run(state)

        profile = state["profile"]

        # Remaining agents still use the old approach
        state = self.statistics.run(state)
        stats = state["stats"]

        state = self.visualizer.run(state)
        charts = state["charts"]

        health_score = calculate_health_score(
            profile
        )

        business_result = self.business.run(
            profile,
            stats
        )

        report_path = self.reporter.run(
            profile,
            stats,
            business_result["insights"],
            business_result["ai_analysis"],
            health_score,
            charts
        )

        return {
            **profile,
            "numeric_summary": stats,
            "generated_charts": charts,
            "insights": business_result["insights"],
            "ai_analysis": business_result["ai_analysis"],
            "health_score": health_score,
            "report": report_path
        }