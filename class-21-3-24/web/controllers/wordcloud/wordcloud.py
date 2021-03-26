from flask import Blueprint, render_template
from common.models.model import Cucnew
from common.libs.Hepler import ops_render
# from application import app

route_wordcloud = Blueprint('wordcloud_page',__name__)

@route_wordcloud.route('/')
def wordcloud():
    resp_data = {}
    wanted = "保卫处"
    list = Cucnew.query.filter_by(department=wanted).all()
    resp_data['list'] = list
    return ops_render("/wordcloud/wordcloud.html",resp_data)
