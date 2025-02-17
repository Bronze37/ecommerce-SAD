from django.urls import path
from .views import customer_list, customer_create, customer_update, customer_delete

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('create/', customer_create, name='customer_create'),
    path('update/<int:pk>/', customer_update, name='customer_update'),
    path('delete/<int:pk>/', customer_delete, name='customer_delete'),
]