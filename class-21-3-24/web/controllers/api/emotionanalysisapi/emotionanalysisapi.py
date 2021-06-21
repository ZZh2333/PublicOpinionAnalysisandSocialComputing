from flask import Blueprint,request
from common.models.model import Moviekill, Moviesunrise
from snownlp import SnowNLP
from application import app

route_emotionanalysisapi = Blueprint('emotionanalysisapi_page',__name__)


@route_emotionanalysisapi.route('/MarvelEmotionAnalysis',methods=["GET","POST"])
def MarvelEmotionAnalysis():
    req = request.values
    message = req.get('message')
    # app.logger.info(message)
    s = SnowNLP(str(message))
    count = s.sentiments
    app.logger.info(count)
    keywords = s.keywords()
    data = {'count':count,'keywords':keywords}
    return data


@route_emotionanalysisapi.route('/moviesunrise',methods=["GET","POST"])
def moviesunrise():
    req = request.values
    id = req.get('id')
    rs = Moviesunrise.query.filter_by(id=id).first()
    words = rs.content.strip()
    s = SnowNLP(str(words))
    count = s.sentiments
    keywords = s.keywords()
    data = {'id':id,'count':count,'keywords':keywords}
    resp = {'code':200,'msg':count,'data':{}}
    return data



@route_emotionanalysisapi.route('/moviekill',methods=["GET","POST"])
def moviekill():
    req = request.values
    id = req.get('id')
    rs = Moviekill.query.filter_by(id=id).first()
    words = rs.content.strip()
    s = SnowNLP(str(words))
    count = s.sentiments
    keywords = s.keywords()
    data = {'id':id,'count':count,'keywords':keywords}
    resp = {'code':200,'msg':count,'data':{}}
    return data
