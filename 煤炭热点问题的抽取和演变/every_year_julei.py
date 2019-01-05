from sklearn.cluster import Birch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname=r'C:\\Windows\\Fonts\\汉仪魏碑简.ttf')

file1 = ['E:\\a\\2005.txt','E:\\a\\2006.txt','E:\\a\\2007.txt','E:\\a\\2008.txt','E:\\a\\2009.txt',
        'E:\\a\\2010.txt','E:\\a\\2011.txt','E:\\a\\2012.txt','E:\\a\\2013.txt','E:\\a\\2014.txt',
        'E:\\a\\2015.txt','E:\\a\\2016.txt','E:\\a\\2017.txt','E:\\a\\2018.txt']
file2 = ['E:\\b\\2005.txt','E:\\b\\2006.txt','E:\\b\\2007.txt','E:\\b\\2008.txt','E:\\b\\2009.txt',
        'E:\\b\\2010.txt','E:\\b\\2011.txt','E:\\b\\2012.txt','E:\\b\\2013.txt','E:\\b\\2014.txt',
        'E:\\b\\2015.txt','E:\\b\\2016.txt','E:\\b\\2017.txt','E:\\b\\2018.txt']
file3 = ['E:\\c\\2005.txt','E:\\c\\2006.txt','E:\\c\\2007.txt','E:\\c\\2008.txt','E:\\c\\2009.txt',
        'E:\\c\\2010.txt','E:\\c\\2011.txt','E:\\c\\2012.txt','E:\\c\\2013.txt','E:\\c\\2014.txt',
        'E:\\c\\2015.txt','E:\\c\\2016.txt','E:\\c\\2017.txt','E:\\c\\2018.txt']

#读取文件
def read1(i):
    # 新建列表
    corpus = []
    f = open(file1[i], 'r+')
    #按行读取
    lines = f.readlines()
    for i in range(len(lines)):
        content = lines[i]
        #按行加入列表
        corpus.append(content)
    f.close()
    return corpus

def read2(i):
    corpus = []
    f = open(file1[i], 'r+',encoding='ANSI')
    #按行读取
    lines = f.readlines()
    for i in range(len(lines)):
        content = lines[i]
        #按行加入列表
        corpus.append(content)
    f.close()
    return corpus

#计算关键词权值
def deal(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    # print(weight.shape)
    return word,weight

#设置3个类并分类
def julei(word,weight):
    clusterer = Birch(n_clusters=3)
    y = clusterer.fit_predict(weight)
    print(y)
    print(y.shape)
    
    for i in range(14):
        f2 = open(file3[i], 'w+')
        for j in range(len(y)):
            f2.write(word[j] + "   " + str(y[j]) + "\n")
            # print(word[j] + "   " + str(y[j]))
    f2.close()
    return y

#对分类结果计数
def jishu(y):

    a = 0
    b = 0
    c = 0
    for i in range(len(y)):
        if y[i] == 0:
            a += 1
        if y[i] == 1:
            b += 1
        if y[i] == 2:
            c += 1
    print('第0类的个数为：'+str(a)+'\n'+
          '第1类的个数为：'+str(b)+'\n'+
          '第2类的个数为：'+str(c)+'\n'+
          '        ')
    return a,b,c

#得出每年的热点类
def hot0(a):
    x = a

    # print(x)
    return x


def hot2(c):
    z = c

    # print(x)
    return z

if __name__ == '__main__':
    Longitudinal0 = []
    Longitudinal2 = []
    Transverse = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    for i in range(len(file1)):
        print('这是'+str(i+2005)+'年的聚类结果：')
        if i != 4:
            aaa = []
            aaa = read1(i)
            bbb,ccc = deal(aaa)
            ddd = julei(bbb,ccc)
            eee = jishu(ddd)
            # Longitudinal0.append(hot0(eee[0]))
            Longitudinal2.append(hot2(eee))

        else:
            aaa = read2(i)
            bbb, ccc = deal(aaa)
            ddd = julei(bbb, ccc)
            eee = jishu(ddd)
            # Longitudinal0.append(hot0(eee[0]))
            Longitudinal2.append(hot2(eee))
    # print(Transverse)
    # print(Longitudinal)

    # plt.figure(1, dpi=100)
    # plt.plot(Transverse,Longitudinal0)
    # plt.title(u'按年度的热点轨迹',fontproperties=myfont)
    # plt.xlabel('年份变化-->',fontproperties=myfont)
    # plt.ylabel('0类的个数',fontproperties=myfont)
    # plt.savefig('hot.jpg')
    # plt.show()

    plt.figure(1, dpi=100)
    plt.plot(Transverse, Longitudinal2)
    plt.title(u'按年度的热点轨迹', fontproperties=myfont)
    plt.xlabel('年份变化-->', fontproperties=myfont)
    plt.ylabel('蓝色=0类，橙色=1类，绿色=2类', fontproperties=myfont)
    plt.savefig('hot2.jpg')

