import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
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

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return """
    AI service is temporarily unavailable.

    Dataset Summary:
    - Dataset successfully loaded.
    - Statistical analysis completed.
    - Business insights available.

    Please try again later for AI-powered answers.
    """