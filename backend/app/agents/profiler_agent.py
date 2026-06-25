from app.services.profiler import get_profile


class ProfilerAgent:

    def run(self, state):

        print("Profiler Agent Running...")

        profile = get_profile(
            state["df"]
        )

        state["profile"] = profile

        return state