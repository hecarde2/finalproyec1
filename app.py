from servicios import *
from archivos import guardar_csv, cargar_csv

print("\nBIENVENIDO/A AL SISTEMA DE INVENTARIO")

inventario = []
option = 0


# MENÚ PRINCIPAL, OPCION 9 PARA SALIR

while option != 9:

    mostrar_menu()

    # SI HAY ALGÚN ERROR DE UN NÚMERO FUERA DE RANGO, SE REPITA EL MENÚ Y EL PROGRAMA SIGA
    try:
        option = int(input("Ingrese una opción (1-9): "))

        if option < 1 or option > 9:
            print("Opción fuera de rango.")
            continue

    except ValueError:
        print("Debe ingresar un número.")
        continue


    # FUNCIONES DEFINIDAS CON LAS OPCIONES DEL MENÚ 

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


    #  GUARDAR CSV

    elif option == 7:
        ruta = input("Nombre del archivo (ej: inventario.csv): ")
        guardar_csv(inventario, ruta)


    #  CARGAR CSV

    elif option == 8:
        ruta = input("Archivo a cargar: ")
        inventario = cargar_csv(ruta, inventario)




    elif option == 9:
        print("HASTA PRONTO")
        break
