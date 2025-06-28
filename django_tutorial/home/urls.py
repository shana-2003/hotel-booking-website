from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.index,name='Home'),
     path('menu', views.menus,name='menu'),
     path('booking', views.booking,name='booking'),
     path('deals', views.dealss,name='deals'),
     path('about/', views.about,name='about'),
     path('contact', views.contact,name='contact'),
] 
