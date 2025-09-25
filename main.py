""" Integrantes:
    * Han's De Ávila
    * Andrés Narvaez
    * Isabel Lara
    * Sebastian Mejía
    * Camilo Ortíz 
"""

def sumarNumeros(n1, n2):
    suma = n1 + n2
    print("Suma:", suma)

def restarNumeros(n1, n2):
    resta = n1 - n2
    print("Resta:", resta)

def multiplicarNumeros(n1, n2):
    multiplicacion = n1 * n2
    print("Multiplicación:", multiplicacion)

def dividirNumeros(n1, n2):
    if n2 != 0:
        division = n1 / n2
        print("División:", division)
    else:
        print("Error: No se puede dividir entre 0")

def potenciarNumeros (n1,n2):
    potencia=n1**n2
    print(potencia)


if __name__ == "__main__":
    sumarNumeros(1, 2)
    restarNumeros(3, 5)
    multiplicarNumeros(4, 6)
    dividirNumeros(10, 2)
    potenciarNumeros (2,4)

