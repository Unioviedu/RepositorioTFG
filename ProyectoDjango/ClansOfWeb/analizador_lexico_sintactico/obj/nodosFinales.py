from ..obj.nodos import *

class Node_Value(Node):
	def __init__(self, childrens, attributes, value):
		Node.__init__(self, childrens, attributes)
		self.value = value
	def __str__(self):
		string = self.tipo
		for a in self.attributes:
				string = string+" "+str(a)
		string = string+" VALUE "+self.value
		return string

class Node_TITLE(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "TITLE"

class Node_LINK(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "LINK"

class Node_P(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "P"

class Node_H(Node_Value):
	def __init__(self, childrens, attributes, value, index):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "H"
		self.index = index
	def __str__(self):
		string = self.tipo+" "+self.index
		for a in self.attributes:
				string = string+" "+str(a)
		string = string+" VALUE "+self.value
		return string	

class Node_LI(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "LI"

class Node_IMG(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "IMG"

class Node_TD(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "TD"

class Node_TH(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "TH"

class Node_CAPTION(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "CAPTION"

class Node_A(Node_Value):
	def __init__(self, childrens, attributes, value):
		Node_Value.__init__(self, childrens, attributes, value)
		self.tipo = "A"

class Node_BR(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "BR"




