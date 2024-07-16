#!/usr/bin/python3
"""
implement object relation mapping using sqlalchemy
mapping class state to states table in relational db
"""


from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, mapped_column
from sqlalchemy.orm import Mapped
from sys import argv


url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class State(Base):
    """State represent table in relational db
    Args:
        id (int): id of state
        name (string): name of state
    """
    tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
