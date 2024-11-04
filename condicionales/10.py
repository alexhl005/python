# 10. Algoritmo que pide una nota numérica entre 0 y 10 y muestra la calificación correspondiente
def ejercicio10(args):
    nota = float(input("Introduce una nota entre 0 y 10: "))
    
    if 0 <= nota < 5:
        print("Calificación: IN (Insuficiente)")
    elif 5 <= nota < 6:
        print("Calificación: SF (Suficiente)")
    elif 6 <= nota < 7:
        print("Calificación: BI (Bien)")
    elif 7 <= nota < 9:
        print("Calificación: NT (Notable)")
    elif 9 <= nota <= 10:
        print("Calificación: SB (Sobresaliente)")
    else:
        print("Nota no válida, debe estar entre 0 y 10.")
    
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio10(sys.argv))