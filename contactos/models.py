from django.db import models

# Create your models here.

class Contacto(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField()

	def __unicode__(self):
		return "%s - %s" % (self.name, self.email)