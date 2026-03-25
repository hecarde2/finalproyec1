from servicios import *
from archivos import guardar_csv, cargar_csv

print("\nBIENVENIDO/A AL SISTEMA DE INVENTARIO")

inventario = []
option = 0

# MENÚ PRINCIPAL
while option != 9:

    mostrar_menu()

    try:
        option = int(input("Ingrese una opción (1-9): "))

        if option < 1 or option > 9:
            print("Opción fuera de rango.")
            continue

    except ValueError:
        print("Debe ingresar un número.")
        continue


    # OPCIONES DEL MENÚ
    if option == 1:
        agregar_producto(inventario)

    elif option == 2:
        mostrar_inventario(inventario)

    elif option == 3:
        buscar_producto(inventario)

    elif option == 4:
        actualizar_producto(inventario)

    elif option == 5:
        eliminar_producto(inventario)

    elif option == 6:
        calcular_estadisticas(inventario)

       # GUARDAR CSV
    elif option == 7:
        ruta = input("Nombre del archivo .CSV: ")

        partes = ruta.split(".")
        #NO PERMITE GUARDAR ARCHIVO QUE NO SEA CSV
        if partes[-1] != "csv":
            print("Archivo con formato invalido, formato permitido .CSV")
            continue

        guardar_csv(inventario, ruta)

    # CARGAR CSV
    elif option == 8:
        ruta = input("Archivo a cargar: ")

        partes = ruta.split(".")

        if partes[-1] != "csv":
            print("Archivo con formato invalido, formato permitido .CSV")
            continue

        inventario = cargar_csv(ruta, inventario)


    elif option == 9:
        print("HASTA PRONTO")
        break