import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, expected_first, expected_last",
    [
        (1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001"),
        (1234567890123456, 1234567890123456, "1234 5678 9012 3456", "1234 5678 9012 3456"),
        (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
    ],
)
def test_card_number_generator_valid(start, stop, expected_first, expected_last):
    generator = card_number_generator(start, stop)
    numbers = list(generator)
    assert len(numbers) == stop - start + 1
    assert numbers[0] == expected_first
    assert numbers[-1] == expected_last


def test_card_number_generator_start_too_low():
    """Тест на ошибку: start < 1"""
    with pytest.raises(ValueError):
        list(card_number_generator(0, 1))


def test_card_number_generator_stop_too_high():
    """Тест на ошибку: stop > 9999999999999999"""
    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000000000000000))


def test_card_number_generator_start_gt_stop():
    """Тест на ошибку: start > stop"""
    with pytest.raises(ValueError):
        list(card_number_generator(10, 5))


def test_card_number_generator_empty_range():
    """Тест на пустой диапазон (start == stop + 1)"""
    with pytest.raises(ValueError):
        list(card_number_generator(5, 4))


def test_card_number_generator_formatting():
    """Тест на форматирование: ровно 16 цифр с пробелами"""
    generator = card_number_generator(123456789012345, 123456789012345)
    number_str = next(generator)
    assert len(number_str) == 19
    parts = number_str.split()
    assert len(parts) == 4
