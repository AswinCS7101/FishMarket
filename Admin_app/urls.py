from django.urls import path,include
from . import views

urlpatterns = [
   path('admin_login',views.admin_login,name='admin_login'), 
   path('admin_registeration',views.admin_registeration,name='admin_registeration'),
   path('member_login',views.member_login,name='member_login'),
   path('admin_logout',views.admin_logout,name='admin_logout'),
   path('admin_index',views.admin_index,name='admin_index'),
   path('add_category',views.add_category,name='add_category'),
   path('view_category',views.view_catagory,name='view_category'),
   path('adding_category',views.adding_category,name='adding_category'),
   path('edit_category<int:ID>',views.edit_category,name='edit_category'),
   path('edit_add_category<int:Id>',views.edit_add_category,name='edit_add_category'),
   path('delete_category<int:Id>',views.delete_category,name='delete_category'),
   path('add_product',views.add_product,name='add_product'),
   path('adding_product',views.adding_product,name='adding_product'),
   path('view_products',views.view_products,name='view_products'),
   path('add_recipe',views.add_recipe,name='add_recipe'),
   path('adding_recipe',views.adding_recipe,name='adding_recipe'),
   path('view_recipe',views.view_recipe,name='view_recipe'),
   path('view_users',views.view_users,name='view_users'),
   path('new_admin_register',views.new_admin_register,name='new_admin_register'),
   path('approve_user<int:ID>',views.approve_user,name='approve_user'),
   path('user_delete<int:Id>',views.user_delete,name='user_delete'),
   path('check_out_table',views.check_out_table,name='check_out_table')
   
]