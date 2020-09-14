# coding:utf-8


from flask import Flask, abort


app = Flask(__name__)


@app.route("/")
def index():
    # 通过调用abort函数，可以立即终止视图函数的继续执行，返回前端一个错误信息
    # 错误转台码是标准的http协议状态码
    abort(404)
    return "index page"


# 自定义的错误处理方法，在发生特定错误的时候，flask会调用，返回值决定用户最终看到的结果
@app.errorhandler(404)
def handler_404(e):
    return u"发生了404错误 : %s" % e


# 自定义的错误处理方法，在发生特定错误的时候，flask会调用，返回值决定用户最终看到的结果
@app.errorhandler(405)
def handler_405(e):
    return u"发生了405错误 : %s" % e


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)