#2. Diseñar un algoritmo que muestre la suma de los 10 primeros números.
def main(args):
    suma = 0
    for i in range(10):
        suma = suma + i
    print(suma)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
