#Algoritmo que lee 5 números y muestra la media aritmética.
def main(args):
    vueltas=int(input("Cuantos numeros quieres introducir: "))
    contador=0
    num2=0
    while contador<vueltas:
        num=int(input("Introduce el numero: "))
        num2=num + num2
        contador=contador+1
    resultado=num2 / vueltas
    print(resultado)

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))