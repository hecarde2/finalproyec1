from servicios import *
print("\n Bienvenido/a a su inventario")

inventario = []
option = 0

while option != 7:
    mostrar_menu()

    try:
        option = int(input("Ingrese una opcion del menú: "))
    except ValueError:
        print(" Debe ingresar un número")
        continue  

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

    elif option == 7:
        print(" HASTA PRONTO")

    else:
        print(" VUELVE A INTENTAR")

          
   



