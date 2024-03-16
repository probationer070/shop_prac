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