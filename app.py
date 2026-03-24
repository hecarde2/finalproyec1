from servicios import *
from archivos import guardar_csv, cargar_csv

print("\nBIENVENIDO/A AL SISTEMA DE INVENTARIO")

inventario = []
option = 0

# -------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------
while option != 9:

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
        agregar_producto(inventario)


    # -------------------------------------------------
    # 2. MOSTRAR INVENTARIO
    # -------------------------------------------------
    elif option == 2:
        mostrar_inventario(inventario)


    # -------------------------------------------------
    # 3. BUSCAR PRODUCTO
    # -------------------------------------------------
    elif option == 3:
        buscar_producto(inventario)


    # -------------------------------------------------
    # 4. ACTUALIZAR PRODUCTO
    # -------------------------------------------------
    elif option == 4:
        actualizar_producto(inventario)


    # -------------------------------------------------
    # 5. ELIMINAR PRODUCTO
    # -------------------------------------------------
    elif option == 5:
        eliminar_producto(inventario)


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
