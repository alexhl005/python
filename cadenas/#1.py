def main(args):
    cadena = input("Escribe una cadena de texto: ")
    for letra in cadena:
        print(letra)
    print("Hecho con la característica iterable de las cadenas")
    
    for letra2 in range(len(cadena)):
        print(cadena[letra2])
    print("Hecho con la característica range")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
