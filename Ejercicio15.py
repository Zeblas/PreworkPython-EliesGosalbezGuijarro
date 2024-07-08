"""Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos."""
# Definimos función para la conversión
def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes
# Pedimos al usuario el número de minutos
minutos = int(input("Introduce el número de minutos: "))
# Convertir minutos a horas y minutos
horas, minutos_restantes = convertir_minutos(minutos)
# mostrar resultado
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
