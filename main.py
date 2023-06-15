while True:
    print("Elige una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Raíz")
    print("7. Suma de 5 números")
    print("8. Residuo")
    print("9. Quetzal a Dólar")
    print("10. Dólar a Quetzal")
    print("0. Salir")

    opcion = int(input("Opción: "))

    if opcion == 0:
        break
    elif opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = a + b
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = a - b
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = a * b
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        a = float(input("Ingresa el dividendo: "))
        b = float(input("Ingresa el divisor: "))
        if b == 0:
            print("Error: No se puede dividir entre cero")
        else:
            resultado = a / b
            print(f"El resultado de la división es: {resultado}")
    elif opcion == 5:
        a = float(input("Ingresa la base: "))
        b = float(input("Ingresa el exponente: "))
        resultado = a ** b
        print(f"El resultado de la exponenciación es: {resultado}")
    elif opcion == 6:
        import math
        a = float(input("Ingresa el radicando: "))
        resultado = math.sqrt(a)
        print(f"El resultado de la raíz cuadrada es: {resultado}")
    elif opcion == 7:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        c = float(input("Ingresa el tercer número: "))
        d = float(input("Ingresa el cuarto número: "))
        e = float(input("Ingresa el quinto número: "))
        resultado = a + b + c + d + e
        print(f"La suma de los 5 números es: {resultado}")
    elif opcion == 8:
        a = float(input("Ingresa el dividendo: "))
        b = float(input("Ingresa el divisor: "))
        resultado = a % b
        print(f"El residuo de la división es: {resultado}")
    elif opcion == 9:
        monto = float(input("Ingresa el monto en quetzales: "))
        resultado = monto / 7.91
        print(f"{monto} quetzales equivalen a {resultado} dólares")
    elif opcion == 10:
        monto = float(input("Ingresa el monto en dólares: "))
        resultado = monto * 7.91
        print(f"{monto} dólares equivalen a {resultado} quetzales")
