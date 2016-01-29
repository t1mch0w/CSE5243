from bs4 import BeautifulSoup
from reuter import *

class Parser:
	def __init_(self):
		return		

	def parse(self,vector):
		soup=BeautifulSoup(vector.data,'html.parser')
		for r in soup.findAll('reuters'):
			t1=r['oldid']
			t2=r['newid']
			t3=r.find('body')
			if t1!=None:
				oldid=t1
			else:
				oldid=''
			if t2!=None:
				newid=t2
			else:
				newid=''
			if t3!=None:
				data=t3.string
			else:
				data=''
			tmpreu=Reuter(oldid,newid,data)
			vector.reulist.append(tmpreu)
