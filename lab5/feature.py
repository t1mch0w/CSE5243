import sys

rules={}

f=open(sys.argv[2],'r')
lines=f.readlines()
f.close()
for line in lines:
	if '<-  ' not in line:
		tmpstr=line.replace('<-',' ').replace('(',' ').replace(')',' ').replace(',',' ').split()
		res=tmpstr[0]
		svalue=float(tmpstr[-2])
		cvalue=float(tmpstr[-1])
		keywords=tmpstr[1:-2]
		rules[(svalue,cvalue)]=(res,keywords)
	
rules=sorted(rules.items())

f=open(sys.argv[1],'r')
lines=f.readlines()
f.close

test=[]
for line in lines:
	line=line.split()
	test.append((line[-1],line[0:-1]))

right=0
whole=len(test)

for e in test:
	tresl='earn'
	for rule in rules:
		if set(rule[1][1])<=set(e[1]):
			tresl=rule[1][0]
			break
	if tresl==e[0]:
		right+=1

print right,whole,float(right)/whole*100
