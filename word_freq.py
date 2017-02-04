# -*- coding: utf-8 -*-
# /取除数 %取余数
from __future__ import unicode_literals

word_freq={}
file=open('WordFreqTest.txt','rw')
for line in file:
	words = line.strip().split()
#strip() clear space and specific symbol
#split() split word by space (default)
	for word in words:
		if word in word_freq:
			word_freq[word]+=1
		else: 
			word_freq[word]=1
#print line.title() #首字母自动大写
file.close()

print word_freq
freq_word = []
for word,freq in word_freq.items():
	freq_word.append((freq,word))
freq_word.sort(reverse = True)
print freq_word
for freq,word in freq_word[:3]:
	print word,freq

print "词频分布："
dict1 = {}
for word,freq in word_freq.items():
	if freq in dict1:
		dict1[freq].append(word)
	else:
		dict1[freq]=[word]
print dict1
