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

def validar_codigo_nuevo(productos, inventario, codigo):
    codigo = codigo.upper()
    return codigo != "" and codigo not in productos and codigo not in inventario

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio >= 0

def validar_disponible(opcion):
    if opcion.strip().lower() == "s":
        return True
    elif opcion.strip().lower() == "n":
        return False
    else:
        return -1

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

def buscar_codigo(productos, inventario, codigo):
    codigo = codigo.upper()
    
    if codigo in productos and codigo in inventario:
        return True
    return False

def actualizar_precio(productos, inventario, codigo, nuevo_precio):
    codigo = codigo.upper()
    if buscar_codigo(productos, inventario, codigo):
        inventario[codigo][0] = nuevo_precio
        return True
    return False

def ejecutar_actualizar_precio(productos, inventario):
    while True:
        codigo = input("Ingrese codigo del producto:\n> ").upper()
        if not validar_codigo(codigo):
            print("Error, codigo no puede estar vacio.")
        else:
            break
    while True:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio:\n> "))
            if not validar_precio(nuevo_precio):
                print("Precio no valido.")
            else:
                break
        except ValueError:
            print("Precio debe ser un valor numerico.")
    actualizado = actualizar_precio(productos, inventario, codigo, nuevo_precio)
    if actualizar_precio:
        print("Precio actualizado.")
    else:
        print("El codigo no existe.")

def agregar_producto(productos, inventario, codigo,nombre,categoria,precio,disponible, stock):
    codigo = codigo.upper()
    
    if not validar_codigo_nuevo(productos, inventario, codigo):
        return False
    if disponible == "s":
        disponible_booleano = True
    else:
        disponible_booleano = False

    productos[codigo] = [nombre, categoria, precio, disponible_booleano]
    inventario[codigo] = [precio, stock]
    return True

def ejecutar_agregar_productos(productos, inventario):
    while True:
        codigo = input("Ingrese codigo del producto:\n>").upper()
        if not validar_codigo(codigo):
            print("Error, codigo no puede estar vacio")
        else:
            break
    if not validar_codigo_nuevo(productos, inventario, codigo):
        print("Codigo ya existe")
        return
    while True:
        nombre = input("Ingrese nombre:\n> ")
        if not validar_nombre(nombre):
            print("Error, nombre no puede estaa vacio.")
        else:
            break
    while True:
        categoria = input("Ingrese categoria:\n> ")
        if not validar_categoria(categoria):
            print("Error categoria no puede estar vacia")
        else:
            break
    while True:
        try:
            precio = int(input("Ingrese precio:\n> "))
            if not validar_precio(precio):
                print("Error, precio invalido")
            else:
                break
        except ValueError:
            print("Precio deb tener un valor numerico")
    while True:
        try:
            stock = int(input("Ingrese stock:\n> "))
            if not validar_stock(stock):
                print("Error, stock invalido.")
            else:
                break
        except ValueError:
            print("Stock debe ser un numero.")
    while True:
        disponible = input("Esta disponible? [s : si | n : no]\n> ")
        disponible = validar_disponible(disponible)
        if disponible == -1:
            print("error, ingrese s o n ")
        else:
            break
    agregado = agregar_producto(productos, inventario,codigo, nombre, categoria, precio, disponible,stock)
    if agregado:
        print("Producto agregado")
    else:
        print("El codigo ya existe")

def eliminar_producto(productos, inventario, codigo):
    codigo = codigo.upper()
    if buscar_codigo(productos, inventario, codigo):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False

def ejecutar_eliminar_producto(productos, inventario):
    while True:
        codigo = input("Ingrese codigo del producto a eliminar:\n> ")
        if not validar_codigo(codigo):
            print("Codifo no puede estar vacio")
        else:
            break
    eliminado = eliminar_producto(productos, inventario, codigo)
    if eliminado:
        print("EL producto eliminado")
    else:
        "El codigo no existe."

def mostrar_productos(productos, inventario):
    for codigo in productos:
        nombre = productos[codigo][0]
        categoria = productos[codigo][1]
        precio = productos[codigo][2]
        disponible = productos[codigo][3]
        stock = inventario[codigo][0]
        vendidos = inventario[codigo][1]

        print(f"CODIGO: {codigo}")
        print("-"*25)
        print(f"Nombre: {nombre}")
        print(f"Categoría: {categoria}")
        print(f"Precio: ${precio}")
        print(f"Disponible: {disponible}")
        print(f"Stock: {stock}")
        print(f"Vendidos: {vendidos}")
        print("-"*25)

def main():
    os.system("cls")
    #en el programa final este diccionario debe estar vacio
    #uso solo para pruebas
    productos = {}
    inventario = {}

    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            ejecutar_stock_categoria(productos, inventario)
        elif opcion == 2:
            ejecutar_buscar_precio(productos, inventario)
        elif opcion == 3:
            ejecutar_actualizar_precio(productos, inventario)
        elif opcion == 4:
            ejecutar_agregar_productos(productos, inventario)
        elif opcion == 5:
            ejecutar_eliminar_producto(productos, inventario)
        elif opcion == 6:
            mostrar_productos(productos, inventario )
        elif opcion == 7:
            break

main()