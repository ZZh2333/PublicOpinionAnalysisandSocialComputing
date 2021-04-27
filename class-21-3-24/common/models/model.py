# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



t_4sdian = db.Table(
    '4sdian',
    db.Column('id', db.Integer),
    db.Column('loyalty', db.Float(asdecimal=True)),
    db.Column('frequency', db.Integer),
    db.Column('money', db.Float(asdecimal=True)),
    db.Column('L', db.Text),
    db.Column('F', db.Text),
    db.Column('M', db.Text),
    db.Column('LFM', db.Text)
)



class Bilibili(db.Model):
    __tablename__ = 'bilibili'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)



class Cucnew(db.Model):
    __tablename__ = 'cucnews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='title')
    newsurl = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='newsurl')
    department = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='department')
    date = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='date')
    count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='count')
    content = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='content')



class Cucnewsv1(db.Model):
    __tablename__ = 'cucnewsv1'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='title')
    newsurl = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='newsurl')
    department = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='department')
    date = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='date')
    count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='count')
    content = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='content')



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



t_exasens = db.Table(
    'exasens',
    db.Column('Diagnosis', db.Text),
    db.Column('ID', db.Text),
    db.Column('Imaginary Part', db.Text),
    db.Column('MyUnknownColumn', db.Text),
    db.Column('Real Part', db.Text),
    db.Column('MyUnknownColumn_[0]', db.Text),
    db.Column('Gender', db.Text),
    db.Column('Age', db.Text),
    db.Column('Smoking', db.Text),
    db.Column('MyUnknownColumn_[1]', db.Text),
    db.Column('MyUnknownColumn_[2]', db.Text),
    db.Column('MyUnknownColumn_[3]', db.Text),
    db.Column('MyUnknownColumn_[4]', db.Text)
)



t_forestfires = db.Table(
    'forestfires',
    db.Column('X', db.Integer),
    db.Column('Y', db.Integer),
    db.Column('month', db.Text),
    db.Column('day', db.Text),
    db.Column('FFMC', db.Float(asdecimal=True)),
    db.Column('DMC', db.Float(asdecimal=True)),
    db.Column('DC', db.Float(asdecimal=True)),
    db.Column('ISI', db.Float(asdecimal=True)),
    db.Column('temp', db.Float(asdecimal=True)),
    db.Column('RH', db.Integer),
    db.Column('wind', db.Float(asdecimal=True)),
    db.Column('rain', db.Float(asdecimal=True)),
    db.Column('area', db.Integer)
)



class Moviekill(db.Model):
    __tablename__ = 'moviekill'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger)
    content = db.Column(db.Text)
    likeCount = db.Column(db.Integer)



class Moviesunrise(db.Model):
    __tablename__ = 'moviesunrise'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    content = db.Column(db.Text)
    likeCount = db.Column(db.Integer)



t_orders_central = db.Table(
    'orders_central',
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('State', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product', db.Text),
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Order Year', db.Integer),
    db.Column('Order Month', db.Integer),
    db.Column('Order Day', db.Integer),
    db.Column('Ship Year', db.Integer),
    db.Column('Ship Month', db.Integer),
    db.Column('Ship Day', db.Integer),
    db.Column('Discounts', db.Text)
)



t_orders_south_2015 = db.Table(
    'orders_south_2015',
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Discount', db.Float(asdecimal=True)),
    db.Column('Region', db.Text),
    db.Column('State', db.Text),
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Order Date', db.Text),
    db.Column('Ship Date', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product Name', db.Text)
)



t_orders_south_2016 = db.Table(
    'orders_south_2016',
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Discount', db.Float(asdecimal=True)),
    db.Column('Region', db.Text),
    db.Column('State', db.Text),
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Order Date', db.Text),
    db.Column('Ship Date', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product Name', db.Text)
)



t_orders_south_2017 = db.Table(
    'orders_south_2017',
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Discount', db.Integer),
    db.Column('Region', db.Text),
    db.Column('State', db.Text),
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Order Date', db.Text),
    db.Column('Ship Date', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product Name', db.Text)
)



t_orders_south_2018 = db.Table(
    'orders_south_2018',
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Discount', db.Float(asdecimal=True)),
    db.Column('Region', db.Text),
    db.Column('State', db.Text),
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Order Date', db.Text),
    db.Column('Ship Date', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product Name', db.Text)
)



t_orders_west = db.Table(
    'orders_west',
    db.Column('Row ID', db.Integer),
    db.Column('Order ID', db.Text),
    db.Column('Order Date', db.Text),
    db.Column('Ship Date', db.Text),
    db.Column('Ship Mode', db.Text),
    db.Column('Customer ID', db.Text),
    db.Column('Customer Name', db.Text),
    db.Column('Segment', db.Text),
    db.Column('Country', db.Text),
    db.Column('City', db.Text),
    db.Column('Postal Code', db.Integer),
    db.Column('Region', db.Text),
    db.Column('Product ID', db.Text),
    db.Column('Category', db.Text),
    db.Column('Sub-Category', db.Text),
    db.Column('Product Name', db.Text),
    db.Column('Sales', db.Float(asdecimal=True)),
    db.Column('Quantity', db.Integer),
    db.Column('Discount', db.Float(asdecimal=True)),
    db.Column('Profit', db.Float(asdecimal=True)),
    db.Column('Right_Row ID', db.Integer),
    db.Column('Right_Order Date', db.Text),
    db.Column('Right_Ship Date', db.Text),
    db.Column('Right_Ship Mode', db.Text),
    db.Column('Right_Customer ID', db.Text),
    db.Column('Right_Customer Name', db.Text),
    db.Column('Right_Segment', db.Text),
    db.Column('Right_Country', db.Text),
    db.Column('Right_City', db.Text),
    db.Column('Right_State2', db.Text),
    db.Column('Right_Postal Code', db.Integer),
    db.Column('Right_Region', db.Text),
    db.Column('Right_Product ID', db.Text),
    db.Column('Right_Category', db.Text),
    db.Column('Right_Sub-Category', db.Text),
    db.Column('Right_Product Name', db.Text),
    db.Column('Right_Sales', db.Float(asdecimal=True)),
    db.Column('Right_Quantity', db.Integer),
    db.Column('Right_Discount', db.Float(asdecimal=True)),
    db.Column('Right_Profit', db.Float(asdecimal=True)),
    db.Column('State', db.Text)
)



t_train = db.Table(
    'train',
    db.Column('id', db.Integer),
    db.Column('club', db.Integer),
    db.Column('league', db.Integer),
    db.Column('birth_date', db.Text),
    db.Column('height_cm', db.Integer),
    db.Column('weight_kg', db.Integer),
    db.Column('nationality', db.Integer),
    db.Column('potential', db.Integer),
    db.Column('pac', db.Integer),
    db.Column('sho', db.Integer),
    db.Column('pas', db.Integer),
    db.Column('dri', db.Integer),
    db.Column('def', db.Integer),
    db.Column('phy', db.Integer),
    db.Column('international_reputation', db.Integer),
    db.Column('skill_moves', db.Integer),
    db.Column('weak_foot', db.Integer),
    db.Column('work_rate_att', db.Text),
    db.Column('work_rate_def', db.Text),
    db.Column('preferred_foot', db.Integer),
    db.Column('crossing', db.Integer),
    db.Column('finishing', db.Integer),
    db.Column('heading_accuracy', db.Integer),
    db.Column('short_passing', db.Integer),
    db.Column('volleys', db.Integer),
    db.Column('dribbling', db.Integer),
    db.Column('curve', db.Integer),
    db.Column('free_kick_accuracy', db.Integer),
    db.Column('long_passing', db.Integer),
    db.Column('ball_control', db.Integer),
    db.Column('acceleration', db.Integer),
    db.Column('sprint_speed', db.Integer),
    db.Column('agility', db.Integer),
    db.Column('reactions', db.Integer),
    db.Column('balance', db.Integer),
    db.Column('shot_power', db.Integer),
    db.Column('jumping', db.Integer),
    db.Column('stamina', db.Integer),
    db.Column('strength', db.Integer),
    db.Column('long_shots', db.Integer),
    db.Column('aggression', db.Integer),
    db.Column('interceptions', db.Integer),
    db.Column('positioning', db.Integer),
    db.Column('vision', db.Integer),
    db.Column('penalties', db.Integer),
    db.Column('marking', db.Integer),
    db.Column('standing_tackle', db.Integer),
    db.Column('sliding_tackle', db.Integer),
    db.Column('gk_diving', db.Integer),
    db.Column('gk_handling', db.Integer),
    db.Column('gk_kicking', db.Integer),
    db.Column('gk_positioning', db.Integer),
    db.Column('gk_reflexes', db.Integer),
    db.Column('rw', db.Float(asdecimal=True)),
    db.Column('rb', db.Float(asdecimal=True)),
    db.Column('st', db.Float(asdecimal=True)),
    db.Column('lw', db.Float(asdecimal=True)),
    db.Column('cf', db.Float(asdecimal=True)),
    db.Column('cam', db.Float(asdecimal=True)),
    db.Column('cm', db.Float(asdecimal=True)),
    db.Column('cdm', db.Float(asdecimal=True)),
    db.Column('cb', db.Float(asdecimal=True)),
    db.Column('lb', db.Float(asdecimal=True)),
    db.Column('gk', db.Text),
    db.Column('y', db.Float(asdecimal=True))
)
