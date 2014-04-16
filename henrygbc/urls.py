from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'henrygbc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'posts.views.home', name='home'),
	url(r'^post/([^/]+)$', 'posts.views.showpost', name ='showpost'),
	url(r'^savepost/$', 'posts.views.savePost', name = 'savePost'),
	url(r'^email/$', 'emails.views.emailsave', name='email'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
