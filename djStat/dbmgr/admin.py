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

class g168OrderAdmin(admin.ModelAdmin):
	list_display = ('orderid','cname','username','phone','address','remark','createdate','orderstatus')

class menuTypeAdmin(admin.ModelAdmin):
	list_display = ('type_name',)
	fields = ('type_name',)

class vistCountAdmin(admin.ModelAdmin):
	readonly_fields = ('vdate','vnum')
	def get_readmonly_fields(self, request, obj=None):
		return self.readonly_fields

class g168ExpressAdmin(admin.ModelAdmin):
	fields = ('exname','excnname')

class g168MenuItemAdmin(admin.ModelAdmin):
	list_display = ('content','content_type','link_type','link_value','newline','menu_id','order_by','tagcontent','type_id')
admin.site.register(g168_item,g168ItemAdmin)
admin.site.register(g168_item_status)
admin.site.register(g168_item_type)
admin.site.register(g168_item_resource,g168itemResourceAdmin)
admin.site.register(sys_color)
admin.site.register(sys_size)
admin.site.register(g168_order,g168OrderAdmin)
admin.site.register(g168_express,g168ExpressAdmin)
admin.site.register(g168_order_status)
admin.site.register(visitorcounter,vistCountAdmin)
admin.site.register(t_product_menu_type_approve,menuTypeAdmin)
admin.site.register(t_product_menu_item_approve,g168MenuItemAdmin)
admin.site.register(t_product_menu_approve)
admin.site.register(g168_page_style)
admin.site.register(g168_link_type)
