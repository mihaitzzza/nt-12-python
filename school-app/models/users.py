from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from models.base import DeclarativeBase, BaseModel
from utility.enums import RoleTypes


class Role(DeclarativeBase, BaseModel):
    __tablename__ = 'roles'
    name = Column(Enum(RoleTypes), default=RoleTypes.student, unique=True)


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'users'
    first_name = Column(VARCHAR(255))
    last_name = Column(VARCHAR(255))
    email = Column(VARCHAR(255), unique=True)
    password = Column(VARCHAR(255))

    role_id = Column(INTEGER, ForeignKey(Role.id))
    role = relationship(Role)
