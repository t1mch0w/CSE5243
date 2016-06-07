import sys
import random
import math
import time
import threading

class Kmeans:
	data=[]
	num=0
	length=0
	clusters=[]
	index=[]
	loop=1000
	ran_length=1000
	lock = threading.Lock()
	oldindex=[]
	
	def __init__(self,data,num):
		self.data=data
		self.num=num
		self.length=len(data[0])
		randomlist=random.sample(range(1, len(data)), num)
		for i in randomlist:
			tmp=list(data[i])
			self.clusters.append(tmp)

	def multi(self,sindex,queue):
		findex=sindex+500
		tmplen=len(self.data)
		clulen=len(self.clusters[0])
		for i in range(sindex,findex):
			if i>=tmplen:
				break
			vector=self.data[i]
			minval=sys.maxint
			minindex=0
			for j in range(len(self.clusters)):
				tmp=0.0
				for k in range(clulen):
					tmp+=(vector[k]-self.clusters[j][k])*(vector[k]-self.clusters[j][k])
				tmp=math.sqrt(tmp)
				if tmp<minval:
					minval=tmp
					minindex=j
			self.index[minindex].append(i)
			self.lock.acquire()
			for m in range(clulen):
				queue[minindex][m]+=vector[m]
			self.lock.release()

	def classify(self):
		self.index=[]
		newCluster=[]
		newElement=[]
		for i in range(0,self.length):
			newElement.append(0.0)

		for i in range(0,self.num):
			self.index.append([])
			newCluster.append(list(newElement))

#		p=[]
#		for i in range(20):
#			p.append(threading.Thread(target=self.multi, args=(500*i,newCluster)))
#			p[i].start()
#
#		for i in range(20):
#			p[i].join()


		for vindex, vector in enumerate(self.data):
			minval=sys.maxint
			minindex=0
			for cindex, cluster in enumerate(self.clusters):
				tmp=0.0
				vec=0.0
				clu=0.0
				for i in range(0,len(cluster)):
					tmp+=vector[i]*cluster[i]
					vec+=vector[i]*vector[i]
					clu+=cluster[i]*cluster[i]

				if tmp!=0:
					tmp=1-tmp/(math.sqrt(vec)*math.sqrt(clu))

				if tmp<minval:
					minval=tmp
					minindex=cindex
			for i in range(0,self.length):
				newCluster[minindex][i]+=vector[i]

			self.index[minindex].append(vindex)
		self.clusters=newCluster

	def update(self):
		newCluster=[]
		for i in range(0,self.num):
			if len(self.index[i])==0:
				newCluster.append([float(x)/float(len(self.data)) for x in random.sample(range(1, len(self.data)), len(self.data[0]))])
				#print newCluster[-1]
			else:
				tmp=[x/len(self.index[i]) for x in self.clusters[i]]
				newCluster.append(tmp)
		self.clusters=newCluster

	def compute(self):
		for i in range(0,self.loop):
			self.oldindex=[]
			#print self.clusters
			for x in self.index:
				self.oldindex.append(x)
			print i,' test'
			#print self.index
			#print self.clusters
			self.classify()
			self.update()
			for i in range(len(self.index)):
				print i, len(self.index[i])
			a=1
			for i in range(len(self.index)):
				if len(self.oldindex)==0:
					a=0
					break
				if len(self.oldindex[i])!=len(self.index[i]):
					a=0
					break

			if a==1:
				break

		print 'Result:'
		for ele in self.index:
			for val in ele:
				print val,
			print ''


def main():

	localtime = time.localtime(time.time())
	print "Start time :", localtime

	filename=sys.argv[1]
	numOfCluster=int(sys.argv[2])

	data=[]

	a=0
	with open(filename, 'r') as f:
		for row in f.readlines():
			if (a==0):
				a=1
			else:
				line=[float(x) for x in row.split()]
				data.append(line[2:])

	kmeans=Kmeans(data, numOfCluster)
	kmeans.compute()

	localtime = time.localtime(time.time())
	print "End time :", localtime

if __name__ == "__main__":
	main()
