#!/usr/bin/python

import sys
import collections
import math

# Open topics
topics={}
total=8654
with open('topic','r') as f:
	i=0
	for line in f.readlines():
		line=line.split()
		topics[i]=line[0]
		i+=1

# Open results
data=[]
with open(sys.argv[1],'r') as f:
	for line in f.readlines():
		if line=='':
			continue
		data.append(line.split())

entropy=0.0
for sdata in data:
	if len(sdata)==1:
		continue
	else:
		tmplist=[topics[int(x)] for x in sdata]
		tmpvalue=collections.Counter(tmplist)
		if len(tmpvalue)==1:
			continue	
		sumt=len(sdata)
		for ele in tmpvalue:
			tmp=float(tmpvalue[ele])/float(sumt)
			tmpentropy=(math.log(tmp,2))*tmp*-1
			entropy+=tmpentropy*sumt/total

print entropy
