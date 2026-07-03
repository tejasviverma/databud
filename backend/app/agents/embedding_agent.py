from app.agents.base_agent import BaseAgent

from app.services.embeddings import (
    generate_embedding
)

class EmbeddingAgent(BaseAgent):

    def run(self, state):

        print("Embedding Agent Running...")

        for record in state["knowledge"]:

            record["embedding"] = generate_embedding(
                record["text"]
            )

        print(
        len(record["embedding"])
    )
        print(state["knowledge"][0])

        return state