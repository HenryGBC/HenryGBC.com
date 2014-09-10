from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Skill(models.Model):
	categoria = models.ForeignKey(Categoria)
	skill = models.CharField(max_length=100)
	porcentaje = models.IntegerField()

	def __unicode__(self):
		return self.skill