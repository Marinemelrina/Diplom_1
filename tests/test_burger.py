from burger import Burger
from unittest.mock import Mock, patch, call
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import random


class TestBurger:
    mock_available_buns = Mock()
    mock_available_buns.return_value = [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300),
    ]

    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]

    def test_get_receipt(self):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = random.choice(TestBurger.mock_available_ingredients())
        second_ingridient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        burger.add_ingredient(second_ingridient)
        receipt = burger.get_receipt()

        assert (
            ("(==== test_bun ====)") in receipt
            and first_ingridient.get_type().lower() in receipt
            and second_ingridient.get_type().lower() in receipt
        )

    def test_set_bun(self):
        bun = random.choice(TestBurger.mock_available_buns())
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert bun.name in receipt

    def test_get_receipt_with_bun_only(self):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()

        assert ("(==== test_bun ====)") in receipt

    def test_get_receipt_with_souce(self):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        receipt = burger.get_receipt()

        assert (
            "(==== test_bun ====)"
        ) in receipt and first_ingridient.get_type().lower() in receipt

    def test_get_receipt_with_filling(self):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        receipt = burger.get_receipt()

        assert (
            "(==== test_bun ====)"
        ) in receipt and first_ingridient.get_type().lower() in receipt

    def test_move_ingridient(self):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = random.choice(TestBurger.mock_available_ingredients())
        second_ingridient = random.choice(TestBurger.mock_available_ingredients())
        first_ingridient_name = first_ingridient.get_name()
        second_ingridient_name = second_ingridient.get_name()
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        burger.add_ingredient(second_ingridient)
        receipt = burger.get_receipt()
        first_index = receipt.find(first_ingridient_name)
        second_index = receipt.find(second_ingridient_name)
        burger.move_ingredient(0, 1)
        new_receipt = burger.get_receipt()

        assert burger.ingredients == [second_ingridient, first_ingridient]

    def test_remove_ingridient(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = random.choice(TestBurger.mock_available_ingredients())
        second_ingridient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        burger.add_ingredient(second_ingridient)
        receipt = burger.get_receipt()
        burger.remove_ingredient(0)
        new_receipt = burger.get_receipt()

        assert first_ingridient.get_name() not in new_receipt

    @patch("builtins.print")
    def test_print_receipt(self, mocked_print):
        bun_name = "test_bun"
        bun = Bun(name=bun_name, price=12.5)
        first_ingridient = random.choice(TestBurger.mock_available_ingredients())
        second_ingridient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        burger.add_ingredient(second_ingridient)
        receipt = burger.get_receipt()

        assert ("(==== test_bun ====)") in receipt

    def test_get_price(self):
        bun = random.choice(TestBurger.mock_available_buns())
        ingridient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger_price = 2 * bun.get_price()
        burger.add_ingredient(ingridient)
        burger_price += ingridient.get_price()
        receipt_price = burger.get_price()

        assert receipt_price == burger_price
