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

        profile = self.profiler.run(df)

        stats = self.statistics.run(df)

        charts = self.visualizer.run(df)

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