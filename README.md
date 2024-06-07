# Hash Hunt

## Descripción

**Hash Hunt** es una potente herramienta diseñada para la creación, gestión y búsqueda de diccionarios de números hasheados. Desarrollada en Python, esta aplicación permite a los usuarios generar diccionarios de números y sus correspondientes hashes, proporcionando una manera eficiente de buscar y verificar hashes utilizando una contraseña numérica.

## Características

- **Generación de diccionarios de números**: Crea diccionarios de números permutados según la longitud especificada por el usuario.
- **Hashing seguro**: Convierte cualquier cadena de texto en su hash correspondiente utilizando SHA-1.
- **Búsqueda eficiente de hashes**: Busca un hash específico dentro de un diccionario y proporciona la contraseña original si se encuentra.
- **Interfaz de línea de comandos intuitiva**: Fácil de usar, con menús claros y opciones numeradas.
- **Gestión de archivos**: Crea, lee, actualiza y elimina archivos de diccionarios fácilmente.

## Instalación

Para instalar y ejecutar Hash Hunt en tu máquina local, sigue estos pasos:

1. Clona el repositorio:

    ```sh
    git clone https://github.com/DeymerOspina/hash-hunt.git
    ```

2. Navega al directorio del proyecto:

    ```sh
    cd hash-hunt
    ```

3. Instala las dependencias necesarias:

    ```sh
    pip install -r requirements.txt
    ```

4. Ejecuta el programa:

    ```sh
    python hash_hunt.py
    ```

## Uso

Al ejecutar el programa, verás un menú con las siguientes opciones:

1. **Ver archivos**: Muestra los archivos disponibles en el directorio `Archivos`.
2. **Crear diccionario**: Genera un diccionario de permutaciones de números según la longitud especificada.
3. **Crear hash**: Convierte una cadena de texto en su hash SHA-1 correspondiente.
4. **Brute Force (Búsqueda de Hash)**: Busca un hash específico en un diccionario y proporciona la contraseña original si se encuentra.
5. **Eliminar archivo**: Elimina un archivo de diccionario especificado.
6. **Salir**: Sale del programa.
7. **Diccionario de rangos**: Genera un diccionario de números en rango (por ejemplo, del 00000000 al 99999999).

### Ejemplo de Uso

1. **Crear un diccionario**:
    - Selecciona la opción `2` en el menú.
    - Ingresa el nombre del archivo.
    - Especifica la longitud de las contraseñas.
    - El programa generará y guardará todas las permutaciones posibles en el archivo especificado.

2. **Buscar un hash**:
    - Selecciona la opción `4` en el menú.
    - Ingresa el hash que deseas buscar.
    - Especifica el nombre del diccionario donde se realizará la búsqueda.
    - El programa buscará el hash en el diccionario y, si lo encuentra, mostrará la contraseña correspondiente.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a Hash Hunt, por favor, abre un issue o envía un pull request con tus mejoras o correcciones.

## Licencia

Este proyecto está licenciado bajo la Licencia BSD 3-Clause. Consulta el archivo `LICENSE` para obtener más detalles.

