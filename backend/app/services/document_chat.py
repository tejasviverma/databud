from app.services.gemini_client import client

def answer_document_question(
    context,
    question
):
    prompt = f"""
        You are an AI assistant for document question answering.

        Answer the user's question using ONLY the information provided in the context below.

        If the answer is not explicitly present in the context, respond with:

        "I don't have enough information in the provided document to answer that."

        Do not use prior knowledge.
        Do not make assumptions.
        Do not infer missing information.
        Do not hallucinate.

Context:
{context}

Question:
{question}

        Answer:
        """
    
    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text
    
    except Exception as e:

        print(f"Document Chat Error: {e}")
        return "Sorry, an error occurred while generating the answer."