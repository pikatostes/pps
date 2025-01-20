# funciones.py

def suma(lista):
    res = 0
    for x in lista:
        res += x
    return res

def calcula_media(lista):
    return (suma(lista)/len(lista))


if __name__ == "__main__":
    valores = [1,2,3,4]
    print(suma(valores))
    print(calcula_media(valores))