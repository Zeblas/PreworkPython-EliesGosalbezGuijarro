"""Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo."""
# Definimos función para calcular el área
def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area
# Pedir al usuario longitud y ancho del rectángulo
longitud = float(input("Introduce la longitud del rectángulo (cm): "))
ancho = float(input("Introduce el ancho del rectángulo (cm): "))
# Calculamos el área del rectángulo con la función calculada
area = calcular_area_rectangulo(longitud, ancho)
# Mostrar resultado
print(f"El área del rectángulo es: {area:.2f} cm2")
