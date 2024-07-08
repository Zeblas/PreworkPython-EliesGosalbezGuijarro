"""Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario."""
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error al dividir por cero"
    return a / b
# Creamos un menú de opciones
print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
# Solicitamos al usuario la selección
opcion = input("Introduce el número de la operación (1/2/3/4): ")
# Solicitamos al usuario los dos números