import pytest
from procesa import procesa, cuentaVocales, limpia

def test_procesa_cuenta():
    assert procesa("cuenta", "hola mundo") == 4
    assert procesa("cuenta", "PYTHON") == 1
    assert procesa("cuenta", "") == None

def test_procesa_limpia():
    assert procesa("limpia", "Hola, mundo!") == "Holamundo"
    assert procesa("limpia", "123 !@# abc") == "123abc"
    assert procesa("limpia", "") == None

def test_procesa_operacion_no_permitida():
    assert procesa("invalida", "texto") == "Operación no permitida"

def test_cuentaVocales():
    assert cuentaVocales("AEIOUaeiou") == 10
    assert cuentaVocales("xyz") == 0
    assert cuentaVocales("") == None

def test_limpia():
    assert limpia("Texto con espacios, y signos!") == "Textoconespaciosysignos"
    assert limpia("123 456") == "123456"
    assert limpia("") == None
