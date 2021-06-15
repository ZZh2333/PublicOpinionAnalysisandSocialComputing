from flask import Blueprint, request
from common.libs.Hepler import get_ticket
import requests
from application import app

route_tableauserverapi = Blueprint('tableauserverapi_page',__name__)


@route_tableauserverapi.route('/tableauserver',methods=["GET","POST"])
def tableauserver():
    req = request.values
    username = req.get('username')
    ticket = get_ticket(username)
    app.logger.info(ticket)
    data = {'ticket':str(ticket)}
    return data