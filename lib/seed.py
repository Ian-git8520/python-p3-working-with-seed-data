#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Game

if __name__ == '__main__':
    # Create engine and session
    engine = create_engine('sqlite:///games.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Delete existing data to start fresh
    print("Deleting existing games...")
    session.query(Game).delete()
    session.commit()
    
    # Initialize Faker
    fake = Faker()
    
    # Add console message
    print("Seeding games...")
    
    # Add specific games from the lesson
    specific_games = [
        Game(
            title="Breath of the Wild",
            platform="Switch",
            genre="Adventure",
            price=60
        ),
        Game(
            title="Final Fantasy VII",
            platform="Playstation",
            genre="RPG",
            price=30
        ),
        Game(
            title="Mario Kart 8",
            platform="Switch",
            genre="Racing",
            price=50
        ),
        Game(
            title="Candy Crush Saga",
            platform="Mobile",
            genre="Puzzle",
            price=0
        )
    ]
    
    # Add specific games first
    session.bulk_save_objects(specific_games)
    session.commit()
    print(f"Added {len(specific_games)} specific games")
    
    # Generate 46 more random games (for a total of 50)
    random_games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for i in range(46)
    ]
    
    # Bulk save random games
    session.bulk_save_objects(random_games)
    session.commit()
    print(f"Added {len(random_games)} random games")
    
    # Verify total count
    total_count = session.query(Game).count()
    print(f"\nSuccessfully seeded {total_count} total games!")
    
    # Display some sample data
    print("\nFirst 5 games:")
    sample_games = session.query(Game).limit(5).all()
    for game in sample_games:
        print(f"  - {game.title} ({game.platform}) - {game.genre} - ${game.price}")
    
    print("\nLast game:")
    last_game = session.query(Game).order_by(Game.id.desc()).first()
    print(f"  - {last_game.title} ({last_game.platform}) - {last_game.genre} - ${last_game.price}")
    
    session.close()