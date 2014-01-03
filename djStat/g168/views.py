#-*- coding:utf8 -*-
from django.shortcuts import render_to_response
from djStat.dbmgr.models import *
from django.contrib.sites.models import get_current_site

class Text():
	def __init__(self, base_url="", value="", href="", index=None):
		if index:
			try:
				sindex = unicode(str(index)+".")
				self.value = sindex + value
			except:
				self.value = value
		else:
			self.value = value
		#print "Text value=" + self.value
		if base_url and not href == "" and not href.startswith("http://"):
			href = base_url + href	
		self.href = href

class Image():
	def __init__(self, base_url, alt="image",href=""):
		#print "Image href=" + href
		self.alt = alt
		if base_url and not href == "" and not href.startswith("http://"):
			href = base_url + href	
		self.href = href

class Input():
	def __init__(self, base_url="", title="", name="", href=""):
		self.title = title
		self.name = name
		if base_url and not href == "" and not href.startswith("http://"):
			href = base_url + href	
		self.href = href

class objPair():
	def __init__(self, id="", name=""):
		self.id = id
		self.name = name

class Spec():
	def __init__(self, color=None, sizes=None):
		self.color = color
		self.sizes = sizes

class Order():
	def __init__(self, href="", mprice="",cprice="",dprice="",days=0,specs=[]):
		self.href = href
		self.mprice = mprice
		self.cprice = cprice
		self.dprice = dprice
		self.days = days
		self.specs = specs

class Sublist:
	def __init__(self, style=0, text=None, image=None, order=None):
		#print "Sublist style=%d" % style
		self.style = style
		self.text = text 
		self.image = image
		self.order = order

class MenuItem:
	def __init__(self, type=0, obj=None, newline=0):
		#print "MenuItem type=%d" % type
		#类型
		self.type = type 
		#对象
		self.obj = obj 
		#是否换行
		self.newline = newline

def proList(request,act="",type="",orderby="",pageindex="1",pagesize="5"):
	print ''.join(['http://', request.get_host(), request.get_full_path()])
	base_url = "".join(['http://',request.get_host(),"/"])
	if act == "ls":
		#按价格由高到低排序
		if orderby == "-price":
			print "oder by price -"
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).order_by("-dprice")
			else:
				dbItems = g168_item.objects.order_by("-dprice")
		#按价格由低到高排序
		elif orderby == "+price":
			print "oder by price +"
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).order_by("dprice")
			else:
				dbItems = g168_item.objects.order_by("dprice")
		#按人气排序
		elif orderby == "-vist":
			print "oder by vist -"
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).order_by("vistCount")
			else:
				dbItems = g168_item.objects.order_by("vistCount")
		elif orderby == "+vist":
			print "oder by vist +"
			if not type == "":
				dbItems = g168_item.objects.filter(ctype=type).order_by("vistCount")
			else:
				dbItems = g168_item.objects.order_by("vistCount")
		#仅分类
		elif not type == "":
			print "oder by type"
			dbItems = g168_item.objects.filter(ctype=type).order_by("dprice")
		else:
			print "oder by default"
			dbItems = g168_item.objects.all()
	elif act == "sch":
		tag = request.POST.get("tag",None)
		if tag:
			dbItems = g168_item.objects.filter(cname__icontains=tag,itemcode__icontains=tag).order_by("-dprice")

	menuItems = []

	if not pageindex:
		pageindex = "1"
	pageindex = int(pageindex)
	print "pageindex=%d" % pageindex
	if not pagesize:
		pagesize = "5"
	pagesize = int(pagesize)
	print "pagesize=%d" % pagesize
	pagemax = pageindex*pagesize + 1
	print "pagemax=%d" % pagemax
	pagemin = (pageindex-1)*pagesize + 1
	print "pagemin=%d" % pagemin
	print "maxdbitems=%d" % dbItems.count()
	if dbItems and pagemin < dbItems.count():
		sublists = []
		if pagemax > dbItems.count():
			pagemax = pagemin + (pagesize-(pagemax-dbItems.count())) + 1
		i = pagemin-1
		for item in list(dbItems)[pagemin-1:pagemax-1]:
			i += 1
			href=base_url+"%d" % item.id
			mprice=item.mprice
			cprice=item.cprice
			dprice=item.dprice
			ds = item.list_time-item.active_time
			days=ds.days
			dicSpecs = {}
			dbSpecs = g168_item_resource.objects.filter(resid=item.id)
			for sp in dbSpecs:
				if sp.count > 0 and not sp.specid.id == '---':
					color = objPair(sp.specid.id, sp.specid.name)
					if not dicSpecs.has_key(sp.specid.id):
						sizes = []
						dicSpecs[sp.specid.id] = Spec(color, sizes)
					if not sp.csize.name == '---':
						size = objPair(sp.csize.id, sp.csize.name)
						dicSpecs[sp.specid.id].sizes.append(size)
			sublists.append(Sublist(
				#产品列表点显示类型
				style = 3,
				text = Text(base_url=base_url, value=item.cname, href="#", index=i),
				image = Image(base_url=base_url, href=item.preview_image),
				order = Order(href=href,mprice=mprice,cprice=cprice,dprice=dprice,days=days,specs=dicSpecs.values())
				))
		menuitem = MenuItem(100,sublists)
		menuItems.append(menuitem)
	return render_to_response('prolist.wml', {'menuItems':menuItems})

# Create your views here.
def index(request,id="1"):
	print ''.join(['http://', request.get_host(), request.get_full_path()])
	base_url = "".join(['http://',request.get_host(),"/"])
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
						text = Text(base_url=base_url, value=item.cname, href="#"),
						image = Image(base_url=base_url, href=item.preview_image),
						order = Order()
						))
			menuitem = MenuItem(menu.content_type.id,sublists,menu.newline)
		#这是搜索框
		elif menu.content_type.id == 5:
			input = Input(base_url=base_url, title=menu.content, name="input"+str(menu.order_by), href="")
			menuitem = MenuItem(menu.content_type.id,input,menu.newline)
		#这是图片
		elif menu.content_type.id == 1:
			if menu.link_value:
				h = menu.link_value
			else:
				h = menu.content
			image = Image(base_url=base_url, href=h)
			menuitem = MenuItem(menu.content_type.id,image,menu.newline)
		#这是文本
		elif menu.content_type.id == 0:
			text = Text(base_url=base_url, value=menu.content, href=menu.link_value)
			menuitem = MenuItem(menu.content_type.id,text,menu.newline)
		else:
			print "unknow content_type"

		menuItems.append(menuitem)
	return render_to_response('index.wml', {'menuItems':menuItems})
