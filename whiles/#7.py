#7. Diseñar un algoritmo que muestre la tabla de multiplicar de un número que pide al usuario y que debe estar entre 1 y 10 (ambos inclusive).
def main(args):
    numero = int(input("Introduce un número entre 1 y 10: "))
    if numero < 1 or numero > 10:
        numero = int(input("Número fuera de rango. Introduce un número entre 1 y 10: "))
    else:
        contador = 0
        while contador < 10:
            contador = contador + 1
            resultado = numero * contador
            print(f"{numero} x {contador} = {resultado}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
