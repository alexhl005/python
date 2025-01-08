#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#          FUNCIÓN: cargaDatos    
#          OBJETIVO: crear unalista con las líneas del fichero
#          PARÁMETROS DE ENTRADA: una cadena de texto con el nombre del fichero a leer
#          PARÁMETROS DE SALIDA: una lista con las líneas del fichero
#################################################################################################   
def cargaDatos(archivo1):
	lista = ["iface eth0 inet static address 192.168.1.10 netmask 255.255.255.0 gateway 192.168.1.1",
		"iface eth1 inet static address 192.168.1.20 netmask 255.255.255.0",
		"iface eth3 inet static address 192.168.1.30 netmask 255.255.255.0 gateway 192.168.1.1",
		"iface eth4 inet static address 192.168.1.40 netmask 255.255.255.0"]
	return lista

#################################################################################################
#          FUNCIÓN: mostrarDatos    
#          OBJETIVO: mostrar por pantalla la lista de líneas
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: no devuelve nada. Solo muestra por pantalla
#################################################################################################   
def mostrarDatos(lista):
	for i in range(len(lista)):
		print(f"{lista[i]}")

#################################################################################################
#          FUNCIÓN: filtrarDatos   
#          OBJETIVO: crear un diccionario con las líneas que cumplen una condición.
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: diccionario con las líneas del fichero que contienen "tcp". 
#                                La clave será el número de puerto y el protocolo y los datos el
#                                resto de la línea.
#################################################################################################   
def filtrarDatos(lista):
	dicc = {}
	for i in range(len(lista)):
		if "gateway" not in lista[i]:
			listaF = lista[i].split(" ")
			datos = []
			for j in range(2,len(listaF)):
				datos.append(listaF[j])
			dicc.update({listaF[1]: datos})
	return dicc

#################################################################################################
#          FUNCIÓN: mostrarFiltrados   
#          OBJETIVO: mostrar por pantalla el diccionario con los datos ya filtrados
#          PARÁMETROS DE ENTRADA: diccionario con los datos filtrados
#          PARÁMETROS DE SALIDA: ninguno. Muestra por pantalla el contenido
#################################################################################################  
def mostrarFiltrados(dicc):
	for i in dicc:
		print(f"{i}")
		for j in dicc[i]:
			print(f"\t{j}")



#######################################################################################33##########

def main(args):
    # Uso de las funciones
    listaLineas = cargaDatos("interfaces.txt")
    print("Contenido /etc/networks/interfaces:\n")
    mostrarDatos(listaLineas)
    
    print("\nInterfaces sin gateway\n")
    datosFiltrados=filtrarDatos(listaLineas)
    mostrarFiltrados(datosFiltrados)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
