#Ejercicio 1 

print("Hola, mundo")

#ejercicio 2

nombre= input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}")

# Ejercicio 3

dato_name = input("¿Cuál es tu nombre? ")
dato_surname = input("¿Cuál es tu apellido? ")
dato_age = input("¿Cuál es tu edad? ")
dato_location = input("¿Dónde vives? ")
print(f"Hola, {dato_name} {dato_surname}, tienes {dato_age} años y vives en {dato_location}.")

# Ejercicio 4

radio = float(input("Introduce el radio del círculo: "))
area = 3.14159 * radio ** 2
print(f"El área del círculo con radio {radio} es: {area}")

# Ejercicio 5

segundos = int(input("Introduce el número de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos % 60} segundos.")


# Ejercicio 6

tabla = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")

# Ejercicio 7

num1= int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1/num2 

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")

# Ejercicio 8

altura = float(input("Introduce tu altura en metros: "))
peso = float(input("Introduce tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

# Ejercicio 9

temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f}")

# Ejercicio 10

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

#para importar libretas usamos import , por ejemplo math
#import math 