from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
    path('catalog/', ShoeList.as_view(), name='shoes_list'),
    path('catalog/<int:pk>/', ShoeDetail.as_view(), name='shoes_detail'),
]

router = routers.SimpleRouter()
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/collection', CollectionViewSet, basename='collection')
router.register('api/shoes', ShoesViewSet, basename='shoes')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/order', OrderViewSet, basename='order')
router.register('api/pos_order', PosOrderViewSet, basename='pos_order')
router.register('api/pos_supply', PosSupplyViewSet, basename='pos_supply')

urlpatterns += router.urls
