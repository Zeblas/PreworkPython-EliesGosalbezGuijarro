"""Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros."""
# Función para convertir moneda
def convertir_dolar_euro(dolares):
    tasa_de_cambio = 0.85
    euros = dolares * tasa_de_cambio
    return euros
# Pedimos cantidad de dolares al usuario
dolares = float(input("Introduce la cantidad en dolares: "))
# Convertimos moneda con la función creada
euros = convertir_dolar_euro(dolares)
# Mostrar dólares con 2 decimales
print(f"{dolares:.2f} dólares equivalen a {euros:.2f} euros.")
