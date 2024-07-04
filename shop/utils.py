# Миксины - это функции или классы, которые используются часто в различных методоах views
# и чтобы не переполнять views можно вынести их в отдельных класс utils

# Можно использовать класс, для добавления их в классы View
class CalculateMoney:
    def sum_price_count(self, price: [float, int], count: [float, int], discount: int = None, nds: int = None):
        result = round(count * price, 2)

        if discount:
            result = round(result * (1 - (discount / 100)), 2)
        if nds:
            result = round(result * (1 - (nds / 100)), 2)
        return result

    def sum_price(self,  prices: list, discount: int = None, nds: int = None):
        result = sum(prices)

        if discount:
            result = round(result * (1 - (discount / 100)), 2)
        if nds:
            result = round(result * (1 - (nds / 100)), 2)
        return result

# Или же функции, если нужно добавить их в другие функции
def sum_price_count(price: [float, int], count: [float, int],  discount: int = None, nds: int = None):
    return CalculateMoney().sum_price_count(price=price, count=count,discount=discount, nds=nds)

# Миксины можно использовать для подсчета в view.py или в models.py (Pos_order, Pos_supply)