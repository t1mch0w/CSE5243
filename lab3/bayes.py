import sys
import time

import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

def cosine(x, y):
	return np.sum(x*y)/(np.sqrt(np.sum(x*x))*np.sqrt(np.sum(y*y)))

totalx=[]
totaly=[]
with open(sys.argv[1],'r') as f:
	for line in f:
		tmp=line.split()
		tmparray=[]
		for i in range(2,len(tmp)):
			tmparray.append(float(tmp[i]))
		totalx.append(tmparray)

with open(sys.argv[2],'r') as f:
	for line in f:
		totaly.append(line.strip())

trainx, testx, trainy, testy = train_test_split(totalx, totaly, test_size=0.2)
#trainx, testx, trainy, testy = train_test_split(totalx, totaly, test_size=0.4)

clf = GaussianNB()

start_time = time.time()
clf.fit(trainx,trainy)
traintime=(time.time()-start_time)/len(trainx)

start_time = time.time()
result=clf.predict(testx).tolist()
testtime=(time.time()-start_time)/len(testx)

print traintime, testtime, accuracy_score(testy, result)
