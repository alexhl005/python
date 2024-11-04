#3. Diseñar un algoritmo que pida el inicio y el fin de una serie y la muestre.
def main(args):
    contador=int(input("Inicio de la seria: "))
    contador2=int(input("Fin de la seria: "))
    while contador<contador2:
        contador=contador+1
        print(contador)

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))