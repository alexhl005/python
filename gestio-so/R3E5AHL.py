#!/usr/bin/env python3
import sys
import shutil
import os

def crear_directorios():
    ruta='/home/usuario/Escritorio'
    os.chdir(ruta)
    os.mkdir('proyecto')
    nuevaruta='/home/usuario/Escritorio/proyecto'
    os.chdir(nuevaruta)
    os.mkdir('datos')
    os.mkdir('scripts')
    os.mkdir('informes')
    return 0

def comprimir_directorio():
    ruta='/home/usuario/Escritorio/proyecto'
    archivo_salida = '/home/usuario/Escritorio/proyecto_comprimido'
    formato = "zip"
    shutil.make_archive(archivo_salida, formato, ruta)
    return 0

def extraer_contenido():
    archivo_comprimido='/home/usuario/Escritorio/proyecto_comprimido.zip'
    destino='/home/usuario/Escritorio/proyecto_extraido'
    shutil.unpack_archive(archivo_comprimido, destino)
    
def main(args):
    arboldirectorios=crear_directorios()
    comprimir=comprimir_directorio
    extraer=extraer_contenido()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
