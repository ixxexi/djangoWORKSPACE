from django.shortcuts import render
from .models import Product, PPhoto

# Create your views here.
def index(request):
	products = Product.objects.all()
	return render(request,"mobile/index.html",locals())

def detail(request, id):
	try:
		Product.objects.get(id=id)
		images = PPhoto.objects.filter(products = product)
	except:
		pass
	return render(request, 'mobile/detail.html', locals())

