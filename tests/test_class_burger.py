import pytest
from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger. Один тест — одна проверка."""

    def setup_method(self):
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

    def test_initialization_bun_is_none(self):
        """При инициализации булочка не задана."""
        assert self.burger.bun is None

    def test_initialization_ingredients_is_empty(self):
        """При инициализации список ингредиентов пуст."""
        assert self.burger.ingredients == []

    def test_initialization_ingredients_is_list(self):
        """Список ингредиентов — это list."""
        assert isinstance(self.burger.ingredients, list)

    # ============ set_buns ============

    def test_set_buns_sets_bun_correctly(self):
        """set_buns сохраняет булочку."""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun is self.mock_bun

    def test_set_buns_updates_bun(self):
        """Повторный set_buns заменяет булочку."""
        new_bun = Mock(spec=Bun)
        new_bun.get_name.return_value = "white bun"
        self.burger.set_buns(self.mock_bun)
        self.burger.set_buns(new_bun)
        assert self.burger.bun is new_bun

    def test_set_buns_none(self):
        """set_buns(None) сбрасывает булочку."""
        self.burger.set_buns(self.mock_bun)
        self.burger.set_buns(None)
        assert self.burger.bun is None

    # ============ add_ingredient ============

    def test_add_ingredient_appends_to_list(self):
        """После добавления в списке один ингредиент."""
        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1

    def test_add_ingredient_stores_correct_object(self):
        """Добавленный ингредиент сохранён по индексу 0."""
        self.burger.add_ingredient(self.mock_ingredient1)
        assert self.burger.ingredients[0] is self.mock_ingredient1

    def test_add_ingredient_multiple_count(self):
        """После добавления трёх ингредиентов в списке три элемента."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        assert len(self.burger.ingredients) == 3

    def test_add_ingredient_multiple_first(self):
        """Первый элемент — первый добавленный ингредиент."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        assert self.burger.ingredients[0] is self.mock_ingredient1

    def test_add_ingredient_multiple_second(self):
        """Второй элемент — второй добавленный ингредиент."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        assert self.burger.ingredients[1] is self.mock_ingredient2

    def test_add_ingredient_multiple_third(self):
        """Третий элемент — третий добавленный ингредиент."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        assert self.burger.ingredients[2] is self.mock_ingredient3

    # ============ remove_ingredient ============

    def test_remove_ingredient_by_index_count(self):
        """После удаления по индексу в списке два элемента."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        assert len(self.burger.ingredients) == 2

    def test_remove_ingredient_by_index_first(self):
        """Первый элемент не изменился после удаления по индексу 1."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        assert self.burger.ingredients[0] is self.mock_ingredient1

    def test_remove_ingredient_by_index_second(self):
        """Второй элемент — бывший третий после удаления по индексу 1."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        assert self.burger.ingredients[1] is self.mock_ingredient3

    def test_remove_ingredient_first_element_count(self):
        """После удаления первого элемента остаётся один."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient_first_element_value(self):
        """После удаления первого элемента остаётся бывший второй."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients[0] is self.mock_ingredient2

    def test_remove_ingredient_last_element_count(self):
        """После удаления последнего элемента остаётся один."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient_last_element_value(self):
        """После удаления последнего элемента остаётся бывший первый."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        assert self.burger.ingredients[0] is self.mock_ingredient1

    def test_remove_ingredient_from_empty_list(self):
        """Удаление из пустого списка бросает IndexError."""
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(0)

    def test_remove_ingredient_out_of_range(self):
        """Удаление по индексу вне диапазона бросает IndexError."""
        self.burger.ingredients = [self.mock_ingredient1]
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(5)

    def test_remove_ingredient_negative_index_count(self):
        """После удаления с индексом -1 остаётся один элемент."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient_negative_index_value(self):
        """После удаления с индексом -1 остаётся первый элемент."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        assert self.burger.ingredients[0] is self.mock_ingredient1

    # ============ move_ingredient ============

    @pytest.mark.parametrize(
        "initial_order, index, new_index, expected_order",
        [
            # перемещение вперёд (в начало): [1,2,3] -> [3,1,2]
            ([0, 1, 2], 2, 0, [2, 0, 1]),
            # перемещение назад (в конец): [1,2,3] -> [2,3,1]
            ([0, 1, 2], 0, 2, [1, 2, 0]),
            # перемещение на тот же индекс: [1,2] -> [1,2]
            ([0, 1], 1, 1, [0, 1]),
            # перемещение в начало: [1,2,3] -> [2,1,3]
            ([0, 1, 2], 1, 0, [1, 0, 2]),
            # перемещение в конец: [1,2,3] -> [1,3,2]
            ([0, 1, 2], 1, 2, [0, 2, 1]),
            # отрицательный индекс: [1,2,3] -> [3,1,2]
            ([0, 1, 2], -1, 0, [2, 0, 1]),
        ],
    )
    def test_move_ingredient_order(self, initial_order, index, new_index, expected_order):
        """Проверка порядка ингредиентов после перемещения."""
        ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ][: len(initial_order)]

        self.burger.ingredients = [ingredients[i] for i in initial_order]

        self.burger.move_ingredient(index, new_index)

        expected = [ingredients[i] for i in expected_order]
        assert self.burger.ingredients == expected

    @pytest.mark.parametrize(
        "initial_order, index, new_index",
        [
            ([0, 1, 2], 2, 0),
            ([0, 1, 2], 0, 2),
            ([0, 1], 1, 1),
            ([0, 1, 2], 1, 0),
            ([0, 1, 2], 1, 2),
            ([0, 1, 2], -1, 0),
        ],
    )
    def test_move_ingredient_keeps_count(self, initial_order, index, new_index):
        """После перемещения количество ингредиентов не меняется."""
        ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ][: len(initial_order)]

        self.burger.ingredients = [ingredients[i] for i in initial_order]

        self.burger.move_ingredient(index, new_index)

        assert len(self.burger.ingredients) == len(initial_order)

    def test_move_ingredient_from_empty_list(self):
        """Перемещение в пустом списке бросает IndexError."""
        with pytest.raises(IndexError):
            self.burger.move_ingredient(0, 1)

    def test_move_ingredient_index_out_of_range(self):
        """Перемещение с индексом вне диапазона бросает IndexError."""
        self.burger.ingredients = [self.mock_ingredient1]
        with pytest.raises(IndexError):
            self.burger.move_ingredient(5, 0)

    # ============ get_price ============

    def test_get_price_with_bun_and_ingredients(self):
        """Цена с булочкой и двумя ингредиентами."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # 100
        self.burger.add_ingredient(self.mock_ingredient2)  # 50
        assert self.burger.get_price() == 350.0

    def test_get_price_without_bun(self):
        """Без установленной булочки get_price бросает AttributeError.

        Текущее поведение метода: безусловное обращение к self.bun.get_price().
        """
        self.burger.add_ingredient(self.mock_ingredient1)
        with pytest.raises(AttributeError):
            self.burger.get_price()

    def test_get_price_without_ingredients(self):
        """Цена только с булочкой — двойная стоимость булочки."""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.get_price() == 200.0

    def test_get_price_with_real_ingredient_objects(self):
        """Цена с реальными объектами ингредиентов."""
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30.0)

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        assert self.burger.get_price() == 380.0

    # ============ get_receipt ============

    def test_get_receipt_with_bun_and_ingredients(self):
        """Чек с булочкой и двумя ингредиентами совпадает посимвольно."""
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
        assert self.burger.get_receipt() == expected_receipt

    def test_get_receipt_without_ingredients(self):
        """Чек только с булочкой совпадает посимвольно."""
        self.burger.set_buns(self.mock_bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        assert self.burger.get_receipt() == expected_receipt

    def test_get_receipt_calls_bun_get_name(self):
        """Чек вызывает get_name у булочки."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_name.assert_called()

    def test_get_receipt_calls_bun_get_price(self):
        """Чек вызывает get_price у булочки."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_price.assert_called()

    def test_get_receipt_calls_ingredient_get_name(self):
        """Чек вызывает get_name у ингредиента."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_ingredient1.get_name.assert_called()

    def test_get_receipt_calls_ingredient_get_type(self):
        """Чек вызывает get_type у ингредиента."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_ingredient1.get_type.assert_called()

    def test_get_receipt_with_real_ingredients(self):
        """Чек с реальными объектами Bun и Ingredient совпадает посимвольно."""
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
        assert self.burger.get_receipt() == expected_receipt