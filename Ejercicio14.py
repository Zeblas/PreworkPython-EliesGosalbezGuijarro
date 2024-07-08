"""Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%."""
# Definimos función para calcular el precio
def calculo_precio_final(precio_inicial, descuento):
    descuento_aplicado = precio_inicial * (descuento / 100)
    precio_final = precio_inicial - descuento_aplicado
    return precio_final
# Pedimos al usuario el precio del artículo
precio_inicial = float(input("Introduce el precio del artículo: "))
# Definimos descuento
descuento = 20
# Calculamos precio final
precio_final = calculo_precio_final(precio_inicial, descuento)
# Mostramos resultado
print(f"El precio con el descuento aplicado del {descuento}% es: {precio_final:.2f} ")
