# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
from application import db



class Cucnew(db.Model):
    __tablename__ = 'cucnews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='title')
    newsurl = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='newsurl')
    department = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='department')
    date = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='date')
    count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='count')
    content = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='content')


class Douban(db.Model):
    __tablename__ = 'douban'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info=' 书名')
    bookurl = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='url')
    score = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='得分')
    score_people = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评分人数')
    price = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='价格')
    publishtime = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='出版日期')
    publishcompany = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='出版社')
    author = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='作者')
    comment = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='总结')
    bookintro = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='简介')
