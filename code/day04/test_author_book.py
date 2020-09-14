# coding:utf-8


import unittest
from author_book import Author, db, app


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        """测试添加作者的数据库操作"""
        author = Author(name="zhang", email="itcast@itcast.cn", mobile="18612345678")
        db.session.add(author)
        db.session.commit()

        result_author = Author.query.filter_by(name="zhang").first()
        self.assertIsNotNone(result_author)

    def tearDown(self):
        """在所有的测试执行后，执行， 通常用来进行清理操作"""
        db.session.remove()
        db.drop_all()