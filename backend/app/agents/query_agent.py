class QueryAgent:

    def run(
        self,
        question,
        state
    ):

        question = question.lower()

        if (
            "average revenue" in question
            or "mean revenue" in question
        ):

            return {
                "answered": True,
                "answer":
                f"Average revenue is {state['stats']['Revenue']['mean']}"
            }

        if (
            "health score" in question
        ):

            return {
                "answered": True,
                "answer":
                f"Dataset health score is {state['health_score']}/100"
            }

        if (
            "how many rows" in question
            or "row count" in question
        ):

            return {
                "answered": True,
                "answer":
                f"The dataset contains {state['profile']['rows']} rows."
            }

        if (
            "how many columns" in question
        ):

            return {
                "answered": True,
                "answer":
                f"The dataset contains {state['profile']['columns']} columns."
            }

        return {
            "answered": False
        }