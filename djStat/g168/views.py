from django.shortcuts import render_to_response
from djStat.dbmgr.models import *

# Create your views here.
def index(request):
	objs = t_product_menu_item_approve.objects.filter(menu_id="1").order_by('order_by')
	return render_to_response('index.wml', {'objs':objs})
