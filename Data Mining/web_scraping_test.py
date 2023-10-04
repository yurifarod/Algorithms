#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 02:41:21 2021

@author: yurifarod
"""

import re
import urllib3
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from bs4 import BeautifulSoup
from string import punctuation
import matplotlib.pyplot as plt

http = urllib3.PoolManager()
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Big_data')
content = pagina.data

sopa = BeautifulSoup(content, 'lxml')
for tags in sopa(['script', 'style']):
    tags.decompose()

text_content = ' '.join(sopa.stripped_strings)
text_content = re.sub('[-|0-9]', '', text_content)
text_content  = re.sub('a-zA-Z0-9áéíóúÁÉÍÓÚçÇ: ]', '', text_content)

nltk.download('punkt')
token = sent_tokenize(text_content)
word_token = word_tokenize(text_content.lower())

nltk.download('stopwords')
stopwords = set(stopwords.words('english') +
                stopwords.words('portuguese') +
                list(punctuation) + ['–', '↑', '«', '»', '·', 'b', 'c'])

word_token_clean = [word_token for word_token in word_token if word_token not in stopwords]

frequency = FreqDist(word_token_clean)

fig = plt.figure(figsize = (10,4))
plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
frequency.plot(10, cumulative=False)
plt.show()