from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование коллекции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Shoes(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, null=True, blank=True, verbose_name='Коллекция')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей.)"

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обуви'


class gi(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название поставщика')
    phone = models.CharField(max_length=16, verbose_name='Телефон компании')
    address_company = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    city = models.CharField(max_length=MAX_LENGTH, verbose_name='Город отгрузки')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Supply(models.Model):
    date_supply = models.DateTimeField(verbose_name='Дата поставки')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')

    shoe = models.ManyToManyField(Shoes, through='PosSupply', verbose_name='Товары')

    def __str__(self):
        return f"№{self.pk} - {self.date_supply} ({self.supplier.name})"

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
    ]
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    comment = models.CharField(blank=True, null=True, max_length=MAX_LENGTH, verbose_name='Комментарий')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    finish = models.BooleanField(default=False, verbose_name='Выполнено')

    shoe = models.ManyToManyField(Shoes, through='PosOrder', verbose_name='Позиция обуви')

    def __str__(self):
        return f'#{self.pk} - {self.buyer_name} {self.buyer_firstname} ({self.create_date})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class PosSupply(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, verbose_name='Поставка')
    shoe = models.ForeignKey(Shoes, on_delete=models.PROTECT, verbose_name='Позиция обуви')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество пар')

    def __str__(self):
        return f'#{self.supply.pk} {self.shoe.name} - {self.supply.date_supply}'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставок'


class PosOrder(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.PROTECT, verbose_name='Позиция обуви')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество пар')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'№{self.order.pk} - {self.shoe.name} ({self.order.buyer_name} {self.order.buyer_firstname})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
