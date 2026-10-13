class ShoppingList :
    def __init__(self, goods) :
        self.goods = goods
    def prices(self):
        total=0
        for price in self.goods.values():
            total+=price
        return total