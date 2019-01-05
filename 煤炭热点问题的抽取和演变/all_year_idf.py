#encode = utf-8
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 读取数据，进行TF-IDF计算
print('计算tf-idf，并保存到E盘的b文件夹下...')
corpus = []
#读取关键词文件
f = open('E:\\a\\all_year.txt', 'r+',encoding='ANSI')
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
weight = tfidf.toarray()

print(weight)

# # 这里将每份文档词语的TF-IDF写入文件中保存
for i in range(len(weight)):
    f2 = open('E:\\b\\all_year.txt', 'w+')
    for j in range(len(word)):
        f2.write(word[j] + "   " + str(weight[i][j]) + "\n")
f2.close()
print('保存成功')
