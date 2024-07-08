"""Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario."""
# Definimos la función para contar las palabras
def contar_palabras(oracion):
    # Primero dividimos la oración en palabras usando la función split
    palabras = oracion.split()
    # Contamos la cantidad de palabras con la función len
    cantidad_palabras = len(palabras)
    return cantidad_palabras
# Pedimos al usuario que introduzca una oración
oracion = input("Introduce una oración: ")
cantidad = contar_palabras(oracion)
print(f"La cantidad de palabras en la oración es: {cantidad}")
