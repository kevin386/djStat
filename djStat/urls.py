from django.conf.urls import patterns, include, url, static
from django.conf import settings
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djStat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^grappelli/',include('grappelli.urls')),
	url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views',
	url(r'^media/(?P<path>.*)$','static.serve',{'document_root':settings.MEDIA_ROOT},name='media'),
	url(r'^static/(?P<path>.*)$','static.serve',{'document_root':settings.STATIC_ROOT},name='static'),
)

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
