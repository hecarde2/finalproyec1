# -------------------------------------------------
# AGREGAR PRODUCTO
# -------------------------------------------------
def agregar_producto(inventario):

    nombre = input("Nombre del producto: ")

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print(" Debe ingresar números válidos")
        return

    # Validaciones
    if precio < 0 or cantidad < 0:
        print(" Número inválido")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("✅ PRODUCTO AGREGADO CON ÉXITO")


# -------------------------------------------------
# MENÚ
# -------------------------------------------------
def mostrar_menu():
    print("\n MENÚ DEL SISTEMA DE INVENTARIO")
    print(" 1. AGREGAR PRODUCTO")
    print(" 2. MOSTRAR INVENTARIO")
    print(" 3. BUSCAR PRODUCTO")
    print(" 4. ACTUALIZAR PRODUCTO")
    print(" 5. ELIMINAR PRODUCTO")
    print(" 6. CALCULAR ESTADÍSTICAS")
    print(" 7. SALIR")


# -------------------------------------------------
# MOSTRAR INVENTARIO
# -------------------------------------------------
def mostrar_inventario(inventario):

    if len(inventario) == 0:
        print(" NO HAY PRODUCTOS")
        return

    print("\n INVENTARIO")
    for producto in inventario:
        print(
            f"Nombre: {producto['nombre']} | "
            f"Precio: {producto['precio']} | "
            f"Cantidad: {producto['cantidad']}"
        )


# -------------------------------------------------
# BUSCAR PRODUCTO
# -------------------------------------------------
def buscar_producto(inventario):

    nombre = input("Nombre a buscar: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("✅ Producto encontrado:")
            print(producto)
            return

    print(" Producto no encontrado")


# -------------------------------------------------
# ACTUALIZAR PRODUCTO
# -------------------------------------------------
def actualizar_producto(inventario):

    nombre = input("Producto a actualizar: ")

    for actual in inventario:
        if actual["nombre"].lower() == nombre.lower():

            try:
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print(" Datos inválidos")
                return

            if precio < 0 or cantidad < 0:
                print(" Número inválido")
                return

            actual["precio"] = precio
            actual["cantidad"] = cantidad

            print("✅ Producto actualizado")
            return

    print(" Producto no encontrado")


# -------------------------------------------------
# ELIMINAR PRODUCTO
# -------------------------------------------------
def eliminar_producto(inventario):

    nombre = input("Producto a eliminar: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("✅ Producto eliminado")
            return

    print(" Producto no encontrado")


# -------------------------------------------------
# CALCULAR ESTADÍSTICAS
# -------------------------------------------------
def calcular_estadisticas(inventario):

    if not inventario:
        print(" Inventario vacío")
        return

    unidades_totales = 0
    valor_total = 0

    for t in inventario:
        unidades_totales += t["cantidad"]
        valor_total += t["precio"] * t["cantidad"]

    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])

    print("\n ESTADÍSTICAS")
    print("Unidades totales:", unidades_totales)
    print("Valor total:", valor_total)
    print("Producto más caro:", mas_caro["nombre"])
    print("Mayor stock:", mayor_stock["nombre"])
