#Muestra por pantalla la suma de dos números definidos por el usuario.
def main(args):
    num1=int(input("Introduce el primer número "))
    num2=int(input("Introduce el segundo número "))
    resultado=num1+num2
    print(resultado)
    return 0

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))
