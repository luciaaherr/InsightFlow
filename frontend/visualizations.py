import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure


def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    return df.select_dtypes(include="number").columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> list[str]:
    return df.select_dtypes(exclude="number").columns.tolist()


def create_histogram(
    df: pd.DataFrame,
    column: str,
) -> Figure:
    return px.histogram(
        df,
        x=column,
        title=f"Distribución de {column}",
    )


def create_bar_chart(
    df: pd.DataFrame,
    column: str,
) -> Figure:
    value_counts = (
        df[column]
        .value_counts()
        .head(10)
        .reset_index()
    )

    value_counts.columns = [column, "count"]

    return px.bar(
        value_counts,
        x=column,
        y="count",
        title=f"Top 10 frecuencias de {column}",
    )


def create_scatter_plot(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
) -> Figure:
    return px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"Relación entre {x_column} y {y_column}",
    )