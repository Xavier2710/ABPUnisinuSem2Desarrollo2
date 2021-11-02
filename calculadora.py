# esta achivo contiene la funcion main
import operaciones_aritmeticas as math


def menu():
    print("=====================")
    print(" CALCULADORA POR CLI ")
    print("=====================")
    print()
    num1 = input("Digite un numero: ")
    num1 = float(num1)
    num2 = float(input("Digite otro numero: "))
    print()
    print("=====================")
    print("        MENU ")
    print("=====================")
    while True:
        print("1) SUMAR")
        print("2) RESTAR")
        print("3) MULTIPLICAR")
        print("4) DIVIDIR")
        print("5) POTENCIA DE X a Y")
        op = int(input("Digite la opcion: "))
        if op == 1:
            res = math.sumar(num1, num2)
            print("SUMAR", num1, "+", num2, "=", res)
            break
        elif op >= 2 and op <= 5:
            print("Operacion en desarrollo")
            break
        else:
            print("Debes escoger una opcion valida")


menu()
print("FIN")
