
#  Expresiones regulares. findall

def main(args):
	import re
	patron=r'bella'
	texto = 'Bella, la vida es bella'
	flag=re.I
	coincidencias=re.findall(patron,texto,flag)
	if (coincidencias):
		print(coincidencias)
	else:
		print("El patrón no está en el texto")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))