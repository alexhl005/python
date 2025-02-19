#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################################################################################
####    Programa que analiza un fichero de log con las conexiones a un servidor y pasa a otro  ##
####    fichero la información de las conexiones fallidas.                                    ###
#################################################################################################
# Alejandro herrera Luque
import re
import sys
import argparse


def leer_archivo(archivo):
    ## Función que lee el archivo que recibe como parámetro y devuelve una lista con las 
    ## líneas de texto
    try:
        with open(archivo, "r") as file:
            contenido = file.readlines()
            return contenido
    except FileNotFoundError:
        print("Archivo no encontrado")

def buscar_errores(patron, lista):
    ## Funcion que recibe una lista con las lineas del fichero y devuelve una lista
    ## con las filas en la que hubo un acceso denegado
    patronc = re.compile(patron)
    denegados = []
    for i in lista:
        if re.search(patronc, i) is not None:
            denegados.append(i)
    return denegados

def guardar_informe(ruta_salida, errores):
    ## Función que recibe la ruta del fichero de salida y la lista de intentos denegados
    ## y guarda en el fichero solamente la fecha y hora de conexión y el usuario que intentó conectar
    try:
        with open(ruta_salida, "w") as file:
            for i in errores:
                linea = i.split(" ")
                nuevalinea = f"{linea[0]} - {linea[2]}\n"
                file.writelines(nuevalinea)

    except FileNotFoundError:
        print("Archivo no encontrado")

def main():
    ## Definición de los parámetros de script (fichero origen obligatorio, fichero salida opcional)
    ## Si no se proporciona fichero de salida, se guardará en "informe.txt" en la misma carpeta
    ## que esté el script
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument("entrada", help="Archivo de entrada")
    parser.add_argument("salida", help="Archivo de salida")

    args = parser.parse_args()
    
   
    ## Cuerpo principla. Define el patrón y llama a las funciones
    patron = "denied"
    lista = leer_archivo(args.entrada)
    denied = buscar_errores(patron, lista)
    guardar_informe(args.salida, denied)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)
