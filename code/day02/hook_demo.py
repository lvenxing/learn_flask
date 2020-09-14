# coding:utf-8


from flask import Flask, session


app = Flask(__name__)


# 在第一次请求之前被调用
@app.before_first_request
def handle_before_first_req():
    print("handle before first req called")


# 在每次请求之前被调用
@app.before_request
def handle_before_req():
    print("handle before req called")


# 如果视图没有出现异常，在每次请求之后被调用
@app.after_request
def handle_after_req(response):
    print("handle after req called")
    return response


# 在每次请求之后被调用
@app.teardown_request
def handle_teardown_req(response):
    print("handle teardown req called")
    return response


@app.route("/")
def index():
    print("index called")
    return "index called"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)









