# coding:utf-8


from flask import Flask, make_response, jsonify, redirect, url_for
import json


app = Flask(__name__)


@app.route("/")
def index():
    # 响应体            状态码（不一定是标准的）    响应头
    # return "index page", 666
    # return "index page", "666 itcast python"
                                # 响应头的键  值
    # return "index page", 666, [("itcast", "python"), ("city", "shenzhen")]
    # return "index page", 666, {"itcast1": "python1"}

    # 自己构造响应对象
    resp = make_response("index page pytho itcast")
    resp.status = "666 itcast python"  # 状态码
    resp.headers["city"] = "shenzhen"  # 响应头
    return resp


@app.route("/person")
def get_person():
    p = {
        "name": "zhangsan",
        "age": 24
    }
    # return json.dumps(p), 200, {"Content-Type": "application/json"}
    # jsonify帮助我们转换数据为json字符串，并且设置Content-Type响应头为application/json
    return jsonify(p)


@app.route("/login")
def login():
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)