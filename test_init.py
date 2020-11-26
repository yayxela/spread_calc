from datetime import datetime
import sys
from os import getcwd

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.models import Client, Order

db_url = 'sqlite:///' + getcwd() + '\\database.db'
engine = sqlalchemy.create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

new_client = session.query(Client).filter_by(name="Test").first()
if new_client is None:
    client = Client(name='Test')
    session.add(client)
    session.commit()
    new_client = client

orders = [
    {
        "price": 11.0,
        "side": 'SELL',
        'size': 5
    },
    {
        "price": 10.5,
        "side": 'SELL',
        'size': 3
    },
    {
        "price": 9.5,
        "side": 'BUY',
        'size': 5
    },
    {
        "price": 9.0,
        "side": 'BUY',
        'size': 9
    },
]

for order in orders:
    record = Order(
        account_id=new_client.id,
        timestamp=datetime.now(),
        side=order['side'],
        price=order['price'],
        size=order['size']
    )
    session.add(record)
    session.commit()



