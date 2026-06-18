def get_numeric_summary(df):
    numeric_summary = {}

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:
        numeric_summary[col] = {
            "mean": float(df[col].mean()),
            "median": float(df[col].median()),
            "min": float(df[col].min()),
            "max": float(df[col].max()),
            "std": float(df[col].std())
        }

    return numeric_summary