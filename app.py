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

@app.route('/suc')
def success():
    return render_template("success.html")

# ----------------- 글쓰기 ---------------------
@app.route('/write_board')
def write_board():
    my_db.connect_db()
    info = my_db.select_all(table_name="writers")
    return render_template("writer_board.html", data=info)


@app.route('/write')
def write():
    return render_template('write.html')
#----------------------------------------------


@app.route('/login', methods=['GET', 'POST']) # 로그인
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['usr_id']
        pw = request.form['usr_pw']
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'park' and pw == '00000000':
            session['user'] = id
            return '''
                <script> alert("Hello {}!");
                location.href="/suc"
                </script>
            '''.format(id)
            return redirect(url_for('suc'))
        else:
            return "Check your ID / PASSWORD"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template("signup.html")

# @app.route('/login', methods=['GET', 'POST'])
# def method():
#     if request.method == 'GET':       # GET 방식 전송
#         user_id = request.args["usr-id"]
#         user_pw = request.args.get("usr-pw")

#         return "GET ({}, {})".format(user_id, user_pw)
#     else:                                     # POST 방식 전송
#         user_id = request.form["usr-id"]
#         user_pw = request.form["usr-pw"]
        
#         user_data = {
#             "user_name" : user_id,
#             "user_pass" : user_pw
#         }
#         with open("static/save.json","w", encoding='utf-8') as f:
#             json.dump(user_data, f, ensure_ascii=False)
#         return "POST ({}, {})".format(user_id, user_pw)

# @app.route('/getinfo')            # json 파일 읽어고기
# def getinfo():
#     with open("static/save.json", "r", encoding='utf-8') as file:
#         user = file.read().split(',')  
#     return '번호 : {}, 이름 : {}'.format(user[0], user[1])

@app.route('/signup', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET'
    else:
        user_id = request.form["usr_id"]
        user_pw = request.form["usr_pw"]
        my_db.connect_db()
        my_db.insert_data(user_id, user_pw)
        return 'POST | usr-id: {} usr-pw: {}'.format(user_id, user_pw)

@app.route('/getinfo')
def getinfo():
    my_db.connect_db()
    info = my_db.select_all(table_name='users')
    return render_template("info.html", data=info)


if __name__ == '__main__':
    app.run(debug=True)