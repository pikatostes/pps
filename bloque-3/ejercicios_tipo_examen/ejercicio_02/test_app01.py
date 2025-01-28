import subprocess

def test_app_cuenta():
    result = subprocess.run(["python3", "app.py", "cuenta", "hola mundo"], capture_output=True, text=True)
    assert "> 4" in result.stdout

def test_app_limpia():
    result = subprocess.run(["python3", "app.py", "limpia", "hola, mundo!"], capture_output=True, text=True)
    assert "> holamundo" in result.stdout

def test_app_operacion_invalida():
    result = subprocess.run(["python3", "app.py", "desconocida", "texto"], capture_output=True, text=True)
    assert "> Operación no permitida" in result.stdout