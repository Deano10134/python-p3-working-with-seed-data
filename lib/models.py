from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

# Configure engine and session, then create tables
engine = create_engine('sqlite:///games.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
