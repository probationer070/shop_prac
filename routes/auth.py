from flask import Blueprint, request, render_template, redirect, url_for, abort, session, flash
from models.models import User
from website import Session

import sqlite3
import my_db


auth = Blueprint('auth', __name__)

@auth.route('/logout')
def logout():
    session.pop('usr_name', None)
    return redirect(url_for('views.index'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['usr_id']
        pw = request.form['usr_pw']
        
        data = my_db.select_user(id)
        error = None
        
        if data:
            user_id, user_pw = data[0][0], data[0][1] 


            if user_id == id and user_pw == pw:
                session['usr_name'] = id
                return redirect(url_for('views.home'))
            elif user_id == id and user_pw != pw:
                error = "Check your PASSWORD"
                flash(error, category="error")
            elif user_id != id and user_pw == pw:
                error = "Check your ID"
                flash(error, category="error")
        else:
            error = "확인된 회원이 없습니다"
            flash(error, category="error")

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_id = request.form.get('usr_id')
        user_pw = request.form.get('usr_pw')

        try:
            with Session() as sess:
                existing_user = sess.query(User).filter_by(user_id=user_id).first()
                if existing_user:
                    flash("이미 동일한 사용자가 존재합니다.", category="error")
                    return redirect(url_for('auth.signup'))

                new_user = User(user_id=user_id, user_pw=user_pw)
                sess.add(new_user)
                sess.commit()
                flash("회원가입 완료.", category="success")
                return redirect(url_for('views.index'))

        except Exception as e:
            flash("회원가입 실패: " + str(e), category="error")

    return render_template('signup.html')