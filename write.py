
import sqlite3
import my_db

con = sqlite3.connect('mydb.db')
c = con.cursor()
# c.execute("CREATE TABLE writers (num int, title varchar(50), writer varchar(50), views int, context varchar(200))")

def insert_data(num, title, writer, views, context):  # 데이터 기입
    try:
        db = connect_db()
        c = db.cursor()
        setdata = (user_id, user_pw)
        c.execute("INSERT INTO writers (num, title, writer, views, context) VALUES (?,?,?,?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all(table_name): # 전체 데이터 확인
    ret = list()
    try:
        db = connect_db()
        c = db.cursor()
        c.execute('SELECT * FROM {table_name}')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret



# c.execute("INSERT INTO writers (num, title, writer, views, context) VALUES (?,?,?,?,?)")
# con.commit()
# con.close()


# c.execute("SELECT * from writers")
# data_list = c.fetchall()

# print(data_list[0])