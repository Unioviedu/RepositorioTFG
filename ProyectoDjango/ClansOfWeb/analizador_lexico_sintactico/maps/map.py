from ..obj.nodos import *

class Map(object):
	nodeRoot = Node("","")
	hashMap = {}
	
	def __init__(self):
		self.nodeRoot = Node("","")

	@classmethod
	def setNode(self, nodeRoot):
		self.nodeRoot = nodeRoot

	@classmethod
	def getNode(self):
		return self.nodeRoot

	@classmethod
	def addSelector(self, key, selector):
		try:
			self.hashMap[key].append(selector)
		except:
			self.hashMap[key] = []
			self.hashMap[key].append(selector)

	@classmethod
	def getHashMap(self):
		return self.hashMap
