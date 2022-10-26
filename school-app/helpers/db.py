from sqlalchemy import create_engine
from sqlalchemy.orm import Session

session = Session(
    create_engine(
        'mysql+mysqldb://root:Mihai10!@localhost:3306/nt12pythonschool'
    )
)
