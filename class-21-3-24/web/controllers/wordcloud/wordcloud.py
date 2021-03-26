from flask import Blueprint, render_template

route_wordcloud = Blueprint('wordcloud_page',__name__)

@route_wordcloud.route('/')
def wordcloud():
    return render_template('wordcloud/wordcloud.html')