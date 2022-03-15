import unittest
from src.cafe import *

class TestCafe(unittest.TestCase):
    def setUp(self):

        self.cafe_name = "Cake Corner"
        self.cafe_till = 100

        self.cakes = {
            "cake_1" : {
                "name" : "Carrot Cake",
                "topping" : "cream cheese frosting",
                "gluten_free" : False,
                "price" : 3.00
            },
            "cake_2" : {
                "name" : "Orange Almond Cake",
                "topping" : "citrus glaze",
                "gluten_free" : True,
                "price" : 3.50
            },
            "cake_3" : {
                "name" : "Victoria Sponge",
                "topping" : "icing sugar",
                "gluten_free" : False,
                "price" : 2.75
            },
            "cake_4" : {
                "name" : "Chocolate Brownie",
                "topping" : "no topping",
                "gluten_free" : True,
                "price" : 2.50
            }
        }