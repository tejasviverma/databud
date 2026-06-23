import os
import matplotlib.pyplot as plt


def generate_histograms(df):

    os.makedirs(
        "charts",
        exist_ok=True
    )

    generated_charts = []

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:

        plt.figure(figsize=(8, 5))

        df[col].dropna().hist()

        plt.title(f"{col} Distribution")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        chart_path = os.path.join(
            "charts",
            f"{col}_histogram.png"
        )

        plt.savefig(chart_path)

        plt.close()

        generated_charts.append(chart_path)

    return generated_charts