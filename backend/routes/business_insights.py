from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

import pandas as pd

from backend.services.business_insights_service import (
    generate_business_insights,
)

router = APIRouter(
    prefix="/datasets",
    tags=["Business Insights"],
)


@router.post("/business-insights")
async def business_insights(
    file: UploadFile = File(...),
):
    df = pd.read_csv(file.file)

    insights = generate_business_insights(df)

    return {
        "filename": file.filename,
        "business_insights": insights,
    }