from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from backend.database import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    filename = Column(
        String,
        nullable=False,
    )

    rows = Column(
        Integer,
        nullable=False,
    )

    columns = Column(
        Integer,
        nullable=False,
    )

    upload_date = Column(
        DateTime,
        default=datetime.utcnow,
    )