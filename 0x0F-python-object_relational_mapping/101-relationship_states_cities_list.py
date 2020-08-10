#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects,
in db hbtn_0e_101_usa
"""
if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    records = session.query(State).all()
    for s in records:
        print("{}: {}".format(s.id, s.name))
        for i in range(len(s.cities)):
            print("\t{}: {}".format(s.cities[i].id, s.cities[i].name))
