from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='media/')
	paragraph = models.TextField()
	resume = models.CharField(max_length=255)
	slugtitle = models.SlugField(max_length=255, blank=True)


	def save(self, *args, **kwargs):
		self.slugtitle = self.title.lower().replace(' ','-')
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
