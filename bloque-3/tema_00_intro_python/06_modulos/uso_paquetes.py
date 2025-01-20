# uso_paquetes.py

# Lo normal es organizar los módulos en paquetes siguiendo jerarquía de directorios
# En ese caso la "ruta" al modulo especifica el camino para llegar al módulo
import utiles.salida

utiles.salida.saludo("Ana") # utiles.salida.saludo()

# Usamos modulo calculadora en paquete utiles
""" 
a = int(input("operando 1: "))
b = int(input("operando 2: "))
"""

# importanddo todo el móulo
""" import utiles.calculadora
print(f"suma({a},{b}) = ", utiles.calculadora.suma(a,b))
print(f"resta({a},{b}) = ", utiles.calculadora.resta(a,b)) """


# Variante del anterior importando las funciones a utilizar
""" from utiles.calculadora import suma
print(f"suma({a},{b}) = ", suma(a,b))  """


