#-*- coding:utf8 -*-
from django.conf.urls import patterns, include, url, static
from django.conf import settings
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#菜单
    url(r'^$', 'djStat.g168.views.index'),#首页
    url(r'^(?P<id>\d+)/$', 'djStat.g168.views.index'),#其他页面
	#产品
    url(r'^pro/(?P<pid>\d{1,2})/((?P<type>\w+)/)?$', 'djStat.g168.views.product'),
	#产品列表
	url(r'^ls/(?P<type>\d+)/(?P<orderby>[+-](?:price|vist))/((?P<pageindex>\d{1,2})/((?P<pagesize>\d{1,2})/)?)?$', 'djStat.g168.views.proList'),#排序列表
    url(r'^ls/$', 'djStat.g168.views.proList'),#搜索产品
	#订单
    url(r'^order/$', 'djStat.g168.views.order'),#搜索订单
    url(r'^order/(?P<pid>\d{1,2})/((?P<color>\d{1,2})/((?P<size>\d{1,2})/)?)?$', 'djStat.g168.views.order'),#下订单
	#购物规则
    url(r'^explain/(?P<id>\d{1,2})/$', 'djStat.g168.views.explain'),#搜索订单

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
