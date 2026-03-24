# -------------------------------------------------
# AGREGAR PRODUCTO
# -------------------------------------------------
def agregar_producto(inventario):

    nombre = input("Nombre del producto: ").strip()

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Debe ingresar números válidos")
        return

    # Validaciones
    if precio < 0 or cantidad < 0:
        print("Número inválido")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado con éxito")


# -------------------------------------------------
# MENÚ
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

    nombre = input("Nombre a buscar: ").strip()

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("Producto encontrado:")
            print(producto)
            return producto

    print("Producto no encontrado")
    return None


# -------------------------------------------------
# ACTUALIZAR PRODUCTO
# -------------------------------------------------
def actualizar_producto(inventario):

    nombre = input("Producto a actualizar: ").strip()

    for actual in inventario:
        if actual["nombre"].lower() == nombre.lower():

            try:
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("Datos inválidos")
                return

            if precio < 0 or cantidad < 0:
                print("Número inválido")
                return

            actual["precio"] = precio
            actual["cantidad"] = cantidad

            print("Producto actualizado")
            return

    print("Producto no encontrado")


# -------------------------------------------------
# ELIMINAR PRODUCTO
# -------------------------------------------------
def eliminar_producto(inventario):

    nombre = input("Producto a eliminar: ").strip()

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado")
            return

    print("Producto no encontrado")


# -------------------------------------------------
# CALCULAR ESTADÍSTICAS
# -------------------------------------------------
def calcular_estadisticas(inventario):

    if not inventario:
        print("Inventario vacío")
        return

    unidades_totales = 0
    valor_total = 0

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += producto["precio"] * producto["cantidad"]

    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])

    print("\nESTADÍSTICAS")
    print("Unidades totales:", unidades_totales)
    print("Valor total:", valor_total)
    print("Producto más caro:", mas_caro["nombre"], "-", mas_caro["precio"])
    print("Mayor stock:", mayor_stock["nombre"], "-", mayor_stock["cantidad"])