from django.shortcuts import render,redirect
from .models import *
from shop.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
from time import sleep
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
            return redirect('login')
    return render(request , "shop/re q  1gister.html",{'form':form}) 
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)   
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
               
                return redirect('/')
            else:
                
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
        
        return redirect('collections')
def product_details(request,cname,pname):
    if(Category.objects.filter(status=0,name=cname)):
        if(Product.objects.filter(status=0,name=pname)):
            product = Product.objects.filter(status=0,name=pname).first()    
            return render(request,"shop/product_details.html",{"prod":product})
        else :
            
            return redirect('collections')       
    else:
       
        return redirect('collections')
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_qty = data['product_qty']
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
def remove_cart(request):
   if request.user.is_authenticated: 
     data = json.load(request)
     print(data['cartid'])
     id = data['cartid']
     cartitem = Cart.objects.get(id=id)
     cartitem.delete()
     return JsonResponse({'status':'Product removed successfully'},status=200)
   else :
     return JsonResponse({'status':'Login to remove'},status=200)  
    
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
          return JsonResponse({'status':'Product Added to Favourite successfully..'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
def favview(request):
    favourite = Favourite.objects.filter(user=request.user)
    return render(request,'shop/favourite.html',{'fav':favourite})
def remove_fav(request):
   if request.user.is_authenticated:
    data = json.load(request)  
    id = data['fid']  
    favourite = Favourite.objects.get(id=id)
    favourite.delete()
    return JsonResponse({'status':'Favourite product has been removed successfully'},status=200)
   
   
       