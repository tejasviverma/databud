import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_analysis(
    profile,
    statistics,
    insights
):

    prompt = f"""
    You are a senior business analyst.

    Dataset Profile:
    {profile}

    Statistics:
    {statistics}

    Existing Insights:
    {insights}

    Write:

    1. Executive Summary
    2. Key Findings
    3. Business Recommendations

    Keep it professional and concise.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")

    return """
    AI analysis could not be generated at this time.

    The report was generated successfully,
    but the AI service is temporarily unavailable.
    """