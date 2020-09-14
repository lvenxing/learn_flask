# coding:utf-8


from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)


class Config(object):
    """配置参数"""
    DEBUG = True

    # 连接mysql数据的信息               用户名:密码@主机ip地址: 端口/数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book_02"

    # 让sqlalchemy跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "DHOSHFOS879DSY"


app.config.from_object(Config)
# 创建sqlalchemy的数据库连接对象
db = SQLAlchemy(app)


# 创建flask脚本管理工具对象
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manger对象中添加数据库的操作命令
manager.add_command("db", MigrateCommand)


class Author(db.Model):
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    books = db.relationship("Book", backref="author")
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(64))



class Book(db.Model):
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 创建表单类
class AuthorBookForm(FlaskForm):
    author_name = StringField(label=u"作者", validators=[DataRequired()])
    book_name = StringField(label=u"书籍", validators=[DataRequired()])
    submit = SubmitField(label=u'提交')


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()
    if form.validate_on_submit():
        # 表示数据验证成功
        # 保存数据库
        author_name = form.author_name.data
        book_name = form.book_name.data

        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    authors = Author.query.order_by(Author.id.desc()).all()
    # 渲染模板
    return render_template("author_book.html", authors=authors, form=form)


@app.route("/delete_book/<int:id>")
def delete_book(id):
    # id删除的书的id
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/login")
def login():
    return "login page"


if __name__ == '__main__':
    # # 删除数据库中的所有表
    # db.drop_all()
    # # 创建所有的表
    # db.create_all()
    #
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    #
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    #
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()
    # app.run()

    # 通过manager启动程序
    manager.run()














