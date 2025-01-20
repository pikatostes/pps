import json

# Volcar diccionario a fichero JSON
data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        }
    ]
}


print("type(data):", type(data))
print("data:", json.dumps(data, indent=2))

# usamos dump (sin s) para volcar diccionario a fichero
file = input("Nombre fichero: ")
with open(file, 'w') as outfile:
    json.dump(data, outfile)

# Ver fichero de salida con 
#    $ cat datos.json | json_pp 