"""Crea un programa que sume todos los números en una lista ingresada por el
usuario."""
# Creamos la función para sumar toda la lista de números
def sumar_lista(numeros):
    suma = sum(numeros)
    return suma
# Pedimos al usuario que introduzca la lista de números separados por comas
entrada = input("Introduce los números separados por comas: ")
# Con la función split separamos la cadena de entrada separada por comas en una lista de números
numeros = [int(numero) for numero in entrada.split(",")]
# Llamamos a la función para sumar los números
resultado = sumar_lista(numeros)
print(f"La suma de los números de la lista es: {resultado}")
