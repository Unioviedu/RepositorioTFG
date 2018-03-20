class Selector(object):
	def __init__(self, rules):
		self.rules = rules

	def __str__(self):
		string = ""
		for r in self.rules:
			string = string + str(r)
		return string

class SelectorUniversal(Selector):
	def __init__(self, rules):
		Selector.__init__(self, rules)

class SelectorType(Selector):
	def __init__(self, rules, tipo, father):
		Selector.__init__(self, rules)
		self.tipo = tipo
		self.father = father

class SelectorAttribute(Selector):
	def __init__(self, rules, tipo, attribute, valor):
		Selector.__init__(self, rules)
		self.tipo = tipo
		self.attribute = attribute
		self.valor = valor

class SelectorClass(Selector):
	def __init__(self, rules, tipo, valor):
		Selector.__init__(self, rules)
		self.tipo = tipo
		self.valor = valor

class SelectorId(Selector):
	def __init__(self, rules, valor):
		Selector.__init__(self, rules, valor)
		self.valor = valor
