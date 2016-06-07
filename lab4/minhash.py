import sys
from random import randint
# minhash

f=open(sys.argv[1],'r')
k=256

lines=f.readlines()
data=[]
length=len(lines[0].split())
hf={}
minres={}

def minhash_init():
	for i in range(0,k):
		hf[i]=[]
		hf[i].append(randint(1,1000))
		hf[i].append(randint(1,1000))

def minhash(pos,x):
	resset=[]

	for m in range(0,k):
		minx=6000
		for i in range(0,len(x)):
			if x[i]!=0:
				tmp=((hf[m][0]*i+hf[m][1]))%length
				if tmp<minx:
					minx=tmp
		resset.append(float(minx))
	minres[pos]=resset

for line in lines:
	line = map(int, line.split())
	data.append(line)

minhash_init()

for i in range(0,len(data)):
	minhash(i,data[i])

for i in range(0,len(data)-1):
	for j in range(i+1,len(data)):
		res=0.0
		for k in range(0,256):
			if k in [16,32,64,128]:
				print res/float(k),
			if minres[i][k]==minres[j][k]:
				res+=1.0
		print res/float(256)
