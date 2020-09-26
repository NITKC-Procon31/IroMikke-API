from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class User(Model):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    viewer_id = Column('viewer_id', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False)
    name = Column('name', String(20), nullable=False)

    def __init__(self, viewer_id: int, user_id: int, name: str):
        self.viewer_id = viewer_id
        self.user_id = user_id
        self.name = name
