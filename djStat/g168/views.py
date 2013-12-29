#-*- coding:utf8 -*-
from django.shortcuts import render_to_response
from djStat.dbmgr.models import *

class Text():
	def __init__(self, request=None, value="", href=""):
		self.value = value
		if request and not href == "" and not href.startswith("http://"):
			href = "http://" + request.get_host() +"/" + href	
		self.href = href

class Image():
	def __init__(self, request=None, alt="image",href=""):
		self.alt = alt
		if request and not href == "" and not href.startswith("http://"):
			href = "http://" + request.get_host() +"/" + href	
		self.href = href

class Input():
	def __init__(self, request=None, title="", name="", href=""):
		self.title = title
		self.name = name
		if request and not href == "" and not href.startswith("http://"):
			href = "http://" + request.get_host() +"/" + href	
		self.href = href

class Order():
	def __init__(self, info=""):
		pass

class Sublist:
	def __init__(self, style=0, text=None, image=None, order=None):
		self.style = style
		self.text = text 
		self.image = image
		self.order = order

class MenuItem:
	def __init__(self, type=0, obj=None, newline=0):
		#类型
		self.type = type 
		#对象
		self.obj = obj 
		#是否换行
		self.newline = newline

def proList(request,act="",tag="",type="",code="",price="",vist=""):
	if act == "ls":
		if not price == "":
			if price == "de":
				if not type == "":
					dbItems = g168_item.objects.filter(ctype=type).oder_by("-price")
				else:
					dbItems = g168_item.objects.oder_by("-price")
			else:
				if not type == "":
					dbItems = g168_item.objects.filter(ctype=type).oder_by("price")
				else:
					dbItems = g168_item.objects.oder_by("price")
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).oder_by("-price")
			else:
				dbItems = g168_item.objects.oder_by("-price")
		elif not vist == "":
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).oder_by("vistCount")
			else:
				dbItems = g168_item.objects.oder_by("vistCount")
		elif not type == "":
			dbItems = g168_item.objects.filter(ctype=type).oder_by("-price")
	elif act == "schPro":
		if not type == "":
			dbItems = g168_item.objects.filter(ctype=type,cname__icontains=tag,itemcode__icontains=tag).oder_by("-price")
		else:
			dbItems = g168_item.objects.filter(cname__icontains=tag,itemcode__icontains=tag).oder_by("-price")
	elif act == "schOrd":
		pass
	for item in dbItems:
		print item

# Create your views here.
def index(request,id="1"):
	dbMenuItems = t_product_menu_item_approve.objects.filter(menu_id=id).order_by('order_by')
	menuItems = []
	for menu in dbMenuItems:
		#这是分栏
		if menu.content_type.id == 100:
			sublists = []
			tags = menu.tagcontent.split(",")
			for tag in tags:
				if menu.type_id.type_id != 0:
					items = g168_item.objects.filter(ckeyword__icontains=tag,ctype=menu.type_id.type_id)
				else:
					items = g168_item.objects.filter(ckeyword__icontains=tag)
				for item in items:
					sublists.append(Sublist(
						style = menu.disptype.id,
						text = Text(request=request, value=item.cname, href="#"),
						image = Image(request=request, href=item.preview_image),
						order = Order()
						))
			menuitem = MenuItem(menu.content_type.id,sublists,menu.newline)
		#这是搜索框
		elif menu.content_type.id == 5:
			input = Input(request=request, title=menu.content, name="input"+str(menu.order_by), href="")
			menuitem = MenuItem(menu.content_type.id,input,menu.newline)
		#这是图片
		elif menu.content_type.id == 1:
			image = Image(request=request, href=menu.content)
			menuitem = MenuItem(menu.content_type.id,image,menu.newline)
		#这是文本
		elif menu.content_type.id == 0:
			text = Text(request=request, value=menu.content, href=menu.link_value)
			menuitem = MenuItem(menu.content_type.id,text,menu.newline)
		else:
			print "unknow content_type"

		menuItems.append(menuitem)
	return render_to_response('index.wml', {'menuItems':menuItems})
