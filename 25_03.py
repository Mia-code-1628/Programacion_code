numero = int(input("Ingrese un número entero para la tabla de multiplicar: "))  
tabla_multiplicar = []

for i in range(1, 11): 
    resultado = numero * i 
    tabla_multiplicar.append(resultado) 

print("Tabla de multiplicar de", numero, ":") 
for m in range(10): 
    print(numero, "x", m+1, "=", tabla_multiplicar[m])

numero_dividir = int(input("Ingrese un número entero para la tabla de dividir: ")) 
print("Tabla de dividir del número", numero_dividir, "de mayor a menor:") 
for t in range(10, 0, -1):  
    resultado_division = numero_dividir / t
    print(numero_dividir, "/", t, "=", resultado_division) 
