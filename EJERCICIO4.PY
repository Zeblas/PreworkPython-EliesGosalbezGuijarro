"""Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario."""
def contar_vocales(palabra): # cuenta las vocales de una palabra
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador
# Pedir palabra
palabra = input("Introduce una palabra: ")
# Contar vocales
numero_vocales = contar_vocales(palabra)
# imprimir resultado
print(f"El número de vocales en '{palabra}' es: {numero_vocales}")
