# calculadora.py

def suma(a,b):
    return a+b 

def resta(a,b):
    return a-b

def mediaLista(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma/len(lista)

def otras(lista):    
    pass

# print("__name__:", __name__)

if __name__ == "__main__":
    print("Probando funciones modulo calculadora")
    print("__name__:", __name__)
    print("suma(11,7)=", suma(11,7))
    print("resta(11,7)=", resta(11,7))
    print("mediaLista([1,2,3,4])=", mediaLista([1,2,3,4]))

""" # Líneas para probar las funciones  si no usara __name__
print("Probando funciones")
print("suma(11,7)=", suma(11,7))
print("resta(11,7)=", resta(11,7))
print("mediaLista([1,2,3,4])=", mediaLista([1,2,3,4])) """