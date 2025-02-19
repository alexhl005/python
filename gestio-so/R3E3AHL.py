#!/usr/bin/env python
import os
import subprocess
def mostrar_info():
    print("Mostrar informacion del usuario\n")
    subprocess.run(["w"])
    return 0
def mostrar_variable():
    print("\nMostrar variables del sistema\n")
    subprocess.run(["printenv"])
    return 0
def mostrar_sistema():
    print("\nMostrar sistema en el que se ejecuta el script\n")
    subprocess.run(["lsb_release", "-a"])
    return 0
def main(args):
    infousuario=mostrar_info()
    infovariables=mostrar_variable() 
    infosistema=mostrar_sistema()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
