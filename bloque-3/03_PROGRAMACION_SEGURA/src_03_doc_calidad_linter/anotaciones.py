# función 
def hello(name):
    return(f"Hello {name}")

#funciones con tipos de parámetros y tipo de retorno --> str
def hello_name(name: str) -> str:
    return(f"Hello {name}")

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

# Invocaciones correctas e "incorrectas según anotaciones"
print(hello("Ana"))
print(hello_name("Ana"))
print(headline(" lorem ipsum"))
print(headline(" lorem ipsum", False))
print(headline(" lorem ipsum", "testing"))
print(hello_name(123))
print(hello_name(False))