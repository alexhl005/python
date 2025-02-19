import re


def validar_correo(cadena):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, cadena)

def contar_fechas(texto):
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return len(re.findall(patron, texto))

def encontrar_telefonos(texto):
    patron = r'\b(?:\d{3}-\d{6}|\d{9}|\d{3}\.\d{3}\.\d{3})\b'
    return re.findall(patron, texto)

def reemplazar_texto(texto, buscar, reemplazo):
    return re.sub(re.escape(buscar), reemplazo, texto)

def encontrar_etiquetas_xml(texto):
    patron = r'<(/?[\w]+)[^>]*>'
    return re.findall(patron, texto)

def encontrar_ip(texto):
    patron = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    match = re.search(patron, texto)
    return match.group(0) if match else None



# Ejercicio 1: Validar si es un correo electrónico
def ejecutar_ejercicio_1():
    cadena = input("Introduce una dirección de correo electrónico: ")
    es_valido = validar_correo(cadena)
    print("¿Es un correo válido?:", es_valido)

# Ejercicio 2: Contar fechas en un texto
def ejecutar_ejercicio_2():
    texto = input("Introduce un texto con fechas (dd-mm-aaaa o dd/mm/aaaa): ")
    cantidad = contar_fechas(texto)
    print("Número de fechas encontradas:", cantidad)

# Ejercicio 3: Encontrar números de teléfono en un texto
def ejecutar_ejercicio_3():
    texto = input("Introduce un texto con números de teléfono: ")
    telefonos = encontrar_telefonos(texto)
    print("Números de teléfono encontrados:", telefonos)

# Ejercicio 4: Reemplazar texto
def ejecutar_ejercicio_4():
    texto = input("Introduce el texto original: ")
    buscar = input("Introduce el texto a buscar: ")
    reemplazo = input("Introduce el texto de reemplazo: ")
    nuevo_texto = reemplazar_texto(texto, buscar, reemplazo)
    print("Texto modificado:", nuevo_texto)

# Ejercicio 5: Encontrar etiquetas XML
def ejecutar_ejercicio_5():
    texto = input("Introduce un texto con etiquetas XML: ")
    etiquetas = encontrar_etiquetas_xml(texto)
    print("Etiquetas XML encontradas:", etiquetas)

# Ejercicio 6: Encontrar la primera dirección IP en un texto
def ejecutar_ejercicio_6():
    texto = input("Introduce un texto con direcciones IP: ")
    ip = encontrar_ip(texto)
    print("Primera dirección IP encontrada:", ip)



# Menú principal
def menu():
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Validar si es un correo electrónico")
        print("2. Contar fechas en un texto")
        print("3. Encontrar números de teléfono en un texto")
        print("4. Reemplazar texto en un string")
        print("5. Encontrar etiquetas XML en un texto")
        print("6. Encontrar la primera dirección IP en un texto")
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
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
