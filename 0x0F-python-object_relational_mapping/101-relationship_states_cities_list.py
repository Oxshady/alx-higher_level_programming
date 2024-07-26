#!/usr/bin/python3
"""
select data from two related tables using join
"""
import relationship_state
import relationship_city
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        State = relationship_state.State
        City = relationship_city.City
        data = session.query(State).outerjoin(City).order_by(State.id, City.id).all()
        for state in data:
            print(f"{state.id}: {state.name}")
            if state.cities:
                for city in state.cities:
                    print(f"\t{city.id}: {city.name}")
