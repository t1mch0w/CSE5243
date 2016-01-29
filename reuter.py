from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
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
		stop = stopwords.words('english')
		for r in tokenizer.tokenize(data):
			if r not in stop:
				if not r.isdigit():
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

