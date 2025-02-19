
#  Expresiones regulares. search


def main(args):
	import re
	#patron='Bella'
	patron='Bella'
	texto = 'La vida es bella'
	#coincidencia=re.search(patron,texto,re.I)
	coincidencia=re.search(patron,texto,re.I)
	if (coincidencia):
		inicio = coincidencia.start()
		fin = coincidencia.end()
		print('Se ha encontrado "{}" en "{}" desde {} hasta {} ("{}")'.format(patron, texto, inicio, fin, texto[inicio:fin]))
	else:
		
		print("El patrón no está en el texto ")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
