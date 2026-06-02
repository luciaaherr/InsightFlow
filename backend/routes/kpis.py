from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

import pandas as pd

from backend.services.kpi_service import (
    generate_dashboard_kpis,
)

router = APIRouter(
    prefix="/datasets",
    tags=["KPIs"],
)


@router.post("/kpis")
async def generate_kpis(
    file: UploadFile = File(...),
):
    df = pd.read_csv(file.file)

    kpis = generate_dashboard_kpis(df)

    return {
        "filename": file.filename,
        "kpis": kpis,
    }