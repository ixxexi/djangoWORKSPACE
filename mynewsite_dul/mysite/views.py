from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product
from datetime import datetime
import random


# Create your views here.
def disp_detail(request, sku):
    html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Mobile</title>
</head>
<body>
<h2>{}</h2>
<hr>
<table width=400 border=1 bgcolor="#ccffcc">
{}
</table>
<a href="/list/">back</a>
</body>
</html>
"""


def about(request):
    html = """
<!DOCTYPE html>
<html>
<head>
	<title>About me</title>
</head>
<body>
	<h2>School</h2>
	<hr>
	<p>
		Hi, I am Steven.
	</p>
</body>
</html>
	"""
    return HttpResponse(html)


def listing(request):
    html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>EV</title>
</head>
<body>
<h2>Mobile</h2>
<table width=400 border=1 bgcolor="#ccffcc">
	{}
</table>

</body>
</html>
"""

    products = Product.objects.all()
    tags = "<tr><td>item number</td><td>brand name</td><td>price</td><td>size</td></tr>"
    for p in products:
        tags += "<tr><td>{}</td>".format(p.sku)
        tags += "<td>{}</td>".format(p.name)
        tags += "<td>{}</td>".format(p.price)
        tags += "<td>{}</td></tr>".format(p.get_size_display())
    return HttpResponse(html.format(tags))


def homepage(request):
    return render(request, "index.html", locals())


def week4HW(request, ID=4111029018, name="Steven", age=20):
    n = "{}".format(name)
    a = "{}".format(age)
    i = "{}".format(ID)
    return render(request, "week4.html", locals())


def index(request, tvno=0):
    tv_list = [
        {"name": "東森", "tvcode": "2dfAzcDf"},
        {"name": "民視", "tvcode": "ylYJSBUgaMA"},
        {"name": "台視", "tvcode": "xL0ch83RAK8"},
        {"name": "三立", "tvcode": "m_dhMSvUCIc"},
    ]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    quotes = ["ahuehdue", "bdfjdiow", "cdcjidowjcoiw", "dmcdowicj", "ecdwciwhciud"]
    quote = random.choice(quotes)
    return render(request, "index.html", locals())


def carlist(request, maker=0):
    car_maker = ["Ford", "Honda", "Mazda"]
    car_list = [
        [
            {"model": "Fiesta", "price": 203500},
            {"model": "Focus", "price": 605000},
            {"model": "Mustang", "price": 900000},
        ],
        [
            {"model": "Fit", "price": 450000},
            {"model": "City", "price": 150000},
            {"model": "NSX", "price": 1200000},
        ],
        [
            {"model": "Mazda3", "price": 329999},
            {"model": "Mazda5", "price": 603000},
            {"model": "Mazda6", "price": 850000},
        ],
    ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, "carlist.html", locals())


def engtv(request, tvno=0):
    tv_list = [
        {"name": "Sky News", "tvcode": "w9uJg68CV4g"},
        {"name": "Euro News", "tvcode": "pykpO5kQJ98"},
        {"name": "India News", "tvcode": "Xmm3Kr5P1Uw"},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "engtv.html", locals())
