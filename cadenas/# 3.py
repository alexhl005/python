def main(args):
    cadena = input("Escribe una cadena de texto: ")
    letra = input("Escribe una letra a contar: ")
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:
            contador = contador + 1
    print(contador)
        

    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
