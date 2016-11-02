from django.shortcuts import render
from ecom.models import ItemInfo

# Create your views here.

def product_list(request):
    product_list = ItemInfo.objects.all()
    return render(request, 'product_list.html', {'product_list':product_list})
