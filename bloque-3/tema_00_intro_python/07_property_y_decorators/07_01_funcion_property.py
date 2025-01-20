# Clases y uso de property (función o decoradores) (I)
#  Acceder a atributos a través de propiedades Getter & setter en Python:
#   - https://www.geeksforgeeks.org/getter-and-setter-in-python/
#   - https://www.hackertouch.com/difference-between-attributes-and-properties-in-python.html
#   - https://realpython.com/python-property/

""" 
Properties are unique attributes that contain getter, setter, and deleter methods. 
Python provides  property() function and the @property decorator, which can be used 
to define properties in Python code. 
"""

class Geeks:
	def __init__(self):
		self._age = 0
	
	# function to get value of _age
	def get_age(self):
		print(" > getter method called")
		return self._age
	
	# function to set value of _age
	def set_age(self, a):
		print(" > setter method called with value", a)
		self._age = a

	# function to delete _age attribute
	def del_age(self):
		print(" > del method called")
		del self._age

	# IMPORTANTE: esta sentencia asocia
	#   los accesos a la propiedad age con las funciones anteriores
	age = property(get_age, set_age, del_age)

# se crea objeto
mark = Geeks() 

print("Accedo a mark.age: ")
print(mark.age) # accedemos a la propiedad en modo lectura:  => get_age

print("Ejecuto mark.age = 10: ")
mark.age = 10   # accedemos a la propiedad en modo escritura: => set_age
print("Accedo a mark.age: ")
print(mark.age) # accedemos a la propiedad en modo lectura:  => get_age

print("Ejecuto del : mark.age ")
del mark.age    # borramos la propeidad: => del_age
