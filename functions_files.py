import os
import hashlib
import pyperclip


def escribir(texto, name_file):
    my_file = open(f"{os.getcwd()}\\Archivos\\{name_file}.txt", "w")
    my_file.write(texto)
    my_file.close()


def leer(name_file):
    my_file = open(f"{os.getcwd()}\\Archivos\\{name_file}.txt", "r")
    print(my_file.read())
    my_file.close()


def actualizar(texto, name_file):
    my_file = open(f"{os.getcwd()}\\Archivos\\{name_file}.txt", "a")
    my_file.write(f"{texto}\n")
    my_file.close()


def archivos():
    print("\n====Archivos====\n")
    os.system("ls Archivos -1")
    print("\n================\n")


def create_hash():
    hashing = input("\nConvertir a hash: ")

    salida = hashlib.sha1(hashing.encode("utf-8")).hexdigest()

    print(f"\n{salida} es el hash para {hashing}\n")

    option = int(
        input(
            """¿Deseas copiar el hash en tu portapapeles?

1. Sí
2. No

Opción: """
        )
    )

    if option == 1:
        pyperclip.copy(salida)
        print("\n[+] El hash se ha guardado en tu portapapeles correctamente.")
    else:
        print("\n[-] No se copio el hash en tu papelera.")
