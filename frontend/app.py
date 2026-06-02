import pandas as pd
import streamlit as st

from backend.services.analysis_service import generate_insights
from backend.services.business_insights_service import (
    generate_business_insights,
)
from backend.services.kpi_service import generate_dashboard_kpis
from backend.services.statistics_service import (
    generate_column_statistics,
)

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
st.sidebar.write("Versión 0.8")
st.sidebar.write("Stack: Python · Pandas · Plotly · Streamlit")
st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file",
    type=["csv"],
)

st.title("📊 InsightFlow")
st.markdown("### Turn raw CSV files into business insights")

st.write(
    "InsightFlow es una herramienta interactiva que transforma archivos CSV "
    "en métricas, visualizaciones e insights automáticos. "
    "Está pensada para explorar datos de negocio de forma rápida, "
    "clara y sin necesidad de conocimientos técnicos."
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

    dashboard_kpis = generate_dashboard_kpis(df)

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

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        kpi1.metric(
            "Filas",
            dashboard_kpis["rows"],
        )

        kpi2.metric(
            "Columnas",
            dashboard_kpis["columns"],
        )

        if dashboard_kpis["total_sales"] is not None:
            kpi3.metric(
                "Total ventas",
                dashboard_kpis["total_sales"],
            )

        else:
            kpi3.metric(
                "Columnas numéricas",
                dashboard_kpis["numeric_columns_count"],
            )

        if dashboard_kpis["estimated_profit"] is not None:
            kpi4.metric(
                "Ganancia estimada",
                dashboard_kpis["estimated_profit"],
            )

        elif dashboard_kpis["average_satisfaction"] is not None:
            kpi4.metric(
                "Satisfacción promedio",
                dashboard_kpis["average_satisfaction"],
            )

        else:
            kpi4.metric(
                "Columnas categóricas",
                dashboard_kpis["categorical_columns_count"],
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

        insights = generate_insights(df)

        for insight in insights:
            st.write(f"• {insight}")

        st.write("## Lectura de negocio")

        business_insights = generate_business_insights(df)

        for business_insight in business_insights:
            if business_insight["type"] == "info":
                st.info(
                    business_insight["message"]
                )

            elif business_insight["type"] == "success":
                st.success(
                    business_insight["message"]
                )

            else:
                st.write(
                    business_insight["message"]
                )

    with tab_visualizations:
        st.write("## Visualizaciones inteligentes")

        if numeric_columns:
            selected_numeric = st.selectbox(
                "Elegí una columna numérica para ver su distribución",
                numeric_columns,
                key="hist_numeric",
            )

            metric1, metric2, metric3 = st.columns(3)

            column_statistics = generate_column_statistics(
                df,
                selected_numeric,
            )

            metric1.metric(
                "Promedio",
                column_statistics["average"],
            )

            metric2.metric(
                "Mínimo",
                column_statistics["minimum"],
            )

            metric3.metric(
                "Máximo",
                column_statistics["maximum"],
            )

            visual_histogram = create_histogram(
                df,
                selected_numeric,
            )

            st.plotly_chart(
                visual_histogram,
                use_container_width=True,
                key="visualization_histogram",
            )

        if categorical_columns:
            selected_category = st.selectbox(
                "Elegí una columna categórica para analizar frecuencia",
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
                key="category_bar_chart",
            )

        if len(numeric_columns) >= 2:
            st.write("### Relación entre variables numéricas")

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
                key="numeric_scatter_plot",
            )

        if not numeric_columns and not categorical_columns:
            st.warning(
                "No se detectaron columnas aptas para graficar."
            )

    with tab_raw_data:
        st.write("## Datos originales")

        st.write("### Columnas detectadas")

        st.write(
            list(df.columns)
        )

        st.write("### Dataset completo")

        st.dataframe(
            df,
            use_container_width=True,
        )

else:
    st.info(
        "Subí un archivo CSV desde la barra lateral para comenzar."
    )