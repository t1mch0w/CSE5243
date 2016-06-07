import random
import sys

f=open(sys.argv[1],'r')
lines=f.readlines()
f.close()

random.shuffle(lines)
numlines = int(len(lines)*0.2)

filename=sys.argv[1].split('/')[-1]
trainfile=filename+'-train'
testfile=filename+'-test'

with open(testfile,'w') as f:
	f.writelines(lines[:numlines])

with open(trainfile,'w') as f:
	f.writelines(lines[:numlines])
