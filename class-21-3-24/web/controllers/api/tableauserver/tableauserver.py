from flask import Blueprint, request
from common.libs.Hepler import get_ticket

route_tableauserverapi = Blueprint('tableauserverapi_page',__name__)


@route_tableauserverapi.route('/tableauserver',methods=["GET","POST"])
def tableauserver():
    req = request.values
    username = req.get('username')
    ticket = get_ticket(username)
    return ticket