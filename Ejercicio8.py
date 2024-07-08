"""Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona."""
# Función para calcula el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
# Pedimos que el usuario nos indique su peso y altura
peso = float(input("Introduce tu peso (Kg): "))
altura = float(input("Introduce tu altura (m): "))
# Calcular el IMC
imc = calcular_imc(peso, altura)
# Mostrar resultado con 2 decimales
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
# Evaluación del IMC del usuario
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc <29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
    