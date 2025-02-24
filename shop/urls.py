from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('collection/',views.collection,name="collections"),
    path('collections/<str:name>/',views.products,name="collections"),
    path('collections/<str:cname>/<str:pname>/',views.product_details,name="product_details"),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_cart/',views.remove_cart,name='remove_cart'),
    path('cart',views.cart,name='cart'),
    path('fav',views.fav_page,name="fav"),
    path('favview',views.favview,name='favview'),
    path('remove_fav/',views.remove_fav,name='remove_fav'),
    path("place_order/",views.place_order, name="place_order"),
    path("orders", views.orders, name="orders")

]