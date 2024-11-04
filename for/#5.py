#5. Diseñar un algoritmo que muestre la suma de los pares que hay entre un inicio y un final definidos por el usuario.
def main(args):
    suma = 0
    inicio = int(input("Introduce el inicio de la serie: "))
    fin = int(input("Introduce el fin de la serie: "))
    for i in range(inicio, fin):
        if i%2==0:
            suma = suma + i
    print(suma)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))