from django.shortcuts import render
from .models import Contacto
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def contacto(request):
	print "Entro a la URL"
	name = request.POST['name']
	email = request.POST['email']
	message = request.POST['message']
	print name
	print email
	print message