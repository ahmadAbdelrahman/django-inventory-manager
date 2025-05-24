from django.urls import path
from . import views
from .views import create_sales_order

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/new/', create_sales_order, name='create_order'),
]