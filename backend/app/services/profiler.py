import pandas as pd

def get_profile(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),

        "column_names": df.columns.tolist(),

        "missing_values": df.isnull().sum().to_dict(),

        "duplicate_rows": int(df.duplicated().sum()),

        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        }
    }