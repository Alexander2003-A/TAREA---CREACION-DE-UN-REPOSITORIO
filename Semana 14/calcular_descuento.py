def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total de compra.

    :param monto_total: El monto total de la compra
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10%)
    :return: El monto del descuento
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamadas a la función
compra1 = 100  # Compra de 100
descuento1 = calcular_descuento(compra1)
print(f"Compra: ${compra1}, Descuento: ${descuento1}, Total a pagar: ${compra1 - descuento1}")

compra2 = 200  # Compra de 200 con 20% de descuento
descuento2 = calcular_descuento(compra2, 20)
print(f"Compra: ${compra2}, Descuento: ${descuento2}, Total a pagar: ${compra2 - descuento2}")
