"""Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario."""
# Función para contar los números pares e imares de una lista
def contar_numeros_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
# Pedimos al ususario introducir una lista de números
entrada = input("Introduce una lista de números separados por espacios: ")
# Convertimos la lista de entrada en una lista de enteros, entrada.split() genera una lista con los número de entrada introducidos mientras que la función map(int, ) aplica la función int a cada elemento de la lista
lista_numeros = list(map(int, entrada.split()))
# Llamamos a la función para contar números pares e impares
pares, impares = contar_numeros_pares_impares(lista_numeros)
# Mostramos resultado
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
