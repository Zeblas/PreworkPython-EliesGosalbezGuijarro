"""Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no."""
# Definimos la función para determinar si un año es bisiesto o no, teniendo en cuenta que la regla general es que cualquier año divisibles por 4 es bisiesto, pero para años divisibles por 100, solo son bisiestos si también son divisibles por 400
def bisiesto(ano):
    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        return True
    else:
        return False
# Pedimos al usuario que introduzca el año
ano = int(input("Introduce un año: "))
if bisiesto(ano):
    print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")