#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

from models import Base, Game

if __name__ == '__main__':
    # Create engine and session
    engine = create_engine('sqlite:///games.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a Faker instance for testing
    fake = Faker()
    
    print("Debug session started!")
    print("Available variables:")
    print("  - session: SQLAlchemy session")
    print("  - Game: Game model class")
    print("  - fake: Faker instance")
    print("\nTry commands like:")
    print("  - session.query(Game).count()")
    print("  - session.query(Game).first()")
    print("  - session.query(Game).all()")
    print("  - session.query(Game)[-1]")
    print()
    
    # Start ipdb session
    import ipdb; ipdb.set_trace()
    
    session.close()