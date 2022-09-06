from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

pwd = os.environ['PASSWORD']
user = os.environ['USERNAME1']


engine = create_engine("postgresql://user:pwd@localhost/bookdb", echo = True)

Base=declarative_base()

SessionLocal = sessionmaker(bind=engine)