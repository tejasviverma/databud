from app.agents.base_agent import BaseAgent
from app.services.chat_analyst import answer_question


class GeminiAgent(BaseAgent):

    def run(self, state):

        state["answer"] = answer_question(
            state["df"],
            state["question"]
        )

        state["answered"] = True

        return state