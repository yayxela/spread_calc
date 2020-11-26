import sys
from os import getcwd

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.models import Client

args = sys.argv
if len(args) <= 1:
    raise Exception("not valid count of args")

db_url = 'sqlite:///' + getcwd() + '\\database.db'
engine = sqlalchemy.create_engine(db_url, echo=True)

name = str(args[1])

Session = sessionmaker(bind=engine)
session = Session()
client = Client(name=name)

session.add(client)
session.commit()

print('Client stored successfully')
