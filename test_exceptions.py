import pytest
from cards import Card, CardsDB

# Slide 39/40: Teste que falha na igualdade para explorar traceback
def test_equality_fail():
    c1 = Card("sit there", "John")
    c2 = Card("do something", "okken")
    assert c1 == c2

# Slide 42: Exemplo de falha explícita com pytest.fail()
def test_with_fail():
    c1 = Card("sit there", "John")
    c2 = Card("do something", "Paul")
    
    if c1 != c2:
        pytest.fail("they don't match")

# Slide 44: Testando exceções esperadas com pytest.raises()
def test_no_path_raises():
    with pytest.raises(TypeError):
        CardsDB()
