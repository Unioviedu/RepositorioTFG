import json

from .map import *

class NodeEncoder(json.JSONEncoder):
	def default(self, obj):
		return obj.__dict__

def generate():
	nodeRoot = Map.getNode()
	nodeRoot.padre = ""
	comprobarCss(nodeRoot)
	recorridoRecursivo(nodeRoot.childrens, nodeRoot)
	
	serialize = json.dumps(nodeRoot, cls=NodeEncoder, indent=4)
	return serialize

def recorridoRecursivo(listNodes, padre):
	for node in listNodes:
		node.padre = padre.tipo
		comprobarCss(node)
		recorridoRecursivo(node.childrens, node)

def comprobarCss(node):
	hashSelectors = Map.getHashMap()

	#comprobarCssUniversal(node, hashSelectors["Universal"])
	#comprobarCssType(node, hashSelectors["Type"])
	#comprobarCssClass(node, hashSelectors["Class"])
	#comprobarCssId(node, hashSelectors["Id"])
	#comprobarCssAttribute(node, hashSelectors["Attribute"])

def comprobarCssUniversal(node, list):
	for selector in list:
		addRules(selector, node)

def comprobarCssType(node, list):
	for selector in list:
		if selector.father == "":
			if type(selector.tipo) == type(node):
				if node.tipo == "H":
					if selector.tipo.index == node.index:
						addRules(selector, node)
				else:
					addRules(selector, node)
		else:
			if type(selector.father.tipo) == type(node.padre):
				if selector.father.tipo == "H":
					if selector.tipo.index == node.index:
						comprobarCssTypeAux(selector, node)
				else:
					comprobarCssTypeAux(selector, node)

def comprobarCssClass(node, list):
	for selector in list:
		if selector.tipo == "":
			comprobarCssClassAux(selector, node)
		else:
			if type(selector.tipo) == type(node):
				if selector.tipo.tipo == "H":
					if selector.tipo.index == node.index:
						comprobarCssClassAux(selector, node)
				else:
					comprobarCssClassAux(selector, node)

def comprobarCssId(node, list):
	for selector in list:
		for atr in node.attributes:
			if atr.tipo == "ID":
				if selector.valor == atr.value:
					addRules(selector, node)

def comprobarCssAttribute(node, list):
	for selector in list:
		if selector.tipo == "":
			comprobarCssAttributeAux(selector, node)
		else:
			if type(selector.tipo) == type(node):
				if selector.tipo.tipo == "H":
					if selector.tipo.index == node.index:
						comprobarCssAttributeAux(selector, node)
				else:
					comprobarCssAttributeAux(selector, node)

def comprobarCssAttributeAux(selector, node):
	for atr in node.attributes:
		if selector.valor == "":
			if atr.tipo == selector.attribute.tipo:
				addRules(selector, node)
		else:
			if atr.tipo == selector.attribute.tipo:
				if atr.value == selector.valor:
					addRules(selector, node)

def comprobarCssTypeAux(selector, node):
	if type(selector.tipo) == type(node):
		if node.tipo == "H":
			if selector.tipo.index == node.index:
				addRules(selector, node)
		else:
			addRules(selector, node)

def comprobarCssClassAux(selector, node):
	for atr in node.attributes:
		if atr.tipo == "CLASS":
			if atr.value == selector.valor:
				addRules(selector, node)

def addRules(selector, node):
	for r in selector.rules:
			node.css.append(r)
