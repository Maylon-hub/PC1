import pytest

# Exercício 5: Modifique as instruções assert. Experimente:
# assert 1 in [2, 3, 4] -> este irá falhar! Vamos fazer uma versão que passa e uma que falha para demonstrar.
def test_assert_in_fail():
    assert 1 in [2, 3, 4]

def test_assert_in_pass():
    assert 1 in [1, 2, 3]

def test_assert_less_than():
    a = 10
    b = 20
    assert a < b

def test_assert_not_in():
    assert 'fizz' not in 'fizzbuzz'  # Isto irá falhar porque 'fizz' está em 'fizzbuzz'!
    # Vamos demonstrar um que passa:
    assert 'buzz' in 'fizzbuzz'

# Exercício 4: Crie alguns arquivos de teste. Pratique filtrar usando a opção -k.
# Definimos testes com palavras chaves específicas no nome:
def test_filtro_banana():
    assert True

def test_filtro_laranja():
    assert True
