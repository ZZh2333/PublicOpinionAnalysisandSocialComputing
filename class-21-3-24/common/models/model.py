# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from application import db


# db = SQLAlchemy()



class Cucnew(db.Model):
    __tablename__ = 'cucnews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='title')
    newsurl = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='newsurl')
    department = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='department')
    date = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='date')
    count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='count')
    content = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='content')



class Cucnewsv1(db.Model):
    __tablename__ = 'cucnewsv1'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='title')
    newsurl = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='newsurl')
    department = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='department')
    date = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='date')
    count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='count')
    content = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='content')
