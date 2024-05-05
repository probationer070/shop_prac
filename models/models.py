
from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

from website import Base

class User(Base):
    __tablename__ = 'test'

    user_id = Column(String(30), primary_key=True, nullable=False, unique=True)
    user_pw = Column(String(128), nullable=False)
    datetime = Column(Date, default=datetime.now(), onupdate=datetime.now())
    
    def __repr__(self):
        return f"User(user_id={self.user_id}, user_pw={self.user_pw})"

class Items(Base):
    __tablename__ = "items"
    
    img_path = Column(String)
    
    item_name = Column(String, unique=True)
    item_code = Column(String, unique=True, primary_key=True)
    writer = Column(String, nullable=False)
    datetime = Column(Date , default=datetime.now(), onupdate=datetime.now())
    pubtime = Column(Text)
    option = Column(String)
    stock = Column(Integer)
    price = Column(Integer)
    
    def __repr__(self):
        return f"Item(item_name={self.item_name}, item_code={self.item_code})"