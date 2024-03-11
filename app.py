from flask import Flask, request, render_template, redirect, url_for

import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        user_id = request.args["usr-id"]
        user_pw = request.args.get("usr-pw")

        return "GET으로 전달된 데이터({}, {})".format(user_id, user_pw)
    else:
        user_id = request.form["usr-id"]
        user_pw = request.form["usr-pw"]
        
        user_data = {
            "user_name" : user_id,
            "user_pass" : user_pw
        }
        with open("static/save.json","w", encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False)
        return "POST로 전달된 데이터({}, {})".format(user_id, user_pw)
    
    return render_template(["success.html"])

@app.route('/getinfo')
def getinfo():
    with open("static/save.json", "r", encoding='utf-8') as file:
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])


if __name__ == '__main__':
    app.run(debug=True)