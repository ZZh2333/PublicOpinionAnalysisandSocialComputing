from flask import Blueprint, render_template

route_socialnetwork = Blueprint('socialnetwork_page',__name__)


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
    return render_template('/socialnetwork/test.html')