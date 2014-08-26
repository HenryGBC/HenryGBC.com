from django.db import models

# Create your models here.

class Usuario (models.Model):
	avatar = models.ImageField(upload_to='media/')
	nombre = models.CharField(max_length=100)
	username = models.CharField(max_length=50)
	bio = models.CharField(max_length=240)

	def __unicode__ (self):
		return self.username