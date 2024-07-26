#!/usr/bin/python3
"""
access objeect from another related object
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import relationship_city
import relationship_state
from sys import argv
if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    State = relationship_state.State
    City = relationship_city.City
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        data = session.query(City).order_by(City.id).all()
        for city in data:
            print(f"{city.id}: {city.name} -> {city.state.name}")
