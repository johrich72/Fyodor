from __future__ import division
# -*- coding: utf-8 -*-
import re
import nltk


#figure out some formal delimtiers of the txt
document = open("/home/christoph/Dokumente/Dostoyevsky/thegambler.txt",'r')
lines = document.readlines()
document.close()
delimiter = [[],[],[],[],[],[],[],[],[]]
temp = 0
linecount = 0
chapter  = []
for line in lines:
    linecount = linecount + 1
    if re.match('\s*[A-ZÄÖÜ\d\.\s]{0,10}\s*\n', line):
        temp = temp +1
        #print line
    else:
            if temp > 1:
                    delimiter[temp-1].append(linecount-temp)
            temp = 0

# return the most common delimiter
ref = 0
for l in delimiter:
       if len(l) > ref:
               best = l
               ref = len(l)
               
# returns a list of chapters
start = 1
for line in best:
        s = ''.join(lines[start:line])
        chapter.append(s)
        start = line

#tokenize each chapter
tokens = []
for c in chapter:
    tokens.append(nltk.word_tokenize(c))
    
#make nltk Text
text = []
for t in tokens:
    text.append(nltk.Text(t))
    
#make Frequency Distribustion
dist = []
for te in text:
    dist.append(nltk.FreqDist(te))


superwords = []
from nltk.corpus import stopwords
temp = 0
for d in dist:
    templist = []
    for key in d.keys():
        if len(templist) > 5:
            break
        else:
            if key.lower().strip() not in stopwords.words('english') and len(key) > 3:
                templist.append(key)
    superwords.append(templist)



sentences = []
for c in chapter:
    sentences.append(nltk.sent_tokenize(c))

for s in sentences[1]:
    if superwords[1][1] and superwords[1][2] and superwords[1][0]  in s:
        print 'true'






