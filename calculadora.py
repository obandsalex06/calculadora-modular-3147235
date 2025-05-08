operacion = input("¿Qué operación deseas realizar? (suma/resta/multiplicacion/division): ")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if operacion == "suma":
    print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2}")
elif operacion == "resta":
    print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2}")
elif operacion == "multiplicacion":
    print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2}")
elif operacion == "division":
    if numero2 != 0:
        print(f"La división de {numero1} entre {numero2} es: {numero1 / numero2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no reconocida. Por favor elige entre suma, resta, multiplicación o división.")
