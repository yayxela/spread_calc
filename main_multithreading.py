from os import getcwd
from models.models import Client, Order
# from models import models
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import date, timedelta
from queue import Queue
import threading


db_url = 'sqlite:///' + getcwd() + '\\database.db'
engine = sqlalchemy.create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)


class Parser(threading.Thread):

    def __init__(self, client, spread, size):
        threading.Thread.__init__(self)
        self.client = client
        self.spread = spread
        self.size = size

    def run(self):
        session = Session()
        buy = session.query(Order)\
            .filter(
                Order.timestamp >= date.today(),
                Order.timestamp <= date.today() + timedelta(1),
                Order.side == 'BUY',
                Order.size > 0,
                Order.account_id == self.client.id
                )\
            .order_by(Order.price.asc())\
            .all()
        sell = session.query(Order)\
            .filter(
                Order.timestamp >= date.today(),
                Order.timestamp <= date.today() + timedelta(1),
                Order.side == 'SELL',
                Order.size > 0,
                Order.account_id == self.client.id
                )\
            .order_by(Order.price.asc())\
            .all()
        session.close()
        process_spread(buy, sell, self.size, self.spread, self.client.name)


def process_spread(buy_array, sell_array, SIZE, SPREAD, name):
    if not buy_array and not sell_array is None:
        print('no data')
        return
    size = SIZE
    for buy in buy_array:
        size = size - buy.size
        if size <= 0:
            break
    if size >= 0:
        print('not enough size to buy')
    size = SIZE
    for sell in sell_array:
        size = size - sell.size
        if size <= 0:
            break
    if size >= 0:
        print('not enough size to sell')
    price_buy = buy_array[1].price
    price_sell = sell_array[1].price
    print(price_buy, price_sell)
    result = (price_sell - price_buy) / ((price_buy + price_sell)/2) * 10000
    print('spread for client {} is {} \nspread delta {}'.format(name, result, (SPREAD - result)))


def main():
    spread = input('enter spread: ')
    size = input('enter size: ')
    session = Session()
    clients = session.query(Client).all()
    session.close()

    for client in clients:
        thread = Parser(client, int(spread), int(size))
        thread.start()


if __name__ == '__main__':
    main()

