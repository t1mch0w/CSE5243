from hset import *

import sys
import math
import time
import Queue
import os
import threading
import itertools
from multiprocessing import Pool

class HCluster:
	data=[]
	length=0
	num=0
	clusters=[]
	distance={}
	max_index=0
	q=Queue.PriorityQueue()
	

	#def multi(self,sindex,findex):
	def multi(self,sindex):
		findex=sindex+2000
		tmplen=len(self.clusters)
		for i in range(sindex,findex):
			if i>=tmplen:
				break
			print 'compute', i
			self.name.append(i)
			for j in range(i+1,self.num):
				if i<j:
					self.dist(self.clusters[i],self.clusters[j])
			
	def __init__(self,data):
		self.data=data
		self.length=len(data[0])
		self.num=len(data)
		self.name=[]
		for i in range(0,self.num):
			hset=HSet(i,data[i],None)
			self.clusters.append(hset)
		self.num=len(self.clusters)
		self.max_index=self.num

#		p=[]
#		for i in range(10):
#			p.append(threading.Thread(target=self.multi, args=(2000*i,)))
#			p[i].start()
#
#		for i in range(10):
#			p[i].join()
		for i in range(0,self.num):
			self.name.append(i)
			for j in range(i+1,self.num):
				if i<j:
					self.dist(self.clusters[i],self.clusters[j])

	def multi_classify(self,sindex,queue):
		findex=sindex+2000
		tmplen=len(self.clusters)
		change=0
		minval=sys.maxint
		for i in range(sindex,findex):
			if i>=tmplen:
				break
			for j in range(i+1,tmplen):
				if j>=tmplen:
					continue	
				tmp=self.dist(self.clusters[i],self.clusters[j])
				if tmp<minval:
					change=1
					minval=tmp
					tmpi=i
					tmpj=j
		if change==1:
			queue.append((minval,tmpi,tmpj));

	def classify(self):
#		p=[]
#		q=[]
#		for i in range(10):
#			p.append(threading.Thread(target=self.multi_classify, args=(2000*i,q)))
#			p[i].start()
#
#		for i in range(10):
#			p[i].join()
#
#		minVal=sys.maxint
#		for ele in q:
#			if ele[0]<minVal:
#				minVal=ele[0]
#				tmpi=ele[1]
#				tmpj=ele[2]

		minval=sys.maxint
		for i in range(len(self.clusters)):
			for j in range(i+1,len(self.clusters)):
				tmp=self.dist(self.clusters[i],self.clusters[j])
				if tmp<minval:
					minval=tmp
					tmpi=i
					tmpj=j
		print 'merge', tmpi, tmpj
		self.merge(tmpi,tmpj)


#		minval=sys.maxint
#		for i in range(len(self.clusters)):
#			for j in range(i+1,len(self.clusters)):
#				tmp=self.dist(self.clusters[i],self.clusters[j])
#				if tmp<minval:
#					minval=tmp
#					tmpi=i
#					tmpj=j

	def merge(self,i,j):
		self.max_index+=1
		newSet=HSet(self.max_index,self.clusters[i],self.clusters[j])
		del self.clusters[i]
		del self.clusters[j-1]
		self.clusters.append(newSet)
		
	def dist(self,i,j):
		if (i.name,j.name) not in self.distance:
			minval=sys.maxint
			for x in i.data:
				for y in j.data:
					tmp=0.0
					for m in range(0,len(x)):
						tmp+=abs(x[m]-y[m])
					if tmp<minval:
						minval=tmp
			self.distance[i.name,j.name]=minval
		return self.distance[i.name,j.name] 

	def compute(self):
		iter=0
		while len(self.clusters)!=5:
			iter+=1
			print iter,'iteration.'
			self.classify()
			localtime = time.localtime(time.time())
			print "Local current time :", localtime
			if len(self.clusters) in [5,60,120,240]:
				print "Result:", len(self.clusters)
				for clu in self.clusters:
					for ele in clu.index:
						print ele,
					print ''

def main():
	filename=sys.argv[1]

	data=[]

	a=0
	with open(filename, 'r') as f:
		for row in f.readlines():
			if (a==0):
				a=1
			else:
				line=[int(x) for x in row.split()]
				data.append(line[2:])

	hcluster=HCluster(data)
	hcluster.compute()

if __name__ == "__main__":
	localtime = time.localtime(time.time())
	print "Local current time :", localtime
	main()
