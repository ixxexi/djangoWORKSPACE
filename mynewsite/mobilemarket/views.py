from django.shortcuts import render
from .models import Product, PPhoto


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "mobilemarket/index.html", locals())


def detail(request, id):
    try:
        Product.objects.get(id=id)
        images = PPhoto.objects.filter(products=product)
    except:
        pass
    return render(request, "mobilemarket/detail.html", locals())
