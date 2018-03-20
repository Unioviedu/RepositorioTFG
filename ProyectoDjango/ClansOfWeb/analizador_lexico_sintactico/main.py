from .css.parser import startCss
from .html.parser import startHtml
from .maps.generatorMap import generate

from .obj import nodos as nodos
from .maps.map import *


def start():
	startCss()
	startHtml()

	json = generate()
	return json
