import os
from dotenv import load_dotenv
from dotenv import dotenv_values

# Ejemplos tomados de
#   https://www.twilio.com/blog/environment-variables-python
#   https://pypi.org/project/python-dotenv/

# se usa fichero .env => si hay información sensible usar .gitignore en git
"""But if you cannot commit the .env file, how do you tell users of the project 
which variables need to be set? 
For this you can add an example .env file to your repository with a name such 
as .env.example, that contains the list of variables that the project requires, 
but without including their values. This serves as guidance for users of your project, 
without giving away sensitive information.
"""

# contenido de .env
# TOKEN=12345678901234567890
# DATABASE_URL=sqlite:///mydb.sqlite


load_dotenv()  # o load_dotenv("<file>")
"""The load_dotenv() function will look for a file named .env in the current directory
and will add all the variable definitions in it to the os.environ dictionary"""
""" By default, load_dotenv doesn't override existing environment variables.
If you want to prevent python-dotenv from searching for a .env file through your directories, you can pass an explicit path to your file as an argument to load_dotenv() """

debug = os.environ.get("TOKEN")
print(debug)
print(os.environ.get("DATABASE_URL"))

# otra forma: no incorporamos la lectura diccionario con las varibles de entorno 
# en su lugar el contenido se almacena en una variable de tipo diccionario
# The function dotenv_values works more or less the same way as load_dotenv,
# except it doesn't touch the environment, it just returns a dict with
# the values parsed from the .env file.
config = dotenv_values(".env")
# print(config)
print(config["TOKEN"])
print(config["DATABASE_URL"])
