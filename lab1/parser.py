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
			
			a=[]	
			t4=r['lewissplit']
			a.append(t4)
			t5=r['cgisplit']
			a.append(t5)
			t6=r.find('date')
			if (t6 is None):
				t6='Null'
			else:
				t6=t6.string
			a.append(t6)
			t7=r.find('topics')
			if (t7 is None):
				t7='Null'
			else:
				t7=t7.string
			a.append(t7)
			t8=r.find('places')
			if (t8 is None):
				t8='Null'
			else:
				t8=t8.string
			a.append(t8)
			t9=r.find('people')
			if (t9 is None):
				t9='Null'
			else:
				t9=t9.string
			a.append(t9)
			t10=r.find('orgs') 
			if (t10 is None):
				t10='Null'
			else:
				t10=t10.string
			a.append(t10)
			t11=r.find('exchanges')
			if (t11 is None):
				t11='Null'
			else:
				t11=t11.string
			a.append(t11)
			t12=r.find('companies')
			if (t12 is None):
				t12='Null'
			else:
				t12=t12.string
			a.append(t12)
			t13=r.find('title')
			if (t13 is None):
				t13='Null'
			else:
				t13=t13.string
			a.append(t13)
			t14=r.find('dateline')
			if (t14 is None):
				t14='Null'
			else:
				t14=t14.string
			a.append(t14)

			tmpreu=Reuter(oldid,newid,data, a)
			vector.reulist.append(tmpreu)
