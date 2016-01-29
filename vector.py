from reuter import *
from cleaner import *
from parser import *
from optparse import OptionParser

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

	def writeout(self, tfidfile, frefile):
		tf = open(tfidfile, 'w')
		ff = open(frefile, 'w')
		for r in self.reulist:
			tf.write(r.tfidfstr())
		for r in self.reulist:
			ff.write(r.frestr())

def main():
	if len(sys.argv)!=3:
		print 'Please use following format to run the program:\n'+'python ./vector $INPUT_FILE $OUTPUT_FILE'
		return
	with open(sys.argv[1], 'r') as f:
		data=f.read()
	
	tfidffile=sys.argv[2]+'.vc1'
	frefile=sys.argv[2]+'.vc2'

	vector=Vector(data)	

	cleaner=Cleaner()
	cleaner.clean(vector)

	parser=Parser()
	parser.parse(vector)

	vector.compute()
	vector.writeout(tfidffile, frefile)

if __name__ == "__main__":
	main()
