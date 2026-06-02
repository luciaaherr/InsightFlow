import pandas as pd


def generate_column_statistics(df: pd.DataFrame, column: str) -> dict:
    return {
        "average": round(df[column].mean(), 2),
        "minimum": round(df[column].min(), 2),
        "maximum": round(df[column].max(), 2),
    }