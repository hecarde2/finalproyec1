# finalproyec1
# Inventario-de-productos
# Coder: 
- Hector Carvajal
## Link repositorio : https://github.com/hecarde2/finalproyec1.git

# Descripción

Este programa de consola desarrollado en **Python** permite gestionar un sistema de inventario mediante un menú interactivo en la terminal.

El usuario puede registrar productos ingresando su **nombre, precio y cantidad**, además de administrar la información realizando búsquedas, actualizaciones y eliminaciones.

El proyecto está organizado en diferentes archivos para separar la lógica del sistema, el manejo del menú y la gestión de archivos CSV.


# Funcionamiento

Es un programa de consola que se ejecuta desde la terminal.

Funciona en **Python** utilizando un intérprete (por ejemplo: Python 3).

El sistema muestra un menú principal donde el usuario selecciona opciones para administrar el inventario:

- Agregar productos
- Mostrar inventario
- Buscar productos
- Actualizar información
- Eliminar productos
- Ver estadísticas del inventario
- Guardar datos en archivo CSV
- Cargar inventario desde CSV
- Salir del programa

Permite registrar productos utilizando las siguientes variables:

- **nombre:** nombre del producto.
- **precio:** valor unitario del producto.
- **cantidad:** número de unidades disponibles en el inventario.


# Estructura del proyecto

El sistema está dividido en varios archivos:

- **app.py:** archivo principal que ejecuta el programa y controla el menú.
- **servicios.py:** contiene las funciones del inventario.
- **archivos.py:** permite guardar y cargar información en archivos CSV.


# Requisitos

- Tener instalado **Python 3**
- Contar con una terminal o consola para ejecutar el programa
- Editor de código opcional (Visual Studio Code recomendado)


# Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Abrir la terminal en la carpeta del proyecto.
3. 3. Cambiar la rama de main a  feature/1-app
4. Ejecutar el archivo principal con el siguiente comando:

```bash
python app.py
