#coding:utf-8

from sqlachemy import Colmumn, String, create_engine
from sqlachemy.orm import sessionmark
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ "user"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3306/test")
DBSession = sessionmaker(bind=engine)


