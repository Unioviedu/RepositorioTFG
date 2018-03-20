
from ..ply import yacc as yacc
from ..obj.nodos import *
from ..obj.nodosFinales import *
from ..obj.attributes import *

from .ylex import tokens
from .ylex import lexer

from ..maps.map import *

###################### ELEMENTOS PRINCIPALES #######################

##### Contenedores #####

def p_doc_html(p):
	'''
	doc : html_tag head body HTML_FINISH
	'''
	html = Node_HTML( [p[2],p[3]], p[1])
	Map.setNode(html)

def p_head(p):
	'''
	head : head_tag head_elements HEAD_FINISH
	'''
	p[0] = Node_HEAD(p[2], p[1])

def p_body(p):
	'''
	body : body_tag elements BODY_FINISH
	'''
	p[0] = Node_BODY(p[2], p[1])

def p_section(p):
	'''
	section : section_tag elements SECTION_FINISH
	'''
	p[0] = Node_SECTION(p[2], p[1])

def p_aside(p):
	'''
	aside : aside_tag elements ASIDE_FINISH
	'''
	p[0] = Node_ASIDE(p[2], p[1])

def p_article(p):
	'''
	article : article_tag elements ARTICLE_FINISH
	'''
	p[0] = Node_ARTICLE(p[2], p[1])

def p_nav(p):
	'''
	nav : nav_tag elements NAV_FINISH
	'''
	p[0] = Node_NAV(p[2], p[1])

def p_ul(p):
	'''
	ul : ul_tag list_elements UL_FINISH
	'''
	p[0] = Node_UL(p[2], p[1])

def p_ol(p):
	'''
	ol : ol_tag list_elements OL_FINISH
	'''
	p[0] = Node_OL(p[2], p[1])

def p_footer(p):
	'''
	footer : footer_tag elements FOOTER_FINISH
	'''
	p[0] = Node_FOOTER(p[2], p[1])

def p_header(p):
	'''
	header : header_tag elements HEADER_FINISH
	'''
	p[0] = Node_HEADER(p[2], p[1])

def p_table(p):
	'''
	table : table_tag table_elements TABLE_FINISH
	'''
	p[0] = Node_TABLE(p[2], p[1])

def p_tr(p):
	'''
	tr : tr_tag table_elements_basic TR_FINISH
	'''
	p[0] = Node_TR(p[2], p[1])
##### Contenedores fin #####

def p_title(p):
	'''
	title : title_tag TEXT TITLE_FINISH
	'''
	p[0] = Node_TITLE([], p[1], p[2])

def p_link(p):
	'''
	link : link_tag 
	'''
	p[0] = Node_LINK([], p[1])

def p_p(p):
	'''
	p : p_tag TEXT P_FINISH
	'''
	p[0] = Node_P([], p[1], p[2])

def p_h(p):
	'''
	h : h_tag TEXT H_FINISH
	'''
	tupla = p[1]
	p[0] = Node_H([], tupla[0], p[2], tupla[1])

def p_li(p):
	'''
	li : li_tag TEXT LI_FINISH
	'''
	p[0] = Node_LI([], p[1], p[2])

def p_img(p):
	'''
	img : img_tag 
	'''
	p[0] = Node_IMG([], p[1])

def p_a(p):
	'''
	a : a_tag TEXT A_FINISH
	'''
	p[0] = Node_A([], p[1], p[2])

def p_br(p):
	'''
	br : br_tag 
	'''
	p[0] = Node_BR([], p[1])

def p_th(p):
	'''
	th : th_tag TEXT TH_FINISH
	'''
	p[0] = Node_TH([], p[1], p[2])

def p_td(p):
	'''
	td : td_tag TEXT TD_FINISH
	'''
	p[0] = Node_TD([], p[1], p[2])

def p_caption(p):
	'''
	caption : caption_tag TEXT CAPTION_FINISH
	'''
	p[0] = Node_CAPTION([], p[1], p[2])
###################### ELEMENTOS PRINCIPALES FIN #######################

###################### TAGS #######################

##### Contenedores #####
def p_html_tag(p):
	'''
	html_tag : HTML attributes FINISH
	'''
	p[0] = p[2]

def p_head_tag(p):
	'''
	head_tag : HEAD attributes FINISH
	'''
	p[0] = p[2]

def p_body_tag(p):
	'''
	body_tag : BODY attributes FINISH
	'''
	p[0] = p[2]

def p_section_tag(p):
	'''
	section_tag : SECTION attributes FINISH
	'''
	p[0] = p[2]

def p_aside_tag(p):
	'''
	aside_tag : ASIDE attributes FINISH
	'''
	p[0] = p[2]

def p_article_tag(p):
	'''
	article_tag : ARTICLE attributes FINISH
	'''
	p[0] = p[2]

def p_nav_tag(p):
	'''
	nav_tag : NAV attributes FINISH
	'''
	p[0] = p[2]

def p_ul_tag(p):
	'''
	ul_tag : UL attributes FINISH
	'''
	p[0] = p[2]

def p_ol_tag(p):
	'''
	ol_tag : OL attributes FINISH
	'''
	p[0] = p[2]

def p_footer_tag(p):
	'''
	footer_tag : FOOTER attributes FINISH
	'''
	p[0] = p[2]

def p_header_tag(p):
	'''
	header_tag : HEADER attributes FINISH
	'''
	p[0] = p[2]

def p_table_tag(p):
	'''
	table_tag : TABLE attributes FINISH
	'''
	p[0] = p[2]

##### Contenedores fin #####

def p_title_tag(p):
	'''
	title_tag : TITLE_INITIAL attributes FINISH
	'''
	p[0] = p[2]

def p_link_tag(p):
	'''
	link_tag : LINK attributes FINISH
	'''
	p[0] = p[2]

def p_tag(p):
	'''
	p_tag : P attributes FINISH
	'''
	p[0] = p[2]

def p_h_tag(p):
	'''
	h_tag : H attributes FINISH
	'''
	tag = p[1]
	p[0] = p[2], tag[2]

def p_li_tag(p):
	'''
	li_tag : LI attributes FINISH
	'''
	p[0] = p[2]

def p_img_tag(p):
	'''
	img_tag : IMG attributes FINISH
	'''
	p[0] = p[2]

def p_tr_tag(p):
	'''
	tr_tag : TR attributes FINISH
	'''
	p[0] = p[2]

def p_td_tag(p):
	'''
	td_tag : TD attributes FINISH
	'''
	p[0] = p[2]

def p_th_tag(p):
	'''
	th_tag : TH attributes FINISH
	'''
	p[0] = p[2]

def p_caption_tag(p):
	'''
	caption_tag : CAPTION attributes FINISH
	'''
	p[0] = p[2]

def p_a_tag(p):
	'''
	a_tag : A attributes FINISH
	'''
	p[0] = p[2]

def p_br_tag(p):
	'''
	br_tag : BR 
	'''
	p[0] = []
###################### TAGS_FIN #######################

def p_elements(p):
	'''
	elements : empty
			| elements element
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_element(p): 
	'''
	element : section
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
			| br
	'''
	p[0] = p[1]

def p_list_elements(p):
	'''
	list_elements : empty
				| list_elements list_element
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_list_element(p):
	'''
	list_element : li
	'''
	p[0] = p[1]

def p_table_elements(p):
	'''
	table_elements : empty
				| table_elements table_element
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_table_element(p):
	'''
	table_element : caption
				| tr
	'''
	p[0] = p[1]

def p_table_elements_basic(p):
	'''
	table_elements_basic : empty
				| table_elements_basic table_element_basic
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_table_element_basic(p):
	'''
	table_element_basic : th
						| td
	'''
	p[0] = p[1]


def p_head_elements(p):
	'''
	head_elements : empty
				| head_elements head_element
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_head_element(p):
	'''
	head_element : title
				| link
	'''
	p[0] = p[1]

def p_attributes(p):
	'''
	attributes : empty  
			| attributes attribute
	'''
	if p[1] != "":
		p[0] = p[1]
		p[0].append(p[2])
	else:
		p[0] = []

def p_attribute(p):
	'''
	attribute : ID EQUAL VALUE
			 | CLASS EQUAL VALUE 
			 | HREF EQUAL VALUE
			 | SRC EQUAL VALUE
			 | TITLE EQUAL VALUE
			 | LANG EQUAL VALUE
	'''
	valor = str(p[3])
	valor = valor[ 1 : len(p[3])-1 ]
	if p[1] == "id":
		p[0] = Attribute_ID(valor)

	elif p[1] == "class":
		p[0] = Attribute_CLASS(valor)

	elif p[1] == "href":
		p[0] = Attribute_HREF(valor)

	elif p[1] == "src":
		p[0] = Attribute_SRC(valor)

	elif p[1] == "title":
		p[0] = Attribute_TITLE(valor)

	elif p[1] == "lang":
		p[0] = Attribute_LANG(valor)

def p_empty(p):
	'''
	empty : 
	'''
	p[0] = ""

def p_error(p):
	msg = "Error en la línea {0} por el código {1}, intepretado como {2}"
	pmsg = str(p).split('(')[1]
	pmsg = pmsg.split(',')
	msg = msg.format(pmsg[2], pmsg[1], pmsg[0])
	raise Exception(msg)

parser = yacc.yacc()

def startHtml():
	f = open("ClansOfWeb/analizador_lexico_sintactico/pruebas/html.txt", "r")
	parser.parseopt(f.read(), lexer)