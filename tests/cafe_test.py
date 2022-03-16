import unittest
from src.cafe import *

class TestCafe(unittest.TestCase):
    def setUp(self):

        self.cafe = {
            "name" : "Cake Corner",
            "till" : 100,
            "cake_menu" : [
                {
                    "name" : "Carrot Cake",
                    "topping" : "cream cheese frosting",
                    "gluten_free" : False,
                    "price" : 3.00
                },
                {
                    "name" : "Orange Almond Cake",
                    "topping" : "citrus glaze",
                    "gluten_free" : True,
                    "price" : 3.50
                },
                {
                    "name" : "Victoria Sponge",
                    "topping" : "icing sugar",
                    "gluten_free" : False,
                    "price" : 2.75
                },
                {
                    "name" : "Chocolate Brownie",
                    "topping" : "no topping",
                    "gluten_free" : True,
                    "price" : 2.50
                }
            ],
            "cakes_sold" : 0
        }

    # --- TESTS ---

    # @unittest.skip("delete this line to run the test")
    # def test_cafe_has_name(self):
    #     name = get_cafe_name(self.cafe)
    #     self.assertEqual("Cake Corner", name)

    # @unittest.skip("delete this line to run the test")
    # def test_cafe_has_till(self):
    #     till = get_cafe_till(self.cafe)
    #     self.assertEqual(100, till)

    # @unittest.skip("delete this line to run the test")
    # def test_cafe_has_menu(self):
    #     menu = get_cafe_menu(self.cafe)
    #     self.assertEqual(4, len(menu))

    # @unittest.skip("delete this line to run the test")
    # def test_list_gluten_free_cakes(self):
    #     gf_cakes = list_gluten_free_cakes(self.cafe)
    #     self.assertEqual(2, len(gf_cakes))


    # @unittest.skip("delete this line to run the test")
    def test_can_increase_till(self):
        increase_till(self.cafe, 3.50)
        self.assertEqual(103.50, self.cafe["till"])

    # @unittest.skip("delete this line to run the test")
    def test_can_find_cake_by_name(self):
        cake = find_cake_by_name(self.cafe, "Carrot Cake")
        self.assertEqual("cream cheese frosting", cake["topping"])

    # @unittest.skip("delete this line to run the test")
    def test_can_sell_cake_by_name(self):
        sell_cake(self.cafe, "Carrot Cake")
        self.assertEqual(103, self.cafe["till"])
        self.assertEqual(1, self.cafe["cakes_sold"])

