from app.agents.base_agent import BaseAgent


class QueryAgent(BaseAgent):

    def run(self, state):

        question = state["question"].lower()

        if (
            "average revenue" in question
            or "mean revenue" in question
        ):

            state["answer"] = (
                f"Average revenue is "
                f"{state['stats']['Revenue']['mean']}"
            )

            state["answered"] = True

            return state

        if "health" in question:

            state["answer"] = (
                f"Dataset health score is "
                f"{state['health_score']}/100"
            )

            state["answered"] = True

            return state

        if (
            "rows" in question
        ):

            state["answer"] = (
                f"The dataset contains "
                f"{state['profile']['rows']} rows."
            )

            state["answered"] = True

            return state

        if "columns" in question:

            state["answer"] = (
                f"The dataset contains "
                f"{state['profile']['columns']} columns."
            )

            state["answered"] = True

            return state

        state["answered"] = False

        return state