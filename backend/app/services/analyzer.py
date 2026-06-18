from app.services.profiler import get_profile
from app.services.statistics import get_numeric_summary


def analyze_dataframe(df):

    profile = get_profile(df)

    stats = get_numeric_summary(df)

    return {
        **profile,
        "numeric_summary": stats
    }