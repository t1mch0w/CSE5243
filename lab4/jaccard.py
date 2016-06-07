import sys
# jaccard similarity 

def andop(x,y):
	res=0
	for i in range(0,len(x)):
		res+=x[i] & y[i]
	return float(res)

def orop(x,y):
	res=0
	for i in range(0,len(x)):
		res+=x[i] | y[i]
	return float(res)

def jaccard(x,y):
	b=orop(x,y)
	if b==0: return 0.0
	a=andop(x,y)
	return a/b	

data=[]
f=open(sys.argv[1],'r')
lines=f.readlines()
for line in lines:
	line = map(int, line.split())
	data.append(line)

for i in range(0,len(data)-1):
	for j in range(i+1,len(data)):
		print jaccard(data[i],data[j])
