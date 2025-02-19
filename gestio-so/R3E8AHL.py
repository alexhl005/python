#!/usr/bin/env python3
import shutil
import sys
import os
import subprocess

def ejecutar_ping():
    try:
       comando = subprocess.run(["ping", "-c", "5", "google.com"], capture_output=True, text=True, check=True)
       lineas = comando.stdout.splitlines()[:5]
       print("\nPrimeras 5 lineas de la salida del ping:")
       for linea in lineas:
           print(linea)
    except subprocess.CalledProcess as e:
        print("Error al ejectuar el ping:", e.stderr)

def main(args):
    ping=ejecutar_ping()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
