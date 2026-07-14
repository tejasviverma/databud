from app.agents.base_agent import BaseAgent

from app.services.document_chat import (
    answer_document_question
)


class DocumentGeminiAgent(BaseAgent):

    def run(self, state):

        print(
            "Document Gemini Agent Running..."
        )

        answer = answer_document_question(
            context=state["context"],
            question=state["question"]
        )

        state["answer"] = answer

        return state