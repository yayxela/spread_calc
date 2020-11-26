from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

'''Data model for clients.'''
class Client(Base):
    __tablename__ = "clients"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(100),
        nullable=False
    )

    def __repr__(self):
        return '<Client id:{} name:{}>'.format(self.id, self.name)


'''Data models for orders.'''
class Order(Base):
    __tablename__ = "orders"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    account_id = Column(
        Integer,
        ForeignKey('clients.id'),
        nullable=False
    )
    timestamp = Column(
        DateTime,
        nullable=False
    )
    side = Column(
        String(4),
        nullable=False
    )
    price = Column(
        Float,
        nullable=False
    )
    size = Column(
        Integer,
        nullable=False
    )

    def get_size(self):
        return self.size

    def __repr__(self):
        return '<Order id:{} timestamp:{} account_id:{}>'.format(self.id, self.timestamp, self.account_id)

