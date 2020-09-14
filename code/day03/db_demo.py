# coding:utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


class Config(object):
    """配置参数"""
    DEBUG = True

    # 连接mysql数据的信息               用户名:密码@主机ip地址: 端口/数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python02"

    # 让sqlalchemy跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 让后sqlalchemy显示执行的sql语句
    # SQLALCHEMY_ECHO = True


app.config.from_object(Config)
# 创建sqlalchemy的数据库连接对象
db = SQLAlchemy(app)


class Role(db.Model):
    """角色"""
    __tablename__ = "tbl_roles"  # 自定义数据库表名

    id = db.Column(db.Integer, primary_key=True)  # 设置主键 ,自动设置自增
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """自定义结果的显示信息"""
        return "Role: %s" % self.name


class User(db.Model):
    """用户信息"""
    __tablename__ = "tbl_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))  # 指明外键

    def __repr__(self):
        return "User: %s" % self.name



if __name__ == '__main__':
    # 删除数据库中的所有表
    db.drop_all()
    # 创建所有的表
    db.create_all()
    # 创建对象
    role1 = Role(name="admin")
    # 交代任务
    db.session.add(role1)
    # 提交任务
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    # 一次保存多条记录
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
















