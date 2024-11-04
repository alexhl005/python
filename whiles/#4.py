#4. Diseñar un algoritmos que pida el inicio y el fin de una serie y muestre su suma.
def main(args):
    contador=int(input("Inicio de la seria: "))
    contador2=int(input("Fin de la seria: "))
    suma = 0
    while contador<contador2:
        contador=contador+1
        suma = suma + contador
    print("La suma de la serie es: ", suma)

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))