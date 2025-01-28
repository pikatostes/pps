# test_main_integration.py
import unittest
import subprocess

class TestMainIntegration(unittest.TestCase):

    def run_program(self, *args):
        """
        Ejecuta el programa main.py con argumentos específicos y retorna
        el output (stdout) y los errores (stderr).
        """
        result = subprocess.run(
            ["python", "main.py", *args],
            text=True,
            capture_output=True
        )
        return result.stdout, result.stderr

    def test_agregar_producto(self):
        """Test de integración: Agregar un producto al inventario."""
        stdout, stderr = self.run_program("agregar", "--producto", "naranjas", "--cantidad", "5")
        self.assertIn("Inventario final:  {'manzanas': 2, 'peras': 1, 'naranjas': 5}", stdout)

    def test_eliminar_producto(self):
        """Test de integración: Eliminar un producto existente."""
        stdout, stderr = self.run_program("eliminar", "--producto", "manzanas", "--cantidad", "1")
        self.assertIn("Inventario final:  {'manzanas': 1, 'peras': 1}", stdout)

    def test_consultar_producto(self):
        """Test de integración: Consultar la cantidad de un producto."""
        stdout, stderr = self.run_program("consultar", "--producto", "peras")
        self.assertIn("Cantidad de 'peras': 1", stdout)

    def test_listar_inventario(self):
        """Test de integración: Listar todos los productos del inventario."""
        stdout, stderr = self.run_program("listar")
        self.assertIn("Inventario actual:", stdout)
        self.assertIn("manzanas: 2", stdout)
        self.assertIn("peras: 1", stdout)

    def test_error_sin_producto_agregar(self):
        """Test de integración: Error al intentar agregar sin especificar producto."""
        stdout, stderr = self.run_program("agregar", "--cantidad", "5")
        self.assertIn("Error: Especificar producto y cantidad.", stdout)

    def test_error_producto_inexistente(self):
        """Test de integración: Consultar un producto inexistente."""
        stdout, stderr = self.run_program("consultar", "--producto", "kiwis")
        self.assertIn("Cantidad de 'kiwis': 0", stdout)

if __name__ == "__main__":
    unittest.main()
