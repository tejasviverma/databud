from app.services.ai_analyst import generate_ai_analysis

result = generate_ai_analysis(
    {"rows": 5},
    {"Revenue": {"mean": 1280}},
    ["Revenue averages 1280"]
)

print(result)

