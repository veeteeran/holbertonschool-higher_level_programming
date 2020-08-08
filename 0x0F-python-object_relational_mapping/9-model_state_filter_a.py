#!/usr/bin/python3
"""Lists all State objects containing 'a' in db hbtn_0e_6_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format
            (sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%')).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
