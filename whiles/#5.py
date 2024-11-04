#5. Diseñar un algoritmo que muestre la suma de los pares que hay entre un inicio y un final definidos por el usuario.

def main(args):
    contador=int(input("Inicio de la seria: "))
    contador2=int(input("Fin de la seria: "))
    suma=0
    while contador<contador2:
        contador=contador+1
        if contador%2==0:
            suma = suma + contador
    print("La suma de los pares es: ", suma)
if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))