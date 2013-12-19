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
	vistCount = models.DecimalField('访问量',max_digits=10,decimal_places=0)
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
	count = models.DecimalField('库存量',max_digits=10,decimal_places=0)
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


