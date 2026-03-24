# -------------------------------------------------
# AGREGAR PRODUCTO
# -------------------------------------------------
def agregar_producto(inventario):

    nombre = input("Nombre del producto: ").strip()

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Datos inválidos")
        return

    if precio < 0 or cantidad < 0:
        print("Valores negativos no permitidos")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente")


# -------------------------------------------------
# MENU
# -------------------------------------------------
def mostrar_menu():
    print("\n========= MENÚ INVENTARIO =========")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


# -------------------------------------------------
# MOSTRAR INVENTARIO
# -------------------------------------------------
def mostrar_inventario(inventario):

    if not inventario:
        print("No hay productos")
        return

    print("\nINVENTARIO")
    for p in inventario:
        print(f"{p['nombre']} | {p['precio']} | {p['cantidad']}")


# -------------------------------------------------
# BUSCAR PRODUCTO
# -------------------------------------------------
def buscar_producto(inventario):

    nombre = input("Nombre a buscar: ").strip()

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Producto encontrado:")
            print(p)
            return

    print("Producto no encontrado")


# -------------------------------------------------
# ACTUALIZAR PRODUCTO
# -------------------------------------------------
def actualizar_producto(inventario):

    nombre = input("Producto a actualizar: ").strip()

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():

            try:
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("Datos inválidos")
                return

            if precio < 0 or cantidad < 0:
                print("Valores negativos no permitidos")
                return

            p["precio"] = precio
            p["cantidad"] = cantidad

            print("Producto actualizado")
            return

    print("Producto no encontrado")


# -------------------------------------------------
# ELIMINAR PRODUCTO
# -------------------------------------------------
def eliminar_producto(inventario):

    nombre = input("Producto a eliminar: ").strip()

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Producto eliminado")
            return

    print("Producto no encontrado")


# -------------------------------------------------
# ESTADISTICAS
# -------------------------------------------------
def calcular_estadisticas(inventario):

    if not inventario:
        print("Inventario vacío")
        return

    unidades = sum(p["cantidad"] for p in inventario)
    valor = sum(p["precio"] * p["cantidad"] for p in inventario)

    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])

    print("\nESTADÍSTICAS")
    print("Unidades totales:", unidades)
    print("Valor total:", valor)
    print("Producto más caro:", mas_caro["nombre"])
    print("Mayor stock:", mayor_stock["nombre"])