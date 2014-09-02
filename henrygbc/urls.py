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
    url(r'^summernote/', include('django_summernote.urls')),
	url(r'^$', 'posts.views.home', name='home'),
	url(r'^post/([^/]+)$', 'posts.views.showpost', name ='showpost'),
	url(r'^contact/', 'contactos.views.contacto', name ='contacto'),
	

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
