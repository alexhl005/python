
#  Expresiones regulares. finiter
# lo que devuelve es un objeto match por cada resultado

def main(args):
	import re
	patron=r'bella'
	texto = 'Bella, la vida es bella'
	flag=re.I
	coincidencias=re.finditer(patron,texto,flag)
	if (coincidencias):
		for coincidencia in coincidencias:
			print(coincidencia.start())
	else:
		print("El patrón no está en el texto")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
