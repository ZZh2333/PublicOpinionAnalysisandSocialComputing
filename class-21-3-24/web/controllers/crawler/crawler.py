from flask import Blueprint, render_template

route_crawier = Blueprint('crawier_page',__name__)


@route_crawier.route('/')
def crawier():
    return render_template('/crawier/index.html')