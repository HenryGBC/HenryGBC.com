from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Email

# Create your views here.

@csrf_exempt
def emailsave(request):
	email_index = request.POST['email']
	email = Email(email=email_index)
	email.save()