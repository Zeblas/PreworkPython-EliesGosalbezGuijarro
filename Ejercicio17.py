"""Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros."""
# Definimos función para realizar la conversión
def convertir_millas_a_Km(millas):
    km = millas * 1.60934
    return km
# Pedimos al ususario que introduzca las millas
millas = float(input("Introduce la distancia en millas: "))
kilometros = convertir_millas_a_Km(millas)
print(f"{millas} millas son equivalentes a {kilometros} kilómetros.")
