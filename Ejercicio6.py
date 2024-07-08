"""Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
def es_palindromo(palabra): # verificar si una palabra es un palíndromo
    # Convertir palabra a minúscula para ignorar mayúscula/minúscula
    palabra = palabra.lower()
    # Eliminar espacios en blanco si los hay
    palabra = palabra.replace(" ", "")
    # Comparar palabra con su inversa
    return palabra == palabra[::-1]
# Pedimos palabra al ususario
palabra = input("Introduce una palabra: ")
# Verificamos si es un palíndromo
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")
    