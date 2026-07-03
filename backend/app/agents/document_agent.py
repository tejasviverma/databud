from app.agents.chunk_agent import ChunkAgent
from app.agents.embedding_agent import EmbeddingAgent
from app.services.document_parser import parse_pdf
from app.agents.base_agent import BaseAgent


class DocumentAgent(BaseAgent):

    def run(self, state):

        print("Document Agent Running...")

        text = parse_pdf(
            state["file_path"]
        )

        state["document_text"] = text

        chunk_agent = ChunkAgent()
        state = chunk_agent.run(state)

        embedding_agent = EmbeddingAgent()
        state = embedding_agent.run(state)

        return state