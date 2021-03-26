from flask import Blueprint, request,redirect
from common.models.model import Cucnew
from common.libs.Hepler import ops_render
from application import app
from common.libs.wordc import cut, wordcloudpic

route_wordcloud = Blueprint('wordcloud_page',__name__)

@route_wordcloud.route('/')
def wordcloud():
    # resp_data = {}
    # wanted = "保卫处"
    # result = Cucnew.query.filter_by(department=wanted).all()
    # resp_data['list'] = result
    # return ops_render("/wordcloud/wordcloud.html",resp_data)
    return redirect('/wordcloud/search')


@route_wordcloud.route('/search')
def search():
    resp_data = {}
    wanted = request.args.get("wanted",type=str)
    if wanted == None:
        wanted = "中国传媒大学"
    result = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%"))
    resp_data['list'] = result
    words = ""
    for r in result:
        words += r.content
    picname = wordcloudpic(cut(words))
    return ops_render("/wordcloud/wordcloud.html",resp_data)
