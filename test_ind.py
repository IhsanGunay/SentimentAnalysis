import os
from pickle import load, dump
from itertools import chain
from nltk.tokenize import word_tokenize as tokenize
from scipy.sparse import lil_matrix
from phrases import phrases

testf = 'test.file'

with open('sword.set', 'rb') as f:
    sword_list = load(f)

with open('phrase.set','rb') as f:
    phrase_list = load(f)

problem = lil_matrix((1, 17173))
n = 0

with open(testf) as f:
    text = f.read()
    tokens = tokenize(text)
    fphrases = phrases(tokens)

with open('test.feat','a') as f:
    for token in tokens:
        if token in sword_list:
            ind = sword_list.index(token)
            problem[0, ind] = 1
            f.write(str(token)+'\n')
    for p in fphrases:
        if p in phrase_list:
            ind = phrase_list.index(p) +3111
            problem[0, ind] = 1
            f.write(str(p) + '\n')

with open('test_ind.matrix', 'wb') as f:
    dump(problem, f)
