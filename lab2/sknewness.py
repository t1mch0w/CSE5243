#!/usr/bin/python

import sys
import collections
import math
import numpy as np

# Open results
data=[]
i=0
with open(sys.argv[1],'r') as f:
	for line in f.readlines():
		data.append(int(line))
		i+=1
		#if len(line)==0:
		#	continue
		#data.append(len(line.split()))
print data
v = np.var(data)
u=np.mean(data)
o=math.sqrt(v)
tmp=0.0
for ele in data:
	tmp+=(ele-u)*(ele-u)*(ele-u)
tmp=tmp/(i*o*o*o)

print tmp
print v
