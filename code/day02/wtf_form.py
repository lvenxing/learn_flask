# coding:utf-8


from flask import Flask, render_template, request
from flask_wtf import FlaskForm  # 表单类的父类
from wtforms import StringField, PasswordField, SubmitField  # 表单的字段类型
from wtforms.validators import DataRequired, EqualTo  # 表单的验证器

app = Flask(__name__)

# 为了使用session，需要设置secret_key

app.config['SECRET_KEY'] = "hfsof2982938r982fy29fdsf&(DY(*"


# 定义表单的类
class RegisterForm(FlaskForm):
    user_name = StringField(label=u"用户名", validators=[DataRequired()])
    password = PasswordField(label=u"密码", validators=[DataRequired()])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired(), EqualTo("password", u"密码不一致")])
    submit = SubmitField(label=u"提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单的对象
    form = RegisterForm()
    # 对表单数据进行验证
    if form.validate_on_submit():
        # 表示用户填写的数据符合要求
        # 通过form对象获取用户填写的表单数据
        uname = form.user_name
        password = form.password
        password2 = form.password2
        print(uname.data, password.data, password2.data)
        return "register success"
    else:
        # 表示验证失败
        if request.method == "GET":
            return render_template("register.html", form=form, errmsg="")
        else:
            # 表示以post方式访问，验证又没有成功，用户填写的数据有问题
            return render_template("register.html", form=form, errmsg=u"填写的数据有误")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)









