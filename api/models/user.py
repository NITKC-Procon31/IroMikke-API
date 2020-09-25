from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class User(Model):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    viewer_id = Column('viewer_id', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False)
    name = Column('name', String(20), nullable=False)
