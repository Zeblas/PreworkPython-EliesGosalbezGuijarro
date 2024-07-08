"""Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)."""
# Función para devolver dia de la semana en función del número indicado
def obtener_dia_semana(numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias_semana.get(numero, "Número inválido. Introduce un número del 1 al 7.")
# Pedir al ususario que meta un número
numero = int(input("Introduce un número (1 para lunes, 2 para martes, etc) "))
# Obtener a que dia de la semana corresponde dicho número
dia_de_la_semana = obtener_dia_semana(numero)
# Mostrar resultado
print(f"El día de la semana correspondiente al número {numero} es: {dia_de_la_semana}")
