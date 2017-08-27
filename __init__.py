#-*- coding:utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pylab as plt
from os import path

filename = 'Friends.txt'
with open(filename) as f:
    mytext = f.read()
wordcloud = WordCloud().generate(mytext)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("Friends.jpg")
