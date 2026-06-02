import streamlit as st
import pandas as pd

from analysis import generate_insights
from visualizations import (
    get_numeric_columns,
    get_categorical_columns,
    create_histogram,
    create_bar_chart,
    create_scatter_plot
)

st.set_page_config(
    page_title="InsightFlow",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📊 InsightFlow")
st.sidebar.caption("CSV Analytics Dashboard")
st.sidebar.markdown("---")

st.sidebar.write("### Proyecto")
st.sidebar.success("Portfolio MVP")
st.sidebar.write("Versión 0.7")
st.sidebar.write("Stack: Python · Pandas · Plotly · Streamlit")
st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

st.title("📊 InsightFlow")
st.markdown("### Turn raw CSV files into business insights")

st.write(
    "InsightFlow es una herramienta interactiva que transforma archivos CSV en métricas, "
    "visualizaciones e insights automáticos. Está pensada para explorar datos de negocio "
    "de forma rápida, clara y sin necesidad de conocimientos técnicos."
)

st.caption("Developed by Lucía Hernández · Computer Engineering Student · Uruguay")
st.markdown("---")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("CSV cargado correctamente.")

    numeric_columns = get_numeric_columns(df)
    categorical_columns = get_categorical_columns(df)

    tab_dashboard, tab_insights, tab_visualizations, tab_raw_data = st.tabs(
        ["📊 Dashboard", "💡 Insights", "📈 Visualizaciones", "🧾 Datos"]
    )

    with tab_dashboard:
        st.write("## Resumen ejecutivo")

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        kpi1.metric("Filas", df.shape[0])
        kpi2.metric("Columnas", df.shape[1])

        if "Ventas" in df.columns:
            kpi3.metric("Total ventas", round(df["Ventas"].sum(), 2))
        else:
            kpi3.metric("Columnas numéricas", len(numeric_columns))

        if "Gastos" in df.columns and "Ventas" in df.columns:
            profit = df["Ventas"].sum() - df["Gastos"].sum()
            kpi4.metric("Ganancia estimada", round(profit, 2))
        elif "Satisfaccion" in df.columns:
            kpi4.metric("Satisfacción promedio", round(df["Satisfaccion"].mean(), 2))
        else:
            kpi4.metric("Columnas categóricas", len(categorical_columns))

        st.write("## Vista previa")
        st.dataframe(df.head(), use_container_width=True)

        if numeric_columns:
            st.write("## Distribución rápida")
            selected_quick = st.selectbox(
                "Elegí una métrica para visualizar",
                numeric_columns,
                key="quick_numeric"
            )

            dashboard_histogram = create_histogram(df, selected_quick)
            st.plotly_chart(
                dashboard_histogram,
                use_container_width=True,
                key="dashboard_histogram"
            )

    with tab_insights:
        st.write("## Insights automáticos")

        insights = generate_insights(df)

        for insight in insights:
            st.write(f"• {insight}")

        st.write("## Lectura de negocio")

        if "Ventas" in df.columns:
            best_sale_row = df.loc[df["Ventas"].idxmax()]
            st.info(
                f"La mayor venta registrada fue de {best_sale_row['Ventas']}."
            )

        if "Categoria" in df.columns and "Ventas" in df.columns:
            category_sales = df.groupby("Categoria")["Ventas"].sum()
            best_category = category_sales.idxmax()
            best_category_value = category_sales.max()

            st.success(
                f"La categoría con mayor volumen de ventas es '{best_category}', "
                f"con un total de {best_category_value}."
            )

        if "Ventas" in df.columns and "Gastos" in df.columns:
            total_sales = df["Ventas"].sum()
            total_costs = df["Gastos"].sum()
            profit = total_sales - total_costs

            st.write(
                f"El dataset muestra ventas totales por {round(total_sales, 2)}, "
                f"gastos totales por {round(total_costs, 2)} y una ganancia estimada "
                f"de {round(profit, 2)}."
            )

    with tab_visualizations:
        st.write("## Visualizaciones inteligentes")

        if numeric_columns:
            selected_numeric = st.selectbox(
                "Elegí una columna numérica para ver su distribución",
                numeric_columns,
                key="hist_numeric"
            )

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric("Promedio", round(df[selected_numeric].mean(), 2))
            metric2.metric("Mínimo", round(df[selected_numeric].min(), 2))
            metric3.metric("Máximo", round(df[selected_numeric].max(), 2))

            visual_histogram = create_histogram(df, selected_numeric)
            st.plotly_chart(
                visual_histogram,
                use_container_width=True,
                key="visualization_histogram"
            )

        if categorical_columns:
            selected_category = st.selectbox(
                "Elegí una columna categórica para analizar frecuencia",
                categorical_columns,
                key="bar_category"
            )

            bar_chart = create_bar_chart(df, selected_category)
            st.plotly_chart(
                bar_chart,
                use_container_width=True,
                key="category_bar_chart"
            )

        if len(numeric_columns) >= 2:
            st.write("### Relación entre variables numéricas")

            x_column = st.selectbox(
                "Variable X",
                numeric_columns,
                index=0,
                key="scatter_x"
            )

            y_column = st.selectbox(
                "Variable Y",
                numeric_columns,
                index=1,
                key="scatter_y"
            )

            scatter = create_scatter_plot(df, x_column, y_column)
            st.plotly_chart(
                scatter,
                use_container_width=True,
                key="numeric_scatter_plot"
            )

        if not numeric_columns and not categorical_columns:
            st.warning("No se detectaron columnas aptas para graficar.")

    with tab_raw_data:
        st.write("## Datos originales")
        st.write("### Columnas detectadas")
        st.write(list(df.columns))

        st.write("### Dataset completo")
        st.dataframe(df, use_container_width=True)

else:
    st.info("Subí un archivo CSV desde la barra lateral para comenzar.")