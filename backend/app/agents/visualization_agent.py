from app.services.charts import (
    generate_histograms
)

class VisualizationAgent:

    def run(self, state):

        print("Visualization Agent Running...")

        charts = generate_histograms(
            state["df"]
        )

        state["charts"] = charts

        return state