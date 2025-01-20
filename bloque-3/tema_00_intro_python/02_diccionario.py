
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

coche =  {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
    "kilometros": 125000
}

# muestro el diccionario completo
print("coche:", coche)

# muestro un elemento
print('coche["color"]:', coche["color"])
print('coche["kilometros"]:', coche["kilometros"])
#usando get
print('coche.get("modelo"):', coche.get("modelo"))

# Recorro los valores del diccionario y sus claves
print("Bucle for que recorre diccionario")
for x in coche:
    print(" *", x,"=>", coche[x])

# Modificar de dos formas
coche["color"] = "gris"
coche.update({"kilometros": 99999}) 
print("coche tras modificaciones:", coche)

# Añadir nuevas claves
coche["taller"] = "Alterio reparaciones"
print("coche tras añadir clave:", coche)

# values() y keys() 
valores = coche.values()
print("valores:", valores)
keys = coche.keys()
print("keys:", keys)

# las variables se actulizan tras cambios
print('Se añade precio: coche["precio"] = 17000')
coche["precio"] = 17000
print("valores:", valores)
print("keys:", keys)

# Otros métodos: ....