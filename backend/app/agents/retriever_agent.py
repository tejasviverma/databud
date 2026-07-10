from app.agents.base_agent import BaseAgent
from app.services.retriever import retrieve


class RetrieverAgent(BaseAgent):

    def run(self, state):

        print(
            "Retriever Agent Running..."
        )

        context = retrieve(
            question=state["question"],
            index=state["vector_index"],
            knowledge=state["knowledge"]
        )

        state["context"] = context

        return state