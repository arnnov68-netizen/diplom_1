import unittest
from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger(unittest.TestCase):
    """Тесты для класса Burger с 100% покрытием."""

    def setUp(self):
        """Подготовка данных для каждого теста."""
        self.burger = Burger()

        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "black bun"
        self.mock_bun.get_price.return_value = 100.0

        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_name.return_value = "cutlet"
        self.mock_ingredient1.get_price.return_value = 100.0
        self.mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING

        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_name.return_value = "hot sauce"
        self.mock_ingredient2.get_price.return_value = 50.0
        self.mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        self.mock_ingredient3 = Mock(spec=Ingredient)
        self.mock_ingredient3.get_name.return_value = "dinosaur"
        self.mock_ingredient3.get_price.return_value = 200.0
        self.mock_ingredient3.get_type.return_value = INGREDIENT_TYPE_FILLING

    # ============ __init__ ============

    def test_initialization(self):
        """Проверка инициализации бургера."""
        self.assertIsNone(self.burger.bun)
        self.assertEqual(self.burger.ingredients, [])
        self.assertIsInstance(self.burger.ingredients, list)

    # ============ set_buns ============

    def test_set_buns_sets_bun_correctly(self):
        """Проверка установки булочки."""
        self.burger.set_buns(self.mock_bun)
        self.assertEqual(self.burger.bun, self.mock_bun)

    def test_set_buns_updates_bun(self):
        """Проверка обновления булочки."""
        self.burger.set_buns(self.mock_bun)
        new_bun = Mock(spec=Bun)
        new_bun.get_name.return_value = "white bun"
        self.burger.set_buns(new_bun)
        self.assertEqual(self.burger.bun, new_bun)

    def test_set_buns_none(self):
        """Проверка установки булочки в None."""
        self.burger.set_buns(None)
        self.assertIsNone(self.burger.bun)

    # ============ add_ingredient ============

    def test_add_ingredient_appends_to_list(self):
        """Проверка добавления ингредиента в конец списка."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_add_ingredient_multiple_ingredients(self):
        """Проверка добавления нескольких ингредиентов."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    # ============ remove_ingredient ============

    def test_remove_ingredient_by_index(self):
        """Проверка удаления ингредиента по индексу."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)

    def test_remove_ingredient_first_element(self):
        """Проверка удаления первого ингредиента."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)

    def test_remove_ingredient_last_element(self):
        """Проверка удаления последнего ингредиента."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_remove_ingredient_from_empty_list(self):
        """Проверка удаления ингредиента из пустого списка."""
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(0)

    def test_remove_ingredient_out_of_range(self):
        """Проверка удаления ингредиента с индексом вне диапазона."""
        self.burger.ingredients = [self.mock_ingredient1]
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(5)

    def test_remove_ingredient_negative_index(self):
        """Проверка удаления ингредиента с отрицательным индексом."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    # ============ move_ingredient ============

    def test_move_ingredient_forward(self):
        """Проверка перемещения ингредиента в начало списка."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_backward(self):
        """Проверка перемещения ингредиента в конец списка."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient1)

    def test_move_ingredient_to_same_index(self):
        """Проверка перемещения ингредиента на тот же индекс."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.move_ingredient(1, 1)
        self.assertEqual(len(self.burger.ingredients), 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)

    def test_move_ingredient_to_beginning(self):
        """Проверка перемещения ингредиента в начало списка."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    def test_move_ingredient_to_end(self):
        """Проверка перемещения ингредиента в конец списка."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_from_empty_list(self):
        """Проверка перемещения ингредиента в пустом списке."""
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(0, 1)

    def test_move_ingredient_index_out_of_range(self):
        """Проверка перемещения с индексом вне диапазона."""
        self.burger.ingredients = [self.mock_ingredient1]
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(5, 0)

    def test_move_ingredient_negative_index(self):
        """Проверка перемещения ингредиента с отрицательным индексом."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(-1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    # ============ get_price ============

    def test_get_price_with_bun_and_ingredients(self):
        """Проверка расчета цены с булочкой и ингредиентами."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.assertEqual(self.burger.get_price(), 350.0)

    def test_get_price_without_bun(self):
        """Проверка расчета цены без булочки (AttributeError)."""
        self.burger.add_ingredient(self.mock_ingredient1)
        with self.assertRaises(AttributeError):
            self.burger.get_price()

    def test_get_price_without_ingredients(self):
        """Проверка расчета цены только с булочкой."""
        self.burger.set_buns(self.mock_bun)
        self.assertEqual(self.burger.get_price(), 200.0)

    def test_get_price_with_real_ingredient_objects(self):
        """Проверка расчета цены с реальными объектами ингредиентов."""
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30.0)

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        self.assertEqual(self.burger.get_price(), 380.0)

    # ============ get_receipt ============

    def test_get_receipt_with_bun_and_ingredients(self):
        """Проверка формирования чека с булочкой и ингредиентами."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 350.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_without_ingredients(self):
        """Проверка формирования чека только с булочкой."""
        self.burger.set_buns(self.mock_bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_calls_get_name_and_get_price(self):
        """Проверка, что чек вызывает методы булочек и ингредиентов."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_name.assert_called()
        self.mock_bun.get_price.assert_called()
        self.mock_ingredient1.get_name.assert_called()
        self.mock_ingredient1.get_type.assert_called()

    def test_get_receipt_with_real_ingredients(self):
        """Проверка формирования чека с реальными объектами."""
        real_bun = Bun("red bun", 150.0)
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)

        self.burger.set_buns(real_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        expected_receipt = (
            "(==== red bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== red bun ====)\n"
            "\n"
            "Price: 450.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    # ============ Параметризация ============

    def test_add_multiple_ingredients_parametrized(self):
        """Параметризованный тест добавления нескольких ингредиентов."""
        test_cases = [
            ([self.mock_ingredient1], 1),
            ([self.mock_ingredient1, self.mock_ingredient2], 2),
            (
                [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3],
                3,
            ),
        ]

        for ingredients, expected_count in test_cases:
            with self.subTest(ingredients=ingredients, expected_count=expected_count):
                burger = Burger()
                for ingredient in ingredients:
                    burger.add_ingredient(ingredient)
                self.assertEqual(len(burger.ingredients), expected_count)

    def test_get_price_parametrized(self):
        """Параметризованный тест расчета цены с разными комбинациями."""
        test_cases = [
            (100.0, [100.0, 50.0, 200.0], 550.0),
            (200.0, [100.0, 50.0], 550.0),
            (150.0, [], 300.0),
            (100.0, [50.0], 250.0),
            (200.0, [75.0, 25.0, 100.0], 600.0),
        ]

        for bun_price, ingredient_prices, expected_price in test_cases:
            with self.subTest(
                bun_price=bun_price, ingredient_prices=ingredient_prices
            ):
                burger = Burger()
                bun = Mock(spec=Bun)
                bun.get_price.return_value = bun_price
                burger.set_buns(bun)

                for price in ingredient_prices:
                    ingredient = Mock(spec=Ingredient)
                    ingredient.get_price.return_value = price
                    burger.add_ingredient(ingredient)

                self.assertEqual(burger.get_price(), expected_price)

    def test_move_ingredient_parametrized(self):
        """Параметризованный тест перемещения ингредиентов."""
        test_cases = [
            (0, 2, [2, 3, 1]),
            (2, 0, [3, 1, 2]),
            (1, 0, [2, 1, 3]),
            (1, 2, [1, 3, 2]),
        ]

        for index, new_index, expected_order in test_cases:
            with self.subTest(index=index, new_index=new_index):
                burger = Burger()
                mock_ingredients = []
                for val in [1, 2, 3]:
                    mock = Mock(spec=Ingredient)
                    mock.val = val
                    mock_ingredients.append(mock)
                burger.ingredients = mock_ingredients.copy()

                burger.move_ingredient(index, new_index)

                result = [ing.val for ing in burger.ingredients]
                expected = [mock_ingredients[i - 1].val for i in expected_order]
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()