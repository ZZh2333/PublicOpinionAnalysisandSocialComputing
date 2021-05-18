from application import app
from web.controllers.index import route_index
from web.controllers.static import route_static

from web.controllers.api.emotionanalysisapi.emotionanalysisapi import route_emotionanalysisapi
from web.controllers.wordcloud.wordcloud import route_wordcloud
from web.controllers.crawler.crawler import route_crawier
from web.controllers.socialnetwork.socialnetwork import route_socialnetwork

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_static, url_prefix="/static")

app.register_blueprint(route_emotionanalysisapi,url_prefix='/emotionanalysisapi')
app.register_blueprint(route_wordcloud,url_prefix='/wordcloud')
app.register_blueprint(route_crawier,url_prefix='/crawier')
app.register_blueprint(route_socialnetwork,url_prefix='/socialnetwork')