#Algoritmo que lee 5 números y muestra la media aritmética.
def main(args):
    num1=int(input("Introduce el primer número "))
    num2=int(input("Introduce el segundo número "))
    num3=int(input("Introduce el tercero número "))
    num4=int(input("Introduce el cuarto número "))
    num5=int(input("Introduce el quinto número "))
    resultado=(num1+num2+num3+num4+num5)/5
    print(resultado)
    return 0

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))