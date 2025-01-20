def saluda(name):
    """ Funcion que saluda con parametro nombre."""
    print(f"Hola {name}. ¡Te damos la bienvenida!")

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero
    
    pass