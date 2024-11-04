#2. Diseñar un algoritmo que muestre la suma de los 10 primeros números.
def main(args):
    suma = 0
    contador = 0
    while contador < 10:
        contador = contador + 1
        suma = suma + contador
    print(suma)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))