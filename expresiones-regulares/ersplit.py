
#  Expresiones regulares. split
# Este ejemplo separa una frase en palabras


def main(args):
	import re
	patron=r'\W+'
	texto = 'Esto es un texto de siete palabras'
	palabras=re.split(patron,texto)
	if (palabras):
		print(palabras)
		print(f"Hay {len(palabras)} palabras")
	else:
		print("El patrón no está en el texto")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
