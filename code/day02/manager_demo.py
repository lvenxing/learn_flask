# coding:utf-8


from flask import Flask
from flask_script import Manager


app = Flask(__name__)

# 创建管理员类的对象
manager = Manager(app)


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000)
    manager.run()