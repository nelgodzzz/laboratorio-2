

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
