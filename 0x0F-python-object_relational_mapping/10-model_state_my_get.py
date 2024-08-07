#!/usr/bin/python3
"""
implement object relation mapping using sqlalchemy
fet object with specific name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    state_name = argv[4]
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        x = session.query(State.id)
        x = x.filter_by(name=state_name).first()
        if x:
            print(x.id)
        else:
            print("Not found")
