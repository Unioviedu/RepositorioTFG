from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse

from .analizador_lexico_sintactico.main import start


def index(request):
	return render_to_response('index.html')

def create_post(request):
	print(request.POST.get('msg'))
