#-*- coding:utf8 -*-
from django.db import models

# Create your models here.

class sys_size(models.Model):
	name = models.CharField('尺寸',max_length=100)
	class Meta:
		db_table = 'sys_size'
		verbose_name = '尺寸管理' 
		verbose_name_plural = '尺寸管理'
		app_label = u'宝贝管理'

	def __unicode__(self):
		return self.name;


class sys_color(models.Model):
	name = models.CharField('颜色',max_length=100)
	class Meta:
		db_table = 'sys_color'
		verbose_name = '颜色管理' 
		verbose_name_plural = '颜色管理'
		app_label = u'宝贝管理'

	def __unicode__(self):
		return self.name;


class g168_item_status(models.Model):
	name = models.CharField('宝贝状态',max_length=128)
	class Meta:
		db_table = 'g168_item_status'
		verbose_name = '宝贝状态' 
		verbose_name_plural = '宝贝状态'
		app_label = u'宝贝管理'

	def __unicode__(self):
		return self.name;

class g168_item_type(models.Model):
	name = models.CharField('类型',max_length=255)
	class Meta:
		db_table = 'g168_item_type'
		verbose_name = '宝贝类型' 
		verbose_name_plural = '宝贝类型'
		app_label = u'宝贝管理'

	def __unicode__(self):
		return self.name;

class g168_item(models.Model):
	itemcode = models.CharField('编码',max_length=32)
	user_id = models.DecimalField(max_digits=8,decimal_places=0)	
	#ctype = models.DecimalField('类型', max_digits=8,decimal_places=0)	
	ctype = models.ForeignKey(g168_item_type,db_column='ctype',verbose_name='类型')
	category_id = models.DecimalField(max_digits=8,decimal_places=0)
	cname = models.CharField('宝贝名称',max_length=100)
	cdescription = models.TextField('简单描述')	
	ckeyword = models.CharField('关键字', max_length=256)
	oprice = models.DecimalField('成本价', max_digits=8,decimal_places=2)
	mprice = models.DecimalField('市场价',max_digits=8,decimal_places=2)
	cprice = models.DecimalField('商城价', max_digits=8,decimal_places=2)
	dprice = models.DecimalField('促销价', max_digits=8,decimal_places=2)
	quantity = models.DecimalField(max_digits=8,decimal_places=0)
	list_time = models.DateField('活动截至日期', auto_now=False,auto_now_add=False)
	preview_image = models.CharField('主图', max_length=256)
	preview_big_image = models.CharField(max_length=512)
	#approve_status = models.DecimalField('宝贝状态', max_digits=1,decimal_places=0)
	approve_status = models.ForeignKey(g168_item_status,db_column='approve_status',verbose_name='宝贝状态')
	outward = models.TextField('整体外观')	
	promo = models.TextField('参与活动')	
	recommend = models.TextField('推荐理由')	
	#vistCount = models.DecimalField('访问量',max_digits=10,decimal_places=0)
	vistCount = models.IntegerField('访问量')
	feature = models.TextField('特色介绍')	
	mainparameter = models.TextField('主要参数')	
	fitting = models.TextField('配件描述')	
	parameter = models.TextField('详细参数')	
	cinterface = models.TextField('接口细节')	
	create_time = models.DateField('创建时间',auto_now=False,auto_now_add=True)
	active_time = models.DateField('活动开始日期',auto_now=False,auto_now_add=False)
	reserved1 = models.CharField(max_length=64)
	reserved2 = models.CharField(max_length=128)
	reserved3 = models.CharField(max_length=256)
	reserved4 = models.CharField(max_length=512)
	class Meta:
		db_table = 'g168_item'
		verbose_name = '宝贝信息' 
		verbose_name_plural = '宝贝信息'
		app_label = u'宝贝管理'
	def __unicode__(self):
		return self.cname;

class g168_item_resource(models.Model):
	resid = models.ForeignKey(g168_item,db_column='resid',verbose_name='宝贝名称')
	specid = models.ForeignKey(sys_color,db_column='specid',verbose_name='颜色')
	csize = models.ForeignKey(sys_size,db_column='csize',verbose_name='尺寸')
	isdefault = models.DecimalField(max_digits=1,decimal_places=0)
	#count = models.DecimalField('库存量',max_digits=10,decimal_places=0)
	count = models.IntegerField('库存量')
	cdesc = models.CharField(max_length=4096)
	reserved1 = models.CharField(max_length=64)
	reserved2 = models.CharField(max_length=128)
	reserved3 = models.CharField(max_length=256)
	reserved4 = models.CharField(max_length=512)
	class Meta:
		db_table = 'g168_item_resource'
		verbose_name = '规格管理' 
		verbose_name_plural = '规格管理'
		app_label = u'宝贝管理'

	def __unicode__(self):
		return u'宝贝规格';

class g168_express(models.Model):
	exid = models.IntegerField('快递编号',primary_key=True,unique=True)
	exname = models.CharField('英文名称',max_length=50)
	excnname = models.CharField('中文名称',max_length=50)
	class Meta:
		db_table = 'g168_express'
		verbose_name = '快递管理' 
		verbose_name_plural = '快递管理'
		app_label = u'订单管理'

	def __unicode__(self):
		return self.excnname;


class g168_order_status(models.Model):
	status = models.CharField('订单状态',max_length=250)
	class Meta:
		db_table = 'g168_order_status'
		verbose_name = '订单状态' 
		verbose_name_plural = '订单状态'
		app_label = u'订单管理'

	def __unicode__(self):
		return self.status;


class g168_order(models.Model):
	orderid = models.CharField('订单编号',max_length=20)
	productid = models.CharField('商品编号',max_length=10)
	#cname = models.ForeignKey(g168_item,verbose_name='宝贝名称')
	cname = models.CharField('宝贝名称', max_length=200)
	#specid= models.ForeignKey(sys_color,verbose_name='颜色')
	specid = models.DecimalField('颜色', max_digits=10, decimal_places=0)
	#csize = models.ForeignKey(sys_size,verbose_name='尺寸')
	csize = models.DecimalField('尺寸', max_digits=10, decimal_places=0)
	#count = models.DecimalField('购买数量', max_digits=11,decimal_places=0)
	count = models.IntegerField('购买数量')
	username = models.CharField('联系人', max_length=20)
	price = models.DecimalField('下单价格',max_digits=10,decimal_places=2)
	phone = models.CharField('联系人号码', max_length=15)
	address = models.CharField('地址',max_length=200)
	remark = models.CharField('备注信息',max_length=250)
	#managerid = models.DecimalField('管理员ID',max_digits=11,decimal_places=0)
	managerid = models.IntegerField('管理员ID')
	maremark = models.CharField('管理员备注', max_length=200)
	createdate = models.DateTimeField('下单日期')
	dealdate = models.DateTimeField('成交日期')
	exnumber = models.CharField('快递单号',max_length=20)
	#exid = models.DecimalField('快递公司编号',max_digits=11,decimal_places=0)
	exid = models.IntegerField('快递公司编号')
	exstatus = models.CharField('快递状态',max_length=1000)
	#orderstatus = models.DecimalField('订单状态',max_digits=11,decimal_places=0)
	#orderstatus = models.IntegerField('订单状态')
	orderstatus = models.ForeignKey(g168_order_status,db_column='orderstatus', verbose_name='订单状态')
	class Meta:
		db_table = 'g168_order'
		verbose_name = '订单' 
		verbose_name_plural = '订单管理'
		app_label = u'订单管理'

	def __unicode__(self):
		return self.orderid;


class visitorcounter(models.Model):
	vdate = models.DateField('日期')
	vnum = models.DecimalField('访问量', max_digits=11,decimal_places=0)
	class Meta:
		db_table = 'visitorcounter'
		verbose_name = '访问量' 
		verbose_name_plural = '访问量统计'
		app_label = u'访问量统计'

	def __unicode__(self):
		return '%s' % self.vdate; 

class t_product_menu_type_approve(models.Model):
	type_id = models.IntegerField(primary_key=True,unique=True)
	type_name = models.CharField('类型',max_length=200)
	add_date = models.DateTimeField('日期')
	parent_id = models.DecimalField('父ID', max_digits=8, decimal_places=0)
	class Meta:
		db_table = 't_product_menu_type_approve'
		verbose_name = '菜单类型' 
		verbose_name_plural = '菜单类型'
		app_label = u'菜单管理'

	def __unicode__(self):
		return '%s' % self.type_name; 

class g168_page_style(models.Model):
	id = models.IntegerField(primary_key=True,unique=True)
	name = models.CharField(max_length=45,verbose_name='名称')
	class Meta:
		db_table = 'g168_page_style'
		verbose_name = '模板类型' 
		verbose_name_plural = '模板类型'
		app_label = u'菜单管理'

	def __unicode__(self):
		return '%s' % self.name; 

class g168_link_type(models.Model):
	id = models.IntegerField(primary_key=True,unique=True)
	name = models.CharField(max_length=45,verbose_name='名称')
	class Meta:
		db_table = 'g168_link_type'
		verbose_name = '链接类型' 
		verbose_name_plural = '链接类型'
		app_label = u'菜单管理'

	def __unicode__(self):
		return '%s' % self.name; 


class t_product_menu_approve(models.Model):
	menu_id = models.IntegerField(primary_key=True,unique=True)
	menu_name = models.CharField(max_length=200)
	bg_color = models.CharField(max_length=200)
	font_color = models.CharField(max_length=200)
	link_color = models.CharField(max_length=200)
	font_size = models.CharField(max_length=200)
	type_id = models.DecimalField(max_digits=8,decimal_places=0)
	add_date = models.DateTimeField()
	is_index = models.DecimalField(max_digits=8,decimal_places=0)
	rec_link = models.CharField(max_length=20)
	rec_download = models.CharField(max_length=20)
	user_id = models.DecimalField(max_digits=8,decimal_places=0)
	is_special = models.DecimalField(max_digits=8,decimal_places=0)
	status = models.DecimalField(max_digits=8,decimal_places=0)
	reversed1 = models.CharField(max_length=16)
	reversed2 = models.CharField(max_length=16)
	reversed3 = models.CharField(max_length=32)
	class Meta:
		db_table = 't_product_menu_approve'
		verbose_name = '菜单列表' 
		verbose_name_plural = '菜单列表'
		app_label = u'菜单管理'

	def __unicode__(self):
		return '%s' % self.menu_name; 
	
	
class t_product_menu_item_approve(models.Model):
	item_id = models.IntegerField(primary_key=True,unique=True)
	content_type = models.ForeignKey(g168_page_style,db_column='content_type',verbose_name='模板类型')
	content = models.CharField('内容',max_length=600)
	#link_type = models.CharField('链接类型',max_length=32)
	link_type = models.ForeignKey(g168_link_type,db_column='link_type',verbose_name='链接类型')
	link_value = models.CharField('链接',max_length=400)
	pay_type = models.DecimalField(max_digits=8,decimal_places=0)
	newline = models.DecimalField('是否换行',max_digits=8, decimal_places=0)
	bg_color = models.CharField(max_length=20)
	font_color = models.CharField(max_length=20)
	font_size = models.CharField(max_length=10)
	align = models.CharField(max_length=10)
	font_style = models.CharField(max_length=10)
	menu_id = models.ForeignKey(t_product_menu_approve,db_column='menu_id',verbose_name='菜单')
	order_by = models.DecimalField('排序',max_digits=8, decimal_places=0)
	act_date = models.DateTimeField()
	tagcontent = models.CharField('标签',max_length=32)
	rankcycle = models.DecimalField(max_digits=8,decimal_places=0)
	status = models.DecimalField(max_digits=8,decimal_places=0)
	disptype = models.IntegerField()
	isself = models.IntegerField()
	type_id = models.ForeignKey(t_product_menu_type_approve,db_column='type_id', verbose_name='菜单类型')
	reserved1 = models.IntegerField()
	reserved2 = models.IntegerField()
	reserved3 = models.IntegerField()
	reserved4 = models.IntegerField()

	class Meta:
		db_table = 't_product_menu_item_approve'
		verbose_name = '菜单内容' 
		verbose_name_plural = '菜单内容'
		app_label = u'菜单管理'
		ordering = ['order_by']

	def __unicode__(self):
		return '%s' % self.content; 
