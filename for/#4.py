#4. Diseñar un algoritmos que pida el inicio y el fin de una serie y muestre su suma.
def main(args):
    suma = 0
    inicio = int(input("Introduce el inicio de la serie: "))
    fin = int(input("Introduce el fin de la serie: "))
    for i in range(inicio, fin):
        suma = suma + i
    print(suma)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))