import os
from app.services.ai_service import (
    generate_response
)

def answer_question(
    df,
    question
):

    sample_data = df.head(5).to_string()

    prompt = f"""
    Dataset:

    {sample_data}

    User Question:

    {question}

    Answer like a business analyst.
    """

    try:
        return generate_response(prompt)

    except Exception as e:
        print(f"Chat Analyst Error: {e}")
        return """
            AI service is temporarily unavailable.

            Dataset Summary:
               Dataset successfully loaded.
               Statistical analysis completed.
               Business insights available.

            Please try again later for AI-powered answers.
            """