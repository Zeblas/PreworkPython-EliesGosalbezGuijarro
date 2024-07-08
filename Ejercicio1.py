"""Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit"""
def de_celsius_a_farenheit(celsius):
    # Función que Convierte temperatura celsius a farenheit
    farenheit = (celsius * 9/5) + 32
    return farenheit # devuelve temperatura convertida en farenheit
celsius = float(input("Introduce la tempeatura en grados celsius: ")) # se solicita entrada grados celsius
farenheit = de_celsius_a_farenheit(celsius) # se llama a la función para hacer conversión
print(f"La temperatura en grados farenheit es: {farenheit:.2f}") # se imprime resultado función
