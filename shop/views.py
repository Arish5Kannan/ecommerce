from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from shop.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
    prod = Product.objects.filter(trending=1)
    return render(request , "shop/index.html",{'prod':prod} )
def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration successful You can Login Now ..!')
            return redirect('login')
    return render(request , "shop/register.html",{'form':form}) 
def logout_page(request):
    if request.user.is_authenticated    :
        logout(request) 
        messages.success(request,"You Logged out Successfully..")   
        return redirect('/')
def login_page(request):
    if request.user.is_authenticated :
        return redirect('/')
    else :    
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"You Logged in Successfully...")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username or Password...")
                return redirect('login')    

    return render(request,'shop/login.html')     
def collection(request):
    catagory = Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})
def products(request,name):
    if(Category.objects.filter(status=0,name=name)):
        prod = Product.objects.filter(category__name=name) 
        return render(request,"shop/products.html",{"prod":prod,"category_name":name})        
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')
def product_details(request,cname,pname):
    if(Category.objects.filter(status=0,name=cname)):
        if(Product.objects.filter(status=0,name=pname)):
            product = Product.objects.filter(status=0,name=pname).first()    
            return render(request,"shop/product_details.html",{"prod":product})
        else :
            messages.warning(request,"No such product found")
            return redirect('collections')       
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            # print(data['pid'])
            product_id = data['pid']
            product_qty = data['product_qty']
            # print(data['product_qty'])
            # print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status :
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product is already in  cart'},status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product added to cart successfully..'},status=200) 
                    else :
                        return JsonResponse({'status':'Product out of stock..'},status=200)      
            return JsonResponse({'status':'Product added to cart successfully..'},status=200)
        else:
            return JsonResponse({'status':'Login to add Cart'},status=200)
    else :
        return JsonResponse({'status':'Invalid Access'},status=200) 
def cart(request):
    cartitems = Cart.objects.filter(user=request.user)
    return render(request,'shop/cart.html',{'carts':cartitems})  
def remove_cart(request,id):
    cartitem = Cart.objects.get(id=id)
    cartitem.delete()
    return redirect('cart')
def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
def favview(request):
    favourite = Favourite.objects.filter(user=request.user)
    return render(request,'shop/favourite.html',{'fav':favourite})
def remove_fav(request,id):
    favourite = Favourite.objects.get(id=id)
    favourite.delete()
    return redirect('favview')    