"""Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual."""
from datetime import date
# DEfinimos función para calcular edad
def calcular_edad(ano_nacimiento):
    ano_actual = date.today().year
    edad = ano_actual - ano_nacimiento
    return edad
# Pedir año nacimiento al usuario
ano_nacimiento = int(input("Introduce tu año de nacimiento: "))
# Calcular edad actual usuario
edad = calcular_edad(ano_nacimiento)
# Mostrar edad
print(f"Tu edad es de {edad} años.")

    