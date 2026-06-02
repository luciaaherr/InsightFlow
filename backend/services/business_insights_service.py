import pandas as pd


def generate_business_insights(df: pd.DataFrame) -> list[dict]:
    insights: list[dict] = []

    insights.extend(_generate_best_sale_insight(df))
    insights.extend(_generate_best_category_insight(df))
    insights.extend(_generate_profit_summary_insight(df))

    return insights


def _generate_best_sale_insight(df: pd.DataFrame) -> list[dict]:
    if "Ventas" not in df.columns:
        return []

    best_sale_row = df.loc[df["Ventas"].idxmax()]

    return [
        {
            "type": "info",
            "message": f"La mayor venta registrada fue de {best_sale_row['Ventas']}."
        }
    ]


def _generate_best_category_insight(df: pd.DataFrame) -> list[dict]:
    if "Categoria" not in df.columns or "Ventas" not in df.columns:
        return []

    category_sales = df.groupby("Categoria")["Ventas"].sum()
    best_category = category_sales.idxmax()
    best_category_value = category_sales.max()

    return [
        {
            "type": "success",
            "message": (
                f"La categoría con mayor volumen de ventas es '{best_category}', "
                f"con un total de {best_category_value}."
            )
        }
    ]


def _generate_profit_summary_insight(df: pd.DataFrame) -> list[dict]:
    if "Ventas" not in df.columns or "Gastos" not in df.columns:
        return []

    total_sales = df["Ventas"].sum()
    total_costs = df["Gastos"].sum()
    profit = total_sales - total_costs

    return [
        {
            "type": "text",
            "message": (
                f"El dataset muestra ventas totales por {round(total_sales, 2)}, "
                f"gastos totales por {round(total_costs, 2)} y una ganancia estimada "
                f"de {round(profit, 2)}."
            )
        }
    ]