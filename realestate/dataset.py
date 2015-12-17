from __future__ import absolute_import, unicode_literals  # noqa

import os

import lda.utils

import numpy as np
import lda

def load_realestate():
        realestate_ldac_fn = 'realestate_dtm.ldac'
        return lda.utils.ldac2dtm(open(realestate_ldac_fn), offset=0)
		
def load_realestate_vocab():
        with open('realestate_vocab.txt') as f:
            vocab = tuple(f.read().split())
        return vocab
		
X = load_realestate()
vocab = load_realestate_vocab()

model = lda.LDA(n_topics=5, n_iter=1500, random_state=1)
model.fit(X)
topic_word = model.topic_word_
n_top_words = 3

for i, topic_dist in enumerate(topic_word):
	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
	print('Topic {}: {}'.format(i, ' '.join(topic_words)))
	
# show the document topic distributions 
doc_topic = model.doc_topic_
for i in range(10):
	print ("{} (top topic: {})".format(i, doc_topic[i].argmax()))