import pandas as pd


def generate_dashboard_kpis(df: pd.DataFrame) -> dict:
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    kpis = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_columns_count": len(numeric_columns),
        "categorical_columns_count": len(categorical_columns),
        "total_sales": None,
        "estimated_profit": None,
        "average_satisfaction": None,
    }

    if "Ventas" in df.columns:
        kpis["total_sales"] = round(df["Ventas"].sum(), 2)

    if "Ventas" in df.columns and "Gastos" in df.columns:
        kpis["estimated_profit"] = round(
            df["Ventas"].sum() - df["Gastos"].sum(), 2
        )

    if "Satisfaccion" in df.columns:
        kpis["average_satisfaction"] = round(df["Satisfaccion"].mean(), 2)

    return kpis