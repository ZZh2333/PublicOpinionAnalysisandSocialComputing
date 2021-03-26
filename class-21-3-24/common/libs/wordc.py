import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 分词方法
def cut(words):
    # 加载自定义词库
    jieba.load_userdict('docs/AIDict.txt')
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
    # 加载休止符
    with open('docs/stopword.txt','r',encoding='utf-8') as ft:
        stopword = ft.read()
    # 筛选词语
    for seg in ci:
        if tf[seg]<5 or len(seg)<2 or seg in stopword:
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
    wc = WordCloud(background_color='white',font_path=font).generate_from_frequencies(wcdata)
    plt.imshow(wc)
    plt.axis('off')
    picname = "web/static/outputs/news.jpg"
    wc.to_file(picname)
    return picname
