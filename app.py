from flask import Flask, request, render_template, redirect, url_for, abort, session

import json
import sqlite3
import my_db

app = Flask(__name__)

app.secret_key = '1813508120'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/top')
def top():
    return render_template("top_menu.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/success', methods=['GET', 'POST'])
def success():
    error = None
    id = session['users']
    return render_template("success.html", error=error, name=id)

def template(content):
  liTags = ''

  for topic in topics:
    liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

  return f'''
    <html>
    <head>

    </head>
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
        {liTags}
        </ol>
        {content}
    </body>
    </html>
    '''


# ----------------- 글쓰기 ---------------------
@app.route('/write_board')
def write_board():
    info = my_db.select_all(table_name="content")
    return render_template("writer_board.html", data=info)    

@app.route('/write', methods=['GET', 'POST'])
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
            return redirect(url_for("write_board"))
 
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
 
        return render_template('write.html', error=error, name=id, data_list=data_list) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
    return render_template('write.html', error=error, name=id)

# 수정하기
@app.route('/update/<int:post_id>', methods=['GET','POST']) 
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
        
        return redirect(url_for("write_board"))
    
    return render_template('update.html', data=data)

# 삭제하기 

@app.route('/delete/<int:post_id>/', methods=['POST'])
def delete(post_id):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM content WHERE id = ?", (post_id,))
    
    conn.commit()  # 변경사항 저장
    conn.close()
    
    return redirect(url_for("write_board"))

# ---------------------로그인-----------------------


@app.route('/login', methods=['GET', 'POST']) # 로그인
def login():
    error = None
    
    if request.method == 'POST':
        id = request.form['usr_id']
        pw = request.form['usr_pw']
        
        data = my_db.select_user(id)
        # print(data)
        
        for row in data:
            data = row[0]
            data2 = row[1]
        # print(id==data)
        # print(str(pw)==data2)

        if data == id and data2 == pw:          # Im stupid, in sqlite : user_pw length -> 7;
            session['users'] = id                             # my input : min-length -> 8;
            return redirect(url_for('success'))
        else:
            error = "Check your ID / PASSWORD"
            return '''
                <script> alert("Login Failed");
                location.href="/login"
                </script>
            '''

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST']) # 회원가입
def signup():
    error = None
    if request.method == 'POST':
        user_id = request.form["usr_id"]
        user_pw = request.form["usr_pw"]
        
        try:
            conn = sqlite3.connect('mydb.db')
            cursor = conn.cursor()
            
            setdata = (user_id, user_pw)
            cursor.execute("INSERT INTO users (user_id, user_pw) VALUES(?,?);", setdata)
            
            data = cursor.fetchall()
        
        
            if not data:
                conn.commit()
                return redirect(url_for('index'))
            else:
                conn.rollback()
                return "Register Failed !"
        
        except Exception as e:
            print(e)
            return '''
                <script> alert("Register Failed");
                location.href="/signup"
                </script>
                '''
            
        finally:
            cursor.close()
            conn.close()
    return render_template('signup.html', error=error)

@app.route('/getinfo')
def getinfo():
    my_db.connect_db()
    info = my_db.select_all(table_name='users')
    return render_template("info.html", data=info)


if __name__ == '__main__':
    app.run(debug=True)