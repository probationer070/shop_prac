from flask import Flask, request, render_template, redirect, url_for
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

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict()
        # print(args_dict)
        user_id = request.args["usr-id"]
        user_pw = request.args.get("usr-pw")

        return "GET으로 전달된 데이터({}, {})".format(user_id, user_pw)
    else:
        user_id = request.form["usr-id"]
        user_pw = request.form["usr-pw"]
        with open("static/save.txt","w", encoding='utf-8') as f:
            f.write("%s,%s" % (user_id, user_pw))
        return "POST로 전달된 데이터({}, {})".format(user_id, user_pw)
    
    return render_template(["success.html"])



if __name__ == '__main__':
    app.run(debug=True)