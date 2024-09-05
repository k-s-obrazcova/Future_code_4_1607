from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets

from .models import *
from .forms import OrderForm
from .serializer import CategorySerializer, CollectionSerializer, ShoesSerializer, SupplierSerializer, SupplySerializer, \
    OrderSerializer, PosSupplySerializer, PosOrderSerializer


def home(request):
    return render(request, 'shoes_shop/index.html')


class ShoeList(ListView):
    model = Shoes
    template_name = 'shoes_shop/shoes/list.html'
    allow_empty = True
    paginate_by = 12

    def get_queryset(self):
        return Shoes.objects.filter(is_exists=True)


class ShoeDetail(DetailView):
    model = Shoes
    template_name = 'shoes_shop/shoes/detail.html'


class OrderList(ListView):
    model = Order
    template_name = 'shoes_shop/order/list.html'
    allow_empty = True
    paginate_by = 6


class OrderDetail(DetailView):
    model = Order
    template_name = 'shoes_shop/order/detail.html'


class OrderCreate(CreateView):
    model = Order
    template_name = 'shoes_shop/order/create.html'
    form_class = OrderForm


# _______________________API______________________________
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
