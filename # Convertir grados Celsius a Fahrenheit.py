# Convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit():
    c = float(input("Ingrese la temperatura en grados Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c} grados Celsius equivalen a {f} grados Fahrenheit")

celsius_a_fahrenheit()