from servicios import *
from archivos import guardar_csv, cargar_csv

print("\nBIENVENIDO/A AL SISTEMA DE INVENTARIO")

inventario = []

# -------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------
while True:

    mostrar_menu()

    # -------- VALIDAR OPCIÓN --------
    try:
        option = int(input("Ingrese una opción (1-9): "))

        if option < 1 or option > 9:
            print("Opción fuera de rango.")
            continue

    except ValueError:
        print("Debe ingresar un número.")
        continue


    # -------------------------------------------------
    # 1. AGREGAR PRODUCTO
    # -------------------------------------------------
    if option == 1:
        try:
            agregar_producto(inventario)
        except Exception as e:
            print("Error al agregar producto:", e)


    # -------------------------------------------------
    # 2. MOSTRAR INVENTARIO
    # -------------------------------------------------
    elif option == 2:
        mostrar_inventario(inventario)


    # -------------------------------------------------
    # 3. BUSCAR PRODUCTO
    # -------------------------------------------------
    elif option == 3:
        nombre = input("Nombre del producto: ")
        producto = buscar_producto(inventario, nombre)

        if producto:
            print("Producto encontrado:", producto)
        else:
            print("Producto no encontrado.")


    # -------------------------------------------------
    # 4. ACTUALIZAR PRODUCTO
    # -------------------------------------------------
    elif option == 4:
        nombre = input("Producto a actualizar: ")

        try:
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))

            if precio < 0 or cantidad < 0:
                print("Los valores no pueden ser negativos.")
            else:
                actualizar_producto(inventario, nombre, precio, cantidad)

        except ValueError:
            print("Datos inválidos.")


    # -------------------------------------------------
    # 5. ELIMINAR PRODUCTO
    # -------------------------------------------------
    elif option == 5:
        nombre = input("Producto a eliminar: ")
        eliminar_producto(inventario, nombre)


    # -------------------------------------------------
    # 6. ESTADÍSTICAS
    # -------------------------------------------------
    elif option == 6:
        calcular_estadisticas(inventario)


    # -------------------------------------------------
    # 7. GUARDAR CSV
    # -------------------------------------------------
    elif option == 7:
        ruta = input("Nombre del archivo (ej: inventario.csv): ")
        guardar_csv(inventario, ruta)


    # -------------------------------------------------
    # 8. CARGAR CSV
    # -------------------------------------------------
    elif option == 8:
        ruta = input("Archivo a cargar: ")
        inventario = cargar_csv(ruta, inventario)


    # -------------------------------------------------
    # 9. SALIR
    # -------------------------------------------------
    elif option == 9:
        print("HASTA PRONTO")
        break


