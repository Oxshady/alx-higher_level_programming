#!/usr/bin/python3
"""
module of persisting object in tables
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import relationship_city
import relationship_state
if __name__ == "__main__":
    base = relationship_state.Base
    State = relationship_state.State
    City = relationship_city.City
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    base.metadata.create_all(bind=engine)
    state1 = State(name="California")
    city = City(name="San Francisco", state=state1)
    with Session() as session:
        try:
            session.add(city)
            session.commit()
        except Exception:
            session.rollback()
