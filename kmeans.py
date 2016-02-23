import sys
import random
import math

class Kmeans:
	data=[]
	num=0
	length=0
	clusters=[]
	index=[]
	loop=1000
	ran_length=10000
	
	def __init__(self,data,num):
		self.data=data
		self.num=num
		self.length=len(data[0])
		for i in range(0,num):
			self.clusters.append([(x/float(self.ran_length)) for x in random.sample(xrange(self.ran_length), self.length)])

	def classify(self):
		self.index=[]
		for i in range(0,num):
			self.index.append([])

		for vindex, vector in enumerate(self.data):
			minval=sys.maxint
			minindex=0
			for cindex, cluster in enumerate(self.clusters):
				tmp=0.0
				for i in range(0,len(cluster)):
					tmp+=abs(vector[i]-cluster[i])

				if tmp<minval:
					minval=tmp
					minindex=cindex
			self.clusters[]
			self.index[minindex].append(vindex)

	def update(self):
		

	def compute(self):
		for i in range(0,self.loop):
			old_val = list(self.clusters)
			self.classify()
			print self.index
			self.update()


def main():
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

if __name__ == "__main__":
	main()
