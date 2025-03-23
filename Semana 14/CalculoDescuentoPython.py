def calcular_descuento(Productos, descuento=20):
    descuento = Productos * (descuento / 100)
    return descuento

monto1 = 10
descuento1 = calcular_descuento(10)
monto_final1 = monto1 - descuento1
print(f"Compra 1: Monto Total = {monto1} | Descuento = {descuento1} | Monto a Pagar = {monto_final1}")

monto2 = 159
descuento2 = calcular_descuento(monto2)
monto_final2 = monto2 - descuento2
print(f"Compra 2: Monto Total = {monto2} | Descuento = {descuento2} | Monto a Pagar = {monto_final2}")

print("******* Gracias por su compra *******")