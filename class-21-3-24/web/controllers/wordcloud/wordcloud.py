from flask import Blueprint, request, redirect, render_template
from common.models.model import Cucnew, Douban
from common.libs.Hepler import ops_render
from application import app
from common.libs.wordc.wordc import cut, wordcloudpic
# import jieba

route_wordcloud = Blueprint('wordcloud_page',__name__)


@route_wordcloud.route('/',methods=["Get","POST"])
def wordcloud():
    wanted = request.args.get("wanted",type=str)
    if wanted:
        return redirect("/wordcloud/cucnews?wanted="+wanted)
        # return redirect("/wordcloud/cucnews")
    doubanwanted = request.args.get("doubanwanted",type=str)
    if doubanwanted:
        return redirect("/wordcloud/doubanciyun?doubanwanted="+doubanwanted)
        # return redirect("/wordcloud/doubanciyun")
    return ops_render("/wordcloud/index.html")


@route_wordcloud.route('/doubanciyun',methods=["Get","POST"])
def doubanciyun():
    doubanwanted = request.args.get("doubanwanted",type=str)
    if doubanwanted == None:
        doubanwanted = ""
    rs = list(Douban.query.filter(Douban.bookintro.like("%"+doubanwanted+"%")).all())
    rscount = Douban.query.filter(Douban.bookintro.like("%"+doubanwanted+"%")).count()
    words = ""
    for r in rs:
        words += r.bookintro
    # if words:
    wordcloud = cut(words)
    wordcount = len(wordcloud)
    # return "hello"
    return render_template("/wordcloud/doubanwordcloud.html",rs=rs,wordcloud=wordcloud,wordcount=wordcount)


@route_wordcloud.route('/cucnews',methods=["Get","POST"])
def cucnews():
    wanted = request.args.get("wanted",type=str)
    if wanted == None:
        wanted = ""
    rs = list(Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%")).all())
    rscount = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%")).count()
    words = ""
    for r in rs:
        words += r.content
    # if words:
    wordcloud = cut(words)
    wordcount = len(wordcloud)
    return render_template("/wordcloud/wordcloud.html",rs=rs,wordcloud=wordcloud,wordcount=wordcount)


# @route_wordcloud.route('/cucnews',methods=["Get","POST"])
# def search():
#     resp_data = {}
#     wanted = request.args.get("wanted",type=str)
#     if wanted == None:
#         wanted = "邹子涵"
#     result = Cucnew.query.filter(Cucnew.content.like("%"+wanted+"%"))
#     resp_data['list'] = result
#     words = ""
#     for r in result:
#         words += r.content
#     if words:
#         picname,datetime = wordcloudpic(cut(words))
#         picaddress = "/outputs/news"+datetime+".jpg"
#         resp_data['href'] = picaddress
#     return ops_render("/wordcloud/wordcloud.html",resp_data)


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