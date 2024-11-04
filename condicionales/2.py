# 2. Algoritmo que lee un número y dice si es par o impar
def ejercicio2(args):
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio2(sys.argv))