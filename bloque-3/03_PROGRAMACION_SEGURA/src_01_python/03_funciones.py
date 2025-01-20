
# Definición función sin argumentos

""" def saluda():
    print("_________________________________________")
    print("Hola CETI")
    print("==========================================")

# Uso (invocación) función sin argumentos
saluda()
saluda()
for i in range(1,3):
    saluda() """

# Definición función con 1 argumento

""" 
#  Nota: end="" modifica  terminador de print y evita el salto de línea
def linea(longitud):
    for x in range(longitud):
        print("*", end="")
    print()

# uso de función con 1 argumentos
linea(20)
linea(40)
linea(5)

""" 
# función con 2 argumentos: número y carácter

"""
def lineaV1(longitud, letra="*"):
    for x in range(longitud):
        print(letra, end="")
    print()

# uso de función con 2 argumentos (respetar orden)
lineaV1(20, "#")
lineaV1(40, "%")
lineaV1(5, "@")
""" 

# Prueba de llamadas con nombres de argumentos

"""
def lineaV3(longitud, letra):
    for x in range(longitud):
        print(letra, end="")
    print()

lineaV3(letra="*",longitud=10)
lineaV3(longitud=10, letra="*")
lineaV3(10, "*")
"""

## con argumento con valor por defecto
"""
def lineaV2(longitud, letra="*"):
    for x in range(longitud):
        print(letra, end="")
    print()

lineaV2(25,"&")
lineaV2(70) # sólo un parámetro => el segundo el valor por defecto 
"""

# función que DEVUELVE COMO RESULTADO la suma de valores de una lista
""" def sumaLista(lista):
    suma = 0
    for x in lista:
        suma += x 
    return suma

ventas = [1,2,3,4]
ventasTotales = sumaLista(ventas)
print("ventas:", ventas)
print("ventasTotales:", ventasTotales)
"""

# función que DEVUELVE COMO RESULTADO la media USANDO LA FUNCIÓN sumaLista 
"""
def media(lista):
    return sumaLista(lista)/len(lista)

edades = [23, 46, 56, 72, 12, 34]
print("edades:", edades)
print("sumaLista(edades):", sumaLista(edades))
print("media(edades):", media(edades)) """


# función que recibe diccionario y lo imprime

""" def muestraDicc(dic):
    # print(dic)
    # print(type(dic))
    for x in dic:
        print(x, dic[x], sep="\t") # print(x, dic[x], sep=":")

coche =  {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
    "kilometros": 125000
}

muestraDicc(coche)
muestraDicc({"nombre": "Ana", "cargo": "manager"}) 
"""
     

# funciones: en interior se modifica argumento lista o diccionario 

""" def modifica(lista):
    lista[0] = 1000;

datos = [1,2,3,4,5]
print(datos)
modifica(datos)
print(datos)

# función que modifica un diccionario

def mod(dicc):
    dicc["color"] = "rosa";

coche =  {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
}

print(coche)
mod(coche)
print(coche)  
"""

# función que recibe cadena o entero: no los modifica
#  objetos inmutables vs mutables
def test(edad, nombre):
    edad = edad +1
    nombre = "anónimo"
    print("dentro de test:", edad, nombre)

edad = 24
nombre= "Alfredo"
test(edad, nombre)
print("fuera de test:", edad, nombre)
""" 
Mutable objects in Python are those that can be changed after they are created, 
like lists or dictionaries. Immutable objects, on the other hand, cannot be changed after 
they are created, such as strings, integers, or tuples. 
"""

# uso de una función identificando el  parámetro
#  => en print identificamos end o sep

""" 
# Test: probando parámetro separador en print
print(1,2,3)
print(1,2,3, sep="")
print(1,2,3, sep="-")
# Test: probando parámetro end en print
print("Hola")
print("Mundo")
print("Hola", end="")
print(" mundo") 
"""




