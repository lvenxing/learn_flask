# coding:utf-8


from flask import Flask, render_template


app = Flask(__name__)


# 自定义过滤器
def filter_list_2(li):
    return li[::2]


# 添加到app中的过滤器集合中   过滤器函数      在模板中使用的过滤器名字
app.add_template_filter(filter_list_2, "li_2")


# 第二种定义过滤器的方式
@app.template_filter("li_3")
def filter_list_3(li):
    return li[::3]



@app.route("/")
def index():

    my_dict = {
        "a": 100
    }

    my_list = [1, 2, 3, 4, 5, 6]

    my_int = 0

    context = {
        "name": "python",
        "age": 24,
        "my_dict": my_dict,
        "my_list": my_list,
        "my_int": my_int,
        "brand": "itcast"
    }

    # return render_template("index.html", name="python", age=18)
    return render_template("index.html",  **context)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)









