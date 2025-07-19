#!/usr/bin/python3
"""
Script that changes the name of a State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create database engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Fetch the State with id = 2
    state = session.query(State).filter_by(id=2).first()

    # If found, update its name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
