from app.services.report_generator import (
    generate_pdf_report
)


class ReportWriterAgent:

    def run(self, state):

        print(
            "Report Writer Agent Running..."
        )

        report = generate_pdf_report(
            state["profile"],
            state["stats"],
            state["insights"],
            state["ai_analysis"],
            state["health_score"],
            state["charts"]
        )

        state["report"] = report

        return state