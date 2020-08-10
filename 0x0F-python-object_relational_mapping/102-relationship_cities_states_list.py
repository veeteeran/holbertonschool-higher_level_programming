#!/usr/bin/python3
"""Lists City objects, from db hbtn_0e_101_usa"""
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

    records = session.query(City).all()
    i = 0
    for c in records:
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
        i += 1
