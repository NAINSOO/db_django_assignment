"""category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.display, name='index'),
    path('deletePc/<int:id>', views.deletePc, name='delete'),
    path('deleteLaptop/<int:id>', views.deleteLaptop, name='delete'),
    path('deleteProduct/<int:id>', views.deleteProduct, name='delete'),
    path('deletePrinter/<int:id>', views.deletePrinter, name='delete'),
    path('query1/', views.query1, name='query'),
    path('query2/', views.query2, name='query'),
    path('query3/', views.query3, name='query'),
    path('query4/', views.query4, name='query'),
    path('addproduct/', views.addProduct, name='product'),
    path('addproduct/getproduct/', views.getProduct, name='product'),
    path('addprinter/', views.addPrinter, name='printer'),
    path('addprinter/getprinter/', views.getPrinter, name='printer'),
    path('addpc/', views.addPC, name='pc'),
    path('addpc/getpc/', views.getPC, name='pc'),
    path('createproduct', views.create1, name='create'),
    path('createpc', views.create2, name='create'),
    path('createlaptop', views.create3, name='create'),
    path('createprinter', views.create4, name='create'),

]
