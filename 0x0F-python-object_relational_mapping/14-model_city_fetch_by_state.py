#!/usr/bin/python3
"""Prints all City objects objects from the database hbtn_0e_14_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format
            (sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(City, State).join(
                State, State.id == City.state_id).all()
    for record in records:
        print("{}: ({}) {}".format(
                record[1].name, record[0].id, record[0].name))
