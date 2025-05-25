from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/', views.create_sales_order , name='create_order'),
    path('order_success/', views.order_success , name='order_success'),
    path('orders/', views.order_list , name='order_list'),
    path('order/<int:pk>', views.order_detail , name='order_detail'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]