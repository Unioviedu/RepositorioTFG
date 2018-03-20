
from ..ply import yacc as yacc

from ..obj.nodos import *
from ..obj.nodosFinales import *
from ..obj.attributes import *

from .ylex import tokens
from .ylex import lexer

from .selectores.rules import *
from .selectores.selector import *

from ..maps.map import *

def p_doc_css(p):
	'''
	doc : styles
	'''

################### ELEMENTOS PRINCIPALES ################

def p_styles(p):
	'''
	styles : empty
			| styles style
	'''
	if p[1] != "":
		p[0] = p[1]
		for s in p[2]:
			p[0].append(s)
	else:
		p[0] = []

def p_style(p):
	'''
	style : selectors BRACKET_INITIAL rules BRACKET_FINISH
	'''
	for s in p[1]:
		s.rules = p[3]
	p[0] = p[1]

def p_rules(p):
	'''
	rules : empty
			| rules rule
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_rule(p):
	'''
	rule : MARGIN directions VALUE
		| BORDER DASH COLOR VALUE
		| BORDER DASH WIDTH VALUE
		| FONT DASH SIZE VALUE
		| FONT DASH COLOR VALUE
		| PADDING directions VALUE
		| HEIGHT VALUE
		| WIDTH VALUE
		| BACKGROUND VALUE
		| COLUMNS VALUE
	'''
	if p[1] == "margin":
		p[0] = Rule_Margin(p[3].split(':')[1], p[2])
	
	elif p[1] == "border":
		p[0] = Rule_Border(p[4].split(':')[1], p[3])
	
	elif p[1] == "font":
		p[0] = Rule_Font(p[4].split(':')[1], p[3])
	
	elif p[1] == "padding":
		p[0] = Rule_Padding(p[3].split(':')[1], p[2])
	
	elif p[1] == "height":
		p[0] = Rule_Height(p[2].split(':')[1])
	
	elif p[1] == "width":
		p[0] = Rule_Width(p[2].split(':')[1])
	
	elif p[1] == "background":
		p[0] = Rule_Background(p[2].split(':')[1])
	
	elif p[1] == "columns":
		p[0] = Rule_Columns(p[2].split(':')[1])

def p_selectors(p):
	'''
	selectors : selector
			| selectors COMA selector
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = p[1]
		p[0].append(p[3]) 


def p_selector(p):
	'''
	selector : selector_universal 
			| selector_type
			| selector_attribute 
			| selector_class
			| selector_id
	'''
	p[0] = p[1]

####################### SECUNDARIOS ##########################

def p_selector_universal(p):
	'''
	selector_universal : ASTERISK
	'''
	p[0] = SelectorUniversal([])
	Map.addSelector("Universal", p[0])

def p_selector_type(p):
	'''
	selector_type : type
			| type GREATER_THAN type
	'''
	if len(p) == 2:
		p[0] = SelectorType([],p[1],"")
	else:
		p[0] = SelectorType([],p[3],p[1])
	Map.addSelector("Type", p[0])

def p_selector_attribute(p):
	'''
	selector_attribute : CURLY_INITIAL attribute CURLY_FINISH
					| CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH
					| type CURLY_INITIAL attribute CURLY_FINISH
					| type CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH
	'''
	if len(p) == 4:
		p[0] = SelectorAttribute([], "", p[2], "")
	elif len(p) == 5:
		if p[1] == "[":
			valor = p[3][ 1 : len(p[3]) ]
			p[0] = SelectorAttribute([], "", p[2], valor)
		else:
			p[0] = SelectorAttribute([], p[1], p[3], "")
	else:
		valor = p[4][ 1 : len(p[4]) ]
		p[0] = SelectorAttribute([],  p[1], p[3], valor)
	Map.addSelector("Attribute", p[0])

def p_selector_class(p):
	'''
	selector_class : POINT_TEXT
				| type POINT_TEXT
	'''
	if len(p) == 2:
		valor = p[1][ 1 : len(p[1]) ]
		p[0] = SelectorClass([], "", valor)
	else:
		valor = p[2][ 1 : len(p[2]) ]
		p[0] = SelectorClass([], p[1], valor)
	print(valor)
	Map.addSelector("Class", p[0])

def p_selector_id(p):
	'''
	selector_id : HASHTAG_TEXT
	'''	
	valor = p[1][ 1 : len(p[1]) ]
	p[0] = SelectorId([], valor)
	Map.addSelector("Id", p[0])

def p_directions(p):
	'''
	directions : empty
			| DASH TOP
			| DASH BOTTOM
			| DASH LEFT
			| DASH RIGHT
	'''
	if p[1] != "":
		p[0] = p[2]
	p[0] = ""


############################ FINALES ######################

def p_id(p):
	'''
	id : ID
	'''
	p[0] = Attribute_ID("")

def p_class(p):
	'''
	class : CLASS
	'''
	p[0] = Attribute_CLASS("")

def p_href(p):
	'''
	href : HREF
	'''
	p[0] = Attribute_HREF("")

def p_src(p):
	'''
	src : SRC
	'''
	p[0] = Attribute_SRC("")
	

def p_lang(p):
	'''
	lang : LANG
	'''
	p[0] = Attribute_LANG("")

def p_html_tag(p):
	'''
	html : HTML 
	'''
	Node_HTML("","")

def p_head(p):
	'''
	head : HEAD
	'''
	p[0] = Node_HEAD("","")

def p_body(p):
	'''
	body : BODY
	'''
	p[0] = Node_BODY("", "")

def p_section(p):
	'''
	section : SECTION
	'''
	p[0] = Node_SECTION("", "")

def p_aside(p):
	'''
	aside : ASIDE
	'''
	p[0] = Node_ASIDE("", "")

def p_article(p):
	'''
	article : ARTICLE
	'''
	p[0] = Node_ARTICLE("", "")

def p_nav(p):
	'''
	nav : NAV
	'''
	p[0] = Node_NAV("", "")

def p_ul(p):
	'''
	ul : UL
	'''
	p[0] = Node_UL("", "")

def p_ol(p):
	'''
	ol : OL
	'''
	p[0] = Node_OL("", "")

def p_footer(p):
	'''
	footer : FOOTER
	'''
	p[0] = Node_FOOTER("", "")

def p_header(p):
	'''
	header : HEADER
	'''
	p[0] = Node_HEADER("", "")

def p_table(p):
	'''
	table : TABLE
	'''
	p[0] = Node_TABLE("", "")

def p_tr(p):
	'''
	tr : TR
	'''
	p[0] = Node_TR("", "")

def p_link(p):
	'''
	link : LINK
	'''
	p[0] = Node_Link("", "")

def p_p(p):
	'''
	p : P
	'''
	p[0] = Node_P("", "", "")

def p_h(p):
	'''
	h : H
	'''
	h = p[1]
	p[0] = Node_H("", "", "", h[1])

def p_li(p):
	'''
	li : LI
	'''
	p[0] = Node_LI("", "", "")

def p_img(p):
	'''
	img : IMG 
	'''
	p[0] = Node_IMG("", "")

def p_a(p):
	'''
	a : A
	'''
	p[0] = Node_A("", "", "")

def p_th(p):
	'''
	th : TH
	'''
	p[0] = Node_TH("", "", "")

def p_td(p):
	'''
	td : TD
	'''
	p[0] = Node_TD("", "", "")

def p_caption(p):
	'''
	caption : CAPTION
	'''
	p[0] = Node_CAPTION("", "", "")

def p_empty(p):
	'''
	empty : 
	'''
	p[0] = ""

def p_type(p): 
	'''
	type : 	  html	
			| body
			| head
			| section
			| aside
			| article
			| nav
			| ul
			| ol
			| footer
			| header
			| table
			| p
			| h
			| img
			| a
			| TITLE
			| link
			| th
			| td
			| tr
			| caption
			| li
	'''
	if (p[1] == "title"):
		p[0] = Node_TITLE("", "", "")
	p[0] = p[1]

def p_attribute(p):
	'''
	attribute : id
			 | class 
			 | href
			 | src
			 | TITLE
			 | lang
	'''
	if (p[1] == "title"):
		p[0] = Attribute_TITLE("")
	p[0] = p[1]

def p_error(p):
	msg = "Error en la línea {0} por el código {1}, intepretado como {2}"
	pmsg = str(p).split('(')[1]
	pmsg = pmsg.split(',')
	msg = msg.format(pmsg[2], pmsg[1], pmsg[0])
	raise Exception(msg)

parser = yacc.yacc()

def startCss():
	f = open("ClansOfWeb/analizador_lexico_sintactico/pruebas/css.txt", "r")
	parser.parseopt(f.read(), lexer)