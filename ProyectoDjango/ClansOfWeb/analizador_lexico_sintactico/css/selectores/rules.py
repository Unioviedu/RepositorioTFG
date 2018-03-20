class Rule(object):
	def __init__(self, valor):
		self.tipo = ""
		self.valor = valor

	def __str__ (self):
		return self.tipo+" "+self.valor

class RuleDirection(Rule):
	def __init__(self, valor, direction):
		Rule.__init__(self, valor)
		self.direction = direction

class RuleTwoTypes(Rule):
	def __init__(self, valor, tipo2):
		Rule.__init__(self, valor)
		self.tipo2 = tipo2

class Rule_Margin(RuleDirection):
	def __init__(self, valor, direction):
		RuleDirection.__init__(self, valor, direction)
		self.tipo = "Margin"

class Rule_Border(RuleTwoTypes):
	def __init__(self, valor, tipo2):
		RuleTwoTypes.__init__(self, valor, tipo2)
		self.tipo = "Border"

class Rule_Font(RuleTwoTypes):
	def __init__(self, valor, tipo2):
		RuleTwoTypes.__init__(self, valor, tipo2)
		self.tipo = "Font"

class Rule_Padding(RuleDirection):
	def __init__(self, valor, direction):
		RuleDirection.__init__(self, valor, direction)
		self.tipo = "Padding"

class Rule_Height(Rule):
	def __init__(self, valor):
		Rule.__init__(self, valor)
		self.tipo = "Height"

class Rule_Width(Rule):
	def __init__ (self, valor):
		Rule.__init__(self, valor)
		self.tipo = "Width"

class Rule_Background(Rule):
	def __init__ (self, valor):
		Rule.__init__(self, valor)
		self.tipo = "Background"

class Rule_Columns(Rule):
	def __init__(self, valor):
		Rule.__init__(self, valor)
		self.tipo = "Columns"

