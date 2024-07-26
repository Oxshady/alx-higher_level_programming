#!/usr/bin/python3

"""
implement object relation mapping using sqlalchemy
mapping class city to  cities table in relational db
"""


from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sys import argv
from relationship_state import Base


class City (Base):
    """City represent table in relational db
    Args:
        id (int): id of city
        name (string): name of city
        state_id (int): id of state to est rel
    """
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey('states.id'))
