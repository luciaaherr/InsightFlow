InsightFlow

InsightFlow is an interactive data analytics web application built with Python and Streamlit.

The application allows users to upload CSV datasets and automatically generate:

* business insights,
* KPIs,
* interactive visualizations,
* statistical summaries,
* exploratory data analysis.

Live Demo

https://insightflow-luciaaherr.streamlit.app/

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
* Automatic categorical and numerical column detection
* Modular project structure
* Frontend and backend architecture preparation

⸻

Technologies Used

Frontend

* Streamlit
* Plotly

Backend / Logic

* Python
* Pandas
* FastAPI (architecture setup)

Development Tools

* Git
* GitHub

Deployment

* Streamlit Community Cloud

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
│   │   ├── auth.py
│   │   ├── datasets.py
│   │   └── users.py
│   │
│   ├── models/
│   │   ├── dataset.py
│   │   └── user.py
│   │
│   └── services/
│       └── analysis_service.py
│
├── README.md
├── .gitignore
└── venv/

⸻

How to Run Locally

Clone repository

git clone https://github.com/luciaaherr/InsightFlow.git

Enter project folder

cd InsightFlow

Create virtual environment

python3 -m venv venv

Activate virtual environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install dependencies

pip install -r frontend/requirements.txt

Run frontend application

streamlit run frontend/app.py

⸻

Future Improvements

* PostgreSQL database integration
* Full FastAPI backend implementation
* User authentication with JWT
* Persistent dataset storage
* REST API endpoints
* Advanced analytics engine
* Docker support
* Cloud backend deployment

⸻

Author

Lucía Hernández
Computer Engineering Student — Universidad de la República (Udelar)