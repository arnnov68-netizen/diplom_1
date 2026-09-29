import pytest
from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger."""

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

    # ... остальные тесты без изменений ...

    # ============ move_ingredient (параметризованный) ============

    @pytest.mark.parametrize(
        "initial_order, index, new_index, expected_order",
        [
            # перемещение вперёд (в начало)
            ([0, 1, 2], 2, 0, [2, 0, 1]),
            # перемещение назад (в конец)
            ([0, 1, 2], 0, 2, [1, 2, 0]),
            # перемещение на тот же индекс
            ([0, 1], 1, 1, [0, 1]),
            # перемещение в начало
            ([0, 1, 2], 1, 0, [1, 0, 2]),
            # перемещение в конец
            ([0, 1, 2], 1, 2, [0, 2, 1]),
            # отрицательный индекс (последний элемент в начало)
            ([0, 1, 2], -1, 0, [2, 0, 1]),
        ],
    )
    def test_move_ingredient(self, initial_order, index, new_index, expected_order):
        """Проверка перемещения ингредиента (порядок и количество)."""
        ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ][: len(initial_order)]

        # раскладываем ингредиенты в заданном порядке
        self.burger.ingredients = [ingredients[i] for i in initial_order]

        self.burger.move_ingredient(index, new_index)

        # количество сохраняется
        assert len(self.burger.ingredients) == len(initial_order)

        # порядок соответствует ожидаемому
        expected = [ingredients[i] for i in expected_order]
        assert self.burger.ingredients == expected

    @pytest.mark.parametrize(
        "ingredients, index, new_index, expected_exception",
        [
            # пустой список
            ([], 0, 1, IndexError),
            # индекс вне диапазона
            ([0], 5, 0, IndexError),
        ],
    )
    def test_move_ingredient_raises(
        self, ingredients, index, new_index, expected_exception
    ):
        """Проверка ошибок при перемещении ингредиента."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ][: len(ingredients)]

        with pytest.raises(expected_exception):
            self.burger.move_ingredient(index, new_index)