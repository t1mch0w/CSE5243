from reuter import *
from cleaner import *
from parser import *
import sys

class Vector:
	data=''
	reulist=[]
	textlist=[]
	wholetext=''

	def __init__(self,data):
		self.data=data.lower()

	def compute(self):
		for r in self.reulist:
			self.textlist.append(r.text)
			self.wholetext+=' '+r.text

		# TF-IDF
		tf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 1)
		tfidf_matrix =  tf.fit_transform(self.textlist)
		feature_names = tf.get_feature_names()[:100]

		# Frequency
		fdist = FreqDist(self.wholetext.split())
		fremap=fdist.most_common(100)

		for r in self.reulist:
			r.tfidfatt=feature_names
			r.getTfidf()
		
			for tmp in fremap:
				r.freatt.append(tmp[0])
			r.getFre()

	def writeout(self):
		for r in self.reulist:
			print r.tfidfatt
			print r.tfidfval
			print r.freatt
			print r.freval

def main():
	with open(sys.argv[1], 'r') as f:
		data=f.read()

	vector=Vector(data)	

	cleaner=Cleaner()
	cleaner.clean(vector)

	parser=Parser()
	parser.parse(vector)

	vector.compute()
	vector.writeout()

if __name__ == "__main__":
	main()
