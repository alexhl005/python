#!/usr/bin/env python
import shutil
import os
def crear_archivo():
    ruta='/home/usuario/Escritorio/practica'
    os.chdir(ruta)
    with open("documento.txt", "w") as prueba:
       prueba.writelines("Inicio del registro de operaciones.\n")
    return 0

def main(args):
 nuevoarchivo=crear_archivo()
 return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
