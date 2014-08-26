from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post

class PostModelAdmin(SummernoteModelAdmin):
	pass

admin.site.register(Post, PostModelAdmin)