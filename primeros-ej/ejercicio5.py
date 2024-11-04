#Algoritmo que lee dos datos, intercambia el valor de las variables y las muestra.
def main(args):
    num1=int(input("Introduce el primer número "))
    num2=int(input("Introduce el segundo número "))
    aux=num1
    num1=num2
    num2=aux
    print(num1)
    print(num2)
    return 0

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))        