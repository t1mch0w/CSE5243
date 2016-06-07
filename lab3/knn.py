import sys
import time

import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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


#for k in [35,70,133,260]:
for k in [133]:
	#for i in range(0,3):
	for i in [1]:
		#k=len(totalx)/65
		print 'k=',k
		if i==2:
			neigh = KNeighborsClassifier(n_neighbors=k,metric='pyfunc', func=cosine)
			print 'cosine'
		elif i==0:
			neigh = KNeighborsClassifier(n_neighbors=k,metric='euclidean')
			print 'euclidean'
		else:
			neigh = KNeighborsClassifier(n_neighbors=k,metric='manhattan')
			print 'manhattan'
		
		start_time = time.time()
		neigh.fit(trainx,trainy)
		#traintime=(time.time()-start_time)/len(trainx)
		traintime=(time.time()-start_time)
		print 'train time:', traintime 
		
		start_time = time.time()
		result=neigh.predict(testx).tolist()
		#testtime=(time.time()-start_time)/len(testx)
		testtime=(time.time()-start_time)
		print 'test time:', testtime 
		print accuracy_score(testy, result)

		print traintime, testtime, accuracy_score(testy, result)
