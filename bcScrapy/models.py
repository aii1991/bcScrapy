# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine,Integer
from sqlalchemy import DDL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

Base = declarative_base()

class ImageModel(Base):
    __tablename__ = 't_image'
    
    _id = Column(Integer,primary_key=True,autoincrement=True)
    imgeId = Column(String(100),unique=True)
    title = Column(String(50))
    url = Column(String(100))
    desc = Column(String(50))

class JokeTextModel(Base):
    __tablename__ = 't_joke_text'
    _id = Column(Integer,primary_key=True,autoincrement=True)
    jokeId = Column(String(100),unique=True)
    digest = Column(String(500))
    title = Column(String(50))


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/bc_scrapy')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
# event.listen(
#         ImageModel.__table__,
#         "after_create",
#         DDL("ALTER TABLE t_image change id AUTO_INCREMENT = 1;")
# )