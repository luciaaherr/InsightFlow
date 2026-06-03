import pandas as pd

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database import get_database

from backend.models.dataset import Dataset

from backend.services.analysis_service import generate_insights


router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.post("/insights")
async def generate_dataset_insights(
    file: UploadFile = File(...),
    database: Session = Depends(get_database),
):
    df = pd.read_csv(file.file)

    insights = generate_insights(df)

    dataset = Dataset(
        filename=file.filename,
        rows=df.shape[0],
        columns=df.shape[1],
    )

    database.add(dataset)

    database.commit()

    database.refresh(dataset)

    return {
        "filename": file.filename,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "insights": insights,
    }


@router.get("/history")
def get_dataset_history(
    database: Session = Depends(get_database),
):
    datasets = database.query(Dataset).all()

    return [
        {
            "id": dataset.id,
            "filename": dataset.filename,
            "rows": dataset.rows,
            "columns": dataset.columns,
            "upload_date": dataset.upload_date,
        }
        for dataset in datasets
    ]