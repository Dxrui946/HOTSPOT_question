from sklearn.cluster import Birch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#新建列表
corpus = []
#读取文件
f = open('E:\\a\\all_year.txt', 'r+',encoding='ANSI')
#按行读取
lines = f.readlines()
for i in range(len(lines)):
    # print(lines[i])
    content = lines[i]
    #按行加入列表
    corpus.append(content)
f.close()
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
word = vectorizer.get_feature_names()
weight = tfidf.toarray()
# print(weight.shape)

#设置3个类
clusterer = Birch(n_clusters=3)
y = clusterer.fit_predict(weight)
# print(y)
# print(y.shape)

#输出聚类结果
f2 = open('E:\\c\\all_year.txt', 'w+')
for j in range(len(y)):
    f2.write(word[j] + "   " + str(y[j]) + "\n")
f2.close()
print('已将聚类结果存储到e盘下c文件夹中的all_year.txt中')

#对分类结果计数
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
print('第0类的个数为：'+str(a)+'\n'+'第1类的个数为：'+str(b)+'\n'+'第2类的个数为：'+str(c))




#输出词频矩阵
# for i in range(len(weight)):
#     f1 = open('E:\\b\\all_year.txt', 'w+')
#     for j in range(len(word)):
#         f1.write(word[j] + "   " + str(weight[i][j]) + "\n")
# f1.close()
