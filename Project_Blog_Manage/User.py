from connection_orm import base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    posts = relationship('Post', back_populates='creator')

    def __init__(self, name, email):
        self.name = name
        self.email = email