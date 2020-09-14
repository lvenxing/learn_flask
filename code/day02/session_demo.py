# coding:utf-8


from flask import Flask, session, request, current_app,g


# app = Flask(__name__)
app2 = Flask(__name__)

# 为了使用session，需要设置secret_key

app.config['SECRET_KEY'] = "hfsof2982938r982fy29fdsf&(DY(*"


@app.route("/login")
def login():
    # 保存session数据
    # session中保存的数据，由我们自己决定
    session["name"] = "python"
    session["age"] = 18
    return "login success"


@app.route("/")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)









