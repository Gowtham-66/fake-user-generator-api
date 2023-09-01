from dataBase import Base
from sqlalchemy import Column,Integer, String
class user(Base):
    __tablename__='name'
    id = Column(Integer,primary_key=True,index = True)
    name=Column(String)
    lastname=Column(String)
class fake(Base):
    __tablename__ = 'fake'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    profile_picture = Column(String)
    