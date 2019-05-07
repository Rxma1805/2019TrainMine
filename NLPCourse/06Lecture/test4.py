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

def token(String):
    return String.replace('\n',' ')

def cut(n):
    return ' '.join(jieba.cut(n))

new_content = [token(x) for x in content]
new_content = [cut(x) for x in new_content]
with open('test.txt','w',encoding='utf8') as f:
    for x in new_content:
        f.write(x.strip()+'\n')

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
w = Word2Vec(LineSentence('test.txt'))
# print(w.wv.vocab)
# print(w.most_similar('小米'))

from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=2**10)
def get_releated_word(initialine,model):
    unseen = [initialine]
    seen = defaultdict(int)
    max_size = 500
    while unseen and len(seen)<max_size:
        node = unseen.pop(0)
        new_expanding = [w for w,s in model.most_similar(node,topn=20)]
        unseen += new_expanding
        seen[node] += 1

        # optimal 1:score function could be revided
        # optimal 2:using dymanic programing to reduce
    return seen

print(len(w.wv.vocab))
relate_word = get_releated_word('说',w)
sort_relate_word = sorted(relate_word.items(),key=lambda x:x[1],reverse=True)
print(relate_word)
print(sort_relate_word)


# key words  tf-idf
# idf = log N/dft
#  tf-idf = tf x idf
def document_frequency(word):
    return sum(1 for n in new_content if word in n)
def idf(word):
    import math
    return math.log10(len(new_content)/document_frequency(word))
print(idf('的'))
print(idf('小米'))
def tf(word,document):
    return sum([1 for n in document.split() if word == n])
print(tf('银行',new_content[11]))

def get_keywords_of_a_document(document):
    words = set(document.split())
    tfidf = [
        (w,tf(w,document)*idf(w)) for w in words
    ]
    tfidf = sorted(tfidf,key=lambda x:x[1],reverse=True)
    return tfidf
# %pure
word_frequency = {w:k  for w,k in get_keywords_of_a_document(new_content[11])}

import wordcloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

wc = wordcloud.WordCloud('SourceHanSerifSC-Regular.otf')
img = wc.generate_from_frequencies(word_frequency)
plt.imshow(img)
plt.show()

from PIL import Image
import numpy as np


print(np.array(Image.open('images.png')))
mask= np.array(Image.open('images.png'))

plt.figure()
wc = wordcloud.WordCloud(
    # background_color="white",
    max_words=10,
    font_path='SourceHanSerifSC-Regular.otf',
    mask=mask,
    )
img=wc.generate_from_frequencies(word_frequency)
plt.imshow(img)
plt.show()

from sklearn.feature_extraction.text import TfidfVectorizer
Vect = TfidfVectorizer(max_features=10000)#单词总数
X = Vect.fit_transform(new_content)
# print(X.shape)
# print(Vect.vocabulary)
word2vec = Vect.vocabulary_
vec2word = { word2vec[k]:k   for k in word2vec}
print(np.where(X[0].toarray()))

# print(vec2word[])
import random
from scipy.spatial.distance import cosine

def distance(v1,v2):
    return cosine(v1,v2)

document_id1 = random.randint(0,1000)
document_id2 = random.randint(0,1000)
document_id3 = random.randint(0,1000)

vec1 = X[document_id1].toarray()
vec2 = X[document_id2].toarray()
vec3 = X[document_id3].toarray()

print(distance(vec1,vec2))
print(distance(vec1,vec3))

print(sorted(list(range(1000)),key=lambda i:distance(X[i].toarray(),X[document_id1].toarray())))

print(new_content[418])

print(new_content[356])