#!/usr/bin/env python
#Cree un archivo llamado registro.log en el directorio actual
def creararchivolog():
    subprocess.run(["touch", "registro.log"])
    
def escribirlinea(linea):
    with open("registro.log", "x") as arch:
        arch.write(linea + "\n")

#Cambie el nombre del archivo a log_de_sistema.log. 
def cambiarnombre():
    os.rename("registro.log", "log_de_sistema.log")
    
#Elimine el archivo.
def eliminararchivo(archivo):
    os.remove(f"{archivo}")

def main(args):
    #creararchivolog()
    escribirlinea("Inicio del registro de operaciones")
    cambiarnombre()
    eliminararchivo("log_de_sistema.log")

if __name__ == '__main__':
    import os
    import subprocess
    import sys
    sys.exit(main(sys.argv))
