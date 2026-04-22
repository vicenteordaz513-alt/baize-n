# Pedir el monto de la compra
compra = float(input("Ingresa el monto de la compra: "))

# Evaluar si aplica descuento
if compra > 500:
    descuento = compra * 0.10   # 10% de descuento
    total = compra - descuento
    print("Se aplicó un descuento de:", descuento)
    print("El total a pagar es:", total)
else:
    print("No aplica descuento")
    print("El total a pagar es:", compra)
