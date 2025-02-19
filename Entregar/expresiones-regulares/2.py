import re

def contar_fechas(texto):
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return len(re.findall(patron, texto))

if __name__ == "__main__":
    texto = input("Introduce un texto: ")
    print("Número de fechas encontradas:", contar_fechas(texto))
