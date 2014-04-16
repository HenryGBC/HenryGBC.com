from django.db import models

# Create your models here.
class Email(models.Model):
	email = models.EmailField(max_length=80)
	
	def __unicode__(self):
		return self.email