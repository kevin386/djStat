from django.contrib import admin
from djStat.dbmgr.models import *

# Register your models here.

class g168ItemAdmin(admin.ModelAdmin):
	list_display = ('cname','itemcode','ctype','approve_status','cprice','vistCount','active_time','list_time','create_time')
	search_fields = ('cname','ckeyword','itemcode')
	list_filter = ('ctype','approve_status','active_time','list_time','create_time')
	ordering = ('-create_time',)
	fields = ('cname','itemcode','ckeyword','ctype','approve_status','mprice','cprice','dprice','oprice','active_time','list_time','preview_image','cdescription','outward','promo','recommend','feature','mainparameter','fitting','parameter','cinterface')

class g168itemResourceAdmin(admin.ModelAdmin):
	list_display = ('resid','specid','csize','count')
	list_filter = ('resid','specid','csize')

admin.site.register(g168_item,g168ItemAdmin)
admin.site.register(g168_item_status)
admin.site.register(g168_item_type)
admin.site.register(g168_item_resource,g168itemResourceAdmin)
admin.site.register(sys_color)
admin.site.register(sys_size)
