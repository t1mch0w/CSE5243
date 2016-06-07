class Cleaner:
	def __init__(self):
		return	
			
	def clean(self,v):
		v.data=v.data.replace('\"','')
		v.data=v.data.replace('\'','')
		v.data=v.data.replace('&','')
		return v.data
