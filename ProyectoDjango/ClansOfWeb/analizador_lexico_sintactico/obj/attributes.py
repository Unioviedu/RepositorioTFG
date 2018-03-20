class Attribute(object):
	def __init__(self, value):
		self.value = value
		self.tipo = ""
	def __str__(self):
		return self.tipo+" "+self.value

class Attribute_ID(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "ID"

class Attribute_CLASS(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "CLASS"

class Attribute_HREF(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "HREF"

class Attribute_SRC(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "SRC"

class Attribute_TITLE(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "TITLE"

class Attribute_LANG(Attribute):
	def __init__(self, value):
		Attribute.__init__(self, value)
		self.tipo = "LANG"