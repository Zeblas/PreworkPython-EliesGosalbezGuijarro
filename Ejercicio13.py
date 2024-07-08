"""Escribe un programa que determine si un número ingresado por el usuario es primo o no."""
# Definimos función para comprobar si es un número primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
# Pedir al usuario un múmero
numero = int(input("Introduce un número: "))
# Verificamos con la función si es primo
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
    
