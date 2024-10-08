# calculadora.py

from operaciones import suma, resta, multiplicacion, division


def main():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce números válidos.")
            continue

        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        operacion = input("Elige una operación (1/2/3/4): ")

        if operacion == '1':
            resultado = suma(num1, num2)
        elif operacion == '2':
            resultado = resta(num1, num2)
        elif operacion == '3':
            resultado = multiplicacion(num1, num2)
        elif operacion == '4':
            resultado = division(num1, num2)
        else:
            print("Operación no válida.")
            continue

        print(f"El resultado es: {resultado}")

        otra = input("¿Quieres hacer otra operación? (s/n): ")
        if otra.lower() != 's':
            break


if __name__ == "__main__":
    main()