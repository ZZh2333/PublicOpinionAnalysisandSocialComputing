from flask import Blueprint, render_template
# import tableauserverclient as TSC
from application import app
import requests
from common.libs.Hepler import get_ticket

route_tableau = Blueprint('tableau_page', __name__)


@route_tableau.route('/tableauonline')
def tableauonline():
    return render_template('/tableau/tableauonline.html')


@route_tableau.route('/tableauUI')
def tableauUI():
    ticket = get_ticket("admin")
    app.logger.info(ticket)
    return render_template('/tableau/tableauUI.html', ticket=ticket)


@route_tableau.route("/tableauserver")
def tableauserver():
    ticket = get_ticket("admin")
    # app.logger.info(ticket)
    # tableau_auth = TSC.PersonalAccessTokenAuth('test_zzh', 'yyZjbwiHQcCPnCZrvpVB/A==:40Aw3vDmnUIabk3O8R3zhdfSUbhxoepl', '')
    # server = TSC.Server('http://172.17.33.144:8001/', use_server_version=True)
    # server.auth.sign_in(tableau_auth)

    return render_template('/tableau/tableauserver.html', ticket=ticket)
    # return("http://172.17.33.144:8001/trusted/"+ticket+"/views/test/1")


@route_tableau.route("/tableautest")
def tableautest():
    ticket = get_ticket("admin")
    app.logger.info(ticket)

    # yyZjbwiHQcCPnCZrvpVB/A==:40Aw3vDmnUIabk3O8R3zhdfSUbhxoepl

    # tableau_auth = TSC.PersonalAccessTokenAuth('test_zzh', 'yyZjbwiHQcCPnCZrvpVB/A==:40Aw3vDmnUIabk3O8R3zhdfSUbhxoepl', '')
    # server = TSC.Server('http://172.17.33.144:8001/', use_server_version=True)
    # server.auth.sign_in(tableau_auth)

    # tableau_auth = TSC.TableauAuth('admin', 'admin', site_id='')
    # server = TSC.Server('http://172.17.33.144:8001/', use_server_version=True)
    # server.auth.sign_in(tableau_auth)

    return render_template('/tableau/tableautest.html', ticket=ticket)
