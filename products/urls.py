"""milestone4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('products/products', views.products, name='products'),
    path('products/stylists', views.stylists, name='stylists'),
    path('products/interiordesigners', views.interiordesigners, name='interiordesigners'),
    path('products/lifecoaches', views.lifecoaches, name='lifecoaches'),
    path('products/professionalphotos', views.professionalphotos, name='professionalphotos'),
    path('products/personaltrainers', views.personaltrainers, name='personaltrainers'),
    path('products/<product_id>', views.listing, name='listing'),
    path('categories', views.categories, name='categories')
]
