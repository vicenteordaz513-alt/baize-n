# Pedir tres calificaciones
c1 = float(input("Ingresa la primera calificación: "))
c2 = float(input("Ingresa la segunda calificación: "))
c3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio
promedio = (c1 + c2 + c3) / 3

# Mostrar el promedio
print("El promedio es:", promedio)

# Usar if y else para evaluar
if promedio >= 6:
    print("El estudiante aprobó")
else:
    print("El estudiante reprobó")
