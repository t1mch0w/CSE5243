class HSet:

	def __init__(self,name,hset1,hset2):
		self.name=name
		self.data=[]
		self.index=[]
		if hset2 is None:
			self.data.append(hset1)
			self.index.append(name)
		else:
			for element in hset1.data:
				self.data.append(element)
			for element in hset2.data:
				self.data.append(element)
			for element in hset1.index:
				self.index.append(element)
			for element in hset2.index:
				self.index.append(element)
