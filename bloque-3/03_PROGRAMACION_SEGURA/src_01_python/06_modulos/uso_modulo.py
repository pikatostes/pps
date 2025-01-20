# uso_modulo.py

a = int(input("operando 1: "))
b = int(input("operando 2: "))

# Ejemplo uso funciones en otro fichero/mismo dir
# En este caso se importa el módulo. 
# Para usar las funciones necesito el nombre del módulo

import calculadora
print(f"suma({a},{b}) = ", calculadora.suma(a,b))
print(f"resta({a},{b}) = ", calculadora.resta(a,b))


# Ejemplo donde se importan las funciones concretas
#  Podemos usar directamente sus nombres

""" from calculadora import suma, resta
print(f"suma({a},{b}) = ", suma(a,b))
print(f"resta({a},{b}) = ", resta(a,b))  """


# Ejemplo donde se importan las funciones concretas 
#  y además se renombran

""" from calculadora import suma as miSuma, resta as r
print(f"miSuma({a},{b}) = ", miSuma(a,b)) 
print(f"r({a},{b}) = ", r(a,b))  
 """

