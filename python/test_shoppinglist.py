# %%

import unittest

from shoppinglist import ShoppingList


class TestShoppingList(unittest.TestCase):
    def test_prices(self):
        self.goods=ShoppingList({"毛巾":5,"牙膏":10,"牙刷":8})
        self.assertEqual(self.goods.prices(),23)

