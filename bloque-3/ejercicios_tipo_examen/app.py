import argparse

from procesa import procesa

# Crea el objeto que almacenará los argumemtos
parser = argparse.ArgumentParser()

# Añade argumetos con nombre, tipo y ayuda
parser.add_argument('opera', type=str, help='operación: cuenta | limpia')
parser.add_argument('cadena', type=str, help='cadena a procesar')

# Analiza los argumentos
arguments = parser.parse_args()
res = procesa(arguments.opera, arguments.cadena)
print(">", res)
# print(f"Resultado de <{arguments.opera}> sobre <{arguments.cadena}> es: {res}") 