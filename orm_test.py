from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('sqlite+pysqlite:///A:\\shop_prac\\mydb.db', echo=True)

Base = declarative_base()

# class Movie(Base):
#     __tablename__ = 'movies'
#     id = Column(Integer, primary_key=True)
#     date = Column(Integer)
#     rank = Column(Integer)
#     movieNm = Column(String(30))
#     movieCd = Column(Integer)
#     salesAmt = Column(Integer)
#     audiCnt = Column(Integer)

class users(Base):
  __tablename__ = 'user'
  user_id = Column(String(50), primary_key=True)
  user_pw = Column(String(50))
  

# users.__table__.create(bind=engine, checkfirst=True)

# DB와 대화시 필요, 생성해둔 엔진(DB)을 연결

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# movie_list=Movie(date=20190625, rank=1, movieNm='토이 스토리4', movieCd=12345, salesAmt=1234545123,audiCnt=342) # insert
user_list=users(user_id="park", user_pw="awiorncow1") # insert

session.add(user_list)
session.commit()

result = session.query(users).all()
for row in result:
  print(users.user_id, users.user_pw)
  
some_table = Table("my_db", metadata, autoload_with=engine)
print(some_table)