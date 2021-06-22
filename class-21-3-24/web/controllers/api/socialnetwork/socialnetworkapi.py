from flask import Blueprint, request
from application import app
import os
import pandas as pd
import json

route_socialnetworkapi = Blueprint('socialnetworkapi_page', __name__)


@route_socialnetworkapi.route('/peopleintro', methods=["GET", "POST"])
def peopleintro():
    req = request.values
    name = req.get('name')
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    SITE_ROOT = SITE_ROOT[:-30]
    docs_url = os.path.join(SITE_ROOT, "static/docs/MarvelData", "message.csv")
    data = pd.read_csv(docs_url, header=None, names=[
                       'name', 'fullname', 'isalive', 'group'])
    info = data.loc[data['name'] == name].values
    info = info[0]
    # app.logger.info(info)
    res = "<br><br><br><img class='img-responsive' style='margin: 0 auto ' src='https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/images_doc/marvel/nodeIcons/" + \
        info[0]+".svg' alt=''><br><h4>人物:"+info[0]+"</h4><h4>全称:" + \
        info[1]+"</h4><h4>状况:"+info[2]+"</h4><h4>阵营:"+info[3]+"</h4>"
    # app.logger.info(SITE_ROOT)
    return str(res)
