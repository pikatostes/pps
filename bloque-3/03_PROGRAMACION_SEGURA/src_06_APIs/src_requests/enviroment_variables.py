import os

# Ejemplo a partir de 
#    https://www.twilio.com/blog/environment-variables-python

# Accediendo a variables de entorno del SO
# print(os.environ)
print(os.environ.get("SHELL"))
print(os.environ.get("USER"))
print(os.environ.get("TOKEN"))


# Accediendo a variables de entorno creadas por el usuario para 
#  la aplicación
# Antes  creamos la variable de entrono
#   ejecutamos $ export TOKEN=1234567890
print(os.environ.get("TOKEN"))

# Dos formas de acceder para tratar qué ocurre si no existe
# print(os.environ.get("CLAVE")) # => devuelve None
# print(os.environ["CLAVE"]) # => genera excepción

# Si no existe podemos darle un Valor POR defecto
# database_url = os.environ.get('DATABASE_URL', 'sqlite://')
# print(database_url)
# similar: os.getenv('DATABASE_URL', 'sqlite://')

