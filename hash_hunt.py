import itertools
import time
import os
import hashlib
import pyperclip

from functions_files import *


def hash_hunt():
    hash_number = input("\nNumero hash: ")
    diccionario = input("\nEscribe el nombre del diccionario que vas a usar: ")

    print("\n[+] Buscando...\n")

    with open(f"{os.getcwd()}\\Archivos\\{diccionario}.txt", "r") as file:
        for i in file:
            i = i.strip()
            number_hash = hashlib.sha1(i.encode("utf-8")).hexdigest()
            print(f"{number_hash} ->", i)
            time.sleep(0.05)

            if hash_number == number_hash:
                print(f"\nEl hash {hash_number} corresponde a la contraseña: {i}")
                break

    option = int(
        input(
            """¿Deseas copiar la contraseña en tu portapapeles?

1. Sí
2. No

Opción: """
        )
    )

    if option == 1:
        pyperclip.copy(i)
        print("\n[+] La contraseña se guardo en tu portapapeles correctamente.")
    else:
        print("\n[-] No se copio la contraseña en tu papelera.")


print(
    """

██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██║  ██║██║   ██║████╗  ██║██║╚══██╔══╝
███████║███████║███████╗███████║    ███████║██║   ██║██╔██╗ ██║██║   ██║   
██╔══██║██╔══██║╚════██║██╔══██║    ██╔══██║██║   ██║██║╚██╗██║██║   ██║   
██║  ██║██║  ██║███████║██║  ██║    ██║  ██║╚██████╔╝██║ ╚████║██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   

"""
)

while True:
    try:
        menu = int(
            input(
                """1. Ver archivos
2. Crear diccionario
3. Crear hash
4. Brute Force (Búsqueda de Hash)
5. Eliminar archivo
6. Salir
7. Diccionario de rangos

Opción: """
            )
        )

        match menu:
            case 1:
                archivos()
                continue
            case 2:
                name_file = str(input("\nNombre del archivo: "))
                option = int(input("\nQue longitud tiene la contraseña: "))

                list_numbers = [i for i in range(1, option + 1)]

                print(f"\nLista de los números para permutar: {list_numbers}")

                regex = itertools.permutations(list_numbers)

                print(f"\n[+] Permutando...\n")

                for i in regex:
                    letra_i = i
                    time.sleep(0.05)
                    texto = "".join(str(x) for x in letra_i)

                    actualizar(texto, name_file)

                numero = 1

                for i in range(len(list_numbers)):
                    incremento = int(i) + 1
                    numero *= incremento

                print(f"\nSerian {numero} permutaciones\n")
                print(
                    f"[+] Se a creado el archivo {name_file}.txt y se han guardado las permutaciones"
                )
                print(f"\n[-] Saliendo...\n")
                break
            case 3:
                create_hash()
                break
            case 4:
                hash_hunt()
                break
            case 5:
                archivoEliminar = str(input("\nQue archivo deseas eliminar: "))
                os.system(f"rm Archivos/{archivoEliminar}.txt")
                print(f"\n[-] Se elimino el archivo {archivoEliminar}.txt")
                break
            case 6:
                print("\n[-] Saliendo...")
                break
            case 7:
                name_file = str(input("\nNombre del archivo: "))

                for i in range(100000000):
                    refill_number = str(i).zfill(8)
                    actualizar(refill_number, name_file)
                break
            case _:
                print("\nOpción incorrecta. Selecciona una opción correcta.")
                continue

    except ValueError:
        print("\nNo se permiten letras.")
        print("\n[-] Saliendo...")
        break

if __name__ == "__main__":
    hash_hunt()
