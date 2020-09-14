# coding:utf-8

from flask import Flask, current_app, url_for


# 创建Flask应用对象
#           模块名， flask会把这个模块所在的目录当做当前flask工程目录，在工程目录中找静态文件目录static和模板目录templates
app = Flask(__name__,
            static_url_path="/static",  # 控制访问静态资源url的前缀， 默认是static
            static_folder="static",  # 存放静态文件的文件夹，默认是static
            template_folder="templates",  # 存放模板文件的文件夹，默认是templates
            )
# app = Flask("__main__")
# app = Flask("abc")  # 错误

# 为flask添加配置参数
# 通过配置文件读取配置参数
# app.config.from_pyfile("MyConfig.cfg")


# 通过对象的方式读取配置参数
class MyConfig(object):
    """配置信息"""
    DEBUG = True
    ITCAST = "python"


app.config.from_object(MyConfig)


# 通过route装饰器，将url路径与视图函数绑定到一起
@app.route("/")
def hello():
    # a = 1 / 0
    # 在视图函数中读取配置参数
    # print(app.config.get("ITCAST"))
    print(current_app.config.get("ITCAST"))

    # 通过return字符串返回响应信息
    return "hello itcast 1"


@app.route("/")
def hello2():
    return "hello itcast 2"


@app.route("/index")
@app.route("/hi")
def index():
    return "index page"


@app.route("/python", methods=["GET", "POST"])
def post_only():
    """对于请求方式限制的演示"""
    return "post only page"


@app.route("/redirect")
def redirect_post_only():
    """"""
    return '<a href="%s">post_only</a>' % url_for("post_only")


if __name__ == '__main__':
    # 通过run命令，让flask运行起来
    # app.run(debug=True)
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)





