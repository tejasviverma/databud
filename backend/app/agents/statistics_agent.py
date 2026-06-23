from app.services.statistics import (
    get_numeric_summary
)


class StatisticsAgent:

    def run(self, df):

        print("Statistics Agent Running...")

        return get_numeric_summary(df)