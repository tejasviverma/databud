from app.agents.base_agent import BaseAgent

from app.services.vector_store import (
    create_index
)


class IndexingAgent(BaseAgent):

    def run(self, state):

        print(
            "Indexing Agent Running..."
        )

        index = create_index(
            state["knowledge"]
        )

        state["vector_index"] = index

        return state