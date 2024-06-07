import itertools
import time
import os
import hashlib
import pyperclip

def escribir(texto):
    my_file = open(f"{os.getcwd()}\\Archivos\\{nombreArchivo}.txt", "w")
    my_file.write(texto)
    my_file.close()

def leer():
    my_file = open(f"{os.getcwd()}\\Archivos\\{nombreArchivo}.txt", "r")
    print(my_file.read())
    my_file.close()

def actualizar(texto):
    my_file = open(f"{os.getcwd()}\\Archivos\\{nombreArchivo}.txt", "a")
    my_file.write(f"{texto}\n")
    my_file.close()

def archivos():
    print("\n====Archivos====\n")
    os.system("ls Archivos -1")
    print("\n================\n")

def createhash():
    hashing = input("\nConvertir a hash: ")

    salida = hashlib.sha1(hashing.encode('utf-8')).hexdigest()

    print(f"\n{salida} es el hash para {hashing}\n")

    option = int(input("""¿Deseas copiar el hash en tu portapapeles?

1. Sí
2. No

Opcion: """))

    if option == 1:
        pyperclip.copy(salida)
        print("\n[+] El hash se ha guardado en tu portapapeles correctamente.")
    else:
        print("\n[-] No se copio el hash en tu papelera.")


def hash_hunt():
    hashnumber = input("\nNumero hash: ")
    diccionario = input("\nEscribe el nombre del diccionario que vas a usar: ")

    print("\n[+] Buscando...\n")

    with open(f"{os.getcwd()}\\Archivos\\{diccionario}.txt", "r") as file:
        for i in file:
            i = i.strip()
            numeroshashing = hashlib.sha1(i.encode('utf-8')).hexdigest()
            print(f"{numeroshashing} ->", i)
            time.sleep(0.05)
            
            if hashnumber == numeroshashing:
                print(f"\nEl hash {hashnumber} corresponde a la contraseña: {i}")
                break

    option = int(input("""¿Deseas copiar la contraseña en tu portapapeles?

1. Sí
2. No

Opcion: """))

    if option == 1:
        pyperclip.copy(i)
        print("\n[+] La contraseña se guardo en tu portapapeles correctamente.")
    else:
        print("\n[-] No se copio la contraseña en tu papelera.")

    
print("""
                     
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██║  ██║██║   ██║████╗  ██║██║╚══██╔══╝
███████║███████║███████╗███████║    ███████║██║   ██║██╔██╗ ██║██║   ██║   
██╔══██║██╔══██║╚════██║██╔══██║    ██╔══██║██║   ██║██║╚██╗██║██║   ██║   
██║  ██║██║  ██║███████║██║  ██║    ██║  ██║╚██████╔╝██║ ╚████║██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   
     
""")

while True:
    try:
        menu = int(input("""1. Ver arhivos
2. Crear diccionario
3. Crear hash
4. Brute Force (Busqueda de Hash)
5. Eliminar archivo
6. Salir
7. Diccionario de rangos
                     
Opcion: """))

        if menu == 1:
            archivos()
            continue

        elif menu == 2:
            nombreArchivo = str(input("\nNombre del archivo: "))

            opcion = int(input("\nQue longitud tiene la contraseña: "))

            list_numbers = [i for i in range(1, opcion + 1)]

            print(f"\nLista de los numeros para permutar: {list_numbers}")

            regex = itertools.permutations(list_numbers)

            print(f"\n[+] Permutando...\n")

            for i in regex:
                letra_i = i
                time.sleep(0.05)
                texto = ''.join(str(x) for x in letra_i)

                actualizar(texto)

            numero = 1

            for i in range(len(list_numbers)):
                incremento = int(i) + 1
                numero *= incremento

            print(f"\nSerian {numero} permutaciones\n")
            print(f"[+] Se a creado el archivo {nombreArchivo}.txt y se han guardado las permutaciones")
            print(f"\n[-] Saliendo...\n")
            break

        elif menu == 3:
            createhash()
            break

        elif menu == 4: 
            hash_hunt()
            break

        elif menu == 5:
            arhivoEliminar = str(input("\nQue archivo deseas eliminar: "))
            os.system(f"rm Archivos/{arhivoEliminar}.txt")
            print(f"\n[-] Se elimino el archivo {arhivoEliminar}.txt")
            break

        elif menu == 6:
            print("\n[-] Saliendo...")
            break

        elif menu == 7:
            nombreArchivo = str(input("\nNombre del archivo: "))

            for i in range(100000000):
                refill_number = str(i).zfill(8)
                actualizar(refill_number)
            break

        else:
            print("\nOpcion incorrecta. Selecciona una opcion correcta.")
            continue

    except ValueError:
        print("\nNo se permiten letras.")
        print("\n[-] Saliendo...")
        break