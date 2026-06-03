from fastapi import FastAPI

from backend.database import Base
from backend.database import engine

from backend.models.dataset import Dataset

from backend.routes.datasets import (
    router as datasets_router,
)

from backend.routes.kpis import (
    router as kpis_router,
)

from backend.routes.statistics import (
    router as statistics_router,
)

from backend.routes.business_insights import (
    router as business_insights_router,
)

Base.metadata.create_all(
    bind=engine,
)

app = FastAPI(
    title="InsightFlow API",
    description="Backend API for InsightFlow",
    version="0.4.0",
)

app.include_router(
    datasets_router
)

app.include_router(
    kpis_router
)

app.include_router(
    statistics_router
)

app.include_router(
    business_insights_router
)


@app.get("/")
def root():
    return {
        "message": "Welcome to InsightFlow API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "InsightFlow API",
    }