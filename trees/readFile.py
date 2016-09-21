# coding=utf-8
import codecs
import jieba
import json
from wordcloud import WordCloud

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


file = codecs.open('003.txt','r');

text =  file.read().decode('gbk')

seg_list = jieba.cut(text, cut_all=False)


wordCounts = {}

for words in seg_list:
	currentLabel = words
	if currentLabel not in wordCounts.keys():
		wordCounts[currentLabel] = 0
	wordCounts[currentLabel]+=1

jsonlist = []

# dict= sorted(wordCounts.iteritems(), key=lambda d:d[1], reverse = True)
for key in wordCounts.keys():
	if wordCounts[key] > 150 & len(key)>=2:
		# info = {}
		# info["key"] = key
		# info["counts"] = wordCounts[key]
		info=(key,wordCounts[key])
		jsonlist.append(info)

# savefile = open('jueji.json','w')
# savefile.write("")
# savefile.close()
# file2 = open('jueji.json','a')

# # jsonString = json.dumps(jsonlist)
# for x in jsonlist:
# 	file2.write(x[0])
# 	file2.write(',')
# 	file2.write(str(x[1]))
# 	file2.write('\n')

# file2.close()
# jsonlist2 = [(u"的是",4),(u"有趣",2)]

wordcloud = WordCloud(font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc").fit_words(jsonlist)

import matplotlib.pyplot as plt 
plt.imshow(wordcloud) 
plt.axis("off") 
# take relative word frequencies into account, lower max_font_size 
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text) 
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5,font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc").fit_words(jsonlist) 
plt.figure() 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.show()

