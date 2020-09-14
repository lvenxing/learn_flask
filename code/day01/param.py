# coding:utf-8

from flask import Flask, current_app, url_for, request


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
@app.route("/")
def hello():
    name = request.args.get("name")

    # 通过return字符串返回响应信息
    return "hello %s " % name


@app.route("/upload", methods=["POST"])
def upload():
    # 获取用户上传的文件对象
    pic_file = request.files.get("pic")

    if pic_file:
        # 保存到服务器本地
        # pic_data = pic_file.read()
        # with open("./upload_image", "wb") as f:
        #     f.write(pic_data)
        pic_file.save("./upload_image")
        return "success"
    else:
        return "miss pic_file"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)





