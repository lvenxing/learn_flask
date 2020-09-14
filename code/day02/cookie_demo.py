# coding:utf-8


from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 通过响应对象设置cookie, 默认为浏览器关闭就失效
    resp.set_cookie("itcast", "python")

    # 通过max_age设置有效期， 单位是秒
    resp.set_cookie("itcast1", "python1", max_age=3600)

    # 自己定义响应头
    resp.headers["Set-Cookie"] = "itcast2=python2; Expires=Mon, 30-Oct-2017 09:05:56 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookie():
    # 获取cookie的方法
    cookie = request.cookies.get("itcast1")
    return cookie


@app.route("/del_cookie")
def del_cookie():
    resp = make_response("delete success")
    # 通过响应对象中的delete_cookie删除cookie
    resp.delete_cookie("itcast1")
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)









