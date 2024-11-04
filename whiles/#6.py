#6. Diseñar un algoritmo que calcula la media de una serie de 10 números.
def main(args):
    contador = 0
    suma = 0
    while contador < 10:
        contador = contador + 1
        suma = suma + contador
    media = suma / 10
    print(media)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))