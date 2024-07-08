"""Escribe un programa que calcule la suma de todos los números pares del 1 al 100."""
# Variable que almacena la suma
suma_pares = 0
# Recorrer números del 1 al 100
for numero in range(1, 101):
    # Comprobar si el número es par
    if numero % 2 == 0:
        # Sumar número par a la suma total
        suma_pares += numero
# Imprimir resultado
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}")
