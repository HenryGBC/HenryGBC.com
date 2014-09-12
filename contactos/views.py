from django.shortcuts import render
from .models import Contacto
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.

@csrf_exempt
def contacto(request):
	print "Entro a la URL"
	name = request.POST['name']
	email = request.POST['email']
	message = request.POST['message']
	emailHost= 'contacto@henrygbc.com'
	send_mail("Pendiente: ", message, email,[emailHost], fail_silently=False)