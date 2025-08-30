import pytest
from src.calculate_logarithm import calculate_logarithm



# def test_calculate_logarithm_with_negative_number():
#     with pytest.raises(ValueError) as exc_info:
#         calculate_logarithm(-1)
#
#     # Проверяем, что сообщение об ошибке соответствует ожидаемому
#     assert  str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"

def test_calc_log():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)

    with pytest.raises(ValueError):
        calculate_logarithm(8, 0)