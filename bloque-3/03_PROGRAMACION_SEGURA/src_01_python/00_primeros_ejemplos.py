# Ejemplos iniciales de clase intro Python

# Comentario de línea

""" Comentario 
de 
bloque  """

# Variables, asignación (=) y tipos (int, float, str...) 
""" 
saldo_total = 254.55  # float
email = 'ana@local.com'  # str
print( saldo_total )
#  print(email)   # descomentar para ver erro indentación
print( type(email)  )
print( type(saldo_total)  )

print("El email es ", email, " y el saldo es ", saldo_total) 

 """

"""
# lógica o booleana
autorizado = True    # el otro valor posible False
print( type(autorizado)  )
if (autorizado==True) :  # autorizado==True <=> autorizado 
    print("Puede pasar")
"""

# conversión de tipos
""" texto = "33"
x = int(texto)
y = int(3)
z = 5
print(texto, type(texto))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print("suma  x (33) y z(5): ", x+z)

# el operador + y string: Concatena, no suma..
incremento = "1"
print (texto+incremento) """

# Lectura de valores con input
""" notaExamen = input("Nota examen (0-10):");
print("notaExamen:", notaExamen)
notaTrabajos = input("Nota Trabajo (entre 0 y 1):");
notaFinal = notaExamen + notaTrabajos;
print("Nota Final:", notaFinal)
# Probar con nota 1 y trabajos 0. ¡¡Corregir!!
# print("Tipo: ", type(notaExamen))
# Convertir a números float) antes de sumar !! """

## Selectiva simple (y  probar indentación)
""" 
# edad = int(input("¿Edad?"))
edad = 15 
  print( type(edad) ) ## Error indentación

if  edad >= 18:  # selectiva
    print("Adulto")
        print("puede jugar") ## Error indentación

print("¡Hola CETI!")

 """

# Ejemplo selectiva if-else y condición lógica con and
""" 
saldo = 100
edad = 16

if edad >= 18 and saldo > 0:
    print("Puede jugar")
else:
    print("no puede jugar")

"""

# Ejemplo selectiva anidadas
""" 
a = int(input("valor de a:"))
b = 200

if b > a:
    print("b es mayor que a")
else: 
    if b<a:
        print("a es mayor que b")
    else:
        print("son iguales") 

# lo mismo con elif, más legible/compacto
if b > a:
    print("b is greater than a")
elif b<a:
    print("a es mayorr que b")
else:
    print("son iguales") 
"""

# Ejemplo uso format en print
""" nombre = "Alfredo Zumberg"
edad = 23
altura = 1.915
print(nombre, "su edad es", edad, "y altura", altura)
# con format
print(f"{nombre} su edad es {edad} y altura {altura:.1f}") """


# Algunos métodos de string

""" saludo = "Hola Mundo"
print("saludo:", saludo)
print("saludo,lower():", saludo.lower())
print("saludo:", saludo)
# No modifica cadena oreiginal. 
#  Si queremos modificar hace falta asignación
saludo = saludo.lower()
print("saludo:", saludo)
# Replace, lo mismo..
print("saludo.replace():", saludo.replace("mundo", "universo"))
print("saludo:", saludo) """

# str como array, longitud o tamaño del str
""" saludo ="¡Hola mundo!"
print("Primer carácter:", saludo[0])
print("Segundo carácter:",saludo[1])
print("Longitud saludo:", len(saludo)) """

# Buscar en un str: in y not in


""" texto = "The best thiNgs  life are free!"
busca = "FREE"

if busca in texto():
    print("¡¡Sí está!!")
else:
    print("No está")
# o en negativo
if busca not in texto:
    print("No está")
else:
    print("¡¡Sí está!!") 
# Proponer: no case sensitive
"""
 
# Concatenar str

nombre = "Raquel"
apellidos = "García Ross"
print(nombre + " " + apellidos) 

nombreCompleto = apellidos + ", " + nombre
print(nombreCompleto)

# Recorrer str
for x in nombre:
    print(x)
    
# con índices
for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")



