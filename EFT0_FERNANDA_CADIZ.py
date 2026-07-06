import os

def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio 
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================""")

def leer_opcion():
    while True:
        try:
            opcion = int(input(">"))
            if 1 > opcion > 7:
                return opcion
            else:
                print("Error, opcion invalida")
        except ValueError:
            print("Error, el valor debe ser un numero.")

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio >= 0

def validar_disponible(opcion):
    if opcion == "s":
        return True
    elif opcion == "f":
        return False
    else:
        -1

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass