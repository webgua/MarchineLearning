from os import path
from wordcloud import WordCloud
import codecs

# d = path.dirname(_file_)

text = codecs.open('004.txt','r').read().decode('gbk')
# print text
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt 
plt.imshow(wordcloud)
plt.axis("off")

wordcloud = WordCloud(max_font_size=40,relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()