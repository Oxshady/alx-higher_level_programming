#!/usr/bin/python3
"""
implement object relation mapping using sqlalchemy
get first row from data
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        obj = session.query(State).order_by(State.id).first()
        print(f"{obj.id}: {obj.name}")
