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
            if 1 <= opcion <= 7:
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

def stock_categoria(categoria,productos, inventario):
    total_stock = 0
    encontrado = False
    for codigo in productos:
        categoria_producto = productos[codigo][1]
        if categoria_producto.lower() == categoria.lower():
            encontrado = True
            stock_producto = inventario[codigo][0]
            total_stock += stock_producto
    if encontrado == False:
        print("Categoria no encontrada")
    else:
        print(f"Stock total: {total_stock}")

def ejecutar_stock_categoria(productos, inventario):
    if len(productos) == 0:
        print("No hay productos para mostrar.")
    else:
        while True:
                categoria = input("Ingrese categoria:\n>").strip()
                if not validar_categoria(categoria):
                    print("Categoria no puede estart vacia.")
                else:
                    break
                stock_categoria(categoria, productos, inventario)

def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []
    for codigo in productos:
        nombre = productos[codigo][0]
        precio = productos[codigo][2]
        stock = inventario[codigo][0]
        if precio_min <= precio <= precio_max and stock > 0:
            resultados.append(nombre + "--" + codigo)
    
    resultados.sort()
    return resultados

def ejecutar_buscar_precio(productos, inventario):
    while True:
        try:
            precio_min = float(input("Ingrese precio minimo:\n"))
            if not validar_precio(precio_min):
                precio_min("Precio invalido.")
            else:
                break
        except ValueError:
            print("Error, precio debe ser un valor numerico.")
    while True:
        try:
            precio_max = float(input("Ingrese precio maximo:\n"))
            if not validar_precio(precio_max):
                print("Error, precio invalido")
            else:
                break
        except ValueError:
            print("Error, precio debe tener un valor numerico.")
    
    
    resultados = buscar_precio(precio_min, precio_max, productos, inventario)
    if len(resultados) > 0:
        print(f"Los productos encontrados son:\n{resultados}")
    else:
        print("No hay productos en ese rango de precio.")


def main():
    os.system("cls")
    #en el programa final este diccionario debe estar vacio
    #uso solo para pruebas
    productos = {
    "P101":["Cuaderno","Papelería",2490,True],
    "P102":["Lápiz","Papelería",590,True],
    "P103":["Botella","Accesorios",6990,False],
    "P104":["Mochila","Accesorios",24990,True]
    }
    #en el programa final este diccionario debe estar vacio
    #uso solo para pruebas
    inventario = { "P101":[30,15],
    "P102":[120,50],
    "P103":[0,10],
    "P104":[8,25]
    }


    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            ejecutar_stock_categoria(productos, inventario)
        elif opcion == 2:
            ejecutar_buscar_precio(productos, inventario)
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

main()