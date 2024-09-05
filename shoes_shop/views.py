from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets

from .models import *
from .forms import OrderForm
from .serializer import CategorySerializer, CollectionSerializer, ShoesSerializer, SupplierSerializer, SupplySerializer, \
    OrderSerializer, PosSupplySerializer, PosOrderSerializer

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'shoes_shop/index.html')


class ShoeList(ListView):
    model = Shoes
    template_name = 'shoes_shop/shoes/list.html'
    allow_empty = True
    paginate_by = 12

    def get_queryset(self):
        return Shoes.objects.filter(is_exists=True)


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('shoes_shop.view_shoes'), name='dispatch')
class ShoeDetail(DetailView):
    model = Shoes
    template_name = 'shoes_shop/shoes/detail.html'


@method_decorator(login_required(), name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'shoes_shop/order/list.html'
    allow_empty = True
    paginate_by = 6


@method_decorator(login_required(), name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'shoes_shop/order/detail.html'


@method_decorator(login_required(), name='dispatch')
class OrderCreate(CreateView):
    model = Order
    template_name = 'shoes_shop/order/create.html'
    form_class = OrderForm


# _______________________API______________________________
from rest_framework import permissions


class CustomPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermission]


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    permission_classes = [CustomPermission]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermission]


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [CustomPermission]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer
    permission_classes = [CustomPermission]


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermission]
