import datetime
from flask import g, render_template
from numpy import random
import requests


# # 获取当前时间
# def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
#     return datetime.datetime.now().strftime(format)
#     # return datetime.datetime.now().strftime( format )

def getCurrentDate():
    return datetime.datetime.now()


# 获取格式化的时间
def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
    if date is None:
        date = datetime.datetime.now()

    return date.strftime(format)


# 统一渲染方法
def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


def randomIntIndex(index,begin,end):
    result = []
    for i in range(index):
        a = random.randint(begin,end)
        result.append(a)
    return result




def get_ticket(username):
    tbserver = "http://172.17.33.144:8001"
    url = f"{tbserver}/trusted"
    data = {"username": username}
    res = requests.post(url=url, data=data)
    return(res.text)