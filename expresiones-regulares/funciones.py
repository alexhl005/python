import re

# Ejercicio 1: Validar si es un correo electrónico
def es_correo_electronico(cadena):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, cadena))

def ejecutar_ejercicio_1():
    cadena = input("Introduce una cadena para verificar si es un correo electrónico: ")
    print("Es un correo electrónico:", es_correo_electronico(cadena))

# Ejercicio 2: Contar fechas en un texto
def contar_fechas(texto):
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return len(re.findall(patron, texto))

def ejecutar_ejercicio_2():
    texto = input("Introduce un texto: ")
    print("Número de fechas encontradas:", contar_fechas(texto))

# Ejercicio 3: Encontrar números de teléfono en un texto
def encontrar_telefonos(texto):
    patron = r'\b(?:\d{3}-\d{6}|\d{9}|\d{3}\.\d{3}\.\d{3})\b'
    return re.findall(patron, texto)

def ejecutar_ejercicio_3():
    texto = input("Introduce un texto: ")
    print("Números de teléfono encontrados:", encontrar_telefonos(texto))

# Ejercicio 4: Reemplazar texto en un string
def reemplazar_texto(texto, buscar, reemplazar):
    return re.sub(re.escape(buscar), reemplazar, texto)

def ejecutar_ejercicio_4():
    texto = input("Introduce el texto original: ")
    buscar = input("Introduce el texto a buscar: ")
    reemplazar = input("Introduce el texto de reemplazo: ")
    print("Texto modificado:", reemplazar_texto(texto, buscar, reemplazar))

# Ejercicio 5: Encontrar etiquetas XML en un texto
def encontrar_etiquetas_xml(texto):
    patron = r'<(/?[\w]+)[^>]*>'
    return re.findall(patron, texto)

def ejecutar_ejercicio_5():
    archivo = input("Introduce el nombre del archivo XML: ")
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
        print("Etiquetas XML encontradas:", encontrar_etiquetas_xml(contenido))
    except FileNotFoundError:
        print("El archivo no existe.")

# Ejercicio 6: Encontrar la primera dirección IP en un texto
def encontrar_ip(texto):
    patron = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    match = re.search(patron, texto)
    return match.group(0) if match else None

def ejecutar_ejercicio_6():
    archivo = input("Introduce el nombre del archivo de texto: ")
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
        ips = [encontrar_ip(linea) for linea in lineas if encontrar_ip(linea)]
        print("Direcciones IP encontradas:", ips)
    except FileNotFoundError:
        print("El archivo no existe.")

# Ejercicio 7: Convertir en scripts que reciben parámetros desde la línea de comandos
def ejecutar_ejercicio_7():
    print("Ejercicio 7 no requiere ejecución manual, todos los scripts pueden usar sys.argv para recibir parámetros.")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Validar si es un correo electrónico")
        print("2. Contar fechas en un texto")
        print("3. Encontrar números de teléfono en un texto")
        print("4. Reemplazar texto en un string")
        print("5. Encontrar etiquetas XML en un texto")
        print("6. Encontrar la primera dirección IP en un texto")
        print("7. Modificar scripts para recibir parámetros (Explicación)")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            ejecutar_ejercicio_1()
        elif opcion == '2':
            ejecutar_ejercicio_2()
        elif opcion == '3':
            ejecutar_ejercicio_3()
        elif opcion == '4':
            ejecutar_ejercicio_4()
        elif opcion == '5':
            ejecutar_ejercicio_5()
        elif opcion == '6':
            ejecutar_ejercicio_6()
        elif opcion == '7':
            ejecutar_ejercicio_7()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
