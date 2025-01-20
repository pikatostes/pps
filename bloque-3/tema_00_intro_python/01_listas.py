# Definir lista y uso básico

""" lista = ["Jerez", "Sevilla", "Huelva"]
# mostar toda la lista y su tipo
print(lista)
print(type(lista))
# mostrar un elemento
print(lista[0])
# mostrar el tamaño (longitud)
print("Nº de elementos de la lista:", len(lista))
 """
# Ejemplos uso de lista

""" thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist", thislist)
# mostrar un rango
print("thislist[1:4]", thislist[1:4])

# generar nueva lista a partir de un rango
nueva_lista = thislist[1:4]
print("nueva_lista", nueva_lista)

# imprimir el último
print("thislist[len(thislist)-1]", thislist[len(thislist)-1])

# modificar un elemento
print("Elemento 0: ", thislist[0])
print('ejecutamos thislist[0]="watermelon"')
thislist[0]="watermelon"
print("Elemento 0: ", thislist[0])
 """


# lista vacía y longitud

""" lista = [1,2] 
print("lista: ",lista)
print("len(lista):", len(lista))
if lista: # if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía") 

lista = []  
print("lista: ",lista)
print("len(lista):", len(lista))
if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía")   """ 



# Ejemplos formas de recorrer lista


# lista = ["Jerez", "Sevilla", "Huelva"]

# # los elementos con for
# for x in lista:
#     print("Hola ", x)


# # los elementos y sus índices con for
# for i in range(len(lista)):
#     print(i, lista[i])

# # comprensión de listas: [expresión for elemento in iterable]
# [print(x) for x in lista] 



# Convertir string en lista: split

""" users = "ana:luis:alfredo"
lista = users.split(":")
print("users:", users)
print("type(users)", type(users))
print("lista: ", lista)
print("type(lista)", type(lista))
 """

# Ejemplo lectura input y conversión a lista

""" lectura = input("Notas separadas por el caracter ':'" )
print(lectura, type(lectura))

notas = lectura.split(":")
print(notas, type(notas))

suma = 0 # Almacena la suma de las notas
media = 0

for x in notas:
    suma = suma + int(x)

media = suma/len(notas)

print("Suma: ", suma)
print(f"Media: {media:.2f}") """


# Nota: la conversión a enteros de la lista se puede 
#   hacer con map o con compresión

# comprensión de listas
""" edades = ["14", "21", "17", "33", "45"]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0]):", type(edades[0]))
edades =  [int(x) for x in edades]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0]):", type(edades[0])) """

# método map. ojo que no es una lista, hay que convertirla
""" edades = ["14", "21", "17", "33", "45"]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0])", type(edades[0]))
edades = map(int, edades) 
print("edades:", edades, "tipo:", type(edades))
edades = list(map(int, edades))
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0])", type(edades[0]))
 """

# Buscar 

# Buscar con in => True/False

""" thislist = ["apple", "banana", "cherry"]
print("thislist", thislist)
buscar = input("Fruta a buscar: ")

if buscar.lower() in thislist:
    print(f"Yes, {buscar} is in the fruits list") 
else:
    print(f"No, {buscar} no está")
 """
# Buscar el índice 
""" thislist = ["apple", "banana", "cherry"]
print("thislist", thislist)
buscar = input("Fruta a buscar: ")

# Genera excepción si no está en la lista
# pos = thislist.index(buscar) 
# Se añade bloque try/except  para evitarlo
# hay otras opciones: usar in o count antes de index
try:
    pos = thislist.index(buscar) 
    print(f"{buscar} está en la posición {pos}") 
except ValueError:
    print("That item does not exist") """

    
## TODO:
# - ordenar listas: sort ,reverse
edades = [19, 17, 23, 56, 48, 100, 31]

""" 
print("edades:", edades)
edades.sort()
print("edades tras edades.sort():", edades)
edades.reverse()
print("edades tras edades.reverse():", edades) """

# añadir al final
""" print("edades:", edades)
edades.append(20)
print("edades tras edades.append(20):", edades)

# añadir en cualquier posición: The insert() method inserts an element to the list at the specified index.
edades.insert(1, 44)
print("edades tras edades.insert(1,44):", edades)

# The list pop() method removes the item at the specified index. The method also returns the removed item.
eliminado = edades.pop() # Si no hay index extrae el último
print("edades tras eliminado = edades.pop()", edades)
print("eliminado:", eliminado )

eliminado = edades.pop(0)
print("edades tras eliminado = edades.pop(0)", edades)
print("eliminado:", eliminado )
 """
# The clear() method empties the list.