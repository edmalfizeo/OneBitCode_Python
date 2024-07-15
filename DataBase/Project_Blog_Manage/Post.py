from connection_orm import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    creator_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship('User', back_populates='posts')

    def __init__(self, title, content, creator):
        self.title = title
        self.content = content
        self.creator = creator