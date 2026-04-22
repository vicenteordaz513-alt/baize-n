# Pedir datos
edad = int(input("Ingresa tu edad: "))
tiene_ine = input("¿Tienes credencial de elector? (sí/no): ").lower()
es_estudiante = input("¿Eres estudiante? (sí/no): ").lower()

# Ejemplo con AND
if edad >= 18 and tiene_ine == "sí":
    print("Puedes votar")
else:
    print("No puedes votar")

# Ejemplo con OR
if edad < 18 or es_estudiante == "sí":
    print("Tienes descuento especial")
else:
    print("No tienes descuento")

# Ejemplo con NOT
if not (edad < 18):
    print("No eres menor de edad")
else:
    print("Eres menor de edad")
