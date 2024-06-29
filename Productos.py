
import random
import math
import json
# creamos una lista para los productos
productos = []

#definimos "Generar_precio" para que cuando eligan esta opcion haga lo que esta dentro de la funcion
def generar_precio():
    return random.randint(1, 1000)
# Aqui se agregaran los productos, se generará el precio, inresaran nombre, cantidad y categoria.
def agregar_productos():
    precio = generar_precio()
    nombre = input("Ingrese el nombre del producto: ")
    cant = int(input("Ingrese la cantidad del producto: "))
    categoria = input("Ingrese la categoría del producto: ")
# Creamos un diccionario para que en el txt se vea ordenado (No me acuerdo como hacerlo como en la imagen :c  ).
producto = {
    "Precio": precio,
    "nombre": nombre,
    "cantidad": cant,
    "categoria": categoria,
}
# Aqui el producto se agregara a la lista productos. 
productos[precio] = Producto
    print("Producto agregado exitosamente!")
# Aqui se listaran los productos pero si no hay productos imprimira "No hay productos registrados."
def listar_productos():
    if not Productos:
        print("No hay productos registrados.")
        return
    
 for precio, productos in productos.items():
        print(f"Precio: {precio}")
        print(f"Nombre: {productos['nombre']}")
        print(f"Cantidad: {productos['cantidad']}")
        print(f"Categoría: {productos['categoria']}")
        print()
# Este es para buscar la categoria de un producto por eso realizamos las siguientes funciones.
def buscar_producto():
    categoria = input("Ingrese la categoría del producto a buscar: ")
    encontradas = [producto for producto in productos.values() if producto['categoria'] == categoria]
# Realizamos un if por si no se han encontrado productos de esa categoria, pero si no, imprimira el producto encontrado
if not encontradas:
        print("No se encontraron productos en esa categoría.")
    else:
        for producto in encontradas:
            print(f"Precio: {precio}")
            print(f"Nombre: {productos['nombre']}")
            print(f"Cantidad: {productos['cantidad']}")
            print(f"Categoría: {productos['categoria']}")
            print()
#Y en este ultimo bloque se guardaran todos los productos
def guardar_peliculas():
    with open('productos.txt', 'w') as file:
        for pelicula in peliculas.values():
            file.write(f"Precio: {precio}\n")
            file.write(f"Nombre: {productos['nombre']}\n")
            file.write(f"Cantidad: {productos['cantidad']}\n")
            file.write(f"Categoría: {productos['categoria']}\n")

 print("Productos agregados en Productos.txt")
