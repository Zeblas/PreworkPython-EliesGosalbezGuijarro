"""Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta."""
def calcula_total_cuenta_propina(total_cuenta): # Calcula total cuenta a pagar con propina
    propina = total_cuenta * 0.15
    total_con_propina = total_cuenta + propina
    return total_con_propina
# Uso
total_cuenta = float(input("Introduce el importe de la cuenta: "))
total = calcula_total_cuenta_propina(total_cuenta)
print(f"LA cantidad total a pagar es: {total:.2f}")
