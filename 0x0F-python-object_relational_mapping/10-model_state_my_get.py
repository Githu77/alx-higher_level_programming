#!/usr/bin/python3
"""all States objects that contain
the letter a from the database hbtn_0e_6_usa
"""

import imp
import sys#!/usr/bin/python3
"""state with name "passed" as argument from hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
