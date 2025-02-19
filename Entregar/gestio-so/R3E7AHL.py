#!/usr/bin/env python3
import subprocess
import os
import sys

def ejecutar_ls():
    print("\nMostrar los archivos del directorio actual\n")
    subprocess.run(["ls"])
    return 0

def redigir_salida():
    with open('listar_archivos.txt', "w") as archivo:
         subprocess.run(["ls"], stdout=archivo, stderr=subprocess.DEVNULL)

def leer_contenido():
  try:  
      with open('listar_archivos.txt', 'r') as archivo:
        contenido= archivo.read()
      print(contenido)
  except FileNotFoundError:
      print("El archivo no existe")
  return 0

def main(args):
    listar=ejecutar_ls()
    salida=redigir_salida()
    leer=leer_contenido()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
