from ..ply import lex as lex

attributes = ('ID',
	'CLASS',
	'HREF',
	'SRC',
	'TITLE',
	'LANG',
	)

tokens = attributes + (
	'FINISH',

	'HTML',
	'BODY',
	'HEAD',
	'SECTION',
	'ASIDE',
	'ARTICLE',
	'NAV',
	'UL',
	'OL',
	'FOOTER',
	'HEADER',
	'TABLE',
	
	'LINK', 
	'P',
	'H',
	'LI',
	'IMG',
	'TR',
	'TD',
	'TH',
	'CAPTION',
	'A',
	'TITLE_INITIAL',
	'BR',

	'HTML_FINISH',
	'BODY_FINISH',
	'HEAD_FINISH',
	'SECTION_FINISH',
	'ASIDE_FINISH',
	'ARTICLE_FINISH',
	'NAV_FINISH',
	'UL_FINISH',
	'OL_FINISH',
	'FOOTER_FINISH',
	'HEADER_FINISH',
	'TABLE_FINISH',
	'TITLE_FINISH',
	
	'P_FINISH',
	'H_FINISH',
	'LI_FINISH',
	'TR_FINISH',
	'TD_FINISH',
	'TH_FINISH',
	'CAPTION_FINISH',
	'A_FINISH',

	'TEXT',
	'VALUE',
	'EQUAL')

t_FINISH = r'\>'

t_HTML = r'<html'
t_BODY = r'<body'
t_HEAD = r'<head'
t_SECTION = r'<section'
t_ASIDE = r'<aside'
t_ARTICLE = r'<article'
t_NAV = r'<nav'
t_UL = r'<ul'
t_OL = r'<ol'
t_FOOTER = r'<footer'
t_HEADER = r'<header'
t_TABLE = r'<table'

t_LINK = r'<link'
t_P = r'<p'
t_LI = r'<li'
t_IMG = r'<img'
t_TR = r'<tr'
t_TD = r'<td'
t_TH = r'<th'
t_CAPTION = r'<caption'
t_A = r'<a'
t_TITLE_INITIAL = r'<title'
t_BR = r'<br>'

t_HTML_FINISH = r'</html>'
t_BODY_FINISH = r'</body>'
t_HEAD_FINISH = r'</head>'
t_SECTION_FINISH = r'</section>'
t_ASIDE_FINISH = r'</aside>'
t_ARTICLE_FINISH = r'</article>'
t_NAV_FINISH = r'</nav>'
t_UL_FINISH = r'</ul>'
t_OL_FINISH = r'</ol>'
t_FOOTER_FINISH = r'</footer>'
t_HEADER_FINISH = r'</header>'
t_TABLE_FINISH = r'</table>'

t_P_FINISH = r'</p>'
t_LI_FINISH = r'</li>'
t_TR_FINISH = r'</tr>'
t_TD_FINISH = r'</td>'
t_TH_FINISH = r'</th>'
t_CAPTION_FINISH = r'</caption>'
t_A_FINISH = r'</a>'
t_TITLE_FINISH = r'</title>'

t_VALUE = r'"[a-zA-Z_ñÑ\.\:\/ ][a-zA-Z0-9_ñÑ\.\:\/ ]*"'
t_EQUAL = r'='

t_ignore = r' '

def t_H(t):
	r'<h[1-6]'
	t.priority = int(t.value[2])
	t.type = 'H'
	return t

def t_H_FINISH(t):
	r'</h[1-6]>'
	t.priority = int(t.value[3])
	t.type = 'H_FINISH'
	return t

def t_TEXT(t):
	r'[a-zA-Z0-9_ñÑ\.\:\/ ][a-zA-Z0-9_ñÑ\.\:\/ ]*'
	if t.value.upper() in attributes:
		t.type = t.value.upper()
	else: 
		t.type = 'TEXT'
	return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
	if (t.value[0] != '\t'):
		msg = "HTML: Error en la línea {0} por el código {1}"
		msg = msg.format(t.lexer.lineno, t.value[0])
		raise Exception(msg)
	t.lexer.skip(1)

lexer = lex.lex()

#f = open("pruebas/html.txt", "r")

#lexer.input(f.read())

#while True:
#	tok = lexer.token()
#	if not tok:
#		break
#	print (tok)