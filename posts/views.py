from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.context import RequestContext 
from .forms import savePostForm
from .models import Post
from skills.models import Categoria, Skill
# Create your views here.
def home(request):
	posts = Post.objects.all()
	categorias = Categoria.objects.all()
	skills = Skill.objects.all()
	template = "index.html"
	return render(request,template,locals())

def showpost(request, slugUrl):
	post = get_object_or_404(Post, slugUrl = slugUrl)
	posts = Post.objects.order_by('-pk')[:4]
	template = "post.html"
	return render(request,template,locals())

