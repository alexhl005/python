# 1. Algoritmo que lee un número y dice si es positivo o negativo
def ejercicio1():
    num = float(input("Introduce un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
        