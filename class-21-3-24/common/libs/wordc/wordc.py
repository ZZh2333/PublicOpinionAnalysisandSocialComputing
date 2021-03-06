import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
from PIL import Image
import numpy as np

# 分词方法
def cut(words):
    # 加载自定义词库
    # jieba.load_userdict('docs/AIDict.txt')
    # 分词
    seg_list = jieba.cut(words,cut_all=False)
    # 词频统计
    tf = {}
    for seg in seg_list:
        if seg in tf:
            tf[seg] += 1
        else:
            tf[seg] = 1
    # 出现的词
    ci = list(tf.keys())

    # 加载停顿词
    # with open('docs/stopword.txt','r',encoding='utf-8') as ft:
    #     stopword = ft.read()

    # 筛选词语
    for seg in ci:
        if tf[seg]<10 or len(seg)<2:
            tf.pop(seg)
    ci = list(tf.keys())
    num = list(tf.values())
    data = []
    for i in range(len(tf)):
        data.append((num[i],ci[i]))
    data.sort()
    data.reverse()
    return data

# 词云图方法
def wordcloudpic(data):
    wcdata = {}
    for d in data:
        wcdata[d[1]] = d[0]
    font = r'C:\Windows\Fonts\simfang.ttf'
    # mask = np.array(Image.open("web/static/img/cuc.jpg"))
    # wc = WordCloud(background_color='white',mask=mask,font_path=font).generate_from_frequencies(wcdata)
    wc = WordCloud(background_color='white',font_path=font).generate_from_frequencies(wcdata)
    datetime = time.strftime("%Y%m%d%H%M%S",time.localtime())
    picname = "web/static/outputs/news"+datetime+".jpg"
    wc.to_file(picname)
    return picname,datetime
