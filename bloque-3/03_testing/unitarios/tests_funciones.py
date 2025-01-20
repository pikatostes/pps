# tests_funciones.py
import unittest
from funciones import calcula_media

# Creamos clase que hereda de unittest.TestCase
class TestCalculaMedia(unittest.TestCase):

    # definimos una función para cada prueba
    def test_1(self):
        resultado = calcula_media([10,20,0])
        self.assertEqual(resultado, 10)  # Comprobamos calculado con "esperado"

    def test_2(self):
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 4)

    # def test_3(self):
    #     resultado = calcula_media([-2, 4, 7])
    #     self.assertEqual(resultado, 3)

    # def test_4(self):
    #     resultado = calcula_media([-2, -4, -3])
    #     self.assertEqual(resultado, -3)

    # def test_lista_vacía(self):
    #     resultado = calcula_media([])
    #     self.assertEqual(resultado, 0)        