from flask import Blueprint, request, render_template, redirect, url_for, session
from website import Session
from models.models import Items

import my_db
import sqlite3

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")

@views.route('/home')
def home():
    return render_template("home.html")

# ----------------- 아이템 추가 ---------------------


@views.route('/item/<string:item_code>', methods=['GET', 'POST'])
def item(item_code):
    info = my_db.select_all(table_name="items")
    return render_template("item.html", data=info)

@views.route('/itemAdd', methods=['GET', 'POST'])
def itemAdd():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_code = request.form['item_code']
        writer = request.form['writer']
        pubtime = request.form['pubtime']
        option = request.form['option']
        stock = request.form['stock']
        price = request.form['price']
        
        session = Session()
        new_item = Items(item_name=item_name, 
                        item_code=item_code,
                        writer=writer,
                        pubtime=pubtime,
                        option=option,
                        stock=stock,
                        price=price)
        session.add(new_item)
        session.commit()
        return redirect(url_for('views.home'))
    
    return render_template("itemAdd.html")


# ----------------- 글쓰기 ---------------------

@views.route('/write_board')
def write_board():
    info = my_db.select_all(table_name="content")
    return render_template("writeboard/writer_board.html", data=info)    

@views.route('/write', methods=['GET', 'POST'])
def write():
    error = None
    writer = session['users'] # 세션에 저장했던 로그인 유저 아이디를 변수에 저장함

    if request.method == 'POST': # 게시판에 글 등록하기
        content = request.form['content']
        title = request.form['title']
        anno = request.form['annotation']
        conn = sqlite3.connect('mydb.db')  # DB와 연결
        cursor = conn.cursor()  # connection으로부터 cursor 생성
        
        setdata = (title, writer, content, anno)    # 전달값
        sql = "INSERT INTO content (title, writer, content, annotation) VALUES (?,?,?,?)" # 실행할 SQL문
        
        cursor.execute(sql, setdata)  # 메소드로 전달해 명령문을 실행
        new_data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
 
        if not new_data:
            conn.commit()  # 변경사항 저장
            return redirect(url_for("views.write_board"))
 
        else:
            conn.rollback()  # 데이터베이스에 대한 모든 변경사항을 되돌림
            return "Register Failed"
 
        cursor.close()
        conn.close()
 
    elif request.method == 'GET': # 처음 페이지가 로드되는 GET 통신
        conn = sqlite3.connect('mydb.db')  # DB와 연결
        cursor = conn.cursor()  # connection으로부터 cursor 생성 (데이터베이스의 Fetch 관리)
        sql = "SELECT * FROM content ORDER BY date DESC Limit 1" # 실행할 SQL문
        cursor.execute(sql)  # 메소드로 전달해 명령문을 실행
        data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
 
        data_list = []
 
        for obj in data: # 튜플 안의 데이터를 하나씩 조회해서
            data_dic = { # 딕셔너리 형태로
                # 요소들을 하나씩 넣음
                'id': obj[0],
                'title': obj[1],
                'writer': obj[2],
                'content': obj[3],
                'date':obj[4]
            }
            data_list.append(data_dic) # 완성된 딕셔너리를 list에 넣음
 
        cursor.close()
        conn.close()
 
        return render_template('writeboard.write.html', error=error, name=id, data_list=data_list) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
    return render_template('writeboard/write.html', error=error, name=id)

# 수정하기
@views.route('/update/<int:post_id>', methods=['GET','POST']) 
def update(post_id):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM content WHERE id = ?"
    setdata = (post_id, )
    cursor.execute(sql, setdata)  
    data = cursor.fetchall()
    
    conn.close()
    
    if request.method == 'POST': 
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()
        
        content = request.form['content']
        title = request.form['title']
        anno = request.form['annotation']
        
        setdata = (title, content, anno, post_id)    # 전달값
        sql = "UPDATE content SET title=?, content=?, annotation=? WHERE id=?" # 실행할 SQL문
        
        cursor.execute(sql, setdata)
        conn.commit()  # 변경사항 저장
        conn.close()
        
        return redirect(url_for("views.write_board"))
    
    return render_template('writeboard/update.html', data=data)

# 삭제하기 

@views.route('/delete/<int:post_id>/', methods=['POST'])
def delete(post_id):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM content WHERE id = ?", (post_id,))
    
    conn.commit()  # 변경사항 저장
    conn.close()
    
    return redirect(url_for("views.write_board"))
