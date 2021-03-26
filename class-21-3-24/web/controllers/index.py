from flask import Blueprint

route_index = Blueprint('index_page',__name__)


@route_index.route('/')
def index():
    return "欢迎关注中传小涵的GitHub：https://github.com/ZZh2333?tab=repositories"