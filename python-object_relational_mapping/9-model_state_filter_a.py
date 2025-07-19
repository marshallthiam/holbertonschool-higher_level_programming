#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects that contain the letter 'a', sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == '__main__':
    main()
