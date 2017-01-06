from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

# Create session and connect to DB
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()