from os import getcwd
from models import models
import sqlalchemy

db_url = 'sqlite:///' + getcwd() + '\\database.db'
engine = sqlalchemy.create_engine(db_url, echo=True)

models.Base.metadata.create_all(bind=engine)