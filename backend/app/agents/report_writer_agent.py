from app.services.report_generator import (
    generate_pdf_report
)


class ReportWriterAgent:

    def run(
        self,
        profile,
        stats,
        insights,
        ai_analysis,
        health_score,
        charts
    ):

        print(
            "Report Writer Agent Running..."
        )

        return generate_pdf_report(
            profile,
            stats,
            insights,
            ai_analysis,
            health_score,
            charts
        )