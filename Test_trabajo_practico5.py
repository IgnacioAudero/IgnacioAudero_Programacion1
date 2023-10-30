import pytest
from functions_tps import dni_validator, last_word_len, prime_number

@pytest.mark.parametrize("dni, res", [
    (45257243, True),
    (4525724, True),
    (452572433, False)
])
def test_dni_validator(dni, res):
    assert dni_validator(dni) == res

@pytest.mark.parametrize("phrase, res", [
    ("Hola mundo", 5),
    ("Ignacio Audero", 6),
    ("Python", 6)
])
def test_last_word_len(phrase, res):
    assert last_word_len(phrase) == res

@pytest.mark.parametrize("number, res", [
    (0, False),
    (1, False),
    (17, True)
])
def test_prime_number(number, res):
    assert prime_number(number) == res