import re

def es_correo_electronico(cadena):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, cadena))

if __name__ == "__main__":
    cadena = input("Introduce una cadena para verificar si es un correo electrónico: ")
    print("Es un correo electrónico:", es_correo_electronico(cadena))
