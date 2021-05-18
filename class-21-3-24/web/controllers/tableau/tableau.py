from flask import Blueprint, render_template

route_tableau = Blueprint('tableau_page',__name__)

@route_tableau.route('tableauonline')
def tableauonline():
    return render_template('/tableau/tableauonline.html')