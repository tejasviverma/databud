from app.services.charts import (
    generate_histograms
)


class VisualizationAgent:

    def run(self, df):

        print("Visualization Agent Running...")

        return generate_histograms(df)