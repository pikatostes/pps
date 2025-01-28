# Código borrado
# ....
import unittest
from inventario import agregar_producto, eliminar_producto, consultar_producto, listar_inventario

class TestInventario(unittest.TestCase):

    def setUp(self):
        """Configura un inventario inicial para las pruebas."""
        self.inventario = {
            "manzanas": 10,
            "naranjas": 5
        }

    # Ejemplo de ayuda...
    def test_agregar_producto_nuevo(self):
        """Probar agregar un producto nuevo al inventario."""
        resultado = agregar_producto(self.inventario, "peras", 3)
        self.assertIn("peras", resultado)
        self.assertEqual(resultado["peras"], 3)
        
    def test_agregar_producto_existente(self):
        """Probar agregar un producto existente al inventario."""
        resultado = agregar_producto(self.inventario, "manzanas", 3)
        self.assertEqual(resultado, {'manzanas': 13, 'naranjas': 5})
    
    def test_agregar_producto_sin_cantidad(self):
        """Probar agregar un producto sin cantidad al inventario."""
        self.assertRaises(ValueError, agregar_producto, self.inventario, "manzanas", 0)

    # Código borrado....
    def test_eliminar_producto(self):
        """Probar eliminar un producto del inventario."""
        resultado = eliminar_producto(self.inventario, "manzanas", 1)
        self.assertEqual(resultado, {'manzanas': 9, 'naranjas': 5})
    
    def test_eliminar_producto_inexistente(self):
        """Probar eliminar un producto inexistente del inventario."""
        self.assertRaises(KeyError, eliminar_producto, self.inventario, "platanos", 1)
        
    def test_eliminar_producto_existencias_insuficientes(self):
        """Probar eliminar un producto con existencias insuficientes del inventario."""
        self.assertRaises(ValueError, eliminar_producto, self.inventario, "manzanas", 100)
        
    def test_eliminar_producto_sin_existencias(self):
        """Probar eliminar un producto con existencias insuficientes del inventario."""
        resultado = eliminar_producto(self.inventario, "manzanas", 10)
        self.assertEqual(resultado, {'naranjas': 5})
        
    def test_consultar_producto(self):
        """Probar consultar la cantidad de un producto en el inventario."""
        cantidad = consultar_producto(self.inventario, "manzanas")
        self.assertEqual(cantidad, 10)
        
    def test_listar_inventario(self):
        """Probar listar el inventario."""
        inventario = listar_inventario(self.inventario)
        self.assertIn("manzanas", inventario)
        self.assertIn("naranjas", inventario)