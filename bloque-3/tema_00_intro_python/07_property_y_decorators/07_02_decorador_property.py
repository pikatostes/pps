# Clases y uso de property (función o decoradores) (II)
#   Acceder a los atributos a través de las propiedades
#   - uso del decorador @property

# Python program showing the use of decorator @property
#  + sobre decorators: https://www.geeksforgeeks.org/decorators-in-python/

# Similar al ejemplo de uso la función property usando ahora  decoradores

class Geeks:
	def __init__(self):
		self._age = 0
	
	# using property decorator
	# el nombre de la función será la propiedad expuesta
	#   (no tiene porque coincidir con el atributo)
	@property  # getter function
	def edad(self):
		print(" > getter method called")
		return self._age
	
	# setter function
	@edad.setter
	def edad(self, a):
		print(" > setter method called value", a)
		if a > 0:
			self._age = a
		else:
			print(" > setter warning: age no update to", a)
	
	# a deletter function			
	@edad.deleter
	def edad(self):
		print(" > deletter method called")
		del self._age


mark = Geeks()

mark.edad = 21  # seter
print(mark.edad) # getter

mark.edad = -5  # seter value out of range
print(mark.edad) # getter

print(mark.__dict__)
del mark.edad
print(mark.__dict__)