import numpy as np

# Get the interactive Tools for Matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.decomposition import PCA

from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import os
input_file = os.path.abspath('../glove.6B/glove.6B.100d.txt')
output_file = os.path.abspath('./glove.6B.100d.word2vec.txt')
glove_file = datapath(input_file)
print(glove_file)
word2vec_glove_file = get_tmpfile(output_file)
print(word2vec_glove_file)
glove2word2vec(glove_file, word2vec_glove_file)