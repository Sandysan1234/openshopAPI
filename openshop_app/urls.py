from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Product_list.as_view(), name='product-list'),
    path('products/<uuid:pk>/', views.Product_detail.as_view(), name='product-detail'),
]