from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.context import RequestContext 
from .forms import savePostForm
from .models import Post
# Create your views here.
def home(request):
	posts = Post.objects.all()
	template = "index.html"
	return render(request,template,locals())

def showpost(request, slugTitle):
	post = get_object_or_404(Post, slugtitle = slugTitle)
	posts = Post.objects.all()
	template = "post.html"
	return render(request,template,locals())

def savePost(request):

	if request.POST:
		form = savePostForm(request.POST, request.FILES)
		print "Primer if"
		if form.is_valid():
			form.save()
			print "Segundo if si guardo"
			return HttpResponseRedirect("/")
		else:
			form = savePostForm()
			print "no guardo"

	template = "savepost.html"

	return render_to_response(template,context_instance=RequestContext(request,locals()) )