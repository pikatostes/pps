# Módulos en python

Un módulo no es más que un fichero que contiene instrucciones y definiciones (variables, funciones, clases, …). 

El fichero:
* debe tener extensión `.py`
* y su nombre se corresponde con el nombre del módulo.

# Ejemplo básico

Tenemos el fichero `calculadora.py`

```python
# calculadora.py
def suma(a,b):
    return a+b 

def resta(a,b):
    return a-b

def media(a,b)
    return (a+b)/2
```

Para usar este módulo en un programa tenemos varias opciones. Supongamos que nuestro  programa pide dos números para  operar con ellos:

```python
# mi_programa.py
a = int(input("operando 1: "))
b = int(input("operando 2: "))
...
```

Tenemos dos opciones apra usar el módulo calculadora:

* Opción 1: Importamos el módulo entero, y accedemos a las funciones usando el nomber del módul0
    ```python
    import calculadora    # Se importa el módulo

    ...

    #  Para usar las funciones necesito el nombre del módulo
    print(f"suma({a},{b}) = ", calculadora.suma(a,b))
    print(f"resta({a},{b}) = ", calculadora.resta(a,b)) 
    ```

* Opción 2: importar sólo las funciones que se usanm y podemos usar directamente el nombre de la función:
    ```python
    from calculadora import suma, resta # importa las funciones

    ...

    #  Para usar las funciones no necesito el nombre del módulo
    print(f"suma({a},{b}) = ", suma(a,b))
    print(f"resta({a},{b}) = ", resta(a,b))
    ```
* Opción 2.5: Incluso se pueden renombrar las funciones

    ```python
    from calculadora import suma as miSuma, resta as r

    ...

    print(f"miSuma({a},{b}) = ", miSuma(a,b)) 
    print(f"r({a},{b}) = ", r(a,b)) 
    ```

## Ejecutar módulos como scripts

Un módulo puede ser ejecutado como un script o punto de entrada de un programa cuando se pasa directamente como parámetro al intérprete de Python:

    ```
    $ python3 calculadora.py 
    Probando funciones modulo calculadora
    suma(11,7)= 18
    resta(11,7)= 4
    $
    ```

Cuando esto ocurre el código del módulo se ejecuta como si se hubiera importado, con la particularidad de que el nombre del módulo, `__name__,` toma el valor `__main__`. Esto hace  interesante añadir al final del módulo las siguientes líneas de código que solo se ejecutarán en caso de que dicho módulo se haya ejecutado como el principal:

```python
...
if __name__ == "__main__":
    print("suma(11,7)=", suma(11,7))
    print("resta(11,7)=", resta(11,7))
```

Estas líneas no se ejecutan en caso de que el módulo se importe en vez de invocarse directamente ya que el valor de la variabel `__name__` será el nombre del módulo.

## Paquetes en Python

Del mismo modo en que agrupamos las funciones y demás definiciones en módulos, los paquetes en Python permiten organizar y estructurar de forma jerárquica los diferentes módulos que componen un programa. Además, los paquetes hacen posible que existan varios módulos con el mismo nombre y que no se produzcan errores.

Un paquete es simplemente un directorio que contiene otros paquetes y módulos. Si seguimos con el ejemplo de la calculadora, cree un directorio `utiles` y mueva allí el fichero `calculadora.py`. En este caso 

* Para importar el módulo indicamos su ruta, y para invocar las funciones también usamos la ruta:

    ```python
    import utiles.calculadora
    print(f"suma({a},{b}) = ", utiles.calculadora.suma(a,b))
    print(f"resta({a},{b}) = ", utiles.calculadora.resta(a,b)) 
    ```

* O podríamos importar las funciones concretas a utilizar:

    ```python
    from utiles.calculadora import suma
    print(f"suma({a},{b}) = ", suma(a,b)) 
    ```


