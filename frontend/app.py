import pandas as pd
import requests
import streamlit as st

from visualizations import (
    create_bar_chart,
    create_histogram,
    create_scatter_plot,
    get_categorical_columns,
    get_numeric_columns,
)

st.set_page_config(
    page_title="InsightFlow",
    page_icon="📊",
    layout="wide",
)

st.sidebar.title("📊 InsightFlow")
st.sidebar.caption("CSV Analytics Dashboard")
st.sidebar.markdown("---")

st.sidebar.write("### Proyecto")
st.sidebar.success("Portfolio MVP")
st.sidebar.write("Versión 1.0")

st.sidebar.write(
    "Stack: Python · FastAPI · Pandas · Plotly · Streamlit"
)

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file",
    type=["csv"],
)

st.title("📊 InsightFlow")

st.markdown(
    "### Turn raw CSV files into business insights"
)

st.write(
    "InsightFlow es una herramienta interactiva que transforma "
    "archivos CSV en métricas, visualizaciones e insights "
    "automáticos."
)

st.caption(
    "Developed by Lucía Hernández · Computer Engineering Student · Uruguay"
)

st.markdown("---")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("CSV cargado correctamente.")

    numeric_columns = get_numeric_columns(df)

    categorical_columns = get_categorical_columns(df)

    response = requests.post(
        "http://127.0.0.1:8000/datasets/insights",
        files={
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "text/csv",
            )
        },
    )

    response_data = response.json()

    insights = response_data["insights"]

    tab_dashboard, tab_insights, tab_visualizations, tab_raw_data = st.tabs(
        [
            "📊 Dashboard",
            "💡 Insights",
            "📈 Visualizaciones",
            "🧾 Datos",
        ]
    )

    with tab_dashboard:
        st.write("## Resumen ejecutivo")

        kpi1, kpi2 = st.columns(2)

        kpi1.metric(
            "Filas",
            df.shape[0],
        )

        kpi2.metric(
            "Columnas",
            df.shape[1],
        )

        st.write("## Vista previa")

        st.dataframe(
            df.head(),
            use_container_width=True,
        )

        if numeric_columns:
            st.write("## Distribución rápida")

            selected_quick = st.selectbox(
                "Elegí una métrica para visualizar",
                numeric_columns,
                key="quick_numeric",
            )

            dashboard_histogram = create_histogram(
                df,
                selected_quick,
            )

            st.plotly_chart(
                dashboard_histogram,
                use_container_width=True,
                key="dashboard_histogram",
            )

    with tab_insights:
        st.write("## Insights automáticos")

        for insight in insights:
            st.write(f"• {insight}")

    with tab_visualizations:
        st.write("## Visualizaciones inteligentes")

        if numeric_columns:
            selected_numeric = st.selectbox(
                "Elegí una columna numérica",
                numeric_columns,
                key="hist_numeric",
            )

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "Promedio",
                round(df[selected_numeric].mean(), 2),
            )

            metric2.metric(
                "Mínimo",
                round(df[selected_numeric].min(), 2),
            )

            metric3.metric(
                "Máximo",
                round(df[selected_numeric].max(), 2),
            )

            visual_histogram = create_histogram(
                df,
                selected_numeric,
            )

            st.plotly_chart(
                visual_histogram,
                use_container_width=True,
                key="visual_histogram",
            )

        if categorical_columns:
            selected_category = st.selectbox(
                "Elegí una columna categórica",
                categorical_columns,
                key="bar_category",
            )

            bar_chart = create_bar_chart(
                df,
                selected_category,
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True,
                key="bar_chart",
            )

        if len(numeric_columns) >= 2:
            st.write("### Relación entre variables")

            x_column = st.selectbox(
                "Variable X",
                numeric_columns,
                index=0,
                key="scatter_x",
            )

            y_column = st.selectbox(
                "Variable Y",
                numeric_columns,
                index=1,
                key="scatter_y",
            )

            scatter = create_scatter_plot(
                df,
                x_column,
                y_column,
            )

            st.plotly_chart(
                scatter,
                use_container_width=True,
                key="scatter_plot",
            )

        if not numeric_columns and not categorical_columns:
            st.warning(
                "No se detectaron columnas aptas para graficar."
            )

    with tab_raw_data:
        st.write("## Datos originales")

        st.dataframe(
            df,
            use_container_width=True,
        )

else:
    st.info(
        "Subí un archivo CSV desde la barra lateral para comenzar."
    )