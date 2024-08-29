# Estructuras de datos
numero = int(input("Ingrese un número entero para la tabla de multiplicar: "))  # Entrada de datos - Estructura de datos
tabla_multiplicar = []  # Creación de una lista vacía - Estructura de datos

for i in range(1, 11):  # Estructura de control de programación
    resultado = numero * i  # Operación matemática - Programación
    tabla_multiplicar.append(resultado)  # Agregar resultado a la lista - Estructura de datos

print("Tabla de multiplicar de", numero, ":")  # Salida de texto - Programación
for j in range(10):  # Estructura de control de programación
    print(numero, "x", j+1, "=", tabla_multiplicar[j])  # Salida de texto y elementos de la lista - Programación y estructura de datos

# Estructuras de control de programación
numero_dividir = int(input("Ingrese un número entero para la tabla de dividir: "))  # Entrada de datos - Estructura de datos
print("Tabla de dividir del número", numero_dividir, "de mayor a menor:")  # Salida de texto - Programación
for k in range(10, 0, -1):  # Estructura de control de programación
    resultado_division = numero_dividir / k  # Operación matemática - Programación
    print(numero_dividir, "/", k, "=", resultado_division)  # Salida de texto y resultado de la división - Programación