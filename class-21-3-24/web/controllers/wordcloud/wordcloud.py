from flask import Blueprint, request, redirect
from common.models.model import Cucnew
from common.libs.Hepler import ops_render
from application import app
from common.libs.wordc.wordc import cut, wordcloudpic
# import jieba

route_wordcloud = Blueprint('wordcloud_page',__name__)

@route_wordcloud.route('/',methods=["Get","POST"])
def wordcloud():
    resp_data = {}
    wanted = request.args.get("wanted",type=str)
    if wanted:
        result = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%"))
        resp_data['list'] = result
        words = ""
        for r in result:
            words += r.content
        if words:
            picname,datetime = wordcloudpic(cut(words))
            picaddress = "/outputs/news"+datetime+".jpg"
            resp_data['href'] = picaddress
        return ops_render("/wordcloud/wordcloud.html",resp_data)
    return ops_render("/wordcloud/index.html")


@route_wordcloud.route('/search')
def search():
    resp_data = {}
    wanted = request.args.get("wanted",type=str)
    if wanted == None:
        wanted = "邹子涵"
    result = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%"))
    resp_data['list'] = result
    words = ""
    for r in result:
        words += r.content
    if words:
        picname,datetime = wordcloudpic(cut(words))
        picaddress = "/outputs/news"+datetime+".jpg"
        resp_data['href'] = picaddress
    return ops_render("/wordcloud/wordcloud.html",resp_data)


@route_wordcloud.route('/test')
def test():
    # resp_data = {}
    # wanted = request.args.get("wanted",type=str)
    # if wanted == None:
    #     wanted = "邹子涵"
    # result = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%"))
    # resp_data['list'] = result
    # words = ""
    # for r in result:
    #     words += r.content
    # if words:
    #     picname,datetime = wordcloudpic(cut(words))
    #     picaddress = "/outputs/news"+datetime+".jpg"
    #     resp_data['href'] = picaddress
    return ops_render("/common/layout_main.html")
    # return redirect('/wordcloud/search')layout_main