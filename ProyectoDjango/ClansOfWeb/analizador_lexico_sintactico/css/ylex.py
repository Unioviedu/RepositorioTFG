from ..ply import lex as lex


symbol = (
	'ASTERISK',
	'COMA',
	'BRACKET_INITIAL',
	'BRACKET_FINISH',
	'CURLY_INITIAL',
	'CURLY_FINISH',
	'DASH',
	'GREATER_THAN'
	)

attributes = (
	'ID',
	'CLASS',
	'HREF',
	'SRC',
	'TITLE',
	'LANG',
	)

elements = (
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
	'A'
	)

tokens = symbol + elements + attributes + (
	'MARGIN',
	'BORDER',
	'WIDTH',
	'PADDING',
	'TOP',
	'BOTTOM',
	'LEFT',
	'RIGHT',
	'HEIGHT',
	'BACKGROUND',
	'FONT',
	'SIZE',
	'COLOR',
	'COLUMNS',
	'VALUE',
	'EQUAL_TEXT',
	'POINT_TEXT',
	'HASHTAG_TEXT'
	)

t_ASTERISK = r'\*'
t_COMA = r','
t_BRACKET_INITIAL = r'{'
t_BRACKET_FINISH = r'}'
t_CURLY_INITIAL = r'\['
t_CURLY_FINISH = r']'
t_DASH = r'-'
t_GREATER_THAN = r'>'

t_ID = r'id'
t_CLASS = r'class'
t_HREF = r'href'
t_SRC = r'src'
t_TITLE = r'title'
t_LANG = r'lang'

t_MARGIN = r'margin'
t_BORDER = r'border'
t_PADDING = r'padding'
t_TOP = r'top'
t_BOTTOM = r'bottom'
t_LEFT = r'left'
t_RIGHT = r'right'
t_WIDTH = r'width'
t_HEIGHT = r'height'
t_BACKGROUND = r'background'
t_FONT = r'font'
t_SIZE = r'size'
t_COLOR = r'color'
t_COLUMNS=r'columns'

t_HTML = r'html'
t_BODY = r'body'
t_HEAD = r'head'
t_SECTION = r'section'
t_ASIDE = r'aside'
t_ARTICLE = r'article'
t_NAV = r'nav'
t_UL = r'ul'
t_OL = r'ol'
t_FOOTER = r'footer'
t_HEADER = r'header'
t_TABLE = r'table'

t_LINK = r'link'
t_P = r'p'
t_LI = r'li'
t_IMG = r'img'
t_TR = r'tr'
t_TD = r'td'
t_TH = r'th'
t_CAPTION = r'caption'
t_A = r'a'

t_EQUAL_TEXT = r'\=[ ][a-zA-Z0-9_ñÑ][a-zA-Z0-9_ñÑ]*'
t_POINT_TEXT = r'\.[a-zA-Z0-9_ñÑ][a-zA-Z0-9_ñÑ]*'
t_HASHTAG_TEXT = r'\#[a-zA-Z0-9_ñÑ][a-zA-Z0-9_ñÑ]*' 
t_VALUE = r':[ ][a-zA-Z0-9_ñÑ]*'

t_ignore = r' '

def t_H(t):
	r'h[1-6]'
	t.priority = int(t.value[1])
	t.type = 'H'
	return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
	if (t.value[0] != '\t'):
		msg = "CSS: Error en la línea {0} por el código {1}"
		msg = msg.format(t.lexer.lineno, t.value[0])
		raise Exception(msg)
	t.lexer.skip(1)

lexer = lex.lex()

#f = open("pruebas/css.txt", "r")

#lexer.input(f.read())

#while True:
#	tok = lexer.token()
#	if not tok:
#		break
#	print (tok)