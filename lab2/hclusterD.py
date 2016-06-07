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

		for i in range(0,self.num):
			self.name.append(i)
			for j in range(i+1,self.num):
				if i<j:
					self.dist(self.clusters[i],self.clusters[j])

	def classify(self):

		minval=sys.maxint
		tmp=self.q.get()
		while (tmp[1] not in self.name) or (tmp[2] not in self.name):
			tmp=self.q.get()

		tmpi=tmp[1]
		tmpj=tmp[2]

		print 'merge', tmpi, tmpj
		self.merge(tmpi,tmpj)

	def merge(self,i,j):
		newSet=HSet(self.max_index,self.clusters[i],self.clusters[j])
		self.name.remove(i)
		self.name.remove(j)
		for clu in self.clusters:

			if clu.name not in self.name:
				continue

			if clu.name < i:
				tmpa=self.distance[clu.name,i]
			else:
				tmpa=self.distance[i,clu.name]

			if clu.name < j:
				tmpb=self.distance[clu.name,j]
			else:
				tmpb=self.distance[j,clu.name]

			tmp = max(tmpa,tmpb)
			self.distance[clu.name,self.max_index]=tmp
			self.q.put([tmp,clu.name,self.max_index])

		self.name.append(self.max_index)
		self.clusters.append(newSet)
		self.max_index+=1
		
	def dist(self,i,j):
		minval=-1
		for x in i.data:
			for y in j.data:
				tmp=0.0
				vec=0.0
				clu=0.0
				for m in range(0,len(x)):
					vec+=x[m]*x[m]
					clu+=y[m]*y[m]
					tmp+=x[m]*y[m]
				if vec!=0 and clu!=0:
					tmp=1-tmp/(math.sqrt(vec)*math.sqrt(clu))

				if tmp>minval:
					minval=tmp

		self.q.put([minval,i.name,j.name])
		self.distance[i.name,j.name]=minval

	def compute(self):
		iter=0
		while len(self.name)!=5:
			iter+=1
			print iter,'iteration.'
			self.classify()
			localtime = time.localtime(time.time())
			print "Local current time :", localtime
			if len(self.name) in [5,60,120,240,500]:
				f=open('hcluster_complete_consine_'+str(len(self.name)),'w')
				print "Result:", len(self.name)
				for clu in self.name:
					for ele in self.clusters[clu].index:
						f.write(str(ele)+' ')
						print ele,
					print ''
					f.write('\n')
def main():
	filename=sys.argv[1]

	data=[]

	a=0
	with open(filename, 'r') as f:
		for row in f.readlines():
			if (a==0):
				a=1
			else:
				#line=[int(x) for x in row.split()]
				line=[float(x) for x in row.split()]
				data.append(line[2:])

	hcluster=HCluster(data)
	hcluster.compute()

if __name__ == "__main__":
	localtime = time.localtime(time.time())
	print "Local current time :", localtime
	main()
