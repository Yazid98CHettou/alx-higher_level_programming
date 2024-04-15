#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import seionmaker
from model_state import State
if __name__ == '__main__':
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = seionmaker(bind=engine)
    session = Session()
    up_state = session.query(State).filter_by(id=2).first()
    up_state.name = 'New Mexico'
    session.commit()
