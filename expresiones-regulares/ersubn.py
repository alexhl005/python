
#  Expresiones regulares. subn
# sirve para sustituir una cadena en otra y te devuelve una tupla con la nueva
# cadena y el número de cambios hechos

def main(args):
	import re
	patron=r'bella'
	reemplazo='fea'
	texto = 'Bella, la vida es bella'
	flag=re.I
	resultado=re.subn(patron,reemplazo,texto,0,flag)
	print(f"El nuevo texto es:\n {resultado[0]} \n y se han hecho {resultado[1]} cambios")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
