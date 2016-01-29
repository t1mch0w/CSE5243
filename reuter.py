from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer

class Reuter:
	def __init__(self, newid, oldid, data):
		self.newid=newid
		self.oldid=oldid
		self.data=data
		self.tfidfatt=[]
		self.tfidfval=[]
		self.freatt=[]
		self.freval=[]
		self.text=''
		self.ntlk=[]

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

	def getTfidf(self):
		for tmpstr in self.tfidfatt:
			tmpstr=tmpstr.encode('ascii','ignore')
			tmpcount=0
			for word in self.ntlk:
				if (tmpstr==word):
					tmpcount=tmpcount+1
			self.tfidfval.append(tmpcount)

	def getFre(self):
		for tmpstr in self.freatt:
			tmpstr=tmpstr.encode('ascii','ignore')
			tmpcount=0
			for word in self.ntlk:
				if (tmpstr==word):
					tmpcount=tmpcount+1
			self.freval.append(tmpcount)

	def frestr(self):
		string=self.newid+'\t'+self.oldid+'\t'
		for r in self.freatt:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		for r in self.freval:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string


	def tfidfstr(self):
		string=self.newid+'\t'+self.oldid+'\t'
		for r in self.tfidfatt:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		for r in self.tfidfval:
			r=str(r)
			r=r.encode('ascii','ignore')
			string+=r+'\t'
		string+='\n'
		return string
