from django import forms 
from django.forms import ModelForm
from .models import Post



class savePostForm(ModelForm):

	class Meta:
		model = Post