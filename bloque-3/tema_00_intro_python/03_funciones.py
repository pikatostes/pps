
# Definición función sin argumentos
# def saluda():
#     print("_________________________________________")
#     print("Hola CETI")
#     print("==========================================")


# # Uso (invocación) función sin argumentos
# saluda()
# print("mucho en medio...")
# saluda()
# for i in range(1,3):
#     saluda()




# Definición función con 1 argumento

#  Nota: end="" modifica  terminador de print y evita el salto de línea
""" def linea(longitud):
    for x in range(longitud):
        print("*", end="")
    print()

# uso de función con 1 argumentos
linea(20)
linea(40)
linea(5) """


# función con 2 argumentos: número y carácter


""" def lineaV1(longitud, letra="*"):
    for x in range(longitud):
        print(letra, end="")
    print()

# uso de función con 2 argumentos (respetar orden)
lineaV1(20, "#")
lineaV1(40, "%")
lineaV1(5, "@")
lineaV1(15) """
 

# Prueba de llamadas con nombres de argumentos


""" def lineaV3(longitud, letra):
    for x in range(longitud):
        print(letra, end="")
    print()

lineaV3(letra="*",longitud=10)
lineaV3(longitud=10, letra="*")
lineaV3(10, "*") """


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
        suma += x   # suma = suma + x
    return suma

ventas = [1,2,3,4,5]
print("suma: ", sumaLista(ventas))

ventasTotales = sumaLista(ventas)
print("ventas:", ventas)
print("ventasTotales:", ventasTotales)


# función que DEVUELVE COMO RESULTADO la media USANDO LA FUNCIÓN sumaLista 
def media(lista):
    media = sumaLista(lista)/len(lista)
    return media

edades = [23, 46, 56, 72, 12, 34]
print("edades:", edades)
print("sumaLista(edades):", sumaLista(edades))
print("media(edades):", media(edades))  """


# función que recibe diccionario y lo imprime

""" def muestraDicc(dic):
    print(dic)
    print(type(dic))
    for x in dic:
        print(x, dic[x], sep=" - ") # print(x, dic[x], sep=":")

coche =  {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
    "kilometros": 125000
}

muestraDicc(coche)
muestraDicc({"nombre": "Ana", "cargo": "manager"})  """

     

# funciones: en interior se modifica argumento lista o diccionario 

# modifico un entero : no se modifica...
""" def suma (x, y):
    x = x + y
    # return x

x = 10
y = 5
print(x,y)
x = suma(x,y)
print(x,y)

def modifica(lista):
    lista[0] = 1000;

datos = [1,2,3,4,5]
print(datos)
modifica(datos)
print(datos) """



# función que modifica un diccionario

""" def mod(dicc, colorNuevo):
    dicc["color"] = colorNuevo

coche =  {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
}

print(coche)
mod(coche, "azul")
print(coche)  

moto = {
    "marca": "Honda",
    "color": "negra"
}

print(moto)
mod(moto, "blanca")
print(moto)   """

# función que recibe cadena o entero: no los modifica
#  objetos inmutables vs mutables
""" def test(edad, nombre, adulto):
    edad = edad +1
    nombre = "anónimo"
    adulto = False
    print("dentro de test:", edad, nombre, adulto)

edad = 24
nombre= "Alfredo"
adulto = True
test(edad, nombre, adulto)
print("fuera de test:", edad, nombre, adulto) """

""" 
Mutable objects in Python are those that can be changed after they are created, 
like lists or dictionaries. Immutable objects, on the other hand, cannot be changed after 
they are created, such as strings, integers, or tuples. 
"""

# uso de una función identificando el  parámetro
#  => en print identificamos end o sep


# Test: probando parámetro separador en print
print(1,2,3)
print(1,2,3, sep="")
print(1,2,3, sep="\n")

# Test: probando parámetro end en print
print("Hola")
print("Mundo")
print("Hola", end=" ")
print("Mundo") 


# uso de *args y **kwargs
# https://j2logo.com/args-y-kwargs-en-python/
# https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
# https://ellibrodepython.com/args-kwargs-python


# def test_var_args(f_arg, *argv):
#     print("primer argumento normal:", f_arg)
#     for arg in argv:
#         print("argumentos de *argv:", arg)

# test_var_args('python', 'foo', 'bar')

# def saludame(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))

# >>> saludame(nombre="Covadonga")
# nombre = Covadonga

# def sum(*args):
#     value = 0
#     for n in args:
#         value += n
#     return value

# print(sum(1,2))
# print(sum(1,2,3))



# def greet(name="World", *args, **kwargs):
#     print(f"Hello, {name}!")
#     print("Arguments:", args)
#     print("Keyword Arguments:", kwargs)

# greet("Alice", 1, 2, color="blue", age=30)


