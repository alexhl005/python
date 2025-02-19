#!/usr/bin/env python3
import sys
import os
import subprocess
import shutil

def copiasegura_shutil():
    ruta_origen= "/home/usuario/Escritorio/practica"
    ruta_destino= "/home/usuario/Documentos"
    shutil.copytree(ruta_origen, ruta_destino)

def copiasegura_os():
    with open("/home/usuario/backup.log", "a") as archivo_log:
 
def main(args):
    cshutil=copiasegura_shutil()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
