from app.agents.query_agent import QueryAgent
from app.agents.gemini_agent import GeminiAgent


class RouterAgent:

    def __init__(self):

        self.query_agent = QueryAgent()
        self.gemini_agent = GeminiAgent()

    def run(self, state):

        question = state["question"].lower()

        query_keywords = [
            "average",
            "mean",
            "maximum",
            "minimum",
            "highest",
            "lowest",
            "rows",
            "columns",
            "health",
            "count",
            "total"
        ]

        for keyword in query_keywords:

            if keyword in question:

                return self.query_agent

        return self.gemini_agent