from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.coupon_apply, name='index-temp'),
    path('dashboard', views.test , name='dash')
]