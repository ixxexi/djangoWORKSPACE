from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Product

# Create your views here.
def about(request):
	html = '''
<!DOCTYPE html>
<html>
<head>
	<title>About me</title>
</head>
<body>
	<h2>School</h2>
	<hr>
	<p>
		Hi, I am Josh.
	</p>
</body>
</html>

	'''

	return HttpResponse(html)

def listing(request):
	html = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Mobile</title>
</head>
<body>
<h2>Mobile</h2>
<table width=400 border=1 bgcolor="#ccffcc">
	{}
</table>

</body>
</html>
'''

	products = Product.objects.all()
	tags = "<tr><td>item number</td><td>brand name</td><td>price</td><td>size</td></tr>"
	for p in products:
		tags += "<tr><td>{}</td>".format(p.sku)
		tags += "<td>{}</td>".format(p.name)
		tags += "<td>{}</td>".format(p.price)
		tags += "<td>{}</td></tr>".format(p.get_size_display())


	return HttpResponse(html.format(tags))