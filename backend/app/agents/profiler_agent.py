from app.services.profiler import get_profile


class ProfilerAgent:

    def run(self, df):

        print("Profiler Agent Running...")

        return get_profile(df)