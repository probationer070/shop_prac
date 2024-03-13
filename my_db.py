import sqlite3


# DB파일 접속 함수
def connect_db():
    return sqlite3.connect('mydb.db')

def create_table():         # 테이블 생성 함수
    try:
        db = connect_db()
        c = db.cursor()
        c.execute("CREATE TABLE users (user_id varchar(50), user_pw varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(user_id, user_pw):  # 데이터 기입
    try:
        db = connect_db()
        c = db.cursor()
        setdata = (user_id, user_pw)
        c.execute("INSERT INTO users (user_id, user_pw) VALUES (?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all(): # 전체 데이터 확인
    ret = list()
    try:
        db = connect_db()
        c = db.cursor()
        c.execute('SELECT * FROM users')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret
    
def select_num(user_id):
    ret = ()
    try:
        db = connect_db()
        c = db.cursor()
        setdata = (user_id,)
        c.execute('SELECT * FROM users WHERE user_id = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def getinfo_sql():
    db = connect_db()
    c = db.cursor()
    c.execute('SELECT * FROM user_data WHERE user_id = ? and user_pw = ?',)