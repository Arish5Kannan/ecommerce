from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request , "shop/index.html" )
def register(request):
    return render(request , "shop/register.html")  
def collection(request):
    catagory = Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})
def products(request,name):
    if(Category.objects.filter(status=0,name=name)):
        prod = Product.objects.filter(category__name=name) 
        return render(request,"shop/products.html",{"prod":prod})        
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('shop/collections.html')
