from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *

class Reuter:
	def __init__(self, oldid, newid, data, general):
		self.newid=newid
		self.oldid=oldid
		self.data=data
		self.tfidfatt=[]
		self.tfidfval=[]
		self.freatt=[]
		self.freval=[]
		self.text=''
		self.ntlk=[]
		self.idfvalue=[]
		self.general=general

		tokenizer = RegexpTokenizer(r'\w+')
		#stemmer = SnowballStemmer("english")
		stemmer = PorterStemmer()

		stop = stopwords.words('english')
		for r in tokenizer.tokenize(data):
			a=0
			if r not in stop:
				if not any(i.isdigit() for i in r):
					r = stemmer.stem(r)
					if r not in self.ntlk:
						self.ntlk.append(r)
						self.text=self.text+' '+r

	def getTfidf(self, idflist):
		for index,word in enumerate(self.tfidfatt,start=0):
			#word=word.encode('ascii','ignore')
			below = len(self.ntlk)
			if below==0:
				self.tfidfval.append(0)
			else:
				above = self.ntlk.count(word)
				tf = float(above)/below
				idf = idflist[index]
				self.tfidfval.append(float(tf*idf))

	def getFre(self):
		for tmpstr in self.freatt:
			tmpstr=tmpstr.encode('ascii','ignore')
			tmpcount=self.ntlk.count(tmpstr)
			self.freval.append(tmpcount)

	def frestr(self):
		string=self.newid+'\t'+self.oldid+'\t'
		for r in self.freval:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string

	def freattstr(self):
		string='newid\toldid\t'
		for r in self.freatt:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string

	def tfidfstr(self):
		string=self.newid+'\t'+self.oldid+'\t'
		for r in self.tfidfval:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string
	
	def tfidfattstr(self):
		string='newid\toldid\t'
		for r in self.tfidfatt:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string

	def genattstr(self):
		string='newid\toldid\tlewissplit\tcgisplit\tdate\ttopics\tplaces\t'\
					 'people\torgs\texchanges\tcompanies\ttitle\tdateline\tnumOfWords\n'
		return string

	def genstr(self):
		string=self.newid+'\t'+self.oldid+'\t'
		for r in self.general:
			r=str(r)
			r=r.encode('ascii','ignore')
			r=r.replace('\n','').replace('\t','').strip()
			string+='"'+r+'"'+'\t'
		string+=str(len(self.ntlk))
		string+='\n'
		return string
