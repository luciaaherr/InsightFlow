import pandas as pd

from fastapi import APIRouter, UploadFile, File

from backend.services.analysis_service import generate_insights


router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.post("/insights")
async def generate_dataset_insights(
    file: UploadFile = File(...)
):
    df = pd.read_csv(file.file)

    insights = generate_insights(df)

    return {
        "filename": file.filename,
        "insights": insights,
    }