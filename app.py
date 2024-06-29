import Productos

def menu():
    while True:
        print("1. Registrar producto")
        print("2. Listar todos los productos")
        print("3. Buscar productos por categoría")
        print("4. Calcular el precio promedio de los productos")
        print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                 Productos.agregar_productos()
            elif opcion == 2:
                    Productos.listar_productos()
            elif opcion == 3:
                    Productos.buscar_producto()
            elif opcion == 4:
                    Productos.calcular
            elif opcion == 5:
                    Productos.guardar_productos()
                        print("¡Gracias por usar el programa!")
                            break
                else:
                    print("Opción no válida, intente de nuevo.")
                    except ValueError:
                        print("Error: Ingrese un número válido.")

if __name__ == "__main__"
    menu()
