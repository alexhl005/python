#3. Diseñar un algoritmo que pida el inicio y el fin de una serie y la muestre.
def main(args):
    inicio = int(input("Introduce el inicio de la serie: "))
    fin = int(input("Introduce el fin de la serie: "))
    for i in range(inicio, fin):
        print(i)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))