#!/usr/bin/python3

"""
implement object relation mapping using sqlalchemy
mapping class state to states table in relational db
"""


from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sys import argv


Base = declarative_base()


class State(Base):
    """State represent table in relational db
    Args:
        id (int): id of state
        name (string): name of state
    """
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
