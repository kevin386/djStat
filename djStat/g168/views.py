#-*- coding:utf8 -*-
from django.shortcuts import render_to_response
from djStat.dbmgr.models import *
from django.contrib.sites.models import get_current_site
from datetime import datetime

#文本
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

#图片
class Image():
	def __init__(self, base_url, src="", alt="image",href=""):
		#print "Image href=" + href
		self.alt = alt
		if base_url and not href == "" and not href.startswith("http://"):
			href = base_url + href	
		self.href = href
		if base_url and not src == "" and not src.startswith("http://"):
			src = base_url + src	
		self.src = src

#输入框
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

#预订规格
class Spec():
	def __init__(self, color=None, sizes=None, has_sizes=False):
		self.color = color
		self.sizes = sizes
		self.has_sizes = has_sizes

#预订价格和活动
class BookInfo():
	def __init__(self, href="", mprice="",cprice="",dprice="",days=0,specs=[]):
		self.href = href
		self.mprice = mprice
		self.cprice = cprice
		self.dprice = dprice
		self.days = days
		self.specs = specs

#分栏
class Sublist:
	def __init__(self, style=0, text=None, image=None, book=None):
		#print "Sublist style=%d" % style
		self.style = style
		self.text = text 
		self.image = image
		self.book = book

#菜单项
class MenuItem:
	def __init__(self, type=0, obj=None, newline=0):
		#print "MenuItem type=%d" % type
		#类型
		self.type = type 
		#对象
		self.obj = obj 
		#是否换行
		self.newline = newline

def getSublist(base_url,item,style=1, index=None):
	#生成预订信息
	text_href = base_url+"pro/%d/" % item.id
	order_href = base_url+"order/%d/" % item.id
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
				dicSpecs[sp.specid.id] = Spec(color, sizes, False)
			if not sp.csize.name == '---':
				size = objPair(sp.csize.id, sp.csize.name)
				dicSpecs[sp.specid.id].sizes.append(size)
				dicSpecs[sp.specid.id].has_sizes = True
	return Sublist(
		#产品列表点显示类型
		style = style,
		text = Text(base_url=base_url, value=item.cname, href=text_href, index=index),
		image = Image(base_url=base_url, src=item.preview_image, href=text_href),
		book = BookInfo(href=order_href,mprice=mprice,cprice=cprice,dprice=dprice,days=days,specs=dicSpecs.values())
		)


class ProductHtml:
	def __init__(self,book_h=None,book_t=None,slider=None, content=None,foot=None):
		#订购信息
		self.book_h = book_h
		self.book_t = book_t
		#内容切换栏
		self.slider = slider
		#内容
		self.content = content
		#详细描述
		self.foot = foot

class Product:
	def __init__(self,type,obj=None,explain=None,navi=None):
		self.type = type
		self.obj = obj
		self.explain = explain
		self.navi = navi

def genExpain(base_url):
	explain = [] 
	explain.append(Text(base_url,value=u"【货到付款】", href="explain/1/"))
	explain.append(Text(base_url,value=u"【售后服务】", href="explain/2/"))
	explain.append(Text(base_url,value=u"【退换货流程】", href="explain/3/"))
	explain.append(Text(base_url,value=u"【服务承诺&退换货总则】", href="explain/4/"))
	return explain

def explain(request,id):
	base_url = "".join(['http://',request.get_host(),"/"])
	print base_url
	now = datetime.now()
	return render_to_response('explain%s.wml'%id)

#订单
def order(request,pid,color,size):
	base_url = "".join(['http://',request.get_host(),"/"])
	print base_url
	now = datetime.now()
	return render_to_response('order.wml')

#产品
def product(request,pid,type=None):
	base_url = "".join(['http://',request.get_host(),"/"])
	print base_url
	now = datetime.now()
	dbItems = g168_item.objects.filter(id=pid)
	if dbItems:
		dbItem = list(dbItems)[0]
		print dbItem
	print dbItem.ctype.id
	navi = []
	navi.append(Text(base_url,u"首页",base_url))
	navi.append(Text(base_url,dbItem.ctype,"ls/%d/+price"%dbItem.ctype.id))
	if dbItem.ctype.id == 3:
		sublists_h = []
		sublists_h.append(getSublist(base_url,dbItem,style=5))
		sublists_t = []
		sublists_t.append(getSublist(base_url,dbItem,style=3))
		slider = []
		if not type or type == "design":
			slider.append(Text(base_url,u"实拍图","pro/%s/shots/"%pid))
			slider.append(Text(base_url,u"服装细节","pro/%s/details/"%pid))
			slider.append(Text(base_url,u"产品参数","pro/%s/param/"%pid))
			content = dbItem.cdescription
		elif type == "shots":
			slider.append(Text(base_url,u"设计亮点","pro/%s/design/"%pid))
			slider.append(Text(base_url,u"服装细节","pro/%s/details/"%pid))
			slider.append(Text(base_url,u"产品参数","pro/%s/param/"%pid))
			content = dbItem.parameter
		elif type == "details":
			slider.append(Text(base_url,u"设计亮点","pro/%s/design/"%pid))
			slider.append(Text(base_url,u"实拍图","pro/%s/shots/"%pid))
			slider.append(Text(base_url,u"产品参数","pro/%s/param/"%pid))
			content = dbItem.cinterface
		elif type == "param":
			slider.append(Text(base_url,u"设计亮点","pro/%s/design/"%pid))
			slider.append(Text(base_url,u"实拍图","pro/%s/shots/"%pid))
			slider.append(Text(base_url,u"服装细节","pro/%s/details/"%pid))
			content = dbItem.mainparameter
		obj = ProductHtml(
				book_h=sublists_h,
				book_t=sublists_t,
				slider=slider,
				content=content,
				foot=Text(base_url,u"教你如何选尺码","selsize/")
				)
	else:
		sublists_h = []
		sublists_t = []
		sublists_t.append(getSublist(base_url,dbItem,style=3))
		slider = []
		foot = None
		if not type:
			sublists_h.append(getSublist(base_url,dbItem,style=4))
			slider.append(Text(base_url,u"整体外观","pro/%s/entiry/"%pid))
			slider.append(Text(base_url,u"细节接口","pro/%s/interface/"%pid))
			slider.append(Text(base_url,u"配件","pro/%s/parts/"%pid))
			slider.append(Text(base_url,u"参数","pro/%s/param/"%pid))
			content = dbItem.cdescription + "<br />" + dbItem.recommend + dbItem.feature 
			if dbItem.recommend:
				content += "<br />" + dbItem.recommend
			if dbItem.feature:
				content += "<br />" + dbItem.feature
			foot = Text(base_url,u"查看详细参数","pro/%s/details/"%pid)
		elif type == "entiry":
			sublists_h.append(getSublist(base_url,dbItem,style=1))
			slider.append(Text(base_url,u"整体外观"))
			slider.append(Text(base_url,u"细节接口","pro/%s/interface/"%pid))
			slider.append(Text(base_url,u"配件","pro/%s/parts/"%pid))
			slider.append(Text(base_url,u"参数","pro/%s/param/"%pid))
			content = dbItem.outward
		elif type == "interface":
			sublists_h.append(getSublist(base_url,dbItem,style=1))
			slider.append(Text(base_url,u"整体外观","pro/%s/entiry/"%pid))
			slider.append(Text(base_url,u"细节接口"))
			slider.append(Text(base_url,u"配件","pro/%s/parts/"%pid))
			slider.append(Text(base_url,u"参数","pro/%s/param/"%pid))
			content = dbItem.cinterface
		elif type == "parts":
			sublists_h.append(getSublist(base_url,dbItem,style=1))
			slider.append(Text(base_url,u"整体外观","pro/%s/entiry/"%pid))
			slider.append(Text(base_url,u"细节接口","pro/%s/interface/"%pid))
			slider.append(Text(base_url,u"配件"))
			slider.append(Text(base_url,u"参数","pro/%s/param/"%pid))
			content = dbItem.fitting
		elif type == "param":
			sublists_h.append(getSublist(base_url,dbItem,style=1))
			slider.append(Text(base_url,u"整体外观","pro/%s/entiry/"%pid))
			slider.append(Text(base_url,u"细节接口","pro/%s/interface/"%pid))
			slider.append(Text(base_url,u"配件","pro/%s/parts/"%pid))
			slider.append(Text(base_url,u"参数"))
			content = dbItem.mainparameter
		elif type == "details":
			sublists_h.append(getSublist(base_url,dbItem,style=1))
			content = dbItem.parameter

		obj = ProductHtml(
				book_h=sublists_h,
				book_t=sublists_t,
				slider=slider,
				content=content,
				foot=foot
				)
	p = Product(dbItem.ctype,obj=obj,explain=genExpain(base_url),navi=navi)
	return render_to_response('product.wml', {"product":p})


#产品列表
def proList(request,type="",orderby="",pageindex="1",pagesize="5"):
	base_url = "".join(['http://',request.get_host(),"/"])
	print base_url
	now = datetime.now()

	if not type == "":
		#按价格由低到高排序
		print orderby
		if orderby == "+price":
			print "oder by price +"
			vist_url = "ls/%s/%s/" % (type,"-vist")
			dbItems = g168_item.objects.filter(ctype=type).order_by("dprice")
		#按价格由高到低排序
		#elif orderby == "-price":
		#	print "oder by price -"
		#	dbItems = g168_item.objects.filter(ctype=type).order_by("-dprice")
		#按人气排序
		elif orderby == "-vist":
			print "oder by vist -"
			price_url = "ls/%s/%s/" % (type,"+price")
			dbItems = g168_item.objects.filter(ctype=type).order_by("-vistCount")
		#elif orderby == "+vist":
		#	print "oder by vist +"
		#	dbItems = g168_item.objects.filter(ctype=type).order_by("vistCount")
		#仅分类
		else :
			print "oder by type"
			price_url = "ls/%s/%s/" % (type,"+price")
			dbItems = g168_item.objects.filter(ctype=type).order_by("dprice")
	else:
		#从post里面获取查询内容
		pass

	menuItems = []

	if not pageindex:
		pageindex = "1"
	pageindex = int(pageindex)
	print "pageindex=%d" % pageindex
	if not pagesize:
		pagesize = "5"
	pagesize = int(pagesize)
	print "pagesize=%d" % pagesize
	maxindex = pageindex*pagesize + 1
	print "maxindex=%d" % maxindex
	minindex = (pageindex-1)*pagesize + 1
	print "minindex=%d" % minindex
	print "maxdbitems=%d" % dbItems.count()
	if dbItems and minindex < dbItems.count():
		#最大页数
		maxpages = dbItems.count()/pagesize
		if not dbItems.count()%pagesize == 0:
			maxpages += 1
		print maxpages
		#页数导航
		pagearray = range(1,maxpages+1)
		#前页
		if not pageindex == 1:
			prepageindex = pageindex-1
		#后页
		if not pageindex == maxpages:
			forpageindex = pageindex+1
		#页面导航点url，后加page index
		pageindexurl = "ls/%s/%s/" % (type, orderby)
		print pageindexurl
		#每个产品点订购信息
		sublists = []
		if maxindex > dbItems.count():
			maxindex = minindex + (pagesize-(maxindex-dbItems.count())) + 1
		i = minindex-1
		for item in list(dbItems)[minindex-1:maxindex-1]:
			i += 1
			sublists.append(getSublist(base_url,item,style=5,index=i))
		menuitem = MenuItem(100,sublists)
		menuItems.append(menuitem)
	return render_to_response('prolist.wml', locals())

# Create your views here.
def index(request,id="1"):
	base_url = "".join(['http://',request.get_host(),"/"])
	print base_url
	now = datetime.now()

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
					sublists.append(getSublist(base_url,item,menu.disptype.id))
			menuitem = MenuItem(menu.content_type.id,sublists,menu.newline)
		#这是搜索框
		elif menu.content_type.id == 5:
			input = Input(base_url=base_url, title=menu.content, name="input"+str(menu.order_by), href="")
			menuitem = MenuItem(menu.content_type.id,input,menu.newline)
		#这是图片
		elif menu.content_type.id == 1:
			image = Image(base_url=base_url, href=menu.link_value)
			menuitem = MenuItem(menu.content_type.id,image,menu.newline)
		#这是文本
		elif menu.content_type.id == 0:
			text = Text(base_url=base_url, value=menu.content, href=menu.link_value)
			menuitem = MenuItem(menu.content_type.id,text,menu.newline)
		else:
			print "unknow content_type"

		menuItems.append(menuitem)
	return render_to_response('index.wml', locals())
