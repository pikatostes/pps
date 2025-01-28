# modulo_inventario.py
# import io

def agregar_producto(inventario, producto, cantidad):
    """
    Agrega una cantidad de un producto al inventario.
    
    Comprueba que la cantidad sea mayor a 0. Si el producto ya existe, suma la cantidad al producto. Si no existe, crea el producto con la cantidad.
    
    Args:
        inventario (dict): El inventario.
        producto (str): El nombre del producto.
        cantidad (int): La cantidad de productos a agregar.
    
    Returns:
        dict: El inventario actualizado.
    
    Raises:
        ValueError: Si la cantidad es menor o igual a 0.
        KeyError: Si el producto ya existe en el inventario.
    
    Example:
        >>> inventario = {'manzanas': 2, 'peras': 1}
        >>> agregar_producto(inventario, 'manzanas', 3)
        {'manzanas': 5, 'peras': 1}
        >>> agregar_producto(inventario, 'naranjas', 4)
        {'manzanas': 5, 'peras': 1, 'naranjas': 4}
    """
    # debug = False
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

    return inventario


def eliminar_producto(inventario, producto, cantidad):
    """
    Elimina una cantidad de un producto del inventario.
    
    Comprueba que la cantidad sea menor o igual a la existencia del producto. Si la cantidad es mayor, resta la cantidad del producto. Si la cantidad es menor o igual a 0, elimina el producto.
    
    Args:
        inventario (dict): El inventario.
        producto (str): El nombre del producto.
        cantidad (int): La cantidad de productos a eliminar.
    
    Returns:
        dict: El inventario actualizado.
    
    Raises:
        ValueError: Si la cantidad es mayor que la existencia del producto.
        KeyError: Si el producto no existe en el inventario.
    
    Example:
        >>> inventario = {'manzanas': 2, 'peras': 1}
        >>> eliminar_producto(inventario, 'manzanas', 3)
        {'peras': 1}
        >>> eliminar_producto(inventario, 'naranjas', 4)
        {'manzanas': 2, 'peras': 1}
    """
    if producto not in inventario:
        raise KeyError(f"El producto '{producto}' no existe en el inventario.")
    if cantidad > inventario[producto]:
        txt = f"No hay bastante existencias de {producto}."
        raise ValueError(txt)
    inventario[producto] -= cantidad
    if inventario[producto] == 0:
        del inventario[producto]

    return inventario


def consultar_producto(inventario, producto):
    """
    Devuelve la cantidad de un producto en el inventario.
    
    Args:
        inventario (dict): El inventario.
        producto (str): El nombre del producto.
    
    Returns:
        int: La cantidad de productos en el inventario.
    
    Raises:
        KeyError: Si el producto no existe en el inventario.
    
    Example:
        >>> inventario = {'manzanas': 2, 'peras': 1}
        >>> consultar_producto(inventario, 'manzanas')
        2
    """
    # Devuelve la cantidad de producto
    # o 0 si no está en inventario
    return inventario.get(producto, 0)


def listar_inventario(inventario):
    """
    Listar el inventario.
    
    Args:
        inventario (dict): El inventario.
    
    Returns:
        dict: El inventario.
    
    Example:
        >>> inventario = {'manzanas': 2, 'peras': 1}
        >>> listar_inventario(inventario)
        {'manzanas': 2, 'peras': 1}
    """
    return inventario


if __name__ == "__main__":
    inventario = {
        "manzanas": 10,
        "naranjas": 5
    }
    print(consultar_producto(inventario, "naranjas"))
    print(consultar_producto(inventario, "peras"))
