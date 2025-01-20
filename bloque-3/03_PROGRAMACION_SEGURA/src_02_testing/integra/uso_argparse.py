# uso_argparse.py
import argparse

# Crea el objeto que almacenará los argumemtos
parser = argparse.ArgumentParser()

# Añade argumetos con nombre, tipo y ayuda
parser.add_argument('opera', type=str, help='operación matemática: suma|resta|multiplica|divide')
parser.add_argument('num1', type=int, help='primer operando')
parser.add_argument('num2', type=int, help='segundo operando')

# Analiza los argumentos
arguments = parser.parse_args()

# Acceso a los argumentos por su nombre
print(arguments.opera, arguments.num1, arguments.num2)


