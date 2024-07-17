#!/usr/bin/python3
"""
implement object relation mapping using sqlalchemy
delete object
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
        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            print(state.name, state.id)
            session.delete(state)
        session.commit()
