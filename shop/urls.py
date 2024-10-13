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
    path('cart/<int:id>/',views.remove_cart,name='cart'),
    path('cart',views.cart,name='cart'),
    path('fav',views.fav_page,name="fav"),
    path('favview',views.favview,name='favview'),
    path('remove_fav/<int:id>/',views.remove_fav,name='remove_fav')

]