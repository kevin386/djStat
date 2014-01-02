from django.conf.urls import patterns, include, url, static
from django.conf import settings
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djStat.g168.views.index'),
    url(r'^(?P<id>\d+)/$', 'djStat.g168.views.index'),
    url(r'^(?P<act>ls)/(?P<type>\w+)/$', 'djStat.g168.views.proList'),
    url(r'^(?P<act>ls)/(?P<type>\d+)/(?P<orderby>[+-]price|vist)/$', 'djStat.g168.views.proList'),
    url(r'^(?P<act>sch)/$', 'djStat.g168.views.proList'),

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
