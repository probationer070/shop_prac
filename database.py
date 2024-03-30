import sqlite3


# DB에서 파일 읽어오기
def read_db():
    sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    topics = cursor.fetchall()
    for topic in topics:
         print(topic[0], topic[1])

def insert_data():
    try:
        id = session['users']
        content = request.form['content']
        conn = sqlite3.connect('mydb.db')  # DB와 연결
        cursor = conn.cursor()
        
        setdata = (id, content)    # 전달값
        sql = "INSERT INTO content (writer, content) VALUES (?,?)" # 실행할 SQL문
        
        cursor.execute(sql, setdata)  # 메소드로 전달해 명령문을 실행
        new_data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
        conn.commit()
        
    except Exception as e:
        print('db error:', e)
        db.rollback()
    finally:
        db.close()


def select_all(table_name): # 전체 데이터 확인
    ret = list()
    try:
        db = connect_db()
        c = db.cursor()
        c.execute(f'SELECT * FROM {table_name}')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret
    
def select_user(user_id):
    ret = []
    try:
        db = connect_db()
        c = db.cursor()
        setdata = (user_id,)
        c.execute('SELECT * FROM users WHERE user_id = ?', setdata)
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret


# conn = sqlite3.connect('mydb.db')
# cursor = conn.cursor()
# sql = "SELECT * FROM content WHERE id = '1'"
# cursor.execute(sql)  
# data = cursor.fetchall()

# print(data[0])

# for i in data:
#     print(i[0])