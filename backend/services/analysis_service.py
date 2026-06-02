import pandas as pd


def get_basic_summary(df: pd.DataFrame) -> dict:
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": df.columns.tolist(),
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "missing_values": df.isnull().sum().to_dict(),
    }


def generate_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    insights.extend(_generate_dataset_overview_insights(df))
    insights.extend(_generate_missing_values_insights(df))
    insights.extend(_generate_numeric_column_insights(df))
    insights.extend(_generate_sales_insights(df))
    insights.extend(_generate_profitability_insights(df))
    insights.extend(_generate_satisfaction_insights(df))

    return insights


def _generate_dataset_overview_insights(df: pd.DataFrame) -> list[str]:
    rows, columns = df.shape

    return [
        f"El dataset contiene {rows} filas y {columns} columnas."
    ]


def _generate_missing_values_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    missing_values = df.isnull().sum()
    columns_with_missing_values = missing_values[missing_values > 0]

    if columns_with_missing_values.empty:
        return ["No se detectaron valores faltantes en el dataset."]

    for column, count in columns_with_missing_values.items():
        insights.append(
            f"La columna '{column}' tiene {count} valores faltantes."
        )

    return insights


def _generate_numeric_column_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        average = df[column].mean()
        max_value = df[column].max()
        min_value = df[column].min()
        standard_deviation = df[column].std()

        insights.append(
            f"La columna '{column}' tiene un promedio de {average:.2f}, "
            f"con valores entre {min_value:.2f} y {max_value:.2f}."
        )

        if abs(average) > 0 and standard_deviation > abs(average) * 0.5:
            insights.append(
                f"La variable '{column}' presenta alta variabilidad en sus valores."
            )

    return insights


def _generate_sales_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    if "Ventas" not in df.columns:
        return insights

    total_sales = df["Ventas"].sum()

    insights.append(
        f"Las ventas totales registradas alcanzan {total_sales:.2f}."
    )

    best_sale_row = df.loc[df["Ventas"].idxmax()]

    if "Producto" in df.columns:
        insights.append(
            f"El producto con mayor volumen de ventas es '{best_sale_row['Producto']}'."
        )

    if "Categoria" in df.columns:
        sales_by_category = df.groupby("Categoria")["Ventas"].sum()
        best_category = sales_by_category.idxmax()

        insights.append(
            f"La categoría con mejor rendimiento general es '{best_category}'."
        )

    return insights


def _generate_profitability_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    if "Ventas" not in df.columns or "Gastos" not in df.columns:
        return insights

    total_sales = df["Ventas"].sum()
    total_costs = df["Gastos"].sum()
    profit = total_sales - total_costs

    if total_sales == 0:
        return insights

    margin = (profit / total_sales) * 100

    insights.append(
        f"La ganancia estimada es de {profit:.2f}, "
        f"con un margen aproximado de {margin:.1f}%."
    )

    if margin > 40:
        insights.append("El negocio presenta un margen de ganancia alto.")
    elif margin > 20:
        insights.append("El negocio presenta un margen de ganancia saludable.")
    else:
        insights.append("El margen de ganancia parece relativamente bajo.")

    return insights


def _generate_satisfaction_insights(df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    if "Satisfaccion" not in df.columns:
        return insights

    satisfaction_average = df["Satisfaccion"].mean()

    insights.append(
        f"La satisfacción promedio de clientes es de {satisfaction_average:.2f}/10."
    )

    if satisfaction_average >= 9:
        insights.append("Los niveles de satisfacción son excelentes.")
    elif satisfaction_average >= 7:
        insights.append("Los niveles de satisfacción son positivos.")
    else:
        insights.append("La satisfacción de clientes podría mejorar.")

    return insights