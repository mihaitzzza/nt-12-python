from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER

DeclarativeBase = declarative_base()


class BaseModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)
