#!/usr/bin/env python
  
import random

def main(args):
	print("¡Bienvenido al juego de adivinanza de números!") 
	print("Estoy pensando en un número entre 1 y 100")
	num_secreto = random.randint(1, 100)
	n = 0
	contador = 1
	while num_secreto != n:
		n = int(input("Introduce tu número: "))
		if num_secreto > n:
			print("El numero secreto es mayor.")
		elif num_secreto == n:
			print("¡Felicidades! Has adivinado el numero secreto en",contador,"intentos")
		else:
			print("El numero secreto es menor.")
		contador = contador + 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

