numero = int(input("Ingrese un numero entero: "))#Pide al usuario que ingrese un numero

print("Tabla de multiplicar de", numero)
for i in range(1, 11):  #Bucle for del 1 al 10.
    resultado = numero * i  #Multiplica el número ingresado por el índice del bucle.
    print(numero, "x", i, "=", resultado)  #Muestra la multiplicación en consola.

numero2 = int(input("Ingrese otro número entero: "))  #Lee la entrada del usuario y la convierte a entero.

print("Tabla de dividir de", numero2, "en orden descendente")
for m in range(10, 0, -1):  #Bucle for para iterar de 10 a 1 en orden descendente.
    resultado = numero2 / m  #Divide el segundo número ingresado por el índice del bucle.
    print(numero2, "÷", m, "=", resultado) #Muestra el resultado
