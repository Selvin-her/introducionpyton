# Tabla de multiplicar de un número
def tabla_multiplicar():
    num = int(input("Ingrese un número: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

tabla_multiplicar()
