# Задание 1: Юнит-тесты

Автотесты для программы, которая помогает заказать бургер в Stellar Burgers.

## Реализованные сценарии

Юнит-тесты покрывают классы `Bun`, `Burger`, `Ingredient`, `Database`.
Покрытие — 100% (отчёт: `htmlcov/index.html`).

## Структура проекта

- `bun.py`, `burger.py`, `ingredient.py`, `database.py`, `ingredient_types.py` — код программы
- `praktikum.py` — демо-скрипт
- `tests/test_class_burger.py` — тесты класса `Burger`
- `htmlcov/` — HTML-отчёт о покрытии

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск автотестов и создание HTML-отчёта о покрытии

```bash
pytest --cov=. --cov-report=html
```