#!/usr/bin/env python
#Muestre el directorio de trabajo actual.
def mostrar_directorio():
    return print(f"El directorio de trabajo actual es {os.getcwd()}")

#Cambie a un directorio específico (por ejemplo, /tmp)
def cambiar_directorio(directorio):
    return {
        os.chdir(directorio):
        print(f"El directorio de trabajo actual es {os.getcwd()}")
    }
    
#Cree un subdirectorio llamado practica.
def crearsubdirectorio(directorio):
    return {
        os.mkdir(directorio):
        print(f"El directorio creado es {directorio}")
    }
    
#Liste el contenido del directorio recién creado
def listarcontenido(directorio):
    return print(f"El contenido de {directorio} es:"), [print(f"\t{archivo}") for archivo in os.listdir(directorio)]

def main(args):
    mostrar_directorio()
    #cambiar_directorio("/tmp")
    #crearsubdirectorio("practica")
    #pongo lista pa q se vea algo
    listarcontenido(f"lista")

if __name__ == '__main__':
    import os
    import sys
    sys.exit(main(sys.argv))
