#6. Diseñar un algoritmo que calcula la media de una serie de 10 números. 
def main(args):
    suma = 0
    inicio = int(input("Introduce el inicio de la serie: "))
    fin = int(input("Introduce el fin de la serie: "))
    for i in range(inicio, fin):
        suma = suma + i
    media = suma / i
    print(media)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))