import pandas as pd
import chardet
import os
import re
import jieba

file_name = os.path.abspath("""../data/news_chinese_sqlResult_1558435.csv""")

with open(file_name, 'rb') as f:
    encoding = chardet.detect(f.readline())
print(encoding)

df = pd.read_csv(file_name, encoding=encoding['encoding'], error_bad_lines=False, header=None, dtype='str')
df = df.fillna('')
content = df.iloc[:, 3].to_list()
content = content[:1000]

# print(content)
def token(String):
    return String.replace('\n',' ')

def cut(n):
    return ' '.join(jieba.cut(n))

content = [token(x) for x in content]
content = [cut(x) for x in content]

def naive_search(keywords):
    news_ids = [i for i,n in enumerate(content) if all(w in n for w in keywords.split())]
    return  news_ids

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.spatial.distance import cosine
vec = TfidfVectorizer(max_features=50000)
X = vec.fit_transform(content)

# print(vec.vocabulary_.keys())
# print(X[0])
# print(X[0].toarray())
# print(np.where(X[0].toarray()))

Y = np.transpose(X).toarray()
# print(Y[0])
words = vec.vocabulary_.keys()
word2id = vec.vocabulary_
id2word = {v:k for k,v in word2id.items()}
document = list(range(len(content)))
print(Y.shape)
# print(Y)
# print(id2word)
# print(np.where(Y[27280]))
# print(np.where(Y[27280])[0])


from functools import reduce
from operator import  and_
def search_engineer(query):
    words = query.split()
    # print(words)
    # print(vec.transform([' '.join(words)]))
    quary_vec = vec.transform([' '.join(words)]).toarray()
    # print(quary_vec)
    candidates_ids = [word2id[w] for w in words]
    # print(candidates_ids)
    # print(np.where(Y[34468]))
    # [(np.where(Y[id])[0]) for id in candidates_ids]
    document_ids = [
        list(np.where(Y[id])[0]) for id in candidates_ids
    ]

    megerd_document =  reduce(and_,document_ids)

    return sorted(megerd_document,key = lambda i:cosine(X[i].toarray(),quary_vec))

    # return megerd_document

# print(naive_search('美军'))
print(search_engineer('美军'))
print('888')
print(np.where(vec.transform(['美军','国家']).toarray()))
print([i for i in vec.transform(['美军','国家']).toarray()[0] if i != 0.])
# print(np.where(Y[word2id['美军']]))
print('888')
print([i for i in Y[word2id['美军']] if i != 0.])
print(vec.transform(['美军']).toarray()[0] == Y[word2id['美军']])
a = vec.transform(['美军 国家'])
print(a)
print([i for i in  a.toarray()[0] if i != 0.])

a = vec.transform(['美军'])
# print(for )
print(a)
print([i for i in  a.toarray()[0] if i != 0.])

def document_frequency(word):
    return sum(1 for n in content if word in n)
def idf(word):
    import math
    return math.log10(len(content)/document_frequency(word))
# print(Y[word2id['美军']])
import math
print(len(Y))
print(idf('美军'))
print(idf('国家'))

print(document_frequency('美军'))
print(document_frequency('国家'))



# print(content[187])
# for id in search_engineer('国防'):
#     print(id)

# for id in naive_search('小米 此外'):
#     print(id)

# print(conaive_searchntent[naive_search('小米 此外'.split())])
