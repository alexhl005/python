
#  Expresiones regulares. sub
# sirve para sustituir una cadena en otra

def main(args):
	import re
	patron=r'bella'
	reemplazo='fea'
	texto = 'Bella, la vida es bella'
	flag=re.I
	nuevotexto=re.sub(patron,reemplazo,texto,0,flag)
	print(nuevotexto)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
