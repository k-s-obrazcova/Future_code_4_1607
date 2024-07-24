from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'product'
        ]


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'date_create',
            'date_update',
            'photo',
            'is_exists',
            'warehouse',
            'parametr',
            'category',
            'tag',
        ]


class ProductSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'date_create'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = [
            'date_supply',
            'supplier',
            'product'
        ]


class ParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description'
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'owner_firstname',
            'owner_name',
            'owner_surname',
            'location',
            'type_post',
            'capacity'
        ]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'product',
            'warehouse',
            'quantity',
            'single_item'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'product',
            'user_name',
            'rating',
            'comment',
            'photo'
        ]
