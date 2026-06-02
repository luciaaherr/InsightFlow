import pandas as pd


def get_basic_summary(df: pd.DataFrame) -> dict:
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "categorical_columns": list(df.select_dtypes(exclude="number").columns),
        "missing_values": df.isnull().sum().to_dict()
    }


def generate_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    rows, columns = df.shape

    insights.append(
        f"El dataset contiene {rows} filas y {columns} columnas."
    )

    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]

    if len(missing_cols) > 0:
        for col, count in missing_cols.items():
            insights.append(
                f"La columna '{col}' tiene {count} valores faltantes."
            )
    else:
        insights.append(
            "No se detectaron valores faltantes en el dataset."
        )

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        avg = df[col].mean()
        max_value = df[col].max()
        min_value = df[col].min()
        std = df[col].std()

        insights.append(
            f"La columna '{col}' tiene un promedio de {avg:.2f}, "
            f"con valores entre {min_value:.2f} y {max_value:.2f}."
        )

        if abs(avg) > 0 and std > abs(avg) * 0.5:
            insights.append(
                f"La variable '{col}' presenta alta variabilidad en sus valores."
            )

    if "Ventas" in df.columns:
        total_sales = df["Ventas"].sum()

        insights.append(
            f"Las ventas totales registradas alcanzan {total_sales:.2f}."
        )

        best_row = df.loc[df["Ventas"].idxmax()]

        if "Producto" in df.columns:
            insights.append(
                f"El producto con mayor volumen de ventas es '{best_row['Producto']}'."
            )

    if "Categoria" in df.columns and "Ventas" in df.columns:
        grouped = df.groupby("Categoria")["Ventas"].sum()
        best_category = grouped.idxmax()

        insights.append(
            f"La categoría con mejor rendimiento general es '{best_category}'."
        )

    if "Ventas" in df.columns and "Gastos" in df.columns:
        total_sales = df["Ventas"].sum()
        total_costs = df["Gastos"].sum()

        profit = total_sales - total_costs

        if total_sales != 0:
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

    if "Satisfaccion" in df.columns:
        satisfaction_avg = df["Satisfaccion"].mean()

        insights.append(
            f"La satisfacción promedio de clientes es de {satisfaction_avg:.2f}/10."
        )

        if satisfaction_avg >= 9:
            insights.append("Los niveles de satisfacción son excelentes.")
        elif satisfaction_avg >= 7:
            insights.append("Los niveles de satisfacción son positivos.")
        else:
            insights.append("La satisfacción de clientes podría mejorar.")

    return insights