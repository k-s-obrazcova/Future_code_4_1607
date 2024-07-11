from django.test import TestCase
from shop.utils import *


class CalculateMoneyDefTestCase(TestCase):
    def test_sum_price_count(self):
        result = sum_price_count(price=100, count=10)
        self.assertEqual(result, 1000)

    def test_sum_price_count_with_discount(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEqual(result, 2850)

    def test_sum_price_2_count(self):
        result = sum_price_count(price=850, count=20)
        self.assertEqual(result, 17000)


class CalculateMoneyClassTestCase(TestCase, CalculateMoney):
    def test_sum_price_count_class(self):
        result = self.sum_price_count(price=400, count=19)
        self.assertEqual(result, 7600)

    def test_sum_price_class(self):
        list_prices = [294, 2000, 6942]
        result = self.sum_price(prices=list_prices)
        self.assertEqual(result, 9236)

    def test_sum_price_with_discount_class(self):
        list_prices = [200, 640, 720]
        result = self.sum_price(prices=list_prices, discount=10)
        self.assertEqual(result, 1404)
