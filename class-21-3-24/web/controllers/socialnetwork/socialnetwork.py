from flask import Blueprint, render_template, request
from application import app
import os
import json
import pandas
from common.libs.snetwork.snetwork import findname
from common.libs.snetwork.HITSIterator import HITSIterator
from pygraph.classes.digraph import digraph
import networkx as nx
import matplotlib.pyplot as plt
from random import choice


route_socialnetwork = Blueprint('socialnetwork_page', __name__)


@route_socialnetwork.route('/MarvelData', methods=["Get", "Post"])
def MarvelData():
    wanted = request.args.get("wanted", type=str)

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    SITE_ROOT = SITE_ROOT[:-25]
    docs_url = os.path.join(
        SITE_ROOT, "static/docs/MarvelData", "relation_message.csv")
    # nodes_docs_url = os.path.join(SITE_ROOT,"static\docs\MarvelData","names_message.csv")
    message_docs_url = os.path.join(
        SITE_ROOT, "static/docs/MarvelData", "message.csv")
    # nodes_data = pandas.read_csv(nodes_docs_url).values
    data = pandas.read_csv(docs_url, header=None, names=[
                           'begin', 'end', 'relationship']).values
    links = []
    nodes = []
    nodes_mapping = []

    people = pandas.read_csv(message_docs_url, header=None, names=[
                             'name', 'fullname', 'isalive', 'group']).values
    for row in people:
        # tmp = {"name":row[0],"image":"https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/images_doc/marvel/nodeIcons/"+row[0]+".svg","group":row[3],"intro":row[1]}
        tmp = {"name": row[0], "image": "https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/images_doc/marvel/nodeIcons/"+row[0]+".svg"}
        nodes.append(tmp)
        nodes_mapping.append(row[0])

    G = nx.Graph()
    for i in range(len(nodes_mapping)):
        G.add_node(i)
    for i in data:
        G.add_edge(nodes_mapping.index(
            i[0]), nodes_mapping.index(i[1]), relation=i[2])


    # # 绘出节点度数图
    # x = nx.degree(G)
    # # app.logger.info(x)
    # X = []
    # Y = []
    # for row in x:
    #     X.append(row[0])
    #     Y.append(row[1])
    # Y.sort()
    # Y.reverse()
    # plt.plot(Y)
    # plt.xlabel("num of point")
    # plt.ylabel("degree")
    # plt.savefig("pointDegree.png")

    # 绘出图分布图
    # degree = nx.degree_histogram(G)
    # x = range(len(degree))
    # y = [z/float(sum(degree)) for z in degree]
    # plt.plot(x,y,color=(1,0,0))
    # plt.savefig("degree.png")
    # plt.show()

    if not wanted:
        peoplelist = ["tonys","thor","stever","blackw","bruceb","rhody","hawke","bucky","loki","falcon"]
        # app.logger.info(choice(peoplelist))
        wanted=choice(peoplelist)

    if not wanted or wanted == "all":
        for row in data:
            tmp = {"source": nodes_mapping.index(
                row[0]), "target": nodes_mapping.index(row[1]), "relation": row[2]}
            links.append(tmp)
        return render_template('/socialnetwork/new_MarvelData.html', data=str(links).replace('[', '').replace(']', ''), nodes_data=str(nodes).replace('[', '').replace(']', ''))
    
    else:
        G1 = nx.ego_graph(G, nodes_mapping.index(wanted), 1)
        G1_nodes = []
        G1_edges = []
        G1_people = []
        G1_links = []
        for i in G1.nodes():
            G1_nodes.append(nodes_mapping[int(i)])
        for i,j in nx.get_edge_attributes(G1,'relation').items():
            tmp = (nodes_mapping[i[0]], nodes_mapping[i[1]])
            G1_edges.append((G1_nodes.index(tmp[0]), G1_nodes.index(tmp[1]),j))
        for i in G1_nodes:
            tmp = {"name": i, "image": "https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/images_doc/marvel/nodeIcons/"+i+".svg"}
            G1_people.append(tmp)
        for row in G1_edges:
            tmp = {"source": row[0], "target": row[1], "relation":row[2]}
            G1_links.append(tmp)
        return render_template('/socialnetwork/new_MarvelData.html', data=str(G1_links).replace('[', '').replace(']', ''), nodes_data=str(G1_people).replace('[', '').replace(']', ''))


@route_socialnetwork.route('/facebook', methods=["Get", "Post"])
def facebook():

    wanted = request.args.get("wanted", type=str)
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    SITE_ROOT = SITE_ROOT[:-25]
    docs_url = os.path.join(SITE_ROOT, "static/docs", "fb-pages-food.edges")
    data = pandas.read_csv(docs_url)
    data = data.values
    links = []

    if not wanted or int(wanted) > 619 or int(wanted) < 0:
        for row in data:
            tmp = {"source": row[0], "target": row[1]}
            links.append(tmp)
        return render_template('/socialnetwork/new_facebook.html', data=str(links).replace('[', '').replace(']', ''))

    else:
        info = []
        info.append(int(wanted))
        info.append(findname(int(wanted)))

        dg = digraph()
        nodes = []
        for row in data:
            if(row[0] == int(wanted) or row[1] == int(wanted)):
                if row[0] not in nodes:
                    nodes.append(row[0])
                    dg.add_node(str(row[0]))
                if row[1] not in nodes:
                    nodes.append(row[1])
                    dg.add_node(str(row[1]))

                dg.add_edge((str(row[0]), str(row[1])))

                tmp = {"source": row[0], "target": row[1]}
                links.append(tmp)

        hits = HITSIterator(dg)
        authority, hub = hits.hits()
        info.append(hub[wanted])
        info.append(authority[wanted])
        return render_template('/socialnetwork/new_facebook.html', data=str(links).replace('[', '').replace(']', ''), info=info)

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
