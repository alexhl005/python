
#  Expresiones regulares. fullmatch
#  No da coincidencia porque el patrón y el texto deben coincidir completamente


def main(args):
	import re
	patron = 'bella'
	texto = 'La vida es bella'
	coincidencia = re.fullmatch(patron, texto)
	if (coincidencia):
		inicio = coincidencia.start()
		fin = coincidencia.end()
		print('Se ha encontrado "{}" en "{}" desde {} hasta {} ("{}")'.format(patron, texto, inicio, fin, texto[inicio:fin]))
	else:
		print("El patrón no está en el texto")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
