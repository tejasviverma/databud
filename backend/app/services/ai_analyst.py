from app.services.ai_service import (
    generate_response
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
        return generate_response(prompt)
    except Exception as e:
        print(f"AI Service Error: {e}")

    return """
    AI analysis could not be generated at this time.

    The report was generated successfully,
    but the AI service is temporarily unavailable.
    """