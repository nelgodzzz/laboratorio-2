

# suma.py

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultado = a + b

print(f"El resultado de la suma es: {resultado}")

# resta.py

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultado = a - b

print(f"El resultado de la resta es: {resultado}")

# multiplicacion.py

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultado = a * b

print(f"El resultado de la multiplicación es: {resultado}")

# division.py

a = float(input("Ingresa el dividendo: "))
b = float(input("Ingresa el divisor: "))

if b == 0:
    print("Error: No se puede dividir entre cero")
else:
    resultado = a / b
    print(f"El resultado de la división es: {resultado}")

# exponenciacion.py

a = float(input("Ingresa la base: "))
b = float(input("Ingresa el exponente: "))

resultado = a ** b

print(f"El resultado de la exponenciación es: {resultado}")

# raiz.py
import math

a = float(input("Ingresa el radicando: "))

resultado = math.sqrt(a)

print(f"El resultado de la raíz cuadrada es: {resultado}")

# suma_5_numeros.py

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
d = float(input("Ingresa el cuarto número: "))
e = float(input("Ingresa el quinto número: "))

resultado = a + b + c + d + e

print(f"La suma de los 5 números es: {resultado}")

# residuo.py

a = float(input("Ingresa el dividendo: "))
b = float(input("Ingresa el divisor: "))

resultado = a % b

print(f"El residuo de la división es: {resultado}")

# quetzal_a_dolar.py

monto = float(input("Ingresa el monto en quetzales: "))

resultado = monto / 7.91

print(f"{monto} quetzales equivalen a {resultado} dólares")
