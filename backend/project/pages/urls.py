from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('urunler/', views.products, name="products"),
    path('urundetay/<slug:productslug>/', views.productdetail, name="productdetail"),
]
