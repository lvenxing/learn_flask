# coding:utf-8

from flask import Flask, current_app, url_for
from werkzeug.routing import BaseConverter


# 创建Flask应用对象
#           模块名， flask会把这个模块所在的目录当做当前flask工程目录，在工程目录中找静态文件目录static和模板目录templates
app = Flask(__name__)


# 通过对象的方式读取配置参数
class MyConfig(object):
    """配置信息"""
    DEBUG = True
    ITCAST = "python"


app.config.from_object(MyConfig)


# 通过route装饰器，将url路径与视图函数绑定到一起
# <>转换器，默认把除了/之外的字符串当做匹配对象
# @app.route("/<name>")
# def hello(name):
#
#     # 通过return字符串返回响应信息
#     return "hello %s" % name


@app.route("/id/<int:id>")
def hello_id(id):

    # 通过return字符串返回响应信息
    return "hello id=%s" % id


# 自定义路由转换器
class ReConverter(BaseConverter):
    """自定义的支持传入正则表达式的转换器"""
    def __init__(self, url_map, *args):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 将传入进来的参数args （是我们在route中定义的正则表达式）保存到对象的regex属性中
        self.regex = args[0]  # args[0]就是我们定义的正则表达式

    def to_python(self, value):
        """从正则表达式提取的参数，经过to_python的调用，将调用的结果返回，再传给视图函数"""
        print(u"to_python被调用 value=%s" % value)
        return value

    def to_url(self, value):
        """从python的变量转换到url中时被调用"""
        print(u"to_url被调用 value=%s" % value)
        return value


# app中维护的所有路由转换器， converters是一个字典
app.url_map.converters["re"] = ReConverter


@app.route("/id3/<re('\d{3}'):id>")
def hello_id_3(id):

    # 通过return字符串返回响应信息
    return "hello id=%s" % id


@app.route("/itcast")
def itcast():
    return '<a href="%s">hello_id_3</a>' % url_for("hello_id_3", id=123)


if __name__ == '__main__':
    # 通过run命令，让flask运行起来
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)





