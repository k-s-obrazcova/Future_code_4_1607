from .views import *
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('product/all/', list_product, name='list_product'),
    path('product/all-filter/', list_product_with_filter, name='list_product_filter'),
    path('product/one-filter/', get_one_filter_product, name='one_filter_product'),
    path('product/more-filter/', get_more_filter_product, name='more_filter_product'),
    path('product/detail/<int:id>/', get_one_product, name='one_product_info'),

    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', DeleteSupplier.as_view(), name='supplier_delete'),

    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),

    path('api/orders/', order_api_list, name='api_order_list'),
    path('api/orders/<int:pk>/', order_api_detail, name='api_order_detail'),

    path('page_product_apiview/', ProductListView.as_view(), name='page_product_apiview'),

    path('filters/', template_filter_django, name='template_filter_django'),
    path('tags/', template_tag_django, name='template_tag_django'),

]

router = routers.SimpleRouter()
router.register('api/products', ProductViewSet, basename='product')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supplier_simple', ProductViewSetSimple, basename='supplier_simple')
router.register('api/list_supplier', SupplierListViewSet, basename='list_supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/parametr', ParametrViewSet, basename='parametr')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/tag', TagViewSet, basename='tag')
router.register('api/warehouse', WarehouseViewSet, basename='warehouse')
router.register('api/inventory', InventoryViewSet, basename='inventory')
router.register('api/review', ReviewViewSet, basename='review')
router.register('api/product_pagination', ProductPaginationViewSet, basename='product_pagination')
router.register('api/supplier_admin', SupplierAdminViewSet, basename='supplier_admin')
router.register('api/product_search', ProductSearchViewSet, basename='product_search')
urlpatterns += router.urls
