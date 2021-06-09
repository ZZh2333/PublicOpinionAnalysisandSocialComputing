from flask import Blueprint, render_template, request
from application import app
import os
import json 
import pandas
from common.libs.snetwork.snetwork import findname
from common.libs.snetwork.HITSIterator import HITSIterator
from pygraph.classes.digraph import digraph


route_socialnetwork = Blueprint('socialnetwork_page',__name__)


@route_socialnetwork.route('/facebook',methods=["Get","Post"])
def facebook():

    wanted = request.args.get("wanted",type=str)
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    SITE_ROOT = SITE_ROOT[:-25]
    docs_url = os.path.join(SITE_ROOT,"static/docs","fb-pages-food.edges")
    data = pandas.read_csv(docs_url)
    data = data.values
    links = []

    if not wanted or int(wanted)>619 or int(wanted)<0:
        for row in data:
            tmp = {"source":row[0],"target":row[1]}
            links.append(tmp)
        return render_template('/socialnetwork/new_facebook.html',data=str(links).replace('[','').replace(']',''))

    else:
        info = []
        info.append(int(wanted))
        info.append(findname(int(wanted)))

        dg = digraph()
        nodes = []
        for row in data:
            if(row[0]==int(wanted) or row[1]==int(wanted)):
                if row[0] not in nodes:
                    nodes.append(row[0])
                    dg.add_node(str(row[0]))
                if row[1] not in nodes:
                    nodes.append(row[1])
                    dg.add_node(str(row[1]))

                dg.add_edge((str(row[0]),str(row[1])))

                tmp = {"source":row[0],"target":row[1]}
                links.append(tmp)
        
        hits = HITSIterator(dg)
        authority, hub = hits.hits()
        info.append(hub[wanted])
        info.append(authority[wanted])
        return render_template('/socialnetwork/new_facebook.html',data=str(links).replace('[','').replace(']',''),info=info)

# @route_socialnetwork.route('/facebook')
# def facebook():
#     SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     SITE_ROOT = SITE_ROOT[:-25]
#     docs_url = os.path.join(SITE_ROOT,"static\json","newtest.json")
#     with open(docs_url) as f:
#         data = json.load(f)
#     data = str(data).replace("[","").replace("]","")
#     return render_template('/socialnetwork/new_facebook.html',data=data)


@route_socialnetwork.route('/renmin')
def renmin():
    return render_template('/socialnetwork/renmin.html')


@route_socialnetwork.route('/github')
def github():
    return render_template('/socialnetwork/github.html')


@route_socialnetwork.route('/example')
def example():
    return render_template('/socialnetwork/example.html')


@route_socialnetwork.route('/test')
def test():
    return render_template('/socialnetwork/facebook.html')