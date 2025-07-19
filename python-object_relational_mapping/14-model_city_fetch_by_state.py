#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Set up the engine and session
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities, joined with their corresponding state
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
