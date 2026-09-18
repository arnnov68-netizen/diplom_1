import unittest
from unittest.mock import Mock, patch

from bun import Bun
from burger import Burger
from ingredient import Ingredient
# ИСПРАВЛЕНО: правильные названия констант (INGREDIENT, а не INGREDICT)
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger(unittest.TestCase):
    """Полный набор тестов для класса Burger (100% покрытие)"""

    def setUp(self):
        """Подготовка данных для каждого теста"""
        self.burger = Burger()

        # Создаем моки для булочек
        self.mock_bun = Mock()
        self.mock_bun.get_name.return_value = "black bun"
        self.mock_bun.get_price.return_value = 100

        # Создаем моки для ингредиентов
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_name.return_value = "cutlet"
        self.mock_ingredient1.get_price.return_value = 100
        # ИСПРАВЛЕНО: INGREDIENT_TYPE_FILLING (правильное название)
        self.mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING

        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_name.return_value = "hot sauce"
        self.mock_ingredient2.get_price.return_value = 50
        # ИСПРАВЛЕНО: INGREDIENT_TYPE_SAUCE (правильное название)
        self.mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        self.mock_ingredient3 = Mock(spec=Ingredient)
        self.mock_ingredient3.get_name.return_value = "dinosaur"
        self.mock_ingredient3.get_price.return_value = 200
        # ИСПРАВЛЕНО: INGREDIENT_TYPE_FILLING (правильное название)
        self.mock_ingredient3.get_type.return_value = INGREDIENT_TYPE_FILLING

    # ============ ТЕСТЫ ДЛЯ __init__ ============

    def test_initialization(self):
        """Проверка инициализации бургера"""
        self.assertIsNone(self.burger.bun)
        self.assertEqual(self.burger.ingredients, [])
        self.assertIsInstance(self.burger.ingredients, list)

    # ============ ТЕСТЫ ДЛЯ set_buns ============

    def test_set_buns_sets_bun_correctly(self):
        """Проверка установки булочки"""
        self.burger.set_buns(self.mock_bun)
        self.assertEqual(self.burger.bun, self.mock_bun)

    def test_set_buns_updates_bun(self):
        """Проверка обновления булочки"""
        self.burger.set_buns(self.mock_bun)
        new_bun = Mock()
        new_bun.get_name.return_value = "white bun"
        self.burger.set_buns(new_bun)
        self.assertEqual(self.burger.bun, new_bun)

    def test_set_buns_none(self):
        """Проверка установки булочки в None"""
        self.burger.set_buns(None)
        self.assertIsNone(self.burger.bun)

    # ============ ТЕСТЫ ДЛЯ add_ingredient ============

    def test_add_ingredient_appends_to_list(self):
        """Проверка добавления ингредиента в конец списка"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_add_ingredient_multiple_ingredients(self):
        """Проверка добавления нескольких ингредиентов"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    @patch('burger.Ingredient')
    def test_add_ingredient_with_mock_class(self, mock_ingredient_class):
        """Проверка добавления ингредиента с использованием патча класса"""
        mock_ingredient = Mock()
        mock_ingredient_class.return_value = mock_ingredient

        self.burger.add_ingredient(mock_ingredient)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], mock_ingredient)

    # ============ ТЕСТЫ ДЛЯ remove_ingredient ============

    def test_remove_ingredient_by_index(self):
        """Проверка удаления ингредиента по индексу"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)

    def test_remove_ingredient_first_element(self):
        """Проверка удаления первого ингредиента"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)

    def test_remove_ingredient_last_element(self):
        """Проверка удаления последнего ингредиента"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_remove_ingredient_from_empty_list(self):
        """Проверка удаления ингредиента из пустого списка (должна быть ошибка)"""
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(0)

    def test_remove_ingredient_out_of_range(self):
        """Проверка удаления ингредиента с индексом вне диапазона"""
        self.burger.ingredients = [self.mock_ingredient1]
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(5)

    def test_remove_ingredient_negative_index(self):
        """Проверка удаления ингредиента с отрицательным индексом"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    # ============ ТЕСТЫ ДЛЯ move_ingredient ============

    def test_move_ingredient_forward(self):
        """Проверка перемещения ингредиента вперед (в начало списка)"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_backward(self):
        """Проверка перемещения ингредиента назад (в конец списка)"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(len(self.burger.ingredients), 3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient1)

    def test_move_ingredient_to_same_index(self):
        """Проверка перемещения ингредиента на тот же индекс (ничего не меняется)"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.move_ingredient(1, 1)
        self.assertEqual(len(self.burger.ingredients), 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)

    def test_move_ingredient_to_beginning(self):
        """Проверка перемещения ингредиента в начало списка"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.move_ingredient(1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    def test_move_ingredient_to_end(self):
        """Проверка перемещения ингредиента в конец списка"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.move_ingredient(1, 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_from_empty_list(self):
        """Проверка перемещения ингредиента в пустом списке (должна быть ошибка)"""
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(0, 1)

    def test_move_ingredient_out_of_range(self):
        """Проверка перемещения ингредиента с индексом вне диапазона"""
        self.burger.ingredients = [self.mock_ingredient1]
        # list.insert() не вызывает ошибку при new_index > len(list)
        # Проверяем только случай, когда index вне диапазона
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(5, 0)

    def test_move_ingredient_negative_index(self):
        """Проверка перемещения ингредиента с отрицательным индексом"""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        self.burger.move_ingredient(-1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    # ============ ТЕСТЫ ДЛЯ get_price ============

    def test_get_price_with_bun_and_ingredients(self):
        """Проверка расчета цены с булочкой и ингредиентами"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # 100
        self.burger.add_ingredient(self.mock_ingredient2)  # 50
        expected_price = 100 * 2 + 100 + 50
        self.assertEqual(self.burger.get_price(), expected_price)

    def test_get_price_without_bun(self):
        """Проверка расчета цены без булочки (должна быть ошибка)"""
        self.burger.add_ingredient(self.mock_ingredient1)
        with self.assertRaises(AttributeError):
            self.burger.get_price()

    def test_get_price_without_ingredients(self):
        """Проверка расчета цены только с булочкой"""
        self.burger.set_buns(self.mock_bun)
        expected_price = 100 * 2
        self.assertEqual(self.burger.get_price(), expected_price)

    def test_get_price_with_real_ingredient_objects(self):
        """Проверка расчета цены с реальными объектами ингредиентов (не моками)"""
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30)

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        expected_price = 100 * 2 + 150 + 30
        self.assertEqual(self.burger.get_price(), expected_price)

    def test_get_price_with_different_bun_prices(self):
        """Проверка расчета цены с разной стоимостью булочек"""
        test_prices = [100, 150, 200, 250]

        for bun_price in test_prices:
            with self.subTest(bun_price=bun_price):
                burger = Burger()
                bun = Mock()
                bun.get_price.return_value = bun_price
                burger.set_buns(bun)

                expected_price = bun_price * 2
                self.assertEqual(burger.get_price(), expected_price)

    # ============ ТЕСТЫ ДЛЯ get_receipt ============

    def test_get_receipt_with_bun_and_ingredients(self):
        """Проверка формирования чека с булочкой и ингредиентами"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 350"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_without_ingredients(self):
        """Проверка формирования чека только с булочкой"""
        self.burger.set_buns(self.mock_bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_calls_get_name_and_get_price(self):
        """Проверка, что чек вызывает методы булочек и ингредиентов"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_name.assert_called()
        self.mock_bun.get_price.assert_called()
        self.mock_ingredient1.get_name.assert_called()
        self.mock_ingredient1.get_type.assert_called()

    def test_get_receipt_with_real_ingredients(self):
        """Проверка формирования чека с реальными объектами"""
        real_bun = Bun("red bun", 150)
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        self.burger.set_buns(real_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        expected_receipt = (
            "(==== red bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== red bun ====)\n"
            "\n"
            "Price: 450"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    # ============ ПАРАМЕТРИЗОВАННЫЕ ТЕСТЫ ============

    def test_add_multiple_ingredients_parametrized(self):
        """Параметризованный тест добавления нескольких ингредиентов"""
        test_cases = [
            ([self.mock_ingredient1], 1),
            ([self.mock_ingredient1, self.mock_ingredient2], 2),
            ([self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3], 3)
        ]

        for ingredients, expected_count in test_cases:
            with self.subTest(ingredients=ingredients, expected_count=expected_count):
                burger = Burger()
                for ingredient in ingredients:
                    burger.add_ingredient(ingredient)
                self.assertEqual(len(burger.ingredients), expected_count)

    def test_get_price_parametrized(self):
        """Параметризованный тест расчета цены с разными комбинациями"""
        test_cases = [
            (100, [100, 50, 200], 650),
            (200, [100, 50], 550),
            (150, [], 300),
            (100, [50], 250),
            (200, [75, 25, 100], 600)
        ]

        for bun_price, ingredient_prices, expected_price in test_cases:
            with self.subTest(bun_price=bun_price, ingredient_prices=ingredient_prices):
                burger = Burger()
                bun = Mock()
                bun.get_price.return_value = bun_price
                burger.set_buns(bun)

                for price in ingredient_prices:
                    ingredient = Mock()
                    ingredient.get_price.return_value = price
                    burger.add_ingredient(ingredient)

                self.assertEqual(burger.get_price(), expected_price)

    def test_move_ingredient_parametrized(self):
        """Параметризованный тест перемещения ингредиентов"""
        test_cases = [
            (0, 2, [2, 3, 1]),
            (2, 0, [3, 1, 2]),
            (1, 0, [2, 1, 3]),
            (1, 2, [1, 3, 2])
        ]

        for index, new_index, expected_order in test_cases:
            with self.subTest(index=index, new_index=new_index):
                burger = Burger()
                mock_ingredients = []
                for val in [1, 2, 3]:
                    mock = Mock()
                    mock.val = val
                    mock_ingredients.append(mock)
                burger.ingredients = mock_ingredients.copy()

                burger.move_ingredient(index, new_index)

                result = [ing.val for ing in burger.ingredients]
                expected = [mock_ingredients[i - 1].val for i in expected_order]
                self.assertEqual(result, expected)

    # ============ ТЕСТЫ С ИСПОЛЬЗОВАНИЕМ PATCH ============

    @patch('burger.Bun')
    def test_set_buns_with_mock_class(self, mock_bun_class):
        """Проверка установки булочки с использованием патча класса"""
        mock_bun = Mock()
        mock_bun_class.return_value = mock_bun

        self.burger.set_buns(mock_bun)
        self.assertEqual(self.burger.bun, mock_bun)

    @patch('burger.Ingredient')
    def test_add_ingredient_with_mock_class_patch(self, mock_ingredient_class):
        """Проверка добавления ингредиента с использованием патча класса"""
        mock_ingredient = Mock()
        mock_ingredient_class.return_value = mock_ingredient

        self.burger.add_ingredient(mock_ingredient)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], mock_ingredient)

    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_burger_interactions_with_mocks(self, mock_ingredient_class, mock_bun_class):
        """Проверка взаимодействия бургера с моками классов"""
        mock_bun = Mock()
        mock_bun_class.return_value = mock_bun
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient_class.return_value = mock_ingredient
        mock_ingredient.get_name.return_value = "test ingredient"
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient)

        self.assertEqual(self.burger.bun, mock_bun)
        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0], mock_ingredient)


if __name__ == '__main__':
    unittest.main()