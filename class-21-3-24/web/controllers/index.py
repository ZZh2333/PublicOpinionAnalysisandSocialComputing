from flask import Blueprint
from common.libs.Hepler import ops_render

route_index = Blueprint('index_page',__name__)


@route_index.route('/')
def index():
    # return "欢迎关注中传小涵的GitHub：https://github.com/ZZh2333?tab=repositories"
    return ops_render("index/index.html")
