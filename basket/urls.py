from django.urls import path
from .views import *

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
]