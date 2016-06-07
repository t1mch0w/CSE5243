from reuter import *
from cleaner import *
from parser import *

import sys
import glob   
import math

class Vector:
	data=''
	reulist=[]
	textlist=[]
	wholetext=[]

	def __init__(self,data):
		self.data=data.lower()

	def compute(self, n, tfidffile, frefile, genfile):

		tfile = open(tfidffile, 'w')
		ffile = open(frefile, 'w')
		gfile = open(genfile, 'w')

		# Combine
		for r in self.reulist:
			self.wholetext += r.ntlk
#			for tmpstr in r.ntlk:
#				self.wholetext+=' '+ tmpstr

		# Frequency and Attribute
		fdist = FreqDist(self.wholetext)
		fremap=fdist.most_common(n)

		# Update the attributes
		for r in self.reulist:
			for tmp in fremap:
				r.freatt.append(tmp[0])
				r.tfidfatt.append(tmp[0])

		# Compute IDF
		idf=[]
		for tmp in fremap:
			idfbelow=0
			idfabove=len(self.reulist)
			for r in self.reulist:
				if r.ntlk.count(tmp[0])!=0:
					idfbelow+=1
			idf.append(math.log(idfabove/idfbelow))

		a=0
		for r in self.reulist:
			r.getTfidf(idf)
			r.getFre()

			if a==0:
				tfile.write(r.tfidfattstr())
				ffile.write(r.freattstr())
				gfile.write(r.genattstr())
				a=1

			tfile.write(r.tfidfstr())
			ffile.write(r.frestr())
			gfile.write(r.genstr())

def main():
	if len(sys.argv)!=4:
		print 'Please use following format to run the program:\n'+'python ./vector $INPUT_FILE_DIR $OUTPUT_FILE $#ATTRIBUTES'
		return
	
	print 'Input directory:', sys.argv[1]
	print 'Output file:', sys.argv[2]+'.vc1,', sys.argv[2]+'.vc2,', sys.argv[2]+'.vc3.'
	print 'The num of Attributes:', sys.argv[3]
	print 'Processing...'

	data=''
	filenames=glob.glob(sys.argv[1]+'/*.*')
	for filename in filenames:
		with open(filename, 'r') as f:
			data=data+'\n'+f.read()
	
	tfidffile=sys.argv[2]+'.vc1'
	frefile=sys.argv[2]+'.vc2'
	genfile=sys.argv[2]+'.vc3'

	vector=Vector(data)	

	cleaner=Cleaner()
	cleaner.clean(vector)

	parser=Parser()
	parser.parse(vector)

	vector.compute(int(sys.argv[3]), tfidffile, frefile, genfile)

	print 'Finished.'

if __name__ == "__main__":
	main()