from datetime import datetime
import sys
from os import getcwd

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.models import Order, Client

args = sys.argv
if len(args) <= 6:
    raise Exception("not valid count of args")

db_url = 'sqlite:///' + getcwd() + '\\database.db'
engine = sqlalchemy.create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


name = args[2]

timestamp = datetime.now()
side = args[2]
price = args[3]
size = args[4]

client = session.query(Client).filter(name=name).first()
if  client is None:
    raise Exception('no such client')
account_id = client.id

if args[2] not in ['BUY', 'SELL']:
    raise Exception('side not defined')

order = Order(
    account_id=account_id,
    timestamp=timestamp,
    side=side,
    price=price,
    size=size
    )

session.add(order)
session.commit()

print('Order stored successfully')
