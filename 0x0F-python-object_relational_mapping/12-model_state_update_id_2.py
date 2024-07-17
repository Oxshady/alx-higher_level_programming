#!/usr/bin/python3
"""
implement object relation mapping using sqlalchemy
updating the data of object
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    obj = "Louisiana"
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = "New Mexico"
            session.commit()
