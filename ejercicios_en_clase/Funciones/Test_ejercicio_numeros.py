import pytest
from ejercicios_en_clase_functions import addition_digit

@pytest.mark.parametrize("number, res", [
    (54, 9),
    (99, 18),
    (53, 8)
])

def test_addition_digit(number, res):
    assert addition_digit(number) == res