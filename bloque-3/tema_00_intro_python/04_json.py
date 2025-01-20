import json  # https://www.w3schools.com/python/python_json.asp

# ejemplo uso de bibliotecas

# ejemplos paso de diccionario a string JSON y viceversa
# Datos JSON que podrían venir de una API
jsondata =  '{ "name":"John", "age":30, "city":"New York"}'

#  pasamos de string JSON a diccionario. 
## Ojo existe load y loads, la s de string, sin al s fichero...
data = json.loads(jsondata)

print("type(jsondata):", type(jsondata))
print("jsondata:", jsondata)

print("type(data):", type(data))
print("data:",  data)

# impresión con formato
print( json.dumps(data, indent=4) )  
# print("json.dumps(data, indent=4):", json.dumps(data, indent=4))  


# En sentido contrario: un diccionario a JSON 

# a Python object (dict):
persona = {
  "name": "Anne",
  "age": 24,
  "city": "Boston"
}

# convert into JSON:
cadenaJSON = json.dumps(persona)

# the result is a JSON string:
print("type(persona):", type(persona))
print("persona:", persona)
print("persona, indent=2):",json.dumps(persona, indent=2))  
print("type(cadenaJSON):", type(cadenaJSON)) 
print("cadenaJSON:", cadenaJSON) 
