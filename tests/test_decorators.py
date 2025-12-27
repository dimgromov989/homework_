from src.decorators import my_function


def test_decorators_add(func_for_add):
    """Функция, проверяющая правильность работы декоратора"""
    a, b = func_for_add
    assert my_function(a, b) == 15
