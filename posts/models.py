from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	resume = models.CharField(max_length=255)
	imageIndex = models.ImageField(upload_to='media/')
	imagePost = models.ImageField(upload_to='media/')
	url = models.CharField(max_length=100)
	paragraph = models.TextField()
	usuario = models.ForeignKey(Usuario)
	fecha = models.DateField()
	slugUrl = models.SlugField(max_length=255, blank=True)


	def save(self, *args, **kwargs):
		self.slugUrl = self.title.lower().replace(' ','-')
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title