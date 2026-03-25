# GUARDAR INVENTARIO EN CSV


def guardar_csv(inventario, ruta, incluir_header=True):

    # MIRAMOS SI EL INVENTARIO ESTA VACIO 
    if not inventario:
        print(" No hay productos para guardar.")
        return
    
    #PREVENCIÓN DE ERRORES 
    
    try:
        # ABRIR ARCHIVO EN ESCRITURA
        with open(ruta, "w", encoding="utf-8") as archivo:

            # ENCABEZADO
            if incluir_header:
                archivo.write("nombre,precio,cantidad\n")

            # Escribir productos
            for producto in inventario:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)

        print(f" Inventario guardado en: {ruta}")

    except PermissionError:
        print(" Error: No tienes permisos para escribir en esa ubicación.")

    except Exception as e:
        print(" Error al guardar el archivo:", e)

def cargar_csv(ruta, inventario_actual):

    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            # VALIDACIÓN DEL ENCABEZADO
            encabezado = lineas[0].strip()
            if encabezado != "nombre,precio,cantidad":
                print(" Encabezado inválido.")
                return inventario_actual

            # RECORRE Y LEE LAS LINEAS
            for linea in lineas[1:]:

                datos = linea.strip().split(",")

                # VALIDA LAS COLUMNAS
                if len(datos) != 3:
                    filas_invalidas += 1
                    continue

                try:
                    nombre = datos[0]
                    precio = float(datos[1])
                    cantidad = int(datos[2])

                    # VALIDACIÓN DE NEGATIVOS 
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    productos_cargados.append(producto)

                except ValueError:
                    filas_invalidas += 1

        # USUARIO ESCOGE SI SOBRESCRIBIR
        opcion = input("¿Sobrescribir inventario actual? (S/N): ").upper()

        
        # REEMPLAZAR INVENTARIO SI OPCION = S
        
        if opcion == "S":
            inventario_actual = productos_cargados
            accion = "Reemplazo total"

        # FUSIONAR INVENTARIO
   
        else:
            accion = "Fusión"

            for nuevo in productos_cargados:

                encontrado = False

                for actual in inventario_actual:
                    if actual["nombre"].lower() == nuevo["nombre"].lower():

                        # política:
                        # suma cantidades y actualiza precio
                        actual["cantidad"] += nuevo["cantidad"]
                        actual["precio"] = nuevo["precio"]

                        encontrado = True
                        break

                if not encontrado:
                    inventario_actual.append(nuevo)

       
        print("\n Carga finalizada")
        print("Productos cargados:", len(productos_cargados))
        print("Filas inválidas omitidas:", filas_invalidas)
        print("Acción realizada:", accion)

        return inventario_actual

    # MENSAJE DE ERRORES
    except FileNotFoundError:
        print(" Archivo no encontrado.")
        return inventario_actual

    except UnicodeDecodeError:
        print(" Error de codificación del archivo.")
        return inventario_actual

    except Exception as e:
        print(" Error inesperado:", e)
        return inventario_actual