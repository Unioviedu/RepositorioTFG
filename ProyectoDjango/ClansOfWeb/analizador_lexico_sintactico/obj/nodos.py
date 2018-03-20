import collections

class Node(object):
	def __init__ (self, childrens, attributes):
		self.tipo = ""
		self.childrens = childrens
		self.attributes = attributes
		self.profundidad = 0
		self.css = []
		
	def __str__ (self):
		string = self.tipo
		for a in self.attributes:
				string = string+" "+str(a)
		return string

class Node_HTML(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "HTML"

class Node_HEAD(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "HEAD"

class Node_BODY(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "BODY"

class Node_SECTION(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "SECTION"

class Node_ASIDE(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "ASIDE"

class Node_ARTICLE(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "ARTICLE"

class Node_NAV(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "NAV"

class Node_UL(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "UL"

class Node_OL(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "OL"

class Node_FOOTER(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "FOOTER"

class Node_HEADER(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "HEADER"

class Node_TABLE(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "TABLE"

class Node_TR(Node):
	def __init__(self, childrens, attributes):
		Node.__init__(self, childrens, attributes)
		self.tipo = "TR"

def setNodeRoot(Node):
	nodeRoot = Node
	nodeRoot.profundidad = 0
	printNode(nodeRoot)
	recorridoRecursivo(nodeRoot.childrens, nodeRoot)

def recorridoRecursivo(listNodes, padre):
	for node in listNodes:
		node.profundidad = padre.profundidad + 1
		printNode(node)
		recorridoRecursivo(node.childrens, node)
 
def printNode(node):
	for p in range(0, node.profundidad):
		print ("\t", end="")
	print (node)