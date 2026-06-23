import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    profile,
    statistics,
    insights,
    ai_analysis,
    health_score,
    charts
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_path = os.path.join(
        "reports",
        f"analysis_report_{timestamp}.pdf"
    )

    doc = SimpleDocTemplate(report_path)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "DataBud Analysis Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Rows: {profile['rows']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Columns: {profile['columns']}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Business Insights",
            styles["Heading2"]
        )
    )

    content.append(
    Spacer(1, 20)
)

    content.append(
        Paragraph(
            "Revenue Distribution Chart",
            styles["Heading2"]
        )
    )
    
    content.append(
        Paragraph(
            f"Dataset Health Score: {health_score}/100",
            styles["BodyText"]
        )
    )

    for insight in insights:

        content.append(
            Paragraph(
                insight,
                styles["BodyText"]
            )
        )

    for chart_path in charts:

        if os.path.exists(chart_path):

            chart_name = (
            os.path.basename(chart_path)
            .replace("_histogram.png", "")
            .title()
        )

        content.append(
            Paragraph(
                f"{chart_name} Distribution",
                styles["Heading2"]
            )
        )

        content.append(
            Image(
                chart_path,
                width=350,
                height=220
            )
        )

        content.append(
            Spacer(1, 10)
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
    Paragraph(
        "AI Business Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Paragraph(
        ai_analysis.replace("\n", "<br/>"),
        styles["BodyText"]
    )
)
    

    doc.build(content)

    return report_path