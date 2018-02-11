#!/usr/bin/python

import sys
from operator import itemgetter

wordcount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue

    try:
         wordcount[word] = wordcount[word]+count
    except:
         wordcount[word] = count

sorted_wordcount = sorted(wordcount.items(),key=itemgetter(0))

for word,count in sorted_wordcount:
    print "%s\t%s" %(word, count)
