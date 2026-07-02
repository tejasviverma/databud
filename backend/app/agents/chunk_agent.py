from app.agents.base_agent import BaseAgent

from app.services.chunking import (
    chunk_text
)

class ChunkAgent(BaseAgent):

    def run(self, state):

        print("Chunk Agent Running...")

        chunks = chunk_text(
            state["document_text"]
        )

        state["chunks"] = chunks

        return state