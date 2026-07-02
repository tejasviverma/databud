from app.agents.base_agent import BaseAgent

from app.agents.chunk_agent import (
    ChunkAgent
)

from app.services.document_parser import (
    parse_pdf
)


class DocumentAgent(BaseAgent):

    def run(self, state):

        print(
            "Document Agent Running..."
        )

        text = parse_pdf(
            state["file_path"]
        )

        state["document_text"] = text

        chunk_agent = ChunkAgent()

        state = chunk_agent.run(state)

        return state