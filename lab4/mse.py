import sys

fileA=open(sys.argv[1],'r')
fileB=open(sys.argv[2],'r')

mse=[0.0,0.0,0.0,0.0,0.0]

total=0
while(1):
	try:	
		linesA=fileA.readline()
		linesB=fileB.readline()
		a=float(linesA.strip())
		b=map(float, linesB.split())
	except:
		break	
	for m in range(0,5):
		mse[m]+=abs(b[m]-a)*abs(b[m]-a)
	total+=1

for m in range(0,5):
	mse[m]=float(mse[m])/total

print mse

fileA.close()
fileB.close()
