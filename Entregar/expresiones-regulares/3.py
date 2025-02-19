import re

def encontrar_telefonos(texto):
    patron = r'\b(?:\d{3}-\d{6}|\d{9}|\d{3}\.\d{3}\.\d{3})\b'
    return re.findall(patron, texto)

if __name__ == "__main__":
    texto = input("Introduce un texto: ")
    print("Números de teléfono encontrados:", encontrar_telefonos(texto))
