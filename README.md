InsightFlow

InsightFlow is an interactive data analytics platform built with Python, Streamlit, FastAPI, and PostgreSQL.

The application allows users to upload CSV datasets and automatically generate:

* business insights,
* KPIs,
* statistical summaries,
* interactive visualizations,
* exploratory data analysis.

The project uses a modular frontend/backend architecture with REST API communication and persistent dataset storage using PostgreSQL.

⸻

Live Demo

https://insightflow-luciaaherr.streamlit.app/

⸻

GitHub Repository

https://github.com/luciaaherr/InsightFlow

⸻

Features

* CSV upload and processing
* Automatic dataset analysis
* Dynamic KPI generation
* Interactive Plotly visualizations
* Missing values detection
* Statistical summaries
* Automatic numerical and categorical column detection
* FastAPI backend architecture
* PostgreSQL database integration
* Persistent dataset history
* REST API endpoints
* Swagger API documentation
* Modular project structure
* Frontend/backend separation

⸻

Technologies Used

Frontend

* Streamlit
* Plotly

Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Python
* Pandas

Development Tools

* Git
* GitHub
* Python Virtual Environment (venv)

Deployment

* Streamlit Community Cloud

⸻

Project Architecture

Frontend (Streamlit)
        ↓
REST API Requests
        ↓
Backend (FastAPI)
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database

⸻

Project Structure

InsightFlow/
├── frontend/
│   ├── app.py
│   ├── analysis.py
│   ├── visualizations.py
│   └── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── database.py
│   │
│   ├── routes/
│   │   ├── datasets.py
│   │   ├── kpis.py
│   │   ├── statistics.py
│   │   └── business_insights.py
│   │
│   ├── models/
│   │   ├── dataset.py
│   │   └── user.py
│   │
│   └── services/
│       ├── analysis_service.py
│       ├── kpi_service.py
│       ├── statistics_service.py
│       └── business_insight_service.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
⸻

Current API Endpoints

Datasets

* POST /datasets/insights
* GET /datasets/history

KPIs

* POST /datasets/kpis

Statistics

* POST /datasets/statistics

⸻

How to Run Locally

Clone repository

git clone https://github.com/luciaaherr/InsightFlow.git

Enter project folder

cd InsightFlow

Create virtual environment

python3 -m venv venv

Activate virtual environment

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

⸻

PostgreSQL Setup

Install PostgreSQL locally and create the database:

CREATE DATABASE insightflow_db;

The backend uses SQLAlchemy ORM to connect to PostgreSQL and store uploaded dataset metadata.

⸻

Run Backend

./venv/bin/python -m uvicorn backend.main:app --reload

Backend documentation:

http://127.0.0.1:8000/docs

⸻

Run Frontend

./venv/bin/python -m streamlit run frontend/app.py

⸻

Future Improvements

* User authentication with JWT
* Multi-user dataset management
* Cloud PostgreSQL deployment
* Docker support
* Advanced analytics engine
* Export reports to PDF
* Dataset dashboards
* AI-generated insights
* Background processing system

⸻

Author

Lucía Hernández
Computer Engineering Student — Universidad de la República (Udelar)
