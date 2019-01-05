#encode = utf-8
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 读取数据，进行TF-IDF计算
file1 = ['E:\\a\\2005.txt','E:\\a\\2006.txt','E:\\a\\2007.txt','E:\\a\\2008.txt','E:\\a\\2009.txt',
        'E:\\a\\2010.txt','E:\\a\\2011.txt','E:\\a\\2012.txt','E:\\a\\2013.txt','E:\\a\\2014.txt',
        'E:\\a\\2015.txt','E:\\a\\2016.txt','E:\\a\\2017.txt','E:\\a\\2018.txt']
# 存取数据的分词结果
file2 = ['E:\\b\\2005.txt','E:\\b\\2006.txt','E:\\b\\2007.txt','E:\\b\\2008.txt','E:\\b\\2009.txt',
        'E:\\b\\2010.txt','E:\\b\\2011.txt','E:\\b\\2012.txt','E:\\b\\2013.txt','E:\\b\\2014.txt',
        'E:\\b\\2015.txt','E:\\b\\2016.txt','E:\\b\\2017.txt','E:\\b\\2018.txt']


print('计算tf-idf，并保存到E盘的b文件夹下')

def idf1(i):
    corpus = []
    f = open(file1[i], 'r+')
    content = f.read()
    f.close()
    corpus.append(content)
    #将得到的词语转换为词频矩阵
    vectorizer = CountVectorizer()
    #统计每个单词的tf-idf权值
    transformer = TfidfTransformer()
    #计算出tf-idf并转换为tf-idf矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    # 所有文本的关键字
    word = vectorizer.get_feature_names()
    # 对应的tfidf矩阵
    weight = tfidf.toarray()
    return word,weight
def idf2(i):
    corpus = []
    f = open(file1[i], 'r+',encoding='ANSI')
    content = f.read()
    f.close()
    corpus.append(content)
    #将得到的词语转换为词频矩阵
    vectorizer = CountVectorizer()
    #统计每个单词的tf-idf权值
    transformer = TfidfTransformer()
    #计算出tf-idf并转换为tf-idf矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    # 所有文本的关键字
    word = vectorizer.get_feature_names()
    # 对应的tfidf矩阵
    weight = tfidf.toarray()
    return word,weight

# 这里将每份文档词语的TF-IDF写入文件中保存
def save(word,weight):
    # for i in range(len(file2)):
    f2 = open(file2[i], 'w+')

        # for j in range(len(word)):
    f2.write(str(word) + "   " + str(weight) + "\n")
    f2.close()

if __name__ == '__main__':
    for i in range(len(file1)):
        a = []
        if i !=4:
            a,b = idf1(i)
            for j in range(len(file2)):
                if j != 4:
                    c = save(a,b)
        else:
            a, b = idf2(i)
            for j in range(len(file2)):
                if j == 4:
                    c = save(a, b)

        print('第' + str(i+1) + '个文件已保存')
