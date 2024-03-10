from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dora')
def myimg():
    return render_template("myimg.html")

# @app.route('/method', methods=['GET', 'POST'])
# def method():
#     if request.method == 'GET':
#         # args_dict = request.args.to_dict()
#         # print(args_dict)
#         num = request.args["num"]
#         name = request.args.get("name")
#         return "GET으로 전달된 데이터({}, {})".format(num, name)
#     else:
#         num = request.form["num"]
#         name = request.form["name"]
#         return "POST로 전달된 데이터({}, {})".format(num, name)


if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for('static', filename='index.css'))
    app.run(debug=True)