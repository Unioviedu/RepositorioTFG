from django.shortcuts import render

from django.http import HttpResponse

from .analizador_lexico_sintactico.main import start


def index(request):
	return HttpResponse(start())
