#!/usr/bin/python3
"""Creates State “California” with City “San Francisco”
in db hbtn_0e_100_usa
"""
if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker, relationship
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    """
    City.state = relationship('State', order_by=State.id, backref='cities')
    """
    ca = State(name='California')
    ca.cities = [City(name='San Francisco')]
    session.add(ca)
    session.commit()
