from flask import Blueprint, request, redirect, render_template
from common.models.model import Cucnew, Douban
from common.libs.Hepler import ops_render, randomIntIndex
from application import app
from common.libs.wordc.wordc import cut, wordcloudpic
from snownlp import SnowNLP

route_wordcloud = Blueprint('wordcloud_page',__name__)


@route_wordcloud.route('/cucnewsemotionanalysis',methods=["Get","Post"])
def cucnewsemotionanalysis():
    req = request.values
    id = req.get('id')
    rs = Cucnew.query.filter_by(id=id).first()
    words = rs.content.strip()
    s = SnowNLP(str(words))
    count = s.sentiments
    keywords = s.keywords()
    data = {'id':id,'count':count,'keywords':keywords}
    resp = {'code':200,'msg':count,'data':{}}
    return data

@route_wordcloud.route('/emotionanalysis',methods=["Get","Post"])
def emotionanalysis():
    req = request.values
    id = req.get('id')
    rs = Douban.query.filter_by(id=id).first()
    words = rs.bookintro.strip()
    # app.logger.info(words)
    s = SnowNLP(str(words))
    count = s.sentiments
    keywords = s.keywords()
    # app.logger.info(keywords)
    data = {'id':id,'count':count,'keywords':keywords}
    resp = {'code':200,'msg':count,'data':{}}
    return data


@route_wordcloud.route('/',methods=["Get","POST"])
def wordcloud():
    cucnewrs = []
    # newscount = Cucnew.query.filter(Cucnew.id).count()
    # newsindex = randomIntIndex(3,1,newscount)
    # for i in newsindex:
    #     cucnewrs.append(Cucnew.query.filter_by(id=i).first())
    for i in range(1,4):
        cucnewrs.append(Cucnew.query.filter_by(id=i).first())
    
    doubanrs = []
    doubancount = Douban.query.filter(Douban.id).count()
    doubanindex = randomIntIndex(3,1,doubancount)
    for i in doubanindex:
        doubanrs.append(Douban.query.filter_by(id=i).first())

    wanted = request.args.get("wanted",type=str)
    if wanted:
        return redirect("/wordcloud/cucnews?wanted="+wanted)
    doubanwanted = request.args.get("doubanwanted",type=str)
    if doubanwanted:
        return redirect("/wordcloud/doubanciyun?doubanwanted="+doubanwanted)
    return render_template("/wordcloud/index.html",cucnewrs=cucnewrs,doubanrs=doubanrs)


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
    wordcloud = cut(words)
    wordcount = len(wordcloud)
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
    wordcloud = cut(words)
    wordcount = len(wordcloud)
    return render_template("/wordcloud/wordcloud.html",rs=rs,wordcloud=wordcloud,wordcount=wordcount)
    # return render_template("/wordcloud/wordcloud.html")



@route_wordcloud.route('/test')
def test():
    # doubanwanted = request.args.get("doubanwanted",type=str)
    # if doubanwanted == None:
    #     doubanwanted = ""
    # rs = list(Douban.query.filter(Douban.bookintro.like("%"+doubanwanted+"%")).all())
    # rscount = Douban.query.filter(Douban.bookintro.like("%"+doubanwanted+"%")).count()
    # words = ""
    # for r in rs:
    #     words += r.bookintro
    # wordcloud = cut(words)
    # wordcount = len(wordcloud)
    # return render_template("/wordcloud/test1.html",rs=rs,wordcloud=wordcloud,wordcount=wordcount)
    return render_template("/wordcloud/test.html")

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