from django.urls import path

from .views import Product_record_list,Transaction_record_list

urlpatterns = [
    path('tran/', Transaction_record_list),
    path('pro/<int:pk>/',Product_record_list),
    
  
]
