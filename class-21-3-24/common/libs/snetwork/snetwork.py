import pandas as pd
import os

def findname(num):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    SITE_ROOT = SITE_ROOT[:-20]
    docs_url = os.path.join(SITE_ROOT,"web/static/docs","fb-pages-food.nodes")
    mapping = pd.read_csv(docs_url)
    name = mapping.loc[(mapping['new_id']==num)]['name'].values[0]
    # print(name)
    return name