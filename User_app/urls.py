from django.urls import path,include
from . import views

urlpatterns = [
    path('user_index',views.user_index,name='user_index'),
    path('user_view_recipe',views.user_view_recipe,name='user_view_recipe'),
    path('user_login',views.user_login,name='user_login'),
    path('user_member_login',views.user_member_login,name='user_member_login'), 
    path('user_registeration',views.user_registeration,name='user_registeration'),
    path('add_registeration',views.add_registeration,name='add_registeration'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('single_product<int:ID>',views.single_product,name='single_product'),
    path('user_cart',views.user_cart,name='user_cart'),
    path('add_to_cart<int:Id>',views.add_to_cart,name='add_to_cart'),
    path('cart_delete<int:ID>',views.cart_delete,name='cart_delete'),
    path('check_out',views.check_out,name='check_out'),
    path('checking_out',views.checking_out,name='checking_out'),
    path('filter_category<str:filter>',views.filter_category,name='filter_category'),
    path('new_register',views.new_register,name='new_register'),
    path('add_new_registeration',views.add_new_registeration,name='add_new_registeration'),
    path('new_login',views.new_login,name='new_login'),
    path('new_user_login',views.new_user_login,name='new_user_login'),
    path('cart_update',views.cart_update,name='cart_update')
]