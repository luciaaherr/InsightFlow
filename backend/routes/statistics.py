from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

import pandas as pd

from backend.services.statistics_service import (
    generate_column_statistics,
)

router = APIRouter(
    prefix="/datasets",
    tags=["Statistics"],
)


@router.post("/statistics")
async def generate_statistics(
    file: UploadFile = File(...),
):
    df = pd.read_csv(file.file)

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    statistics = {}

    for column in numeric_columns:
        statistics[column] = generate_column_statistics(
            df,
            column,
        )

    return {
        "filename": file.filename,
        "statistics": statistics,
    }
