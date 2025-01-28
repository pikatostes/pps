# main.py
import argparse

from inventario import agregar_producto, eliminar_producto
from inventario import consultar_producto, listar_inventario

def main():
    """
    Programa principal para gestionar un inventario.
    
    Usa la biblioteca `argparse` para procesar los argumentos de la línea de comandos. Importa las funciones de inventario.py para realizar las acciones de gestión. Las acciones disponibles son `agregar`, `eliminar`, `consultar` y `listar`.
    
    Ejemplos:
        ```$ python main.py consultar --producto manzanas```
    
        ```$ python main.py agregar --producto manzanas --cantidad 5```
        
        ```$ python main.py eliminar --producto manzanas --cantidad 2```
        
        ```$ python main.py listar```
    """
    # Crear un objeto parser
    parser = argparse.ArgumentParser(description="Gestión inventario.")

    # Con choice dammos las valores permitidos
    parser.add_argument("accion", choices=["agregar", "eliminar", "consultar",
                        "listar"], help="Acción a realizar.")
    # Paráemtros "con nombre", pueden aparecer en cualquier orden 
    parser.add_argument("--producto", type=str, help="Nombre del producto.")
    parser.add_argument("--cantidad", type=int, help="Cantidad del producto.")

    # Parsear los argumentos
    args = parser.parse_args()
    accion = args.accion
    producto = args.producto
    cantidad = args.cantidad

    # Inventario inicial
    inventario = {
        'manzanas': 2,
        'peras': 1,
    }

    # Realizar la acción
    try:
        print("Inventario inicial: ", inventario)
        if accion == "agregar":
            # Si no se especifica producto o cantidad
            if not producto or cantidad is None:
                # Lanzar una excepción
                print("antes de la excepción")
                raise ValueError("Especificar producto y cantidad.")

            # global inventario
            
            inventario = agregar_producto(inventario,producto, cantidad)
            print(f"Producto agregado: {producto} ({cantidad}).")

        # Si la acción es eliminar
        elif accion == "eliminar":
            # Si no se especifica producto o cantidad
            if not producto or cantidad is None:
                # Lanzar una excepción
                raise ValueError("Especificar producto y antidad a eliminar.")
            inventario = eliminar_producto(inventario, producto, cantidad)
            # Mostrar inventario actualizado
            print(f"Producto eliminado: {producto} ({cantidad}).")

        # Si la acción es consultar
        elif accion == "consultar":
            # Si no se especifica producto
            if not producto:
                # Lanzar una excepción
                raise ValueError("Especificar producto para consultar.")
            cantidad_disponible = consultar_producto(inventario, producto)
            # Mostrar cantidad disponible
            print(f"Cantidad de '{producto}': {cantidad_disponible}")

        # Si la acción es listar
        elif accion == "listar":
            productos = listar_inventario(inventario)
            if productos:
                print("Inventario actual:")
                # Mostrar productos y cantidades con formato
                for prod, cant in productos.items():
                    print(f"- {prod}: {cant}")
            else:
                print("El inventario está vacío.")
        print("Inventario final: ", inventario)
    # Capturar excepciones
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
