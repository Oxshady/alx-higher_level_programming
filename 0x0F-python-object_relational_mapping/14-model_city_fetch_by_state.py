#!/usr/bin/python3

"""
implement object relation mapping using sqlalchemy
select some data and take adv of relation
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        data = session.query(City, State)
        data = data.filter(City.state_id == State.id).all()
        for city, state in data:
            print(f"{state.name}: ({city.id}) {city.name}")
