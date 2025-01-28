
def procesa(operacion:str, cadena:str) -> str:
  
    if operacion == "cuenta":
        res = cuentaVocales(cadena)
    elif operacion == "limpia":
        res = limpia(cadena)
    else:
        res = "Operación no permitida"
    
    return res

# Cuenta las vocales, da igual mayúsculas o minússculas
def cuentaVocales(cadena:str)->int:
    if not cadena:
        return None
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    
    return contador

# limpia debe eliminar los  
#  - espacios en blanco
#  -  signos de puntuación 
def limpia(cadena:str)->str:
    if not cadena:
        return None
    
    from re import sub
    cadena = cadena.replace(" ", "")
    return sub(r'[^\w\s]','',cadena)
